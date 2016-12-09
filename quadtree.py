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
        #self.data=np.array(data)
        #self.value=np.mean(self.data)
        self.var=None
        mdepth=maxdepth(data) # remaining levels of recursion
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

        ceilj=np.ceil(midj)
        ceili=np.ceil(midi)

        self.sizei=self.maxi-self.mini
        self.sizej=self.maxj-self.minj

        if mdepth>0:
            self.children=[]
            data_nw=data[minj:int(ceilj),mini:int(ceili)]
            data_ne=data[minj:int(ceilj),int(ceili):maxi+1]
            data_sw=data[int(ceilj):maxj+1,mini:int(ceili)]
            data_se=data[int(ceilj):maxj+1,int(ceili):maxi+1]
            if data_nw.shape!=(0,0):
                self.children.append(QuadTree(data_nw,parent=self))
            if data_ne.shape!=(0,0):
                self.children.append(QuadTree(data_ne,parent=self))
            if data_sw.shape!=(0,0):
                self.children.append(QuadTree(data_sw,parent=self))
            if data_se.shape!=(0,0):
                self.children.append(QuadTree(data_se,parent=self))
            #self.data=[child.data for child in self.children]
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
            self.value=np.mean(data)
            self.var=-1

    def prune(self,tolerance): # tolerance should be some acceptable difference in a quadrant normalized to the quadrant mean
        if self.children is not None:
            if self.var<tolerance:
                self.children=None
            else:
                for child in self.children:
                    child.prune(tolerance)
    
#    def displaytree(self,depth):
#        if depth==0:
#            #print self.data
#        else:
#            for child in self.children:
#                child.displaytree(depth-1)

    def decompress(self):
        if self.children is None:
            if self.depth<self.tot_depth:
                self.children=[QuadTree([self.value]),QuadTree([self.value]),QuadTree([self.value]),QuadTree([self.value])]
                for child in self.children:
                    child.tot_depth=self.tot_depth
                    child.depth=self.depth+1
                    child.decompress()
        else:
            for child in self.children:
                child.decompress()

class makedata:
    
    def __init__(self,tree):
        self.data=np.zeros((2**tree.tot_depth,2**tree.tot_depth))
        self.data[:]=np.NAN
        self.tree=tree
        self.build(tree)
        
    def build(self,tree,midi=None,midj=None):
        if midi is None:
            midi=0.5*len(self.data)
        if midj is None:
            midj=0.5*len(self.data[0])
        if tree.depth<tree.tot_depth-1:
            self.build(tree.children[0],midi=midi-2**(tree.tot_depth-tree.depth-2),midj=midj-2**(tree.tot_depth-tree.depth-2))
            self.build(tree.children[1],midi=midi-2**(tree.tot_depth-tree.depth-2),midj=midj+2**(tree.tot_depth-tree.depth-2))
            self.build(tree.children[2],midi=midi+2**(tree.tot_depth-tree.depth-2),midj=midj-2**(tree.tot_depth-tree.depth-2))
            self.build(tree.children[3],midi=midi+2**(tree.tot_depth-tree.depth-2),midj=midj+2**(tree.tot_depth-tree.depth-2))
        else:
            self.data[int(midi-1),int(midj-1)]=tree.children[0].value
            self.data[int(midi-1),int(midj)]=tree.children[1].value
            self.data[int(midi),int(midj-1)]=tree.children[2].value
            self.data[int(midi),int(midj)]=tree.children[3].value


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
