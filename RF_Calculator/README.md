# RF_calculator.py

usage: python RF_calculator.py [full path to directory of trees] [full path to tree file to compare to]

example:

`python RF_calculator.py user/bin/Tree_Files user/bin/best_trees/super_awesome_tree.tre`


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

Here is an example of actual output in one of these files:

```
effective_tree_size	norm_rf	source_edges_in_ref	ref_edges_in_source	rf	max_rf
153	0.386666666667	0.807947019868	0.807947019868	116.0	300.0
153	0.5	0.751655629139	0.751655629139	150.0	300.0
153	0.306666666667	0.847682119205	0.847682119205	92.0	300.0
153	0.346666666667	0.827814569536	0.827814569536	104.0	300.0
153	0.326666666667	0.837748344371	0.837748344371	98.0	300.0
153	0.306666666667	0.847682119205	0.847682119205	92.0	300.0
153	0.4	0.801324503311	0.801324503311	120.0	300.0
153	0.393333333333	0.804635761589	0.804635761589	118.0	300.0
153	0.353333333333	0.824503311258	0.824503311258	106.0	300.0
153	0.4	0.801324503311	0.801324503311	120.0	300.0
153	0.3	0.850993377483	0.850993377483	90.0	300.0
153	0.306666666667	0.847682119205	0.847682119205	92.0	300.0
153	0.34	0.831125827815	0.831125827815	102.0	300.0
153	0.346666666667	0.827814569536	0.827814569536	104.0	300.0
```

-These correspond to the ETE Tree Compare function (tree.compare()) dictionary output (see manual for more deets)
and can be used in various ways to summarize tree properties in addition to the RF metric.


Written for Python 2.7

External Dependencies: ete2, NUMPY

-Install Python ETE2 toolkit (information at http://etetoolkit.org) 
 
 
# Dan Portik

daniel.portik@uta.edu

February 2015

