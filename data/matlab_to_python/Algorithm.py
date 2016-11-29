# @Author: Sarah
# @Date: 2016-11-29 11:40:09
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


A = nx.adjacency_matrix(G) # input

def M1(U,A,B):
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T  # U transpose
    a = U.dot(U) * U_
    b = a.conj().T
    C, C_ = toarray(a, b)
    W = C + C_
    return W

def M2(U,A,B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T         # U transpose
    a = (B.dot(U)) * U_
    b = (U.dot(B)) * U_
    c = (U.dot(U)) * B
    G, H, L = toarray(a, b, c)  # to array

    C = G + H + L
    C_ = C.conj().T
    W = C + C_
    return W

def M3(U,A,B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T         # U transpose
    a = (B.dot(B)) * U
    b = (B.dot(U)) * B
    c = (U.dot(B)) * B
    G, H, L = toarray(a, b, c)  # to array

    C = G + H + L
    C_ = C.conj().T
    W = C + C_
    return W

def M4(U,A,B):
    B = B.toarray()
    W = (B.dot(B) * B)
    return W

def M5(U,A,B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T         # U transpose
    a = (U.dot(U)) * U
    b = (U.dot(U_)) * U
    c = (U_.dot(U)) * U
    G, H, L = toarray(a, b, c)  # to array

    C = G + H + L
    C_ = C.conj().T
    W = C + C_
    return W

def M6(U,A,B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T         # U transpose
    a = (U.dot(B)) * U_

    b = (B.dot(U_)) * U_
    c = (U_.dot(U_)) * B
    G, H, L = toarray(a, b, c)  # to array
    W = G + H + L
    return W

def M7(U,A,B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T         # U transpose
    a = (U_.dot(B)) * U_
    b = (B.dot(U)) * U
    c = (U.dot(U_)) * B
    G, H, L = toarray(a, b, c)  # to array
    W = G + H + L
    return W

A = nx.adjacency_matrix(G) # adjacency matrix
A = A.todense()

a = array(A)
a_ = a.conj().T     # transpose of a


B = a & a_      # bidirectional links, or can use logical_and(a, a_)
sA = sparse.csr_matrix(B)   # sponses part in matlab
y = sA.copy().tocsr()
y.data.fill(1)
B = y
U = A - B       # unidirectional links


# Form motif adjacency matrix. For different motifs,
tempW = []
tempW.append(M1(U,A,B))
tempW.append(M2(U,A,B))
tempW.append(M3(U,A,B))
tempW.append(M4(U,A,B))
tempW.append(M5(U,A,B))
tempW.append(M6(U,A,B))
tempW.append(M7(U,A,B))

min_con = [] # min conductance list in each motifs
list = []    # order list
s_list = []  # split list

# Compute eigenvector of motif normalized Lapacian
count = 1
for W in tempW:
    print ''
    print 'M',count
    count += 1
    Dsqrt = (W.sum(axis=0))
    t = []
    for i in range(0,len(Dsqrt)):
        if Dsqrt[i] != 0:
            t.append(Dsqrt[i] ** (-1.0 / 2.0))
        else:
            t.append(0)

    Dsqrt = array(t)
    Dsqrt = diag(Dsqrt)

    size = W.shape[0]
    tempI = matrix(identity(size))
    I = toarray(tempI)

    tempD = Dsqrt.dot(W)

    tempL = tempD.dot(Dsqrt)
    Lap = toarray(tempL)
    Ln = -array(Lap)
    Ln[Ln == -0] = 0

    lam,tempZ = linalg.eig(Ln) # lam: eignvalues and tempZ: eigenvectors
    tempZ.shape = (10,10)      # to extract 1st and 2nd smallest eigenvectors

    templam = array([lam[0][0],lam[0][1]]) # to extract 1st and 2nd smallest eigenvales
    lambdas_ = diag(templam)

    Z = hstack((tempZ[:,[[0]]],tempZ[:,[[1]]])) # 1st and 2nd smallest eigenvectors
    Z.shape = (10,2)

    # order eig
    lambdas = lambdas_.argsort()[:len(lambdas_)]
    eig_order = diag(lambdas).argsort()[:len(diag(lambdas))]
    y = Dsqrt.dot(Z[:,eig_order[-1]])

    # Linear time sweep procedure
    order = y.argsort(axis=0)
    list.append(order.tolist())

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

    seterr(divide='ignore', invalid='ignore') # set to ignore warning
    conductances = cum / minimum(volumes, volumes_other)
    conductances.shape = (10,1)

    try:
        split = nanargmin(conductances)
        s_list.append(split)
        min_con.append(conductances[split])
        S = order[0:split+1]
        Sbar = order[split + 1:]

        # print 'S'
        # print S
        #
        # print 'Sbar'
        # print Sbar
        #
        # print 'conductances'
        # print conductances
    except ValueError:
          split = 0
          s_list.append(split)
          min_con.append(conductances[split])
          S = order[0:split + 1]
          Sbar = order[split + 1:]

          # print 'S'
          # print S
          #
          # print 'Sbar'
          # print Sbar
          #
          # print 'conductances'
          # print conductances



idx = nanargmin(min_con)

print ''
print 'Best partition with Motif M',idx+1

split = s_list[idx]

print 'S'
print list[idx][0:split+1]

print 'Sbar'
print list[idx][split+1:]


