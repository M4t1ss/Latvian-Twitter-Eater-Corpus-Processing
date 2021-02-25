#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os


if __name__ == "__main__":
    
    outFile = open('found-words-tweets-december-nominative-date-thic.tok.txt','w')
    # Atlasa tvītus pēc sarakstā minētajiem vārdiem 
    inFile = open("vardu-saraksti/thic.txt","r")
    fullFile = open("ltec-full-december-2020-nominative-date.UR.US.tok.u.keep.txt","r")
    
    searchArray = []
    
    #Populate replacement array
    for wi in inFile:
        searchArray.append(wi.strip())
        
    for wi in fullFile:
        words = wi.lower().strip().split()
        
        sentenceparts = wi.strip().split(" VISIATSLEGVARDISEKO ")
        sentence = sentenceparts[0]
        date = sentenceparts[-1]
        if len(sentenceparts) > 2:
            foodWords = sentenceparts[1][:-2].split(" ;")
        else:
            foodWords = ["-"]
            
        for word in searchArray:
            if word.lower().strip() in words:
                for foodWord in foodWords:
                    outFile.write(word + "\t" + foodWord.strip() + "\t" + sentence.strip() + "\t" + date.strip() + "\n")
        
    outFile.close();
    inFile.close();
    fullFile.close();