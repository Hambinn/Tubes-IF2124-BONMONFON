from converterUtility import *
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