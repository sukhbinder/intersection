import numpy as np
import matplotlib.pyplot as plt
"""
Sukhbinder
5 April 2017

Based on:
"""

def _rectangle_intersection_(x1,y1,x2,y2):
    n1=x1.shape[0]-1
    n2=x2.shape[0]-1
    S1=np.tile(np.c_[x1[:-1],x1[1:]].min(axis=1),(n2,1)).T
    S2=np.tile(np.c_[x2[:-1],x2[1:]].max(axis=1),(n1,1))
    S3=np.tile(np.c_[x1[:-1],x1[1:]].max(axis=1),(n2,1)).T
    S4=np.tile(np.c_[x2[:-1],x2[1:]].min(axis=1),(n1,1))
    S5=np.tile(np.c_[y1[:-1],y1[1:]].min(axis=1),(n2,1)).T
    S6=np.tile(np.c_[y2[:-1],y2[1:]].max(axis=1),(n1,1))
    S7=np.tile(np.c_[y1[:-1],y1[1:]].max(axis=1),(n2,1)).T
    S8=np.tile(np.c_[y2[:-1],y2[1:]].min(axis=1),(n1,1))

    C1=np.less_equal(S1,S2)
    C2=np.greater_equal(S3,S4)
    C3=np.less_equal(S5,S6)
    C4=np.greater_equal(S7,S8)

    ii,jj=np.nonzero(C1 & C2 & C3 & C4)
    return ii,jj

def intersection(x1,y1,x2,y2):
    """
INTERSECTIONS Intersections of curves.
   Computes the (x,y) locations where two curves intersect.  The curves
   can be broken with NaNs or have vertical segments.

usage:
x,y=intersection(x1,y1,x2,y2)

    Example:
    a, b = 1, 2
    phi = np.linspace(3, 10, 100)
    x1 = a*phi - b*np.sin(phi)
    y1 = a - b*np.cos(phi)

    x2=phi
    y2=np.sin(phi)+2
    x,y=intersection(x1,y1,x2,y2)

    plt.plot(x1,y1,c='r')
    plt.plot(x2,y2,c='g')
    plt.plot(x,y,'*k')
    plt.show()

    """
    ii,jj=_rectangle_intersection_(x1,y1,x2,y2)
    n=len(ii)

    dxy1=np.diff(np.c_[x1,y1],axis=0)
    dxy2=np.diff(np.c_[x2,y2],axis=0)

    T=np.zeros((4,n))
    AA=np.zeros((4,4,n))
    # for i in range(n):
    #     aview=AA[:,:,i]
    #     aview[np.ix_([0,1],[2])]=-1
    #     aview[np.ix_([2,3],[3])]=-1
    #     aview[np.ix_([0,2],[0])]=dxy1[ii[i],:][:,np.newaxis]
    #     aview[np.ix_([1,3],[1])]=dxy2[jj[i],:][:,np.newaxis]

    AA[0:2,2,:]=-1
    AA[2:4,3,:]=-1
    AA[0::2,0,:]=dxy1[ii,:].T
    AA[1::2,1,:]=dxy2[jj,:].T

    BB=np.zeros((4,n))
    BB[0,:]=-x1[ii].ravel()
    BB[1,:]=-x2[jj].ravel()
    BB[2,:]=-y1[ii].ravel()
    BB[3,:]=-y2[jj].ravel()

    for i in range(n):
        try:
            T[:,i]=np.linalg.solve(AA[:,:,i],BB[:,i])
        except:
            T[:,i]=np.NaN


    in_range= (T[0,:] >=0) & (T[1,:] >=0) & (T[0,:] <=1) & (T[1,:] <=1)

    xy0=T[2:,in_range]
    xy0=xy0.T
    return xy0[:,0],xy0[:,1]


if __name__ == '__main__':

    # a piece of a prolate cycloid, and am going to find
    a, b = 1, 2
    phi = np.linspace(3, 10, 100)
    x1 = a*phi - b*np.sin(phi)
    y1 = a - b*np.cos(phi)

    x2=phi
    y2=np.sin(phi)+2
    x,y=intersection(x1,y1,x2,y2)
    plt.plot(x1,y1,c='r')
    plt.plot(x2,y2,c='g')
    plt.plot(x,y,'*k')
    plt.show()
