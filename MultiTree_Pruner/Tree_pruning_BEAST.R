rm(list=ls())

library(ape)
library(phytools)
library(geiger)

#read in all the trees from a BEAST run
Trees <- read.nexus("/PATH TO /BEAST_output.trees")

ls(Trees)
#plot one of the trees
plotTree(Trees[[10]])


#insert names of taxa to drop from tree set
drop_list = c("Taxa_1", "Taxa_2", "Taxa_3")


#below will iterate across all trees and drop tips not matched
Pruned_Trees <- lapply(Trees,drop.tip,tip=drop_list)

#check any of the trees to see that it has removed the tips
plotTree(Pruned_Trees[[10]])
typeof(Pruned_Trees)
"multiPhylo" <- class(Pruned_Trees)


#If you want to subsample trees at random, this is a way to do it
Subsampled_Trees<-sample(Pruned_Trees,size=100)
ls(Subsampled_Trees)
write.nexus(Subsampled_Trees, file="/PATH TO /Subsampled_Pruned_BEAST_output.trees")


#Write output tree file with updated trees
write.nexus(Pruned_Trees, file="/PATH TO /Pruned_BEAST_output.trees")
