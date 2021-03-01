import sys
from enum import Enum
from operator import add, mul, sub, truediv

class DivisionByZero(Exception):
    pass

class UnknownInTree(Exception):
    pass

class OutputFormat(Enum):
    PREFIX = 0
    INFIX = 1
    POSTFIX = 2

class BinaryTreeNode:
    def __init__(self, data = "", left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Tokenizer:
    def __init__(self, string = ""):
        self.string = string
        self.pos = 0

    def __str__(self):
        return_string = ""
        curr = 0
        for x in self.string:
            if x == " ":
                curr +=1 
            elif curr == self.pos:
                return_string += x
        return return_string

    def get_next(self):
        self.pos += 1 
        return self

class PrefixParseTree:
    def __init__(self):
        self.root = None
        self.format = OutputFormat.PREFIX
    
    def __str__(self):
        recur = self._print_recur
        ret_str = ""
        for output in recur(self.root):
            if ret_str and ret_str[-1] == ")":
                ret_str += " "
            if output == "(":
                ret_str += str(output)
            elif output == ")":
                ret_str = ret_str[:-1] + output
            else:
                ret_str += str(output) + " "
        return ret_str

    def load_statement_string(self, statement):
        tokenizer = Tokenizer(statement)
        self.root = self._load_statement_string_recur(tokenizer)

    def set_format(self, out_format):
        self.format = out_format

    def root_value(self):
        return self.solve_tree(0)

    def simplify_tree(self):
        self.root = self._simplify_tree_recur(self.root)

    def solve_tree(self, root_value):
        if root_value != 0:
            self.simplify_tree()
            return self._solve_for_x_recur(self.root, root_value)
        return self.solve_tree_recur(self.root)
    

    def _load_statement_string_recur(self, tokenizer):
        recur = self._load_statement_string_recur
        token = str(tokenizer)
        if token.isdigit():
            return BinaryTreeNode(int(token))
        if token.isalpha():
            return BinaryTreeNode(token)
        left = recur(tokenizer.get_next())
        right = recur(tokenizer.get_next())
        return BinaryTreeNode(token, left, right)

    def _simplify_tree_recur(self, node):
        recur = self._simplify_tree_recur
        if node == None:
            return
        try:
            node.data = self.solve_tree_recur(node)
            node.left = None
            node.right = None
        except:
            recur(node.left)
            recur(node.right)
        return node

    def _solve_for_x_recur(self, node, value):
        recur = self._solve_for_x_recur
        data = node.data
        left = node.left
        right = node.right

        if type(data) != int and data.isalpha():
            return value
        
        if type(left.data) == int:
            operator = {"/":truediv, "-":sub, "+":sub, "*":truediv}
            node = int(left.data)
        else:
            operator = {"/":mul, "-":add, "+":sub, "*":truediv}
            node = int(right.data)

        if data in "+*":
            new_val = operator[data](value, node)
        else:
            new_val = operator[data](node, value)

        if type(left.data) == int:
            return recur(right, new_val)
        else:
            return recur(left, new_val)

    def solve_tree_recur(self, node):
        recur = self.solve_tree_recur
        operator = {"+":add, "-":sub, "*":mul}

        if type(node.data) == int:
            return node.data
        if node.data.isalpha():
            raise UnknownInTree()

        if node.data == "/":
            denominator = recur(node.right)
            if denominator == 0:
                raise DivisionByZero()
            else:
                return recur(node.left) / denominator
        
        return operator[node.data](recur(node.left), recur(node.right))

    def _print_recur(self, node): 
        recur = self._print_recur
        if node == None:
            return
        if self.format == OutputFormat.PREFIX:
            yield node.data
        if self.format == OutputFormat.INFIX:
            if node.left != None:
                yield "("
        if node.left!= None:
            for x in recur(node.left):
                yield x
        if self.format == OutputFormat.INFIX:
            yield node.data
        if node.right != None:
            for x in recur(node.right):
                yield x
        if self.format == OutputFormat.INFIX:
            if node.right != None:
                yield ")"
        if self.format == OutputFormat.POSTFIX:
            yield node.data

def test_prefix_parser(str_statement, solve = False, root_value = 0):
    if solve == True:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        print("The value of x if the root_value is " + str(root_value) + " is: " + str(prefix_tree.solve_tree(root_value)))
    else:
        prefix_tree = PrefixParseTree()
        prefix_tree.load_statement_string(str_statement)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

        str_print = "The value of the tree is: "
        try:
            str_print += str(prefix_tree.root_value())
        except DivisionByZero:
            str_print += str("A division by zero occurred")
        except UnknownInTree:
            str_print += str("There is an unknown value in the tree")
        print(str_print)

        print("SIMPLIFIED:")
        prefix_tree.simplify_tree()
        prefix_tree.set_format(OutputFormat.PREFIX)
        print("PREFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.INFIX)
        print("INFIX: " + str(prefix_tree))
        prefix_tree.set_format(OutputFormat.POSTFIX)
        print("POSTFIX: " + str(prefix_tree))

    print("\n\n")

def quick_tester(string):
    prefix_tree = PrefixParseTree()
    prefix_tree.load_statement_string(string)

    prefix_tree.set_format(OutputFormat.INFIX)
    print("INFIX: " + str(prefix_tree))
    a_str = "Root value of tree is: "
    try:
        print(a_str, prefix_tree.root_value())
    except DivisionByZero:
        print(a_str, "No division by 0 allowed")
    except UnknownInTree:
        print(a_str, "O-oh! Unknown value cannot solve")
    prefix_tree.simplify_tree()
    # print(prefix_tree.root.data)
    # print(prefix_tree.root.left)
    # print(prefix_tree.root.right)
    print("Simplified, INFIX: " + str(prefix_tree))
    print("Done\n")

def teacher_test():
    org_out = sys.stdout
    fout = open(sys.path[0] + "/parse_out.txt", "w+")
    sys.stdout = fout
    f = open(sys.path[0] + "/prefix_statements.txt", "r")
    previous_line = None
    for line in f:
        some_split = line.split()
        if some_split[0] == "solve":
            test_prefix_parser(previous_line.strip(), True, int(some_split[1]))
        test_prefix_parser(line.strip())
        previous_line = line
    f.close()
    sys.stdout = org_out
    fout.close()

if __name__ == "__main__":
    teacher_test()
    # quick_tester("x")
    # quick_tester("/ + x 2 2")
    # quick_tester("* + - 7 0 * Bjartur 1 * 0 - 8 7")