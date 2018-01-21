import numpy as np
from astropy.io import fits

def make2n(table_in,default=100):
    """ Takes a rectangular table and makes it divisble for a quadtree"""
    try:
        table=table_in.tolist()
    except AttributeError:
        table=table_in[:]
    lside1=len(table)
    lside2=len(table[0])
    ncount=0
    ncount1=np.ceil(np.log2(lside1))
    ncount2=np.ceil(np.log2(lside2))
    ncount=int(max(ncount1,ncount2))
    ladd1=2**ncount-lside1
    ladd2=2**ncount-lside2
    for row in table:
        for i in range(ladd2):
            row.append(default)
    for i in range(ladd1):
        table.append([default]*(2**ncount))
    table=np.array(table)
    return table
    
def read_fits(filename):
    """ Returns image data for all images in a fits file"""
    hdulist=fits.open(filename)
    data=np.array([hdulist[i].data for i in range(1,len(hdulist))])
    return data
