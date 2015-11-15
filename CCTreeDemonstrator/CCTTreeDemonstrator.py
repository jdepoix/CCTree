__author__ = 'Jonas'

import sys

from CCTree.CCTree import CCTree

class CCTreeDemonstrator(object):
    """
    A class with the sole purpose of demonstrating how the CCTree works. It takes a CCTree object and goes through each
    iteration interactively by printing out to the console
    """
    def __init__(self, cctree):
        """
        instantiates a new CCTreeDemonstrator

        :param: a unclustered CCTree which will be clustered for demonstration
        """
        assert(isinstance(cctree, CCTree))
        self.cctree = cctree

    def print_cctree_leafs(self):
        """
        print all leafs of a the CCTree to the console
        """
        leafs = self.cctree.root.get_leafs()
        line_height = max([len(node_data.data) for node_data in leafs])
        line = ''

        for j in range(line_height):
            for i in range(len(leafs)):
                line_width = max([len(node_data.__str__()) for node_data in leafs[i].data])
                if j < len(leafs[i].data):
                    new_str = leafs[i].data[j].__str__()
                    if len(new_str) < line_width:
                        new_str += ' ' * (line_width - len(new_str))
                    line += new_str
                else:
                    line += ' ' * line_width
                line += '\t\t'

            print(line)
            line = ''


    def build_cctree_interactive(self):
        """
        goes through the process of clustering with a CCTree interactively, by printing out each iteration
        """
        print('-------------------------------------------- INPUT ---------------------------------------------')
        self.print_cctree_leafs()

        while self.cctree.split_nodes():
            do = raw_input("press 'n' for next iteration, press any other key to cancel\n")
            if do == 'n':
                print('\n---------------------------------------- NEXT ITERATION ----------------------------------------')
                self.print_cctree_leafs()
            else:
                print('cancelled!')
                sys.exit(0)

        print('cluster finished!')