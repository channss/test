class parent(object):
    def __init__(self,p1,p2, asdf):
        super(parent, self).__init__()
        self.asdf = {}
        self.asdf['asdf'] = asdf
        self.p1= p1
        self.p2= p2

class child(parent):
    def __init__(self,p1,p2,p3,asdf):
        super(child,self).__init__(p1, p2, asdf)
        # self.asdf['asdf'] = asdf
        self.p3 = p3


child1 = child(1,2,3, 'asdf')
child2 = child(4,5,6, 'qwer')
# print(child1.p1, child1.p2, child1.p3)

a = ['1','2','3','4','5']
l = map(int, a)