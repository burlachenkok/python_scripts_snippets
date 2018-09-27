#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Copyright (c) 2018, Konstantin Burlachenko (burlachenkok@gmail.com).  All rights reserved.

import sys, os

def print2args(a, b):
    print a, b
    
def printEnvVariable(name, extraDescr = ""):
    if name in os.environ:
        print2args("Env.Variable '" + name + "': " + os.environ[name], extraDescr)
    else:
        print2args("Env.Variable '" + name + "': " + "NOT SETUPED", extraDescr)

print2args("Path to python interpretator: ", sys.executable)
print2args("Version: ", sys.version)
print2args("Max stack-frame depth: ", sys.getrecursionlimit())
print2args("Platform name: ", sys.platform)
printEnvVariable("PYTHONPATH", "(Path with extra modules)")
print2args("\nSearch modules paths:\n", sys.path)
print2args("File name: ", __file__)

