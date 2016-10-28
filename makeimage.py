import numpy as np

def make2n(table,default=0):
    """ Takes a square table and makes it divisble for a quadtree"""
    try:
        table=table.tolist()
    except AttributeError:
        pass
    lside=len(table)
    ltest=float(lside)
    ncount=0
    while ltest >1.:
        ltest=ltest/2.
        ncount+=1
    ladd=2**ncount-lside
    for row in table:
        for i in range(ladd):
            row.append(default)
    for i in range(ladd):
        table.append([])
        for j in range(2**ncount):
            table[-1].append(default)
    table=np.array(table)
    return table
    

