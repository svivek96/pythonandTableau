# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 17:28:29 2023

@author: Lenovo
"""

import pandas as pd 
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df=pd.read_excel('articles.xlsx')

###counting the number of articles per source
df.groupby(['source_id'])['article_id'].count()

###number of reactions by publishers
df.groupby(['source_id'])['engagement_reaction_count'].sum()

##dropping a column
df = df.drop('engagement_comment_plugin_count', axis = 1)


def keywordflag(keyword):
    keyword_flag= []
    for x in range(0,len(df)):
        heading = df['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag  

keywordflag = keywordflag('murder')    


###creating a new column in dataframe
df['keyword_flag'] = pd.Series(keywordflag)

#SentimentIntensityAnalyzer


##adding a for loop to extract Sentiment per title
sent_int = SentimentIntensityAnalyzer()

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []
for i in range(0,len(df)):
    try:
        text = df['title'][i]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)  
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)  


df['title_neg_sentiment'] = title_neg_sentiment
df['title_pos_sentiment'] = title_pos_sentiment
df['title_neu_sentiment'] = title_neu_sentiment



df.to_excel('blogme_clean.xlsx',sheet_name='blogmedata', index=False)
    
    
    
    
    
    



            
    