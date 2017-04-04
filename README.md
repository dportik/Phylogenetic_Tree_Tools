# Phylogenetic_Tree_Tools

Scripts for: 

1) pruning taxa from multiple trees - designed to work with a directory filled with tree files


2) performing Robinson-Foulds comparisons for a set of trees to an optimal tree - uses a directory filled with tree files and a best tree file


3) calculating node-support indices - uses a directory containing RAxML bootstrapped output files to calculate the percentage of nodes with >70% bs support for each tree file

All scripts make use of the ete2 python module, which needs to be installed. If a different or newer version of ete is used, the top of these scripts will need to be changed to reflect the different module name (ie change 'from ete2 import Tree' to 'from ete3 import Tree' for example).
