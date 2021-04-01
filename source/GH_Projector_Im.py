import numpy as np
import numpy.linalg as npl 
def Projector_im(A):
    #This function defines the projection operator on the orthogonal space of the Image space of a matrix A
    
    m,n=np.shape(A) 
    return np.eye(n)- np.dot(A, npl.inv(np.dot(A.T,A)).dot(A.T))
