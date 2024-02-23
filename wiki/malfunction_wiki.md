### Consumer grouping으로 발생한 컨슈머 성능 저하
---

### 내용 요약
모든 api/client log를 한 개의 컨슈머 그룹(다양한 topic)으로 모아두었더니 특정 파티션의 소비 속도가 다른 파티션에 비해 상당히 떨어지는 성능 저하 이슈 발생.

### 프로젝트 keywords
weaver, consumer, kafka, firelens

### 종류
오작동, 성능 저하

### 발생 일시
2023-06-01

### 배경/원인 및 세부 내용
Firelens log의 경우 비슷한 목적을 가진 다양한 topic이 모여있는 구조입니다. 그래서 kafka 관리의 편의성을 위해 airflow에 firelens log 빅쿼리 컨슈머를 붙이면서 한 개의 컨슈머 그룹으로 묶는 시도를 해보았습니다. 
하지만 이와 같은 구조에서는 한 topic 내의 다양한 파티션의 메세지 소비 속도가 다르다는 것을 확인했습니다. 
간과했던 부분은 카프카의 rebalancing protocol입니다.
카프카는 그룹에 새로운 consumer instance가 들어오거나 나가면 해당 instance의 topic에 관계 없이 그룹 내 전체 instance의 rebalance가 발생합니다. 한 개의 그룹 내에 비슷한 목적을 가진 여러 topic을 묶어둔다면 그만큼 rebalance가 자주 일어나는 것입니다. 
만약 상시로 인스턴스가 떠 있어서 메세지를 소비하는 구조라면 group join/exit이 흔하지 않기 때문에 문제의 소지가 적습니다. 하지만 airflow 처럼 배치 처리를 위해 인스턴스가 잠깐 join 했다가 일을 마친 후 exit 하는 구조에서는 rebalancing이 불필요하게 자주 일어납니다.
즉, 상황에 따라서 특정 partition은 메세지를 전혀 소비하지 못할 수도 있는 것입니다. 


### 해결방식
topic 별로 consumer group을 따로 지정하는 것이 성능상으로 훨씬 좋다는 결론을 내렸습니다. 다행히 아직 firelens-log는 빅쿼리 외에 소비하는 곳이 없기 때문에 기존의 consumer group을 완전히 삭제한 후 새로 instance를 띄워 주었습니다. 
이 과정에서 중복 메세지가 빅쿼리에 쌓입니다. 왜냐하면 kafka는 consumer group 으로 최신 메세지 offset을 관리하는데, 새로 띄운 instance는 group이 바꾸었기 때문입니다. 그래서 이전 그룹에서 이미 소비한 메세지도 새로운 그룹에서 재소비가 됩니다. 중복된 메세지는 쿼리를 이용해 삭제해주었습니다. 
관련된 내용은 [지라 이슈](https://wantedlab.atlassian.net/browse/DATARQ-4586?atlOrigin=eyJpIjoiZTgwN2RlOTIyZDJjNDkzYzliZjRmNTBhYjNhNjVkM2QiLCJwIjoiaiJ9)에서 확인할 수 있습니다.

위 해결 과정에서 `partition.assignment.strategy` config에 대해 테스트를 진행하였습니다. 
기본값인 range, round-robin의 경우에는 같은 그룹에 새로운 consumer instance가 들어오면 그룹에 있는 모든 기존 instance들에서 partition revoke가 일어난 후 새로 topicPartition을 할당(assign) 받습니다.
이를 stop-the-world-rebalance라고 표현합니다. 이유는 rebalance가 일어날 때 모든 instance가 멈추기 때문입니다. 아래 사진이 그 현상을 보여줍니다. 

조금 더 효율적인 방법은 `partition.assignment.strategy`를 cooperative-sticky로 설정하는 것입니다. 이 경우에는 새로운 instance가 join-group 할 때, 전체 partition에서 revoke가 일어나지는 않습니다. 대신 rebalance 대상이 되는 하나의 partition만 기존에 할당된 instance로 부터 revoke한 후 새로운 instance에 할당합니다. Revoke 되지 않은 대부분의 topicPartition에서는 끊김 없이 이벤트를 소비할 수 있는 것입니다. 
아래 사진이 바로 cooperative-sticky 방식의 rebalance를 보여줍니다. 

저희는 굳이 cooperative-sticky를 사용하지는 않았습니다. 왜냐면 이 문제에서 중요한 것은 rebalance가 얼마나 잦은가이지, 멈추고 다시 진행하고 말고는 큰 상관이 없기 때문입니다. 