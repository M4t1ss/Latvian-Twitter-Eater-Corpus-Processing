#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os
import codecs


if __name__ == "__main__":

    sents = []
    
    with codecs.open('/mnt/d/Twitediens/full.only.predictions-best.txt', 'r', encoding='utf-8', errors='ignore') as fullFile:
        for wi in fullFile:
            sents.append(wi)
    
    outFile = open("/mnt/d/Twitediens/ltec-full-december-2020-emo-best.txt","w", encoding='utf-8', errors='ignore')
    
    #Šis nomirst pie pimrā jaunā emoji un tālāk aiziet normāli. HELP?
    # with codecs.open('/mnt/d/Twitediens/ltec-full-december-2020-fw.json', 'r', encoding='') as fullFile:
    with codecs.open('/mnt/d/Twitediens/ltec-full-december-2020-fw.json', 'r', encoding='utf-8', errors='ignore') as fullFile:
    # with codecs.open('/mnt/d/Twitediens/test.json', 'r', encoding='utf-8') as fullFile:
        for wi in fullFile:
            if len(wi) > 5:
                text = ' '.join(wi.strip()[:-1].split()).replace('}, ]','} ]')
                
                try:
                    tweet_dict = json.loads(text)
                except json.decoder.JSONDecodeError as e:
                    sys.stderr.write(wi.strip()[:-1])
                    sys.exit(e.message)
                    
                if "food_nominative_form" in tweet_dict:
                    nominative = " VISIATSLEGVARDISEKO " + tweet_dict["food_nominative_form"]
                else:
                    nominative = ""
                outFile.write(tweet_dict["tweet_text"] + nominative + " VISIATSLEGVARDISEKO " + tweet_dict["created_at"] + " VISIATSLEGVARDISEKO " + str(sents.pop(0).strip()) + "\n")
                # print(tweet_dict["tweet_text"])
        
    outFile.close();