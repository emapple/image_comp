import numpy as np

#class Node:
#    ROOT=0
#    BRANCH=1
#    LEAF=2
#    def __init__(self,parent,rect):
#        self.parent=parent
#        self.children=[None,None,None,None]
#        if self.parent==None:
#            self.depth=0
#        else:
#            self.depth=parent.depth+1
#        self.rect=rect
#        i1,j1,i2,j2=rect
#        if self.parent==None:
#            self.type=Node.ROOT
#        elif(i2-i1)<2:
#            self.type=Node.LEAF
#        else:
#            self.type=Node.BRANCH
#

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
    def __init__(self,data,mini=None,minj=None,maxi=None,maxj=None,depth=None):
        self.data=np.array(data)
        if depth is None:
            depth=maxdepth(self.data)
        if mini is None:
            mini = 0
        if minj is None:
            minj=0
        if maxi is None:
            maxi=len(data)-1
        if maxj is None:
            maxj=len(data)-1
        self.depth=depth
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
            data_ne=data[minj:int(np.ceil(midj)),int(np.floor(midi)):maxi+1]
            data_sw=[int(np.floor(midj)):maxj+1,mini:int(np.ceil(midi))]
            data_se=[int(np.floor(midj)):maxj+1,int(np.floor(midi)):maxi+1]
            
            #if data_nw.shape!=(1,1):
                #self.children.append(QuadTree(data_nw,


if __name__=='__main__':
    table=np.array([[0,1,2,3],[5,3,6,4],[6,6,7,4],[6,4,7,5]])
    testtree=QuadTree(table)
