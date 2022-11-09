import ast

from ezflake import ViolationType, Plugin, Visitor


__version__ = '1.1.0'


UNF001 = ViolationType('UNF001', "Don't raise '{}'")
UNF001.names = ('NotImplementedError',)

UNF002 = ViolationType('UNF002', "Don't reference '{}'")
UNF002.names = UNF001.names  # (,)


class UnfinishedVisitor(Visitor):
    def visit_Raise(self, node: ast.Raise):
        name = None
        if isinstance(node.exc, ast.Name):
            name = node.exc.id
        elif isinstance(node.exc, ast.Call) and isinstance(node.exc.func, ast.Name):
            name = node.exc.func.id

        if name in UNF001.names:
            self.violate_node(UNF001, node, name)
        self.generic_visit(node)

    def visit_Name(self, node: ast.Name):
        name = node.id
        if name in UNF002.names:
            self.violate_node(UNF002, node, name)
        self.generic_visit(node)


class UnfinishedPlugin(Plugin):
    name = __name__
    version = __version__
    visitors = [UnfinishedVisitor]
