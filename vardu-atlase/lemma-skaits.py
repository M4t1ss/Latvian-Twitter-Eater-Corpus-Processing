#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os


if __name__ == "__main__":
    
    outFile = open('lemma-skaits.txt','w')
    # Atlasa tvītus pēc sarakstā minētajiem vārdiem 
    inFile = open("vards-skaits.txt","r")
    fullFile = open("lemma-vards.txt","r")
    
    skaiti = {}
    rezultats = {}
    
    #Populate replacement array
    for wi in inFile:
        parts = wi.strip().split("\t")
        skaiti[parts[0]] = parts[1]
        
    for wi in fullFile:
        parts = wi.strip().split("\t")
        lemma = parts[0]
        vards = parts[1]
        
        if vards in skaiti:
            if lemma in rezultats:
                rezultats[lemma] = rezultats[lemma] + int(skaiti[vards])
            else:
                rezultats[lemma] = int(skaiti[vards])
        else:
            if lemma not in rezultats:
                rezultats[lemma] = 0
        
            
            
    for lemma in rezultats:
        outFile.write(lemma + "\t" + str(rezultats[lemma]) + "\n")
        
    outFile.close();
    inFile.close();
    fullFile.close();