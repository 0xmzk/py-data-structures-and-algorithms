from DataStructures.Trees import *

def binary_tree():
    root_node = BinaryNode('Root')
    child_node_1 = BinaryNode('Child 1')
    child_node_2 = BinaryNode('Child 2')
    root_node.setLeftNode(child_node_1)
    root_node.setRightNode(child_node_2)