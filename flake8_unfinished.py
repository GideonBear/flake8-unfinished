import ast

from ezflake import ViolationType, Plugin, Visitor


__version__ = '1.0.3'


UNF001 = ViolationType('UNF001', "Don't raise '{}'")


class UnfinishedVisitor(Visitor):
    def visit_Raise(self, node: ast.Raise):
        if isinstance(node.exc, ast.Name):
            name = node.exc.id
        elif isinstance(node.exc, ast.Call):
            if isinstance(node.exc.func, ast.Name):
                name = node.exc.func.id
            else:
                name = None
        else:
            raise ValueError
        if name == 'NotImplementedError':
            self.violate_node(UNF001, node, name)
        self.generic_visit(node)


class UnfinishedPlugin(Plugin):
    name = __name__
    version = __version__
    visitors = [UnfinishedVisitor]
