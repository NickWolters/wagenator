# Generated by Grammarinator 23.7

import itertools

from math import inf
from grammarinator.runtime import *

class WagGenerator(Generator):


    def EOF(self, parent=None):
        pass
    EOF.min_depth = 0

    def INCLUDEDECL(self, parent=None):
        with RuleContext(self, UnlexerRule(name='INCLUDEDECL', parent=parent)) as current:
            UnlexerRule(src='::', parent=current)
            return current
    INCLUDEDECL.min_depth = 0

    def PROPESITION_SIGN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='PROPESITION_SIGN', parent=parent)) as current:
            UnlexerRule(src='->', parent=current)
            return current
    PROPESITION_SIGN.min_depth = 0

    def IDENTIFIER(self, parent=None):
        with RuleContext(self, UnlexerRule(name='IDENTIFIER', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[1]), parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src=self._model.charset(current, 1, self._charsets[2]), parent=current)
            return current
    IDENTIFIER.min_depth = 0

    def TERMOP(self, parent=None):
        with RuleContext(self, UnlexerRule(name='TERMOP', parent=parent)) as current:
            with AlternationContext(self, [0, 0, 0, 0], [1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['*', '//', '/', '%'][choice0], parent=current)
            return current
    TERMOP.min_depth = 0

    def ATTRSPEC(self, parent=None):
        with RuleContext(self, UnlexerRule(name='ATTRSPEC', parent=parent)) as current:
            with AlternationContext(self, [0, 0, 0], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['$', '*', '&'][choice0], parent=current)
            return current
    ATTRSPEC.min_depth = 0

    def SUMOP(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SUMOP', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['+', '-'][choice0], parent=current)
            return current
    SUMOP.min_depth = 0

    def EBNFTYPE(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EBNFTYPE', parent=parent)) as current:
            with AlternationContext(self, [0, 0, 0], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['@', '~', '?'][choice0], parent=current)
            return current
    EBNFTYPE.min_depth = 0

    def BOOL(self, parent=None):
        with RuleContext(self, UnlexerRule(name='BOOL', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                UnlexerRule(src=['true', 'false'][choice0], parent=current)
            return current
    BOOL.min_depth = 0

    def NUM(self, parent=None):
        with RuleContext(self, UnlexerRule(name='NUM', parent=parent)) as current:
            UnlexerRule(src=self._model.charset(current, 0, self._charsets[3]), parent=current)
            return current
    NUM.min_depth = 0

    def FLOAT(self, parent=None):
        with RuleContext(self, UnlexerRule(name='FLOAT', parent=parent)) as current:
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    UnlexerRule(src=self._model.charset(current, 0, self._charsets[4]), parent=current)
            UnlexerRule(src='.', parent=current)
            if self._max_depth >= 0:
                for _ in self._model.quantify(current, 1, min=0, max=inf):
                    UnlexerRule(src=self._model.charset(current, 1, self._charsets[5]), parent=current)
            return current
    FLOAT.min_depth = 0

    def STRING(self, parent=None):
        with RuleContext(self, UnlexerRule(name='STRING', parent=parent)) as current:
            with AlternationContext(self, [0, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    UnlexerRule(src='"', parent=current)
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            UnlexerRule(src=self._model.charset(current, 0, self._charsets[6]), parent=current)
                    UnlexerRule(src='"', parent=current)
                elif choice0 == 1:
                    UnlexerRule(src='\'', parent=current)
                    if self._max_depth >= 0:
                        for _ in self._model.quantify(current, 1, min=0, max=inf):
                            UnlexerRule(src=self._model.charset(current, 1, self._charsets[7]), parent=current)
                    UnlexerRule(src='\'', parent=current)
            return current
    STRING.min_depth = 0

    def EBNF_OPTION(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EBNF_OPTION', parent=parent)) as current:
            UnlexerRule(src='|', parent=current)
            return current
    EBNF_OPTION.min_depth = 0

    def SUBPROC(self, parent=None):
        with RuleContext(self, UnlexerRule(name='SUBPROC', parent=parent)) as current:
            UnlexerRule(src='$( /[^)]*/ )', parent=current)
            return current
    SUBPROC.min_depth = 0

    def DECLARATION(self, parent=None):
        with RuleContext(self, UnlexerRule(name='DECLARATION', parent=parent)) as current:
            UnlexerRule(src=':', parent=current)
            return current
    DECLARATION.min_depth = 0

    def STATEMENT_END(self, parent=None):
        with RuleContext(self, UnlexerRule(name='STATEMENT_END', parent=parent)) as current:
            UnlexerRule(src=';', parent=current)
            return current
    STATEMENT_END.min_depth = 0

    def EQ(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EQ', parent=parent)) as current:
            UnlexerRule(src='=', parent=current)
            return current
    EQ.min_depth = 0

    def META_END(self, parent=None):
        with RuleContext(self, UnlexerRule(name='META_END', parent=parent)) as current:
            UnlexerRule(src='****', parent=current)
            return current
    META_END.min_depth = 0

    def INVERSE_SIGN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='INVERSE_SIGN', parent=parent)) as current:
            UnlexerRule(src='!', parent=current)
            return current
    INVERSE_SIGN.min_depth = 0

    def BRACKET_L(self, parent=None):
        with RuleContext(self, UnlexerRule(name='BRACKET_L', parent=parent)) as current:
            UnlexerRule(src='[', parent=current)
            return current
    BRACKET_L.min_depth = 0

    def BRACKET_R(self, parent=None):
        with RuleContext(self, UnlexerRule(name='BRACKET_R', parent=parent)) as current:
            UnlexerRule(src=']', parent=current)
            return current
    BRACKET_R.min_depth = 0

    def ATTR_ASSIGN_L(self, parent=None):
        with RuleContext(self, UnlexerRule(name='ATTR_ASSIGN_L', parent=parent)) as current:
            UnlexerRule(src='{', parent=current)
            return current
    ATTR_ASSIGN_L.min_depth = 0

    def ATTR_ASSIGN_R(self, parent=None):
        with RuleContext(self, UnlexerRule(name='ATTR_ASSIGN_R', parent=parent)) as current:
            UnlexerRule(src='}', parent=current)
            return current
    ATTR_ASSIGN_R.min_depth = 0

    def LPAREN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='LPAREN', parent=parent)) as current:
            UnlexerRule(src='(', parent=current)
            return current
    LPAREN.min_depth = 0

    def RPAREN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='RPAREN', parent=parent)) as current:
            UnlexerRule(src=')', parent=current)
            return current
    RPAREN.min_depth = 0

    def LEFT_ANGLE_BRACKET(self, parent=None):
        with RuleContext(self, UnlexerRule(name='LEFT_ANGLE_BRACKET', parent=parent)) as current:
            UnlexerRule(src='<', parent=current)
            return current
    LEFT_ANGLE_BRACKET.min_depth = 0

    def RIGHT_ANGLE_BRACKET(self, parent=None):
        with RuleContext(self, UnlexerRule(name='RIGHT_ANGLE_BRACKET', parent=parent)) as current:
            UnlexerRule(src='>', parent=current)
            return current
    RIGHT_ANGLE_BRACKET.min_depth = 0

    def DELIMITER(self, parent=None):
        with RuleContext(self, UnlexerRule(name='DELIMITER', parent=parent)) as current:
            UnlexerRule(src=',', parent=current)
            return current
    DELIMITER.min_depth = 0

    def IF(self, parent=None):
        with RuleContext(self, UnlexerRule(name='IF', parent=parent)) as current:
            UnlexerRule(src='if', parent=current)
            return current
    IF.min_depth = 0

    def ELSE(self, parent=None):
        with RuleContext(self, UnlexerRule(name='ELSE', parent=parent)) as current:
            UnlexerRule(src='else', parent=current)
            return current
    ELSE.min_depth = 0

    def THEN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='THEN', parent=parent)) as current:
            UnlexerRule(src='then', parent=current)
            return current
    THEN.min_depth = 0

    def AND(self, parent=None):
        with RuleContext(self, UnlexerRule(name='AND', parent=parent)) as current:
            UnlexerRule(src='&&', parent=current)
            return current
    AND.min_depth = 0

    def OR(self, parent=None):
        with RuleContext(self, UnlexerRule(name='OR', parent=parent)) as current:
            UnlexerRule(src='||', parent=current)
            return current
    OR.min_depth = 0

    def FACTORIAL(self, parent=None):
        with RuleContext(self, UnlexerRule(name='FACTORIAL', parent=parent)) as current:
            UnlexerRule(src='**', parent=current)
            return current
    FACTORIAL.min_depth = 0

    def LEQ(self, parent=None):
        with RuleContext(self, UnlexerRule(name='LEQ', parent=parent)) as current:
            UnlexerRule(src='<=', parent=current)
            return current
    LEQ.min_depth = 0

    def GEQ(self, parent=None):
        with RuleContext(self, UnlexerRule(name='GEQ', parent=parent)) as current:
            UnlexerRule(src='>=', parent=current)
            return current
    GEQ.min_depth = 0

    def EQ2(self, parent=None):
        with RuleContext(self, UnlexerRule(name='EQ2', parent=parent)) as current:
            UnlexerRule(src='==', parent=current)
            return current
    EQ2.min_depth = 0

    def NEQ(self, parent=None):
        with RuleContext(self, UnlexerRule(name='NEQ', parent=parent)) as current:
            UnlexerRule(src='!=', parent=current)
            return current
    NEQ.min_depth = 0

    def IN(self, parent=None):
        with RuleContext(self, UnlexerRule(name='IN', parent=parent)) as current:
            UnlexerRule(src='in', parent=current)
            return current
    IN.min_depth = 0

    def wag(self, parent=None):
        with RuleContext(self, UnparserRule(name='wag', parent=parent)) as current:
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    self.rule(parent=current)
            return current
    wag.min_depth = 0

    def metadata(self, parent=None):
        with RuleContext(self, UnparserRule(name='metadata', parent=parent)) as current:
            if self._max_depth >= 3:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    self.meta(parent=current)
            self.META_END(parent=current)
            return current
    metadata.min_depth = 1

    def meta(self, parent=None):
        with RuleContext(self, UnparserRule(name='meta', parent=parent)) as current:
            with AlternationContext(self, [2, 2], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.include, self.config][choice0](parent=current)
            return current
    meta.min_depth = 2

    def include(self, parent=None):
        with RuleContext(self, UnparserRule(name='include', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.IDENTIFIER(parent=current)
            self.INCLUDEDECL(parent=current)
            self.IDENTIFIER(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 1, min=0, max=1):
                    self.include(parent=current)
            return current
    include.min_depth = 1

    def config(self, parent=None):
        with RuleContext(self, UnparserRule(name='config', parent=parent)) as current:
            self.IDENTIFIER(parent=current)
            self.DECLARATION(parent=current)
            self.IDENTIFIER(parent=current)
            self.STATEMENT_END(parent=current)
            return current
    config.min_depth = 1

    def rule(self, parent=None):
        with RuleContext(self, UnparserRule(name='rule', parent=parent)) as current:
            self.IDENTIFIER(parent=current)
            if self._max_depth >= 3:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.nTArgs(parent=current)
            self.PROPESITION_SIGN(parent=current)
            self.rhs(parent=current)
            self.STATEMENT_END(parent=current)
            return current
    rule.min_depth = 1

    def rhs(self, parent=None):
        with RuleContext(self, UnparserRule(name='rhs', parent=parent)) as current:
            with AlternationContext(self, [1, 0], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    if self._max_depth >= 3:
                        for _ in self._model.quantify(current, 0, min=0, max=1):
                            self.weight(parent=current)
                    if self._max_depth >= 3:
                        for _ in self._model.quantify(current, 1, min=0, max=inf):
                            self.chunk(parent=current)
                    self.EBNF_OPTION(parent=current)
                    self.rhs(parent=current)
                elif choice0 == 1:
                    if self._max_depth >= 3:
                        for _ in self._model.quantify(current, 2, min=0, max=1):
                            self.weight(parent=current)
                    if self._max_depth >= 3:
                        for _ in self._model.quantify(current, 3, min=0, max=inf):
                            self.chunk(parent=current)
            return current
    rhs.min_depth = 0

    def weight(self, parent=None):
        with RuleContext(self, UnparserRule(name='weight', parent=parent)) as current:
            self.BRACKET_L(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.attrIdentifier(parent=current)
            self.expression(parent=current)
            self.BRACKET_R(parent=current)
            return current
    weight.min_depth = 2

    def chunk(self, parent=None):
        with RuleContext(self, UnparserRule(name='chunk', parent=parent)) as current:
            self.chunkP(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.EBNFTYPE(parent=current)
            return current
    chunk.min_depth = 2

    def chunkP(self, parent=None):
        with RuleContext(self, UnparserRule(name='chunkP', parent=parent)) as current:
            with AlternationContext(self, [3, 1], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.symbol(parent=current)
                elif choice0 == 1:
                    self.LPAREN(parent=current)
                    if self._max_depth >= 3:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            self.chunk(parent=current)
                    self.RPAREN(parent=current)
            return current
    chunkP.min_depth = 1

    def symbol(self, parent=None):
        with RuleContext(self, UnparserRule(name='symbol', parent=parent)) as current:
            with AlternationContext(self, [2, 2, 3], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.nonTerminal, self.terminal, self.assignment][choice0](parent=current)
            return current
    symbol.min_depth = 2

    def terminal(self, parent=None):
        with RuleContext(self, UnparserRule(name='terminal', parent=parent)) as current:
            with AlternationContext(self, [1, 1, 1, 1], [1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.STRING, self.FLOAT, self.BOOL, self.NUM][choice0](parent=current)
            return current
    terminal.min_depth = 1

    def nonTerminal(self, parent=None):
        with RuleContext(self, UnparserRule(name='nonTerminal', parent=parent)) as current:
            self.IDENTIFIER(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.EBNFTYPE(parent=current)
            return current
    nonTerminal.min_depth = 1

    def nTArgs(self, parent=None):
        with RuleContext(self, UnparserRule(name='nTArgs', parent=parent)) as current:
            self.LEFT_ANGLE_BRACKET(parent=current)
            self.attrIdentifierList(parent=current)
            self.RIGHT_ANGLE_BRACKET(parent=current)
            return current
    nTArgs.min_depth = 2

    def attrIdentifier(self, parent=None):
        with RuleContext(self, UnparserRule(name='attrIdentifier', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.ATTRSPEC(parent=current)
            self.IDENTIFIER(parent=current)
            return current
    attrIdentifier.min_depth = 1

    def attrIdentifierList(self, parent=None):
        with RuleContext(self, UnparserRule(name='attrIdentifierList', parent=parent)) as current:
            with AlternationContext(self, [2, 2, 1], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.attrIdentifier(parent=current)
                    self.DELIMITER(parent=current)
                    self.attrIdentifierList(parent=current)
                elif choice0 == 1:
                    self.attrIdentifier(parent=current)
                elif choice0 == 2:
                    self.STRING(parent=current)
            return current
    attrIdentifierList.min_depth = 1

    def assignment(self, parent=None):
        with RuleContext(self, UnparserRule(name='assignment', parent=parent)) as current:
            with AlternationContext(self, [4, 2], [1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.nTAssigment, self.attributeAssignment][choice0](parent=current)
            return current
    assignment.min_depth = 2

    def nTAssigment(self, parent=None):
        with RuleContext(self, UnparserRule(name='nTAssigment', parent=parent)) as current:
            self.nonTerminal(parent=current)
            self.nTArgs(parent=current)
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.EBNFTYPE(parent=current)
            return current
    nTAssigment.min_depth = 3

    def attributeAssignment(self, parent=None):
        with RuleContext(self, UnparserRule(name='attributeAssignment', parent=parent)) as current:
            self.ATTR_ASSIGN_L(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=inf):
                    self.attrIdentifier(parent=current)
                    self.EQ(parent=current)
                    self.expression(parent=current)
                    self.STATEMENT_END(parent=current)
            self.ATTR_ASSIGN_R(parent=current)
            return current
    attributeAssignment.min_depth = 1

    def expression(self, parent=None):
        with RuleContext(self, UnparserRule(name='expression', parent=parent)) as current:
            with AlternationContext(self, [1, 9, 8], [1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.SUBPROC, self.if_statement, self.disjunct][choice0](parent=current)
            return current
    expression.min_depth = 1

    def if_statement(self, parent=None):
        with RuleContext(self, UnparserRule(name='if_statement', parent=parent)) as current:
            self.IF(parent=current)
            self.disjunct(parent=current)
            self.THEN(parent=current)
            self.disjunct(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.ELSE(parent=current)
                    self.expression(parent=current)
            return current
    if_statement.min_depth = 8

    def disjunct(self, parent=None):
        with RuleContext(self, UnparserRule(name='disjunct', parent=parent)) as current:
            self.conjunct(parent=current)
            if self._max_depth >= 8:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.AND(parent=current)
                    self.disjunct(parent=current)
            return current
    disjunct.min_depth = 7

    def conjunct(self, parent=None):
        with RuleContext(self, UnparserRule(name='conjunct', parent=parent)) as current:
            self.inverse(parent=current)
            if self._max_depth >= 7:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.OR(parent=current)
                    self.conjunct(parent=current)
            return current
    conjunct.min_depth = 6

    def inverse(self, parent=None):
        with RuleContext(self, UnparserRule(name='inverse', parent=parent)) as current:
            if self._max_depth >= 1:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.INVERSE_SIGN(parent=current)
            self.comparison(parent=current)
            return current
    inverse.min_depth = 5

    def comparison(self, parent=None):
        with RuleContext(self, UnparserRule(name='comparison', parent=parent)) as current:
            self.sum(parent=current)
            if self._max_depth >= 4:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.compop(parent=current)
                    self.sum(parent=current)
            return current
    comparison.min_depth = 4

    def sum(self, parent=None):
        with RuleContext(self, UnparserRule(name='sum', parent=parent)) as current:
            self.term(parent=current)
            if self._max_depth >= 4:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.sumP(parent=current)
            return current
    sum.min_depth = 3

    def sumP(self, parent=None):
        with RuleContext(self, UnparserRule(name='sumP', parent=parent)) as current:
            self.SUMOP(parent=current)
            self.term(parent=current)
            if self._max_depth >= 4:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.sumP(parent=current)
            return current
    sumP.min_depth = 3

    def term(self, parent=None):
        with RuleContext(self, UnparserRule(name='term', parent=parent)) as current:
            self.factor(parent=current)
            if self._max_depth >= 3:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.termP(parent=current)
            return current
    term.min_depth = 2

    def termP(self, parent=None):
        with RuleContext(self, UnparserRule(name='termP', parent=parent)) as current:
            self.TERMOP(parent=current)
            self.factor(parent=current)
            if self._max_depth >= 3:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.termP(parent=current)
            return current
    termP.min_depth = 2

    def factor(self, parent=None):
        with RuleContext(self, UnparserRule(name='factor', parent=parent)) as current:
            self.atom(parent=current)
            if self._max_depth >= 2:
                for _ in self._model.quantify(current, 0, min=0, max=1):
                    self.FACTORIAL(parent=current)
                    self.factor(parent=current)
            return current
    factor.min_depth = 1

    def atom(self, parent=None):
        with RuleContext(self, UnparserRule(name='atom', parent=parent)) as current:
            with AlternationContext(self, [2, 3, 1, 0, 1, 1, 2], [1, 1, 1, 1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                if choice0 == 0:
                    self.attrIdentifier(parent=current)
                elif choice0 == 1:
                    self.dictonary(parent=current)
                elif choice0 == 2:
                    self.BOOL(parent=current)
                elif choice0 == 3:
                    if self._max_depth >= 1:
                        for _ in self._model.quantify(current, 0, min=0, max=inf):
                            self.NUM(parent=current)
                elif choice0 == 4:
                    self.FLOAT(parent=current)
                elif choice0 == 5:
                    self.STRING(parent=current)
                elif choice0 == 6:
                    self.LPAREN(parent=current)
                    self.expression(parent=current)
                    self.RPAREN(parent=current)
            return current
    atom.min_depth = 0

    def dictonary(self, parent=None):
        with RuleContext(self, UnparserRule(name='dictonary', parent=parent)) as current:
            self.BRACKET_L(parent=current)
            self.expression(parent=current)
            self.BRACKET_R(parent=current)
            return current
    dictonary.min_depth = 2

    def compop(self, parent=None):
        with RuleContext(self, UnparserRule(name='compop', parent=parent)) as current:
            with AlternationContext(self, [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]) as weights0:
                choice0 = self._model.choice(current, 0, weights0)
                [self.LEFT_ANGLE_BRACKET, self.LEQ, self.RIGHT_ANGLE_BRACKET, self.GEQ, self.EQ2, self.NEQ, self.IN][choice0](parent=current)
            return current
    compop.min_depth = 1

    _default_rule = wag

    _charsets = {
        0: list(itertools.chain.from_iterable([range(32, 127)])),
        1: list(itertools.chain.from_iterable([range(65, 91), range(97, 123)])),
        2: list(itertools.chain.from_iterable([range(48, 58), range(65, 91), range(95, 96), range(97, 123)])),
        3: list(itertools.chain.from_iterable([range(48, 58)])),
        4: list(itertools.chain.from_iterable([range(48, 58)])),
        5: list(itertools.chain.from_iterable([range(48, 58)])),
        6: list(itertools.chain.from_iterable([range(32, 34), range(35, 127)])),
        7: list(itertools.chain.from_iterable([range(32, 34), range(35, 127)])),
    }
