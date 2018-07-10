# tree_pruner.py

usage: python tree_pruner.py [directory of trees] [taxa file]

example:

`python dan/scripts/tree_pruner.py dan/tree_bin dan/taxon_set1.txt`

taxa file format:
```
Name1
Name2
Name3
```

Removes tips listed in taxa file from all tree files in the directory.

NOTE - ete only supports NEWICK format trees, so a nexus tree file will not work here!

Check outputs in 'Pruned_Trees/' directory.


DEPENDENCIES:

-Install Python ETE toolkit (information at http://etetoolkit.org) 

-download from https://pypi.python.org/pypi/ete2/

  
Written for Python 2.7


**Contact:**

Daniel Portik, PhD

Postdoctoral Researcher

University of Arizona

daniel.portik@gmail.com
