#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os
import codecs, datetime


if __name__ == "__main__":
    
    with codecs.open('/mnt/d/Twitediens/ltec-full-december-2020-fw.json', 'r', encoding='utf-8', errors='ignore') as fullFile:
        for wi in fullFile:
            if len(wi) > 5:
                text = ' '.join(wi.strip()[:-1].split()).replace('}, ]','} ]')
                
                try:
                    tweet_dict = json.loads(text)
                except json.decoder.JSONDecodeError as e:
                    sys.stderr.write(wi.strip()[:-1])
                    sys.exit(e.message)
                    
                
                if "food_nominative_form" in tweet_dict:
                    foodWords = tweet_dict["food_nominative_form"][:-1].split(";")
                        
                    for foodWord in foodWords:
                        print(foodWord.strip() + "\t" + tweet_dict["created_at"])