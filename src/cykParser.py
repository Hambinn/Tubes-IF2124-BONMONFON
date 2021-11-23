# IMPORT EXTERNAL MODULES
import os.path
import grammarConverter

class Parser:
    def __init__(self, grammar, sentence):
        self.parse_chart = None
        self.grammar = None
        self.input = None
        self.sentence = sentence
        if os.path.isfile(grammar):
            self.grammar_from_file(grammar)
        else:
            self.grammar_from_string(grammar)
        self.__call__(sentence)

    def __call__(self, sentence, parse=False):
        if os.path.isfile(sentence):
            with open(sentence) as inp:
                self.input = inp.readline().split()
                if parse:
                    self.parse()
        else:
            self.input = sentence.split()
            self.sentence = sentence

    def grammar_from_file(self, grammar):
        self.grammar = grammarConverter.convGrammar(grammarConverter.readGrammar(grammar))

    def grammar_from_string(self, grammar):
        self.grammar = grammarConverter.convGrammar([x.replace("->", "").split() for x in grammar.split("\n")])

    def parse(self):
        '''
            initialize a data structure
            chart construction for CYK algorithm
        '''
        length = len(self.input)
        self.parse_chart = [[[] for x in range(length)] for y in range(length)]

        '''
            dealing with strings of length = 1 (individual words)
            check each word with rule
        '''
        for i, word in enumerate(self.input):
            for rule in self.grammar:
                if f"'{word}'" == rule[1]:
                    self.parse_chart[0][i].append(Node(rule[0], word))

        '''
            dealing with strings of length >= 2 (substring of increasing length)
            starting with pairs of words to the full length of the sentence
        '''
        for words_to_consider in range(2, length + 1):
            for starting_cell in range(0, length - words_to_consider + 1):
                for left_size in range(1, words_to_consider):
                    right_size = words_to_consider - left_size
                    left_cell = []
                    right_cell = []
                    left_cell = self.parse_chart[left_size - 1][starting_cell]
                    right_cell = self.parse_chart[right_size - 1][starting_cell + left_size]
                    # print(len(left_cell))
                    for rule in self.grammar:
                        left_nodes = [n for n in left_cell if n.symbol == rule[1]]
                        if left_nodes:
                            right_nodes = [n for n in right_cell if n.symbol == rule[2]]
                            self.parse_chart[words_to_consider - 1][starting_cell].extend([Node(rule[0], left, right) for left in left_nodes for right in right_nodes])

    def print_tree(self, output=True):
        start_symbol = self.grammar[0][0]
        final_nodes = [n for n in self.parse_chart[-1][0] if n.symbol == start_symbol]
        if final_nodes:
            if output:
                return True
        else:
            return False

    def __del__(self):
        print("Closing parser...")


def generate_tree(node):
    if node.childRight is None:
        return f"[{node.symbol} '{node.childLeft}']"
    return f"[{node.symbol} {generate_tree(node.childLeft)} {generate_tree(node.childRight)}]"

class Node:
    '''
        Storing information about a non-terminal symbol
    '''
    def __init__(self, symbol, childLeft, childRight=None):
        self.symbol = symbol
        self.childLeft = childLeft
        self.childRight = childRight

    def __repr__(self):
        return self.symbol