#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os
import codecs, datetime


if __name__ == "__main__":
    
    DT = "2000-01-01"
    max = {}
    today = {}
    maxD = {}
    
    with codecs.open('/mnt/d/Twitediens/WTF-Snickers.json', 'r', encoding='utf-8', errors='ignore') as fullFile:
        for wi in fullFile:
            if len(wi) > 5:
                text = ' '.join(wi.strip()[:-1].split()).replace('}, ]','} ]')
                
                try:
                    tweet_dict = json.loads(text)
                except json.decoder.JSONDecodeError as e:
                    sys.stderr.write(wi.strip()[:-1])
                    sys.exit(e.message)
                    
                if DT != str(datetime.datetime.strptime(tweet_dict["created_at"], '%Y-%m-%d %H:%M:%S'))[:10]:
                    #New day! Check if we have any new records
                    for word in today:
                        if word not in max or max[word] < today[word]:
                            max[word] = today[word]
                            maxD[word] = DT
                            sys.stderr.write(word + "\t" + str(max[word]) + "\t" + maxD[word] + "\n")
                        
                    #Restart counting
                    DT = str(datetime.datetime.strptime(tweet_dict["created_at"], '%Y-%m-%d %H:%M:%S'))[:10]
                    today = None
                    today = {}
                
                if "food_nominative_form" in tweet_dict:
                    foodWords = tweet_dict["food_nominative_form"][:-1].split(";")
                    sys.stderr.write(tweet_dict["food_nominative_form"] + "\n")
                        
                    for foodWord in foodWords:
                        if len(foodWord) > 0:
                            if foodWord not in today:
                                today[foodWord] = 1
                            else:
                                if tweet_dict["tweet_text"][0:4] != "RT @":
                                    today[foodWord] += 1
                        
                      
    for word in today:
        if word not in max or max[word] < today[word]:
            max[word] = today[word]
            maxD[word] = DT
            sys.stderr.write(word + "\t" + str(max[word]) + "\t" + maxD[word] + "\n")  
    for word in max:
        print(word + "\t" + str(max[word]) + "\t" + maxD[word])
                        
                        
                        
                        
                        
                        
                        
                        
                        