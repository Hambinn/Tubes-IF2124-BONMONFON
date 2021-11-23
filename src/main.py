""" -------------------------- MAIN.PY -------------------------- """

# IMPORT EXTERNAL MODULES
import re
import sys
import os
import argparse

import lexer
import cykParser
from rulesDictionary import rules

def title():
    """ --- PRINT TITLE BANNER --- """
    print('\n\n')
    print('                        TUGAS BESAR')
    print('           IF2124 TEORI BAHASA FORMAL DAN OTOMATA')
    print('              ______      _   _                          ')
    print('              | ___ \    | | | |                         ')
    print('              | |_/ /   _| |_| |__   ___  _ __           ')
    print('              |  __/ | | | __| \'_ \ / _ \| \'_ \          ')
    print('              | |  | |_| | |_| | | | (_) | | | |         ')
    print('              \_|   \__, |\__|_| |_|\___/|_| |_|         ')
    print('            ____     __/ |             _ _               ')
    print('           / __ \   |___/             (_) |              ')
    print('          | /  \/ ___  _ __ ___  _ __  _| | ___ _ __ ')
    print('          | |    / _ \| \'_ ` _ \| \'_ \| | |/ _ \ \'__|')
    print('          | \__/\ (_) | | | | | | |_) | | |  __/ |   ')
    print('           \____/\___/|_| |_| |_| .__/|_|_|\___|_|   ')
    print('                                | |                  ')
    print('                                |_| Created by: BonMonFon')
    print('\n\n')

def fileReader(fileName):
    """ --- READ FILE --- """
    try:
        fileRead = open(fileName, 'r', encoding="utf8")
        return fileRead.read()
    except Exception as e:
        print('Error opening: ' + fileName)
        exit(0)

def processFile(file):
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
                    if (not processText(line)):
                        foundError = True
                        break
                elif (line.find('ELIF') != -1):
                    if (conditional > 0):
                        line = 'ELIFTOK' + line
                    if (not processText(line)):
                        foundError = True
                        break
                elif (line.find('ELSE') != -1):
                    if (conditional > 0):
                        line = 'ELIFTOK' + line
                    conditional -= 1
                    if (not processText(line)):
                        foundError = True
                        break
                else:
                    if (not processText(line)):
                        foundError = True
                        break

    if (foundError == False):
        print('Accepted')
    else:
        print('Syntax Error')
        print('Error found in line: {}'.format(lineIndex))


def processText(text):
    """ ------------ PROCESS TEXT ------------ """
    """ return True if no Syntax errors found  """
    
    CYK.__call__(text)
    CYK.parse()
    return CYK.print_tree()

if __name__ == '__main__':
    CYK = cykParser.Parser('grammar.txt', " COMMENT ")

    # MAIN PROGRAM
    title()

    # Open and Read File
    fileName = './test/' + input('Input file name: ')
    fileInput = fileReader(fileName)
    lex = lexer.Lexer(rules)
    lex.inputConverter(fileInput)

    # INITIALIZATION
    output = ''
    try:
        for token in lex.token():
            if token == '':         # BASE
                output = output
            else:                   # RECURRENCE
                output += token + ' '
    except lexer.Error as e:
        print('LexerError at position %s' % e.pos)
        exit(0)

    fileOutput = output.split('NEWLINE')

    print('\n======================== COMPILING =======================\n')

    print('Compiling {}...\n'.format(fileName))
    print('Waiting for yout verdict...\n')
    print('========================= VERDICT ========================\n')

    processFile(fileOutput)
    print('\n')