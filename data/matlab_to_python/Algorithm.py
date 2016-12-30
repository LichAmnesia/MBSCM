# @Author: Sarah
# @Date: 2016-12-02 11:40:09
# @Last Modified by: Shen
# The python implmentation for Higher-order Organization of Complex Networks. Austin R. Benson, David F. Gleich, and Jure Leskovec. Science, vol. 353, no. 6295, pp. 163-166, 2016.

from sklearn.metrics.cluster import normalized_mutual_info_score
import networkx as nx
from scipy import sparse
from numpy import *
from scipy.sparse import identity
import collections
import time

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

filename = "reddit.txt"
mynumbers = []
with open(filename) as f:
    for line in f:
        mynumbers.append([int(n) for n in line.strip().split()])
for pair in mynumbers:
    try:
        x,y = pair[0],pair[1]
        # Do Something with x and y
        G.add_edge(x,y)
    except IndexError:
        print "A line in the file doesn't have enough entries."

# example in the ppt
# spectral partitioning for motif M7
# input directed, unweighted graph

# G.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6),
#                   (2,1),(2,3),(2,4),(2,5),(6,2),(6,7),
#                   (7,2),(7,6),
#                   (8,2),(8,6),(8,9),(8,10),
#                   (9,8),(9,6),(9,7),(9,10)])

start = time.time()

A = nx.adjacency_matrix(G)  # input
num_nodes = G.number_of_nodes()

def M1(U, A, B):
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T  # U transpose
    a = U.dot(U) * U_
    b = a.conj().T
    C, C_ = toarray(a, b)
    W = C + C_
    return W

