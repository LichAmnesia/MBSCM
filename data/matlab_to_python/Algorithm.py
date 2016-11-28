# @Author: Sarah
# @Date: 2016-11-28 01:32:09
# @Last Modified by: Sarah



import networkx as nx
from scipy import sparse
from numpy import *

def tomat(*Z):
    """Converts the list of arrays in *Z to matrices"""
    Out = []
    for iter in Z:
        iter = mat(iter)
        Out.append(iter)
    return Out


def toarray(*Z):
    """Converts the list of matrices in *Z to arrays"""
    Out = []
    for iter in Z:
        iter = array(iter)
        Out.append(iter)
    return Out

# example in the ppt
# spectral partitioning for motif M7
# input directed, unweighted graph
G = nx.DiGraph()
G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6),
                  (2,1),(2,3),(2,4),(2,5),(6,2),(6,7),
                  (7,2),(7,6),
                  (8,2),(8,6),(8,9),(8,10),
                  (9,8),(9,6),(9,7),(9,10)])


A = nx.adjacency_matrix(G)
A = A.todense()

a = array(A)
a_ = a.conj().T # transpose of a


B = a & a_ # bidirectional links, you can use logical_and(a, a_)
sA = sparse.csr_matrix(B) # sponses part in matlab
y = sA.copy().tocsr()
y.data.fill(1)
B = y
U = A - B  # unidirectional links


# Form motif adjacency matrix. For different motifs,
# replace this line with another matrix formulation
B = B.toarray()
U = squeeze(asarray(U)) # np matrix to np array
U_ = U.conj().T # U transpose
a = (U_.dot(B)) * U_  # component of M7 formulation
b = (B.dot(U)) * U
c = (U.dot(U_)) * B
G,H,L = toarray(a,b,c) # to array
W = G + H + L # motif M7 matrix formulation, MotifSpectralPartition M7


# Compute eigenvector of motif normalized Lapacian
Dsqrt = (W.sum(axis=0))
#Dsqrt.shape =(size(Dsqrt),1)
Dsqrt =  Dsqrt ** (-1.0/2.0)  # exception handling needed for value zero
Dsqrt = diag(Dsqrt)

size = W.shape[0]
tempI = matrix(identity(size))
I = toarray(tempI)
tempD = Dsqrt.dot(W)
tempL = tempD.dot(Dsqrt)
Lap = toarray(tempL)
Ln = -array(Lap)
Ln[Ln == -0] = 0
print 'Ln'
print Ln

lam,tempZ = linalg.eig(Ln) # lam: eignvalues and tempZ: eigenvectors
tempZ.shape = (10,10) # to extract 1st and 2nd smallest eigenvectors

templam = array([lam[0][0],lam[0][1]]) # to extract 1st and 2nd smallest eigenvectors
lambdas_ = diag(templam)

Z = hstack((tempZ[:,[[0]]],tempZ[:,[[1]]]))
Z.shape = (10,2)

# order eig
lambdas = lambdas_.argsort()[:len(lambdas_)]
eig_order = diag(lambdas).argsort()[:len(diag(lambdas))]
y = Dsqrt.dot(Z[:,eig_order[-1]])

# Linear time sweep procedure
order = y.argsort(axis=0)
C = W
C_sums = (C.sum(axis=1))
idx = order
C_sums = C_sums[idx]
C_sums.shape = (10,1)

volumes = cumsum(C_sums)
volumes.shape = (10,1)# made it to column

sum_W = (W.sum(axis=0))
sum_W_ = sum(sum_W)
volumes_other = sum_W_ * ones((order.shape[0],1)) - volumes

T = (2*(tril(C).sum(axis=1))) # compute conductances
T.shape = (10,1)
cum = cumsum(C_sums - T)
cum.shape = (10,1)
conductances = cum / minimum(volumes, volumes_other)
conductances.shape = (10,1)

split = nanargmin(conductances)
S = order[0:split+1]
Sbar = order[split+1:]

print 'S'
print S

print 'Sbar'
print Sbar

print 'conductances'
print conductances






