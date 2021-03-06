from __future__ import absolute_import

from copy import deepcopy
from .node import Node


class HyperEdge:

    def __init__(self, head=set(), tail=set(), weight=0):
        self._head = head
        self._weight = weight
        self._tail = tail

    @property
    def weight(self):
        '''
        Returns the weight of the edge
        '''
        return self._weight

    @property
    def tail(self):
        '''
        Returns the edge tail
        '''
        return self._tail

    @property
    def head(self):
        '''
        Returns the edge head
        '''
        return self._head

    def __contains__(self, n):
        '''
        Returns true if edge contains the node.
        '''
        try:
            return n in self.head() or n in self.tail()
        except TypeError:
            return False

    def copy(self):
        '''
        Returns a copy of the edge
        '''
        return deepcopy(self)

    def cardinality(self):
        '''
        return the number of nodes in tail and head
        '''
        return len(self._head) + len(self._tail)

    def cardinalityHead(self):
        '''
        return the number of nodes in head
        '''
        return len(self._head)

    def cardinalityTail(self):
        '''
        return the number of nodes in tail
        '''
        return len(self._tail)


class DirectedHyperArc(HyperEdge):

    def __init__(self, head=set(), tail=None, weight=0):
        try:
            assert isinstance(tail, Node)
        except:
            raise ValueError("Invalid tail node %s", tail)
        HyperEdge.__init__(head, tail, weight)


class DirectedHyperEdge(HyperEdge):

    def __init__(self, head=set(), tail=set(), weight=0):
        HyperEdge.__init__(head, tail, weight)


class UndirectedHyperEdge(HyperEdge):

    '''
        In an undirected hyperedge, the head of parent class contains all nodes
        and the tail is empty.
        head and tail properties are disabled by raising exception when called
        (since python has no private property like c or java)
        To get the nodes inside the UndirectedHyperEdge
        used the 'nodes' property.
    '''

    def __init__(self, nodes=set(), weight=0):
        HyperEdge.__init__(self, nodes, set(), weight)

    @property
    def nodes(self):
        ''' Returns the edge nodes (stored in the head set) '''
        return self._head

    @property
    def head(self):
        ''' Disable  head property'''
        raise AttributeError("Undirected HyperGraph has no attribute head")

    @property
    def tail(self):
        ''' Disable tail property'''
        raise AttributeError("Undirected HyperGraph has no attribute tail")
