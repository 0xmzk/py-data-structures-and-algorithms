from DataStructures.Graphs import *


def test():
    A,B,C,D = [Vertex(i) for i in ["A","B","C","D"]]
    e1 = UndirectedEdge(A,B)
    e2 = UndirectedEdge(B,C)
    e3 = UndirectedEdge(C,D)
    e4 = UndirectedEdge(A,C)
    e5 = UndirectedEdge(B,D)
    v = {A,B,C,D}
    e = {e1,e2,e3,e4,e5}
    G = UndirectedGraph(v, e)
    for vertex in v:
        print(f"{vertex}:{G.getVertexDegree(vertex)}")
