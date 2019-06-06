#!/usr/bin/python env
# -*- coding: utf-8 -*-
import os

import grammars

Grammars = grammars.Grammars()

choice = 0
while choice != 5:
  os.system('cls||clear')

  print "G1 = ({S}, {a,b}, S, P1) com P1 = {S → aSbb | aab}"
  print "G2 = ({S, A, B},{a,b},S, P2) com P2 = {S → aABB | aAA, A→aBB|a, B→bBB|A }"
  print "G3 = ({S,A},{a,b},S, P3) com P3 = {S → AA|a, A→ AS|b}"
  print "G4 = ({S,X,A,B},{a,b}, S, P4) com P4 = {S → aXAX | aBX | b, X → aBX | b , A → a, B → b}"

  grammar = raw_input("\nEscolha a Gramatica:\n  1 -> [G1]\n  2 -> [G2]\n  3 -> [G3]\n  4 -> [G4]\n  5 -> Sair\n -> ") 

  if grammar == "1":
    entry = raw_input("\nDigite a linguagem -> ")
    Grammars.G1(entry)

  elif grammar == "2":
    entry = raw_input("\nDigite a linguagem -> ")
    Grammars.G2(entry)

  elif grammar == "3":
    entry = raw_input("\nDigite a linguagem -> ")
    Grammars.G3(entry)

  elif grammar == "4":
    entry = raw_input("\nDigite a linguagem -> ")
    Grammars.G4(entry)

  elif grammar == "5":
    break;

  else:
    print "OPCAO INVALIDA INDEFERIDA"

  raw_input("\nPRESSIONE <ENTER> PARA CONTINUAR ")