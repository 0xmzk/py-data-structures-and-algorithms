# TODO: Graph Traversals (Breadth first seach, Depthfirst search, pre/in/post order)
# TODO: Graph Algorithms (Dijkstras)

class Vertex:
    class VertexRequiresLabel(Exception):
        def __str__(self) -> str:
            return f"Vertex requires a label"

    def __init__(self, label: str):
        if not label:
            raise Vertex.VertexRequiresLabel

        self.label = str(label)

    def getLabel(self):
        return self.label


    def __hash__(self):
        return hash(self.label)

    def __eq__(self, operand):
        if isinstance(operand, Vertex):
            return self.label == operand.getLabel()
        return False

    def __repr__(self) -> str:
        return f"Vertex(label='{self.label}')"


class Edge:
    def __init__(self, A, B, weight) -> None:
        self.weight = weight
        self.A = A
        self.B = B

    def __eq__(self, operand):
        if isinstance(operand, Edge):
            return self.__hash__() == operand.__hash__()
        return False

    def setWeight(self, weight_value):
        self.weight = weight_value

    def isWeighted(self):
        if self.weight is None:
            return False
        else:
            return True

    def getVertices(self):
        return (self.A, self.B)

class DirectedEdge(Edge):
    def __init__(self, src: Vertex, dst: Vertex, weight: int | float = None):
        super().__init__(src, dst, weight)

    def __str__(self) -> str:
        return f"{self.A} -> {self.B}"

    def __hash__(self) -> int:
        return hash(f"{self.A.getLabel()}->{self.B.getLabel()}")

    def __repr__(self) -> str:
        return f"DirectedEdge(src={self.A.__repr__()}, dst={self.B.__repr__()}, weight={self.weight})"

class UndirectedEdge(Edge):
    def __init__(self, A: Vertex, B: Vertex, weight: int | float = None):
        super().__init__(A, B, weight)

    def __str__(self) -> str:
        return f"{self.A} -- {self.B}"

    def __hash__(self) -> int:
        A = hash(self.A.getLabel())
        B = hash(self.B.getLabel())
        return A & B


    def __repr__(self) -> str:
        return f"DirectedEdge(src={self.A.__repr__()}, dst={self.B.__repr__()}, weight={self.weight})"

class BidirectionalEdge(Edge):
    def __init__(self, A: Vertex, B: Vertex, weight: int | float = None):
        super().__init__(A, B, weight)

    def __str__(self) -> str:
        return f"{self.A} <-> {self.B}"

    def __hash__(self) -> int:
        A = hash(self.A.getLabel())
        B = hash(self.B.getLabel())
        return (A & B) ^ ord('b')


    def __repr__(self) -> str:
        return f"DirectedEdge(src={self.A.__repr__()}, dst={self.B.__repr__()}, weight={self.weight})"

class Graph:
    class ObjNotInGraph(Exception):
        def __init__(self, obj):
            self.obj = obj

        def __str__(self) -> str:
            return f"{self.obj.__repr__()} is not an element of the graph"

    class InvalidObjType(Exception):
        def __init__(self, obj, graph):
            self.obj = obj
            self.graph = graph

        def __str__(self) -> str:
            return f"{type(self.obj)} cannot be used in {type(self.graph)}"

    class ObjAlreadyInGraph(Exception):
        def __init__(self, obj):
            self.obj = obj

        def __str__(self) -> str:
            return f"{self.obj.__repr__()} is alreadyan element of the graph"


class MixedGraph(Graph):

    def __init__(self, v: set = set(), e: set = list()):
        self.edges = e
        self.vertices = v
        self.valid_edges = [UndirectedEdge, DirectedEdge, BidirectionalEdge]

    def vertexSetContains(self, v: Vertex):
        return (v in self.vertices)

    def edgeSetContains(self, e: Edge):
        return (e in self.edges)

    def addVertex(self, v: Vertex):
        if self.vertexSetContains(v):
            raise Graph.ObjAlreadyInGraph(v)
        else:
            self.vertices.add(v)

    def removeVertex(self, v: Vertex):
        if not self.vertexSetContains(v):  
            raise Graph.ObjNotInGraph(v)
        else:
            self.vertices.remove(v)

    def getNumberOfEdges(self):
        return len(self.edges)

    def getNumberofVertices(self):
        return len(self.vertices)

    def addEdge(self, e: Edge):
        if not self._isEdgeValid(e):
            raise Graph.InvalidObjType(e, self)
        if self.edgeSetContains(e):
            raise Graph.ObjAlreadyInGraph(e)
        else:
            self.edges.add(e)

    def removeEdge(self, e: Edge):
        if not self._isEdgeValid(e):
            raise Graph.InvalidObjType(e, self)
        if self.edgeSetContains(e):
            self.edges.remove(e)
        else:
            raise Graph.ObjNotInGraph(e)

    def getEdgeSet(self):
        return self.edges

    def getVertexSet(self):
        return self.vertices

    def getVertexDegree(self, v:Vertex):
        if not self.vertexSetContains(v):
            raise Graph.ObjNotInGraph(v)
        degree = 0
        for edge in self.edges:
            if v in edge.getVertices():
                degree += 1
        return degree

    # TODO: Fix the code below to function
    # These slides + nodes should help:
    # https://jlmartin.ku.edu/courses/math105-F11/Lectures/chapter5-part2.pdf

    # def hasEulerianCircuit(self):
    #     for vertex in self.vertices:
    #         d = self.getVertexDegree(vertex)
    #         if not self._isEven(d):
    #             return False
    #     return True

    # def hasEulerianPath(self):
    #     odd_vertex_count = 0
    #     for vertex in self.vertices:
    #         d = self.getVertexDegree(vertex)
    #         if not self._isEven(d):  
    #             odd_vertex_count += 1
    #         if odd_vertex_count > 2:
    #             return False
    #     return True

    def _isEdgeValid(self, e: Edge):
        for i in self.valid_edges:
            if not isinstance(e, i):
                return False
        return True

    def _isEven(self, number:int):
        return not bool(number % 2)

class DirectedGraph(MixedGraph):
    def __init__(self, v: set = set(), e: set = set()):
        self.vertices = v
        self.edges = set()
        self.valid_edges = [DirectedEdge, BidirectionalEdge]
        for edge in e:
            if not self._isEdgeValid(edge):
                raise Graph.InvalidObjType(edge, self)
            self.edges.add(edge)


class UndirectedGraph(MixedGraph):
    def __init__(self, v: set = set(), e: set = set()):
        self.vertices = v
        self.edges = set()
        self.valid_edges = [UndirectedEdge]
        for edge in e:
            if not self._isEdgeValid(edge):
                raise Graph.InvalidObjType(edge, self)
            self.edges.add(edge)


