import ast

from ezflake import create_violation, Plugin, Visitor


UNF001 = create_violation('UNF001', "Do not raise 'NotImplementedError'")
UNF001_NAMES = ('NotImplementedError',)


class UnfinishedVisitor(Visitor):
    def visit_Raise(self, node: ast.Raise):
        name = None
        if isinstance(node.exc, ast.Name):
            name = node.exc.id
        elif isinstance(node.exc, ast.Call) and isinstance(node.exc.func, ast.Name):
            name = node.exc.func.id
        if name in UNF001_NAMES:
            self.violate(UNF001, node, name)
        self.generic_visit(node)


class UnfinishedPlugin(Plugin):
    name = __name__
    visitors = [UnfinishedVisitor]
