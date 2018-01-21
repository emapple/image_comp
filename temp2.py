import quadtree as qt
import svd
import makeimage as mi
import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
    datalist=mi.read_fits('images/uba10104m_d0m.fits')
    #datalist=mi.read_fits('images/icsh10l9q_flt.fits')
    data=[datalist[1]]
    #data=[datalist[0][:,:-1]]
    
    for i in np.arange(100,0,-5):
        u,s,vt=svd.PCA_compress(data[0],i)
        data.append(u.dot(s).dot(vt))

    plt.figure()
    plt.imshow(data[0],interpolation='none',cmap='gray')
    plt.title('components=all')
    plt.xlim([0,800])
    plt.ylim([800,0])
    plt.savefig('svd_image/800.png')
    
    for i in range(1,len(data)):
        plt.figure()
        plt.imshow(data[i],interpolation='none',cmap='gray')
        plt.title('components={}'.format(100-(i-1)*5))
        plt.xlim([0,800])
        plt.ylim([800,0])
        plt.savefig('svd_image/{}.png'.format(100-(i-1)*5))

    plt.show()
