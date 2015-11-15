__author__ = 'Jonas'

import random

from CCTree.CCTree import CCTree
from CCTreeDemonstrator.CCTTreeDemonstrator import CCTreeDemonstrator

if __name__ == '__main__':
    # set a range of possible attributes which random test data is created from later on
    languages = ['english', 'german', 'french', 'italian', ]
    nr_of_links = range(5)
    nr_of_words = range(30, 40)
    has_non_ascii = [True, False]

    # create test data example 1
    data_x1 = [
        ['english', False, 1],
        ['english', True, 1],
        ['english', False, 1],
        ['english', False, 2],
        ['german', False, 2],
        ['english', False, 3],
        ['english', True, 3],
        ['english', False, 2],
    ]

    # test data example 2
    data = []

    # test data for example 2 is created randomly
    for i in range(1000):
        data.append([
            random.choice(languages),
            random.choice(nr_of_links),
            random.choice(nr_of_words),
            random.choice(has_non_ascii),
        ])

    # create CCTree with test data
    cctree = CCTree(data, 1, 10)

    # create Demonstrator object
    demonstrator = CCTreeDemonstrator(cctree)

    # interactively build up the CCTree
    demonstrator.build_cctree_interactive()