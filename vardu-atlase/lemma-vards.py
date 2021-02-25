#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os


if __name__ == "__main__":
    
    outFile = open('vardu-saraksti/lemma-vaards-thic.txt','w')
    # Atlasa tvītus pēc sarakstā minētajiem vārdiem 
    inFile = open("vardu-saraksti/thic-lemmas.txt","r")
    fullFile = open("vardu-saraksti/thic-le.txt","r")
    
    vardi = {}
    
    #Populate replacement array
    for wi in inFile:
        parts = wi.strip().split("\t")
        vardi[parts[1]] = parts[0]
        
    for wi in fullFile:
        vards = wi.strip()
        outFile.write(vardi[vards] + "\n")
        
    outFile.close();
    inFile.close();
    fullFile.close();