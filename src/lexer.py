""" -------------------------- LEXER.PY -------------------------- """

# IMPORT EXTERNAL MODULES
import re
import sys
import argparse
import cykParser

class Lexer(object):

    # CONSTRUCTOR
    def __init__(self, rules):
        """ CONSTRUCTOR """

        # INITIALIZATION
        regexRules = []
        self.groupType = {}
        i = 0

        for regex, type in rules:
            i += 1
            groupName = 'GROUP' + str(i)
            regexRules.append('(?P<%s>%s)' % (groupName, regex))
            self.groupType[groupName] = type

        self.regex = re.compile('|'.join(regexRules))
        self.skipWhitespace = re.compile('[\S^\n]')

    # INPUT CONVERTER
    def inputConverter(self, input):
        """
            ---- INPUT CONVERTER ----

            Convert input into buffer 
        """

        self.buffer = input
        self.pos = 0
    
    # TOKENIZER
    def tokenizer(self):
        """
            ------------- TOKENIZER -------------

            Return nextToken from buffer input;
            if None is returned, buffer is empty.
        """

        if (len(self.buffer) <= self.pos):
            return None
        else:
            m = self.skipWhitespace.search(self.buffer, self.pos)

            if m:
                self.pos = m.start()
                m = self.regex.match(self.buffer, self.pos)
                
                if m:
                    groupName = m.lastgroup
                    tokenType = self.groupType[groupName]
                    nextToken = tokenType
                    self.pos = m.end()
                    if (nextToken == 'WHITESPACE'):
                        return ''
                    return nextToken
                else:
                    raise Error(self.pos)
            else:
                return None
            
    
    def token(self):
        """
            ------------ TOKEN ------------

            Return token from input buffer.
        """

        token = self.tokenizer()
        while (token is not None):
            if (token is not None):
                yield token
                token = self.tokenizer()
        # token == None

class Token(object):

    # CONSTRUCTOR
    def __init__(self, type, val, pos):
        """ CONSTRUCTOR """
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%s(%s) at %s' % (self.type, self.val, self.pos)

class Error(Exception):
    def __init__(self, pos):
        self.pos = pos