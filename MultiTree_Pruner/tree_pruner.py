import sys
import os
import shutil
import subprocess as sp
from ete2 import Tree
'''
usage: python tree_pruner.py [directory of trees] [taxa file]

ex. python dan/scripts/tree_pruner.py dan/tree_bin dan/taxon_set1.txt

taxa file format:
Name1
Name2
Name3

Removes tips listed in taxa file from all tree files in the directory.

Check outputs in 'Pruned_Trees/' directory.

######################################################
DEPENDENCIES:
-Install Python ETE toolkit (information at http://etetoolkit.org) 
  -download from https://pypi.python.org/pypi/ete2/
  -unzip folder
  -cd into resulting folder and type 'python setup.py install' or 'sudo python setup.py install'
######################################################
------------------------
written for Python 2.7.3
Dan Portik
daniel.portik@berkeley.edu
September 2015
------------------------
'''

#Read in directory and file information
tree_dir = sys.argv[1]
os.chdir(tree_dir)

taxa_list = sys.argv[2]
fh_taxa = open(taxa_list, 'r')


#create Results folder in directory
results_dir = "Output_Pruned_Trees"
if not os.path.exists(results_dir):
    os.mkdir(results_dir)

#put taxon names to test in a list
prune_taxa = set()
for line in fh_taxa:
    taxon = line.strip()
    prune_taxa.add(taxon)
fh_taxa.close()


#start trying to open trees, prune   
for filetype in os.listdir('.'):
    try:
        temp_tree = Tree(filetype)
        temp_set = set()
        for tip in temp_tree.iter_leaves():
            tip = str(tip)
            tip = tip.strip()
            tip = tip.replace('--','')
            temp_set.add(tip)
        print filetype
        print "Number of taxa in tree", len(temp_set)
        temp_set.difference_update(prune_taxa)
        print "Number of taxa after pruning", len(temp_set), '\n'
        prune_list = list(temp_set)
        temp_tree.prune(prune_list, preserve_branch_length=True)
        temp_tree.write(format = 1, outfile = "Pruned_{}".format(filetype))
        
            
    except:
        pass

for filetype2 in os.listdir('.'):
    if filetype2.startswith('Pruned_'):
        proc = sp.Popen(['mv', filetype2, results_dir])
        proc.wait()
print '\n', '\n', "All finished, check Output_Pruned_Trees folder", '\n', '\n'
