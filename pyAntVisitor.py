#!/usr/bin/env python
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser
from Python3Visitor import Python3Visitor

import sys

class Visitor(Python3Visitor):
    def visitChildren(self, node):
        # if isinstance(node, Python3Parser.AtomContext):
        print(node.getText(), type(node))
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result

            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)

        return result


def main(args):
    file = FileStream(args[1])
    lexer = Python3Lexer(file)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)

    tre = parser.file_input()
    if parser.getNumberOfSyntaxErrors()!=0:
        print("File contains {} "
              "syntax errors".format(parser.getNumberOfSyntaxErrors()))

    print("\n\nDefault Tree: ")
    print(tree.Trees.Trees.toStringTree(tre,None, parser))

    # print("Using Visitor: ")
    # visitor = Visitor()
    # visitor.visit(tre)

if __name__ == '__main__':
    main(sys.argv)