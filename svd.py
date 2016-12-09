import numpy as np

def PCA_compress(data, num_comp):
    """ Returns compressed data using PCA with num_comp eigenvalues """
    u,s,vT=np.linalg.svd(data)
    ucut=u[:,:num_comp]
    scut=np.diag(s)[:num_comp,:num_comp]
    vTcut=vT[:num_comp,:]
    return ucut.dot(scut).dot(vTcut)
