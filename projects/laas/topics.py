from melting_pot.google import gbq, safe_send_bigquery
from projects.laas import StageABC
from bertopic import BERTopic


class Env(StageABC):
    _stage = {
        'nextweek': 'nw',
        'www': 'www',
    }


def get_skills():
    return gbq(
        '''
        WITH skill_df AS (
        SELECT
            wd_id,
            jd,
            STRUCT(
            JSON_EXTRACT_STRING_ARRAY(skills_json) AS skills
            ) skill
        FROM `wanted_ml.jd_skills_json`)

        SELECT DISTINCT skill_name_flattened as content FROM skill_df
        CROSS JOIN UNNEST(skill.skills) AS skill_name_flattened
        '''
    , Env.config("_stage"))


if __name__ == '__main__':
    results = get_skills()
    topic_model = BERTopic()
    topics, probs = topic_model.fit_transform(results.content)

    groups = topic_model.get_topic_info()
    names = groups['Name']
    safe_send_bigquery(groups, 'temp.channtest', if_exists='replace')

    # topic_model.get_representative_docs() 번역 때리기
