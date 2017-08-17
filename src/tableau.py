from src.kripke import *
from src.formula import Atom

class ProofTree():
    """
    TODO
    """

    def __init__(self, formula):
        self.nodes = [Node('s', formula)]  # Initial world s, False = not derived yet
        self.ks = KripkeStructure([], {})

    # TODO
    def derive(self):
        node = self.nodes.pop()
        world_name, formula, children = node.formula.derive('s')
        node.children.append(Node(world_name, formula, children))

        if isinstance(node.formula, Atom):
            self.ks.worlds.append(World(node.world_name, {node.formula.name: True}))

        return self.ks


class Node():
    """
    TODO
    """

    def __init__(self, world_name, formula, children=[]):
        self.world_name = world_name
        self.formula = formula
        self.is_derived = False
        self.children = children

    def __eq__(self, other):
        return self.world_name == other.world_name \
               and self.formula == other.formula \
               and self.is_derived == other.is_derived \
               and self.children == self.children


class Bottom(Node):
    """
    TODO
    """

    def __init__(self):
        self.world_name = None
        self.formula = None
        self.is_derived = True
        self.children = None
