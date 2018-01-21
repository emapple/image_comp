import quadtree as qt
import svd
import makeimage as mi
import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
    #datalist=mi.read_fits('images/uba10104m_d0m.fits')
    datalist=mi.read_fits('images/icsh10l9q_flt.fits')
    #data=[mi.make2n(datalist[1])]
    data=[datalist[0][:,:-1]]
    tree=qt.QuadTree(data[0])

    print 'done building tree'

    for i in np.arange(.05,.5,.05):
        tree.prune(i)
        tree.decompress()
        recon=qt.makedata(tree)
        data.append(recon.data)
        print 'done with {}'.format(i)
    
    print 'done pruning'

    for i in range(len(data)):
        plt.figure()
        plt.imshow(data[i],interpolation='none',cmap='gray')
        #plt.xlim([0,800])
        #plt.ylim([800,0])
        plt.title('tolerance={}'.format(i*.05))
    

    plt.show()
