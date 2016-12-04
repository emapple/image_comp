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
            self.tot_depth=maxdepth(data) # total depth of quadtree, root to leaves
        else:
            self.depth=parent.depth+1
            self.tot_depth=parent.tot_depth
        self.data=np.array(data)
        #self.value=np.mean(self.data)
        self.var=None
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
            self.data=[child.data for child in self.children]
            self.value=np.mean([child.value for child in self.children])
            sortlist=np.sort([child.value for child in self.children])
            varvalue=(sortlist[-1]-sortlist[0])/self.value
            comparevar=max([child.var for child in self.children])
            if varvalue<comparevar:
                self.var=comparevar
            else:
                self.var=varvalue
            
        else:
            self.children=None
            self.value=np.mean(self.data)
            self.var=-1

    def prune(self,tolerance): # tolerance should be some acceptable difference in a quadrant normalized to the quadrant mean
        if self.children is not None:
            if self.var<tolerance:
                self.children=None
            else:
                for child in self.children:
                    child.prune(tolerance)
    
    def displaytree(self,depth):
        if depth==0:
            print self.data
        else:
            for child in self.children:
                child.displaytree(depth-1)

def decompress(tree):
    if tree.children is None:
        if tree.depth<tree.tot_depth:
            tree.children=[QuadTree([tree.value]),QuadTree([tree.value]),QuadTree([tree.value]),QuadTree([tree.value])]
            for child in tree.children:
                child.tot_depth=tree.tot_depth
                decompress(child)
    else:
        for child in tree.children:
            decompress(child)
        

#    def prune(self,tolerance):
#        if self.children is not None:
#            for child in self.children:
#                child.prune(tolerance)
#        else: # does this if no children
#            if self.parent.children is not None: # asserting siblings still exist; may have been removed in previous iteration
#                lnorm=np.sqrt(sum([child.value**2 for child in self.parent.children])) # calculates lnorm from siblings
#                diffs=[abs(lnorm-child.value)/lnorm for child in self.parent.children]
#                if max(diffs)<tolerance:
#                    self.parent.children=None
        
#    def setvars(self):
#        if self.children is not None:
#            if self.children[0].var is None or self.children[1].var is None or self.children[2].var is None or self.children[3].var is None:
#                for child in self.children:
#                    child.setvars()
#            else:
#                if self.
#        else:
#            if self.parent.var is None:
#                sortlist=np.sort([child.value for child in self.parent.children])
#                varvalue=(sortlist[-1]-sortlist[0])/self.parent.value
#                self.parent.var = 
                

       
#class Nodes:
#    def __init__(self,tree):
#        self.tree=tree
#        self.tot_depth=maxdepth(tree.data)
#
#    def nodevalues(self,depth):
#        nodes=[]
#        if depth==0:
#            nodes.append(self.value)
#        else:
#            for child in self.children:
#                if child is not None:
                
            


if __name__=='__main__':
    table=np.array([[0,1,2,3],[5,3,6,4],[6,6,7,4],[6,4,7,5]])
    testtree=QuadTree(table)

    testtree.displaytree(0)
    testtree.displaytree(1)
    testtree.displaytree(2)
