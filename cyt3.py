from Bio import Phylo 
import pylab 
f = 'path/to/my/file' 
tree = Phylo.read('RAxML_bipartitionsBranchLabels.T20', 'newick') 
tree.ladderize() 
Phylo.draw(tree, do_show=False) 
pylab.axis() 
pylab.savefig("tree2.png",format='png', bbox_inches='tight', dpi=300) 