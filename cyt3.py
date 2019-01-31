from Bio import Phylo 
import pylab 
def draw_tree(path_to_file):
	tree = Phylo.read('RAxML_bipartitionsBranchLabels.T20', 'newick') 
	tree.ladderize() 

	Phylo.draw(tree, label_func= str, show_confidence = True, do_show=False)
	pylab.axis() 
	pylab.savefig("tree2.png",format='png', bbox_inches='tight', dpi=300) 
draw_tree('tree2')