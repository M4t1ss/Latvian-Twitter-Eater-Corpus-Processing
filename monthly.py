#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os
import codecs, datetime


if __name__ == "__main__":
    
    authorDict = {}
    authorDict[2011] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2012] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2013] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2014] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2015] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2016] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2017] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2018] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2019] = [0,0,0,0,0,0,0,0,0,0,0,0]
    authorDict[2020] = [0,0,0,0,0,0,0,0,0,0,0,0]
    
    with codecs.open('/mnt/d/Twitediens/ltec-full-december-2020-fw.json', 'r', encoding='utf-8', errors='ignore') as fullFile:
        for wi in fullFile:
            if len(wi) > 5:
                text = ' '.join(wi.strip()[:-1].split()).replace('}, ]','} ]')
                
                try:
                    tweet_dict = json.loads(text)
                except json.decoder.JSONDecodeError as e:
                    sys.stderr.write(wi.strip()[:-1])
                    sys.exit(e.message)
                    
                dateTime = datetime.datetime.strptime(tweet_dict["created_at"], '%Y-%m-%d %H:%M:%S')
                authorDict[dateTime.year][dateTime.month-1] += 1
        
    for year in range(2011, 2021):
        print(year)
        print(authorDict[year])