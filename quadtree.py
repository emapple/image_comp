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
    def __init__(self,data,parent=None):
        self.parent=parent
        if self.parent is None:
            self.depth=0
            #self.tot_depth=maxdepth(self.data) # total depth of quadtree, root to leaves
        else:
            self.depth=parent.depth+1
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

        if mdepth>0:
            self.children=[]
            data_nw=data[minj:int(np.ceil(midj)),mini:int(np.ceil(midi))]
            data_ne=data[minj:int(np.ceil(midj)),int(np.ceil(midi)):maxi+1]
            data_sw=data[int(np.ceil(midj)):maxj+1,mini:int(np.ceil(midi))]
            data_se=data[int(np.ceil(midj)):maxj+1,int(np.ceil(midi)):maxi+1]
            if data_nw.shape!=(0,0):
                self.children.append(QuadTree(data_nw,parent=self))
            if data_ne.shape!=(0,0):
                self.children.append(QuadTree(data_ne,parent=self))
            if data_sw.shape!=(0,0):
                self.children.append(QuadTree(data_sw,parent=self))
            if data_se.shape!=(0,0):
                self.children.append(QuadTree(data_se,parent=self))
        else:
            self.children=None

    def prune(self,tolerance):
        if self.children is not None:
            for child in self.children:
                child.prune(tolerance)
        else: # does this if no children
            if self.parent.children is not None: # asserting siblings still exist; may have been removed in previous iteration
                lnorm=np.sqrt(sum([child.value**2 for child in self.parent.children])) # calculates lnorm from siblings
                diffs=[abs(lnorm-child.value)/lnorm for child in self.parent.children]
                if max(diffs)<tolerance:
                    self.parent.children=None
        

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
