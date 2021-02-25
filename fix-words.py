#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json, sys, os
import codecs



if __name__ == "__main__":
    
    outFile = codecs.open('mini-test-fixed-words-broken-emoji.json','w')
    
    searchArray = ['alīna','alīni','alīnu','asākas','asākās','ašākās','čala','čaliem','čaľiem','čaļa','čaļa','čaļiem','čaļiem','čočo','čočo','drāzējas','galā','galā','galiņa','galiņā','galiņu','galīgas','galīgās','gaļina','gaļinu','guļas','guļās','koļai','koļas','koļās','kukū','miklā','negūs','oļa','oļas','oļu','rīīšu','rīšu','rīšu','rīšū','sautētiem','seklās','senu','skābenu','spēki','spēki','alina','gala','galá','galà','galina','galinu']
    
    
    with codecs.open("mini-test.json", 'r', encoding="utf8") as fullFile:
        for wi in fullFile:
            if len(wi) > 5:
                text = ' '.join(wi.strip()[:-1].split()).replace('}, ]','} ]')
                
                try:
                    tweet_dict = json.loads(text)
                except json.decoder.JSONDecodeError as e:
                    sys.stderr.write(wi.strip()[:-1])
                    sys.exit(e.message)
                
                # Work with tweet
                changed = False
                
                # Has foods... let's see
                if "food_nominative_form" in tweet_dict:
                    surfaces = tweet_dict["food_surface_form"].split(";")
                    nominatives = tweet_dict["food_nominative_form"].split(";")
                    englishes = tweet_dict["food_english_translation"].split(";")
                    groups = tweet_dict["food_group"].split(";")
                    # Krabis - krējums?
                    for i, nominative in enumerate(nominatives):
                        # Do we have a crab?
                        if nominative == "krabis":
                            # Is it actually cream?
                            if surfaces[i][0:3].lower()!='kra':
                                # Got one!
                                changed = True
                                nominatives[i] = 'krējums'
                                englishes[i] = 'Cream'
                                groups[i] = '3'
                                tweet_dict["food_nominative_form"] = ';'.join(nominatives)
                                tweet_dict["food_english_translation"] = ';'.join(englishes)
                                tweet_dict["food_group"] = ';'.join(groups)
                    for i, surface in enumerate(surfaces):
                        if surface.lower() in searchArray:
                            # Got one!
                            changed = True
                            del surfaces[i]
                            del nominatives[i]
                            del englishes[i]
                            del groups[i]
                            tweet_dict["food_surface_form"] = ';'.join(surfaces)
                            tweet_dict["food_nominative_form"] = ';'.join(nominatives)
                            tweet_dict["food_english_translation"] = ';'.join(englishes)
                            tweet_dict["food_group"] = ';'.join(groups)
                if changed:
                    # Write to output file
                    output = json.dumps(tweet_dict, sort_keys=True, ensure_ascii=False)
                    output = output.strip() + ",\n"
                else:
                    output = wi
                outFile.write(output)
        
    outFile.close();
