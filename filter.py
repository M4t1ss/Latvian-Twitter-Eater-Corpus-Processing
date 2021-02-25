#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os



if __name__ == "__main__":
    
    outFile = open('found-tweets.json','w')
    inFile = open("visivardi.txt","r")
    fullFile = open("ltec-full-august-2020.json","r")
    
    searchArray = []
    
    #Populate replacement array
    for wi in inFile:
        searchArray.append(wi.strip())
    sys.stderr.write(searchArray[0] + "\n")
    sys.stderr.write(searchArray[-1] + "\n")
    sys.stderr.write(str(len(searchArray)) + "\n")
        
    line = 1
    for wi in fullFile:
        # sys.stderr.write(str(line)+"\n")
        line+=1
        if len(wi) > 5:
            text = ' '.join(wi.strip()[:-1].split()).replace('}, ]','} ]')
            
            try:
                tweet_dict = json.loads(text)
            except json.decoder.JSONDecodeError as e:
                sys.stderr.write(wi.strip()[:-1])
                sys.exit(e.message)
            
            
            for word in searchArray:
                if word.lower().strip() in tweet_dict["tweet_text"].lower():
                    tweet_dict["found_word"] = word
                    # sys.stderr.write("FOUND!\n")
                    output = json.dumps(tweet_dict, sort_keys=True, ensure_ascii=False)
                    outFile.write(output.strip() + ",\n")
        
    outFile.close();
    inFile.close();
    fullFile.close();