def M2(U, A, B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T  # U transpose
    a = (B.dot(U)) * U_
    b = (U.dot(B)) * U_
    c = (U.dot(U)) * B
    G, H, L = toarray(a, b, c)  # to array

    C = G + H + L
    C_ = C.conj().T
    W = C + C_
    return W

def M3(U, A, B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T  # U transpose
    a = (B.dot(B)) * U
    b = (B.dot(U)) * B
    c = (U.dot(B)) * B
    G, H, L = toarray(a, b, c)  # to array

    C = G + H + L
    C_ = C.conj().T
    W = C + C_
    return W

def M4(U, A, B):
    B = B.toarray()
    W = (B.dot(B) * B)
    return W

def M5(U, A, B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T  # U transpose
    a = (U.dot(U)) * U
    b = (U.dot(U_)) * U
    c = (U_.dot(U)) * U
    G, H, L = toarray(a, b, c)  # to array

    C = G + H + L
    C_ = C.conj().T
    W = C + C_
    return W

def M6(U, A, B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T  # U transpose
    a = (U.dot(B)) * U

    b = (B.dot(U_)) * U_
    c = (U_.dot(U)) * B
    G, H, L = toarray(a, b, c)  # to array
    W = G + H + L
    return W

def M7(U, A, B):
    B = B.toarray()
    U = squeeze(asarray(U))  # np matrix to np array
    U_ = U.conj().T  # U transpose
    a = (U_.dot(B)) * U_
    b = (B.dot(U)) * U
    c = (U.dot(U_)) * B
    G, H, L = toarray(a, b, c)  # to array
    W = G + H + L
    return W

A = nx.adjacency_matrix(G)  # adjacency matrix
A = A.todense()

a = array(A)
a_ = a.conj().T  # transpose of a

B = a & a_  # bidirectional links, or can use logical_and(a, a_)
sA = sparse.csr_matrix(B)  # sponses part in matlab
y = sA.copy().tocsr()
y.data.fill(1)
B = y
U = A - B  # unidirectional links

# Form motif adjacency matrix. For different motifs,
tempW = []
print 'M1'
tempW.append(M1(U,A,B))
print 'M2'
tempW.append(M2(U,A,B))
print 'M3'
tempW.append(M3(U,A,B))
print 'M4'
tempW.append(M4(U,A,B))
print 'M5'
tempW.append(M5(U, A, B))
print 'M6'
tempW.append(M6(U,A,B))
print 'M7'
tempW.append(M7(U,A,B))

min_con = []  # min conductance list in each motifs
list = []  # order list
s_list = []  # split list

# Compute eigenvectors and eigenvalues of motif normalized Lapacian
count = 1
for W in tempW:
    print ''
    print 'M', count
    count += 1
    Dsqrt = (W.sum(axis=0))
    t = []
    for i in range(0, len(Dsqrt)):
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

    lam, tempZ = linalg.eig(Ln)  # lam: eignvalues and tempZ: eigenvectors
    tempZ.shape = (num_nodes,num_nodes)

    idx = argsort(lam)
    templam = array([lam[0][idx[0][0]], lam[0][idx[0][1]]])  # to extract 1st and 2nd smallest eigenvales

    lambdas_ = diag(templam)

    Z = hstack((tempZ[:, [[idx[0][0]]]], tempZ[:, [[idx[0][1]]]]))  # 1st and 2nd smallest eigenvectors
    Z.shape = (num_nodes,2)

    # order eig
    lambdas = lambdas_.argsort()[:len(lambdas_)]
    eig_order = diag(lambdas).argsort()[:len(diag(lambdas))]
    y = Dsqrt.dot(Z[:, eig_order[-1]])
    y.shape = (num_nodes,1)

    # Linear time sweep procedure
    order = y.argsort(axis=0)
    list.append(order.tolist())

    C = W
    idx = order
    W = W[idx]
    W.shape = (num_nodes,num_nodes)

    W = W[:, idx]
    C = W
    W.shape = (num_nodes, num_nodes)

    C_sums = (C.sum(axis=1))
    C_sums.shape = (num_nodes, 1)

    volumes = cumsum(C_sums)
    volumes.shape = (num_nodes,1)

    sum_W = (W.sum(axis=0))
    sum_W_ = sum(sum_W)
    volumes_other = sum_W_ * ones((order.shape[0], 1)) - volumes

    T = (2 * (tril(C).sum(axis=1)))  # compute conductances
    T.shape = (num_nodes,1)

    cum = cumsum(C_sums - T)
    cum.shape = (num_nodes,1)


    seterr(divide='ignore', invalid='ignore')  # set to ignore warning
    conductances = cum / minimum(volumes, volumes_other)
    conductances.shape = (num_nodes, 1)

    try:
        split = nanargmin(conductances)
        s_list.append(split)
        min_con.append(conductances[split])
        S = order[0:split + 1]
        Sbar = order[split + 1:]

        print 'S'
        print S

        print 'Sbar'
        print Sbar

        print 'conductances'
        print conductances
    except ValueError:
        split = 0
        s_list.append(split)
        min_con.append(conductances[split])
        S = order[0:split + 1]
        Sbar = order[split + 1:]
        print 'all nan'

        print 'S'
        print S

        print 'Sbar'
        print Sbar

        print 'conductances'
        print conductances

print 'minimal conductances'
print min_con
idx = nanargmin(min_con)

print ''
print 'Best partition with Motif M', idx + 1

split = s_list[idx]

print 'S'
print list[idx][0:split + 1]

print 'Sbar'
print list[idx][split + 1:]

with_labels = []
filename = 'reddit_metadata.txt'
mynumbers = []
with open(filename) as f:
    for line in f:
        mynumbers.append([int(n) for n in line.strip().split()])
for pair in mynumbers:
    x, y = pair[0], pair[1]
    with_labels.append(pair[1])

print 'with_labels'
print with_labels

r2 = list[idx][0:split+1]
r1 = list[idx][split+1:]

l1 = [x[0] for x in r1] # list of list to list
l2 = [x[0] for x in r2]

n1 = map(lambda x:x+1, l1)
print 'n1'
print n1
n2 = map(lambda x:x+1, l2)
print 'n2'
print n2

new_list = []
new_list.append(n1)
new_list.append(n2)

print 'new_list',new_list

p = new_list

d = {}
count = 1
for i in p:
    for k in i:
        (key,val) = k,count
        d[int(key)] = val
    count += 1
l = collections.OrderedDict(d)

without_labels = l.values()
print 'without_labels'
print without_labels

end = time.time()

print 'time',end-start

n = normalized_mutual_info_score(with_labels, without_labels)
print ''
print 'NMI',n




