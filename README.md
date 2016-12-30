# MBSCM
Python implementation for Motif-based spectral clustering method for single cluster.

Motif-based spectral clustering method is an algorithm posted in [Higher-order Organization of Complex Networks](http://snap.stanford.edu/higher-order/higher-order-science16.pdf) by Austin R. Benson, David F. Gleich, and Jure Leskovec.

The implemented [Code](https://github.com/LichAmnesia/MBSCM/blob/master/data/matlab_to_python/Algorithm.py) is here.

# Algorithm
The algorithm performs the following steps:

1. input Graph G, unweighted and directed.
2. Using G form a new weighted graph W.
3. Apply spectral clustering on W.
4. Output the clusters for each 7 motifs.
5. Examine each output to see which motif has thebest cluster.
6. Return  best  cluster  and  the  motif  used  to  get that cluster.



# Reference
Higher-order Organization of Complex Networks. Austin R. Benson, David F. Gleich, and Jure Leskovec. Science, vol. 353, no. 6295, pp. 163-166, 2016.
