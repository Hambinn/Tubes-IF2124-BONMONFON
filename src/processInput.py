""" --------------------- PROCESSINPUT.PY --------------------- """

def processFile(file,CYK):
    """ ------------------ PROCESS FILE ------------------ """
    """ Prints 'Accepted' if no errors found in text;
               'Syntax Error' and error location if found  """

    # INITIALIZATION
    multiLine = False
    conditional = 0
    foundError = False
    lineIndex = 0

    for line in file:
        lineIndex += 1
        # MULTILINE CHECKER
        if ((line.find('TRIPLEQUOTE') != -1) and (multiLine == False)):
            multiLine = True
        elif ((line.find('TRIPLEQUOTE') != -1) and (multiLine == True)):
            multiLine = False
        else:
            if (line == ' ' or line == ''):
                print("",end='')
            elif (multiLine == False):
                # CONDITIONAL CHECKER
                if (line.find(' IF') != -1):
                    conditional += 1
                    if (not processText(line,CYK)):
                        foundError = True
                        break
                elif (line.find('ELIF') != -1):
                    if (conditional > 0):
                        line = 'ELIFTOK' + line
                    if (not processText(line,CYK)):
                        foundError = True
                        break
                elif (line.find('ELSE') != -1):
                    if (conditional > 0):
                        line = 'ELIFTOK' + line
                    conditional -= 1
                    if (not processText(line,CYK)):
                        foundError = True
                        break
                else:
                    if (not processText(line,CYK)):
                        foundError = True
                        break

    if (foundError == False):
        print('Accepted')
    else:
        print('Syntax Error')
        print('Error found in line: {}'.format(lineIndex))


def processText(text,CYK):
    """ ------------ PROCESS TEXT ------------ """
    """ return True if no Syntax errors found  """
    
    CYK.__call__(text)
    CYK.parse()
    return CYK.print_tree()