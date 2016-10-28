import numpy as np

def maxdepth(data):
    """ Finds the tree depth of a square array """

    lside=len(data)
    n=0
    while lside>1:
        lside=lside/2
        n+=1
    return n

class QuadTree:
    leaves=[]
    allnodes=[]
    def __init__(self,data):
        self.data=np.array(data)
        depth=maxdepth(self.data)
        mini = 0
        minj=0
        maxi=len(data)-1
        maxj=len(data)-1
        self.mini=mini
        self.minj=minj
        self.maxi=maxi
        self.maxj=maxj

        midi=0.5*(self.mini+self.maxi)
        midj=0.5*(self.minj+self.maxj)

        self.sizei=self.maxi-self.mini
        self.sizej=self.maxj-self.minj

        self.children=[]

        if depth>0:
            data_nw=data[minj:int(np.ceil(midj)),mini:int(np.ceil(midi))]
            data_ne=data[minj:int(np.ceil(midj)),int(np.ceil(midi)):maxi+1]
            data_sw=data[int(np.ceil(midj)):maxj+1,mini:int(np.ceil(midi))]
            data_se=data[int(np.ceil(midj)):maxj+1,int(np.ceil(midi)):maxi+1]
            if data_nw.shape!=(0,0):
                self.children.append(QuadTree(data_nw))
            if data_ne.shape!=(0,0):
                self.children.append(QuadTree(data_ne))
            if data_sw.shape!=(0,0):
                self.children.append(QuadTree(data_sw))
            if data_se.shape!=(0,0):
                self.children.append(QuadTree(data_se))

    def displaytree(self,depth):
        if depth==0:
            print self.data
        else:
            for child in self.children:
                child.displaytree(depth-1)

if __name__=='__main__':
    table=np.array([[0,1,2,3],[5,3,6,4],[6,6,7,4],[6,4,7,5]])
    testtree=QuadTree(table)

    testtree.displaytree(0)
    testtree.displaytree(1)
    testtree.displaytree(2)
