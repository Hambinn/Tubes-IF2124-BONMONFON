RULE_DICTIONARY = {}

def print_grammar(grammar):
	for rule in grammar:
		print(rule[0], " -> ", end='')
		for i in rule[1:]:
			print(i, end=' ')
		print()

def writeGrammar(grammar):
    file = open('cnf_grammar.txt', 'w')
    for rule in grammar:
        file.write(rule[0])
        file.write(" -> ")
        for i in rule[1:]:
            file.write(i)
            file.write(" ")
        file.write("\n")
    file.close()

def readGrammar(grammar_file):
    with open(grammar_file) as cfg:
        lines = cfg.readlines()
    return [x.replace("->", "").split() for x in lines]

def addRule(rule):
    global RULE_DICTIONARY

    if rule[0] not in RULE_DICTIONARY:
        RULE_DICTIONARY[rule[0]] = []
    RULE_DICTIONARY[rule[0]].append(rule[1:])