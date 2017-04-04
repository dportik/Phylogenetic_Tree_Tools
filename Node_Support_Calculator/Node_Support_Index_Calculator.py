import sys
import os
import subprocess as sp
import shutil
import numpy as np
from ete2 import Tree
'''
usage: python Node_Support_Index_Calculator.py [full path to directory of trees]

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

######################################################
Written for Python 2.7.3
DEPENDENCIES:
-ete2
  -Install Python ETE2 toolkit (information at http://etetoolkit.org) 
  -download from https://pypi.python.org/pypi/ete2/
  -unzip folder
  -cd into resulting folder and type 'python setup.py install' or 'sudo python setup.py install'
-numpy
######################################################

Dan Portik
daniel.portik@uta.edu
August 2016
'''

#===============================================================================================
#simple function for calculating NSI
def NSI_calc(x,y):
    percentage = float( ( float(x) / float(y)))
    percentage = np.around(percentage, decimals = 2)
    return percentage

#===============================================================================================
#Move to tree directory
tree_dir = sys.argv[1]
os.chdir(tree_dir)
print '\n', "Moving to {} to begin node support index calculations.".format(tree_dir)

#create empty list to populate with tree file names
tree_source = []

#search this directory for tree files
for filetype in os.listdir('.'):
    if filetype.startswith("RAxML_bipartitions."):
        if os.path.getsize(filetype) > int(0):
            tree_source.append(filetype)

#count how many tree files are in the list
tree_count = int(len(tree_source))
print '\n',"Number of trees to be included for node support index comparisons = {}".format(tree_count),'\n'

#initialize empty list to put the actual trees into
tree_shapes = []

#for every tree file in our tree_source list, get the tree shapes loaded
for t_file in tree_source:
    print "Reading tree file {}...".format(t_file)
    
    #use the ete Tree() function to grab info from the file, indicate format type 2 (all branches + leaf names + internal supports)
    t_shape = Tree(t_file, format=2)
    temp_list = []
    
    #append the tree shape and filename to a temp list, which then is appended to the tree_shapes list
    names = t_file.split('_bipartitions.')
    temp_list.append(names[1])
    temp_list.append(t_shape)
    tree_shapes.append(temp_list)
    
#===============================================================================================  
#Performing node support calculations on all trees in tree folder

#create an output file
out_name = 'Node_Support_Calculations.txt'
fh_out = open(out_name, 'a')
fh_out.write('Locus\tinternal_nodes\tsupported_nodes\tnode_support_index\n')

#loop through trees in our list of [[tree_names, tree_shapes], etc]
for tree in tree_shapes:
    print "Examining tree {}...".format(tree[0])

    #start two simple counters, one for total nodes, one for nodes above support value thresholds
    node_count = int(0)
    node_support = int(0)

    #start iterating over every node in this tree
    for node in tree[1].traverse():
        
        #note that tips (leaves) are nodes, and we need to skip these using the following conditional
        if node.is_leaf():
            pass
        
        #now just looking at internal nodes
        else:
            node_count += 1
            #check if support is > 70% bootstrap
            if int(node.support) >= int(70):
                node_support += 1

    #use function to divide and round index
    NSI = NSI_calc(node_support,node_count)
            
    #write info to screen and to file
    print '\t', "Number of internal nodes: {}".format(node_count)
    print '\t', "Nodes with support > 70: {}".format(node_support)
    print '\t', "Node support index = {}".format(NSI),'\n'
    fh_out.write("{0}\t{1}\t{2}\t{3}\n".format(tree[0],node_count,node_support,NSI))
    

fh_out.close()

print '\n', "Output written to {}.".format(out_name), '\n'
#===============================================================================================  
