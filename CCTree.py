__author__ = 'Jonas'

import math

class CCTree(object):
    """
    represents a CCTree.

    If you want to find out more about how the CCTree algorithm works, read the paper, which proposed it. You can find
    it here:
    http://www.scitepress.org/portal/PublicationsDetail.aspx?ID=44Nf2WZJ6Qw=&t=1
    """
    def __init__(self, data, purity_threshold, max_elements):
        """
        initializes the tree

        :param data: a list of data points. Each data point is a list by itself, containing the attribute values
        :param purity_threshold: the threshold of purity a node has to reach, to be able to turn into a leaf
        :param max_elements: the maximum number of elements a node can contain while being able to turn into a leaf
        """
        self.data = data
        self.validate_data()

        self.purity_threshold = purity_threshold
        self.max_elements = max_elements

        self.root = Node(self.data)

    def validate_data(self):
        """
        validates the list of data points, to make sure the structure of their attributes match

        :raises: UnsuitableAttributesException in case structure of attributes does not match
        """
        for data_point in self.data:
            if len(data_point) != len(self.data[0]):
                raise UnsuitableAttributesException

    def split_nodes(self):
        """
        split all non final leaf nodes up

        :return: True in case another split up is possible, False otherwise, which means the clustering is complete
        """
        leafs = self.root.get_non_final_leafs()

        if leafs:
            for leaf in leafs:
                if leaf.get_purity() < self.purity_threshold or leaf.get_data_length() < self.max_elements:
                    leaf.final_leaf = True
                else:
                    leaf.split_node()
            return True
        else:
            return False

    def cluster_data(self):
        """
        splits the nodes as long as possible, until the clustering process is completed
        """
        while self.split_nodes():
            pass


class Node(object):
    """
    represents a node in a CCTree
    """
    def __init__(self, data):
        self.data = data
        self.children = []
        self.final_leaf = False

    def get_data_length(self):
        """
        returns the amount of data points

        :return: length of the set of data pointss
        """
        return len(self.data)

    def get_purity(self):
        """
        calculates the purity of this node.
        Lookup the paper in case you want to see in more detail how this purity function works.

        :return: purity of this node
        """
        result = 0

        for j in range(len(self.data[0])):
            result += self.get_entropy(j)

        return result

    def get_entropy(self, i):
        """
        calculates the shannon entropy of a selected attribute.

        :param i: the index of the attribute the entropy is calculated of
        :return: entropy
        """
        h = 0
        occurrences = {}
        total = 0

        for k in range(len(self.data)):
            total += 1

            if self.data[k][i] in occurrences:
                occurrences[self.data[k][i]] += 1
            else:
                occurrences[self.data[k][i]] = 1

        for p in occurrences:
            pj = occurrences[p]/total
            h += pj * math.log(pj)

        return -h

    def get_max_entropy_attribute_index(self):
        """
        :returns the index of the attribute with the highest shannon entropy
        :return: attribute index
        """
        maximum = 0
        index = 0

        for i in range(len(self.data[0])):
            h = self.get_entropy(i)

            if h > maximum:
                maximum = h
                index = i

        return index

    def split_node(self):
        """
        splits up the node and its data into new child nodes, based on the maximum shannon entropy
        :return:
        """
        if len(self.data) > 1:
            attribute_index = self.get_max_entropy_attribute_index()

            attribute_data_dict = {}
            for data_point in self.data:
                if data_point[attribute_index] in attribute_data_dict:
                    attribute_data_dict[data_point[attribute_index]].append(data_point)
                else:
                    attribute_data_dict[data_point[attribute_index]] = [data_point, ]

            for new_node_data in attribute_data_dict:
                self.children.append(Node(attribute_data_dict[new_node_data]))

    def get_leafs(self):
        """
        returns all leafs of the tree
        :return: leafs
        """
        if not self.children:
            return [self]
        else:
            children = []

            for child in self.children:
                children.extend(child.get_leafs())

            return children

    def get_non_final_leafs(self):
        """
        returns all leafs of the tree which haven't been marked as final yet
        :return: non final leafs
        """
        leafs = []

        for leaf in self.get_leafs():
            if not leaf.final_leaf:
                leafs.append(leaf)

        return leafs

    def get_final_leafs(self):
        """
        returns all leafs of the tree which have been marked as final
        :return: final leafs
        """
        leafs = []

        for leaf in self.get_leafs():
            if leaf.final_leaf:
                leafs.append(leaf)

        return leafs


class UnsuitableAttributesException(Exception):
    """
    is raised in case data is given to a CCTree which has data points with a unsuitable attribute structure.
    This is most likely the case, whenever there are any data points with a differentiating amount of attributes
    """
    pass