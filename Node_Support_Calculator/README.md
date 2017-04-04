# Node_Support_Index_Calculator.py

usage: python Node_Support_Index_Calculator.py [full path to directory of trees]

example:

'python Node_Support_Index_Calculator.py user/bin/TreeFiles'

Will calculate how many nodes of the total internal nodes of a bootstrapped
tree are above 70% support. I call this the Node Support Index, which is on
a scale of 0 to 1. An index of 1 indicates all nodes are above 70%, whereas
a score of 0.5 indicates only half the total nodes are above 70% support.


This script will iterate over all the tree files in a given directory.
I assume here that you've used RAxML to do boostrapping, and this script
will look for the default output files that should be named
"RAxML_bipartitions.SOMETHING". The script will use the SOMETHING part of
the name to label the different loci in the output, so make sure these aren't
identical. The output file will be tab-delimited and look like this:


Locus    internal_nodes  supported_nodes  node_support_index

contig4  268             189              0.71

contig5  274             163              0.59


The index can be used to find the most informative of your loci, or
draw comparisons between locus length or number of variable sites, 
for example. I find it useful to quantify information content of
sequence capture loci in various ways, including this method.

Written for Python 2.7.3

External Dependencies: ete2, NUMPY
-Install Python ETE2 toolkit (information at http://etetoolkit.org) 
 
 
# Dan Portik

daniel.portik@uta.edu

August 2016
