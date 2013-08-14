# 6.00x Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(Node(src) in self.nodes and Node(dest) in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedDigraph(Digraph):

    def __init__(self):
        Digraph.__init__(self)
    

    def addEdge(self, weightedEdge):

        src = weightedEdge.getSource()
        dest = weightedEdge.getDestination()
        total = 1.0*weightedEdge.getTotalDistance()
        outdoor = 1.0*weightedEdge.getOutdoorDistance()
        value = [dest, (total, outdoor)]

        if not(Node(src) in self.nodes and Node(dest) in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[Node(src)].append(value)


    def childrenOf(self, node):
        res = []
        
        for d in self.edges[node]:
            res.append(d[0])
        return res

    def getDistance(self, src, dest):
        for children in self.edges[(src)]:
            if children[0] == dest:
                return children[1][0]

    def totalDistance(self, path):
        total = 0
        for n in range( len(path) - 1 ):
            total += self.getDistance(Node(path[n]), Node(path[n+1]))
        
        return total

    def totalOutdoor(self, path):
        total = 0
        for n in range( len(path) - 1 ):
            total += self.getOutdoor(Node(path[n]), Node(path[n+1]))
        
        return total
    def getOutdoor(self, src, dest):
        for children in self.edges[(src)]:
            if children[0] == dest:
                return children[1][1]    

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} {3}\n'.format(res, k, d[0], d[1])

        return res




class WeightedEdge(Edge):
    """
    A double WeightedEdge
    """

    def __init__(self, src, dest,  total, outdoor):
        Edge.__init__(self, src, dest)
        self.total = float(total)
        self.outdoor = float(outdoor)

    def getTotalDistance(self):
        return self.total

    def getOutdoorDistance(self):
        return self.outdoor

    def __str__(self):
        return str(self.src) + '->' + str(self.dest) + '(' + str(self.total)\
            + ', ' + str(self.outdoor) + ')'

    










