#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os
import codecs

def longestCommonSubstring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

if __name__ == "__main__":
    
    delFile = open("ltec-full-december-2020-nominative-date.UR.US.tok.u.del.txt","w")
    keepFile = open("ltec-full-december-2020-nominative-date.UR.US.tok.u.keep.txt","w")
    
    prevline = ""
    currline = ""
    prevsent = ""
    currsent = ""
    
    
    #Filters out consecutive lines that have a certain overlap of content
    
    
    with codecs.open('ltec-full-december-2020-nominative-date.UR.US.tok.u.txt', 'r', encoding='utf-8', errors='ignore') as fullFile:
        for currline in fullFile:
            if len(prevline.strip()) > 0:
            
                currsent = currline.strip().split(" VISIATSLEGVARDISEKO ")[0]
            
                longest = longestCommonSubstring(prevsent.lower(), currsent.lower()).strip()
                similarity = len(longest)/len(currsent)
                
                if (similarity > 0.4):
                    #Too similar... keep longest
                    if len(currsent) > len(prevsent):
                        delFile.write(prevline.strip() + "\n")
                        prevline = currline
                        prevsent = currsent
                    else:
                        delFile.write(currline.strip() + "\n")
                else:
                    #Not too similar... move along...
                    keepFile.write(prevline.strip() + "\n")
                    prevline = currline
                    prevsent = currsent
            else:
                prevline = currline
                prevsent = currsent
        
        keepFile.write(prevline.strip() + "\n")
        
        
    delFile.close();
    keepFile.close();
    
    