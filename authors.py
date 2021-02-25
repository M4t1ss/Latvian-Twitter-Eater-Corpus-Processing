#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os
import codecs, datetime


if __name__ == "__main__":
    
    authorDict = {}
    authorDict[2011] = []
    authorDict[2012] = []
    authorDict[2013] = []
    authorDict[2014] = []
    authorDict[2015] = []
    authorDict[2016] = []
    authorDict[2017] = []
    authorDict[2018] = []
    authorDict[2019] = []
    authorDict[2020] = []
    total = []
    
    with codecs.open('/mnt/d/Twitediens/ltec-full-october-2020-fixed-words-broken-emoji.json', 'r', encoding='utf-8', errors='ignore') as fullFile:
        for wi in fullFile:
            if len(wi) > 5:
                text = ' '.join(wi.strip()[:-1].split()).replace('}, ]','} ]')
                
                try:
                    tweet_dict = json.loads(text)
                except json.decoder.JSONDecodeError as e:
                    sys.stderr.write(wi.strip()[:-1])
                    sys.exit(e.message)
                    
                dateTime = datetime.datetime.strptime(tweet_dict["created_at"], '%Y-%m-%d %H:%M:%S')
                    
                if tweet_dict["tweet_author"] not in authorDict[dateTime.year]:
                    authorDict[dateTime.year].append(tweet_dict["tweet_author"])
                if tweet_dict["tweet_author"] not in total:
                    total.append(tweet_dict["tweet_author"])
        
    for year in range(2011, 2021):
        print(str(year) + " - " + str(len(authorDict[year])))
    print("Total unique - " + str(len(total)))