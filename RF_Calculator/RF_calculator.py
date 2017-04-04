import sys
import os
import subprocess as sp
import shutil
import numpy as np
from ete2 import Tree

'''
usage: python RF_calculator.py [full path to directory of trees] [full path to tree file to compare to]

Outputs are written to the '/Trees' directory pointed to via command line.

Will produce separate tab-delimited files for each type of analysis.

A corresponding log file is also written for both the best tree and internal
comparisons. This file simply summarizes the average normalized and absolute RF metric
across the analysis for a quick glance.

The R-F metric is calculated as a normalized measure (scale 0-1) and as 
an absolute measure (will be relative to total number of nodes on tree).
Detailed information on this is summarized in the folder:
'/RF_calculations'

-Each tab-delimited text file in this directory contains the following headers:
'effective_tree_size'	'norm_rf'	'source_edges_in_ref'	'ref_edges_in_source'	'rf'	'max_rf'

-These correspond to the ETE Tree Compare function (tree.compare()) dictionary output (see manual for more deets)
and can be used in various ways to summarize tree properties in addition to the RF metric.

######################################################
Written for Python 2.7.3
DEPENDENCIES:
-Install Python ETE toolkit (information at http://etetoolkit.org) 
  -download from https://pypi.python.org/pypi/ete2/
  -unzip folder
  -cd into resulting folder and type 'python setup.py install' or 'sudo python setup.py install'
-numpy
######################################################

Dan Portik
daniel.portik@uta.edu
February 2015
'''

tree_dir = sys.argv[1]
os.chdir(tree_dir)

tree_path = sys.argv[2]
best_tree = Tree(tree_path)

#===============================================================================================

os.chdir(tree_dir)
print '\n', "****************************************************************"
print "Moving to ", tree_dir, "to begin Robinson-Foulds analyses."
print "****************************************************************", '\n'

#create empty list to populate with tree file names
tree_source = []

#search this directory for tree files
for filetype in os.listdir('.'):
    if filetype.endswith(".tre"):
        if os.path.getsize(filetype) > int(0):
            tree_source.append(filetype)

#count how many tree files are in the list
tree_count = int(len(tree_source))
print
print "Number of trees to be included for Robinson-Foulds comparisons = ", tree_count
print

#initialize empty list to put the actual trees into
tree_shapes = []
#for every tree file in our tree_source list, get the tree shapes loaded
for t_file in tree_source:
    #use the Tree() function to grab info from the file
    t_shape = Tree(t_file)
    temp_list = []
    #append the tree shape and filename to a temp list, which then is appended to the tree_shapes list
    temp_list.append(t_file)
    temp_list.append(t_shape)
    tree_shapes.append(temp_list)
    
#===============================================================================================  
#Performing Robinson-Foulds calculations on all trees in tree folder

#create an output file to put RF calculations in
out_name = 'RF_calculations.txt'
out_fh = open(out_name, 'a')
out_fh.write('Locus'+'\t'+'effective_tree_size'+'\t'+'norm_rf'+'\t'+'source_edges_in_ref'+'\t'+'ref_edges_in_source'+'\t'+'rf'+'\t'+'max_rf'+'\n')

print
print "Beginning pairwise comparison of trees to user best tree topology."
print

#start complex loop to run through tree comparisons
#for every tree in the list:
for items in tree_shapes:
    #create a temporary place to store the comparison values, perform function
    tr1 = items[1].compare(best_tree, unrooted=True)
    print "{0}: Normalized Robinson-Foulds = {1}, Absolute Robinson-Foulds = {2}".format(items[0],tr1['norm_rf'],tr1['rf'])
    ets = str(tr1['effective_tree_size'])
    nrf = str(tr1['norm_rf'])
    seir = str(tr1['source_edges_in_ref'])
    reis = str(tr1['ref_edges_in_source'])
    rf = str(tr1['rf'])
    mrf = str(tr1['max_rf'])
    out_fh.write("{}".format(items[0])+'\t'+ets+'\t'+nrf+'\t'+seir+'\t'+reis+'\t'+rf+'\t'+mrf+'\n')
#close temporary file
out_fh.close()

print '\n', "Output written to {}.".format(out_name), '\n'

