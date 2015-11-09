__author__ = 'Jonas'

import random

from CCTree.CCTree import CCTree
from CCTreeDemonstrator.CCTTreeDemonstratorr import CCTreeDemonstrator

if __name__ == '__main__':
    # set a range of possible attributes which random test data is created from later on
    languages = ['english', 'german', 'french', 'italian', ]
    nr_of_links = range(5)
    nr_of_words = range(30, 40)
    has_non_ascii = [True, False]

    data = []

    # test data is created randomly
    for i in range(10):
        data.append([
            random.choice(languages),
            random.choice(nr_of_links),
            random.choice(nr_of_words),
            random.choice(has_non_ascii),
        ])

    # create CCTree with test data
    cctree = CCTree(data, 0.5, 2)

    # create Demonstrator object
    demonstrator = CCTreeDemonstrator(cctree)

    # interactively build up the CCTree
    demonstrator.build_cctree_interactive()