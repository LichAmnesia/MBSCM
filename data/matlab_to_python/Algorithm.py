# @Author: Sarah
# @Date: 2016-11-26 11:38:09
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

B = B.toarray()
U = squeeze(asarray(U)) # np matrix to np array

U_ = U.conj().T # U transpose

a = (U_.dot(B)) * U_  # component of M7 formulation
b = (B.dot(U)) * U
c = (U.dot(U_)) * B
G,H,L = toarray(a,b,c) # to array

### Form motif adjacency matrix. For different motifs,
### replace this line with another matrix formulation
W = G + H + L # motif M7 matrix formulation, MotifSpectralPartition M7

### Compute eigenvector of motif normalized Lapacian
tempDsqrt = diag(W.sum(axis=0))
Dsqrt = linalg.matrix_power(tempDsqrt,-1/2) # numpy.ndarray


size = W.shape[0]
tempI = matrix(identity(size))
I = toarray(tempI)
tempD = Dsqrt.dot(W)
tempL = tempD.dot(Dsqrt)
Lap = toarray(tempL)
Ln = array(I) - array(Lap) # normalized laplacian, numpy.ndarray


lam,tempZ = linalg.eig(Ln) # eignvalues and eigenvectors

templam = array([lam[0][0],lam[0][1]])
lambdas_ = diag(templam)

lambdas = lambdas_.argsort()[:len(lambdas_)]
eig_order = diag(lambdas).argsort()[:len(diag(lambdas))]

Z_ = hstack((tempZ[:,[0]],tempZ[:,[1]]))
Z = Z_.conj().T
Z.shape = (10,2)

y = Dsqrt.dot(Z[:,eig_order[-1]])

### Linear time sweep procedure
#order = y.argsort()[:len(y)]
order = y.argsort(axis=0)
C = A
C_sums = (C.sum(axis=1))
idx = order
C_sums = C_sums[idx]


vol = cumsum(C_sums)
volumes = vol.conj().T # made it to column

sum_A = (A.sum(axis=0))
sum_A_ = sum(sum_A)
volumes_other = sum_A_ * ones((order.shape[0],1)) - volumes

T = (2*(tril(C).sum(axis=1)))
T.shape = (10,1)
cum =  cumsum(C_sums - T)
cum.shape = (10,1)

conductances = cum / minimum(volumes, volumes_other)
conductances.shape = (10,1)

split = conductances.argmin(0) # it is for because index starts from 0 instead of 1
split=squeeze(split)

S = order[0:split+1]
Sbar = order[split+1:]









