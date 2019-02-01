from Bio import Phylo 
import pylab 
import sys
print(sys.argv)
in_tree = sys.argv[1]
out_tree = sys.argv[2]
def draw_tree(path_to_file):
	tree = Phylo.read(in_tree, 'newick') 
	tree.ladderize() 

	Phylo.draw(tree, label_func= str, show_confidence = True, do_show=False)
	pylab.axis() 
	pylab.savefig(out_tree,format='png', bbox_inches='tight', dpi=300) 
draw_tree(out_tree)