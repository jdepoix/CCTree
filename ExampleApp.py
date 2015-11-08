import random
import sys

__author__ = 'Jonas'

from CCTree import CCTree


def print_cctree_leafs(cctree):
    """
    print all leafs of a given CCTree to the console

    :param cctree: CCTree
    """
    leafs = cctree.root.get_leafs()
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


def build_cctree_interactive(cctree):
    """
    goes through the process of clustering with a CCTree interactively, by printing out each iteration

    :param cctree: CCTree
    """
    print_cctree_leafs(cctree)

    while cctree.split_nodes():
        do = input("press 'n' for next iteration, press any other key to cancel\n")
        if do == 'n':
            print('\n---------------------------------------- NEXT ITERATION ----------------------------------------')
            print_cctree_leafs(cctree)
        else:
            print('cancelled!')
            sys.exit(0)

    print('cluster finished!')


if __name__ == '__main__':
    # set a range of possible attributes which random test data is created from later on
    languages = ['english', 'german', 'french', 'italian', ]
    nr_of_links = range(5)
    nr_of_words = range(20, 40)
    has_non_ascii = [True, False]

    data = []

    # test data is created randomly
    for i in range(200):
        data.append([
            random.choice(languages),
            random.choice(nr_of_links),
            random.choice(nr_of_words),
            random.choice(has_non_ascii),
        ])

    tree = CCTree(data, 2, 5)

    # interactively build up the CCTree
    build_cctree_interactive(tree)