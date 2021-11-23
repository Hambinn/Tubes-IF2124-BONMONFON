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
    
def convGrammar(grammar):
    global RULE_DICTIONARY
    unit_productions, result = [], []
    res_append = result.append
    index = 0

    for rule in grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            unit_productions.append(rule)
            addRule(rule)
            continue
        elif len(rule) > 2:
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    rule[item[1]] = f"{rule[0]}{str(index)}"
                    new_rules += [f"{rule[0]}{str(index)}", item[0]]
                index += 1
            while len(rule) > 3:
                new_rules += [f"{rule[0]}{str(index)}", rule[1], rule[2]]
                rule = [rule[0]] + [f"{rule[0]}{str(index)}"] + rule[3:]
                index += 1
        addRule(rule)
        res_append(rule)
        if new_rules:
            res_append(new_rules)
    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in RULE_DICTIONARY:
            for item in RULE_DICTIONARY[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    res_append(new_rule)
                else:
                    unit_productions.append(new_rule)
                addRule(new_rule)
    return result

if __name__ == '__main__':

    writeGrammar(convGrammar(readGrammar('grammar.txt')))