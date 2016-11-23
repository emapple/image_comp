import numpy as np

def maxdepth(data):
    """ Finds the tree depth of a square array """

    lside=float(len(data))
    n=0
    while lside>1:
        lside=lside/2
        n+=1
    return n


class QuadTree:
    leaves=[]
    allnodes=[]
    def __init__(self,data,parent_depth=None):
        if parent_depth is None:
            self.depth=0
            self.tot_depth=maxdepth(self.data) # total depth of quadtree, root to leaves
        else:
            self.depth=parent_depth+1
            self.tot_depth=
        self.data=np.array(data)
        self.value=np.mean(self.data)
        mdepth=maxdepth(self.data) # remaining levels of recursion
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

        if mdepth>0:
            data_nw=data[minj:int(np.ceil(midj)),mini:int(np.ceil(midi))]
            data_ne=data[minj:int(np.ceil(midj)),int(np.ceil(midi)):maxi+1]
            data_sw=data[int(np.ceil(midj)):maxj+1,mini:int(np.ceil(midi))]
            data_se=data[int(np.ceil(midj)):maxj+1,int(np.ceil(midi)):maxi+1]
            if data_nw.shape!=(0,0):
                self.children.append(QuadTree(data_nw,parent_depth=self.depth))
            if data_ne.shape!=(0,0):
                self.children.append(QuadTree(data_ne,parent_depth=self.depth))
            if data_sw.shape!=(0,0):
                self.children.append(QuadTree(data_sw,parent_depth=self.depth))
            if data_se.shape!=(0,0):
                self.children.append(QuadTree(data_se,parent_depth=self.depth))
            else:
                self.children=None

    def prune(self,tolerance):
        if self.depth<max:
            for child in self.children:
                child.prune(tolerance)
        else:
            a
                

    def displaytree(self,depth):
        if depth==0:
            print self.data
        else:
            for child in self.children:
                child.displaytree(depth-1)

#class TreeNodes:
#    leaves=[]
#    allnodes=[]
#    def __init__(self,tree):
#        if tree.children is None:
#            leaves.append(tree)
#        else:
            


if __name__=='__main__':
    table=np.array([[0,1,2,3],[5,3,6,4],[6,6,7,4],[6,4,7,5]])
    testtree=QuadTree(table)

    testtree.displaytree(0)
    testtree.displaytree(1)
    testtree.displaytree(2)
