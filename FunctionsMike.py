# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:36:50 2019

@author: MWorthington
"""
import pandas as pd
import numpy as np
import matplotlib as mlp
"""
-------------------------------------------------------------------------------
Created on Mon Mar 18th 18:14:51 2019

Returns Root Mean Square Error Score

Required arguments: predictions,targets where predictions,targets are array-like
                    
@author: MWorthington
-------------------------------------------------------------------------------
"""
def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

"""
-------------------------------------------------------------------------------
Created on Mon Oct 11th 13:44:07 2019

Returns R^2 Score

Required arguments: x,y where x,y are array-like.
                    
@author: MWorthington
-------------------------------------------------------------------------------
"""

def rsquared(x, y):
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
    return r_value**2

"""
-------------------------------------------------------------------------------
Created on Mon Mar 18th 11:44:07 2019

Takes outcome_insight output and splits of the first column at index position [0].
Converts list to pandas dataframe for easier data management.
Adds the appropriate column names and then drops duplicated row at index position [0].
Finally outputs to .csv file using the name entered by the users input via console command line. -->

Required arguments: 1. User input for the .csv file name. 
                    2. Dataset.
                    
@author: MWorthington
-------------------------------------------------------------------------------
"""
def DataframeConversionOutput(CSVName, Data):
    fields = Data
    OutputCSV = pd.DataFrame(data=fields,columns = ['Phrase', 'LCL','UCL','z','n1'])
    OutputCSV = OutputCSV.drop([0])
    OutputCSV.to_csv(CSVName, index= False)
"""
-------------------------------------------------------------------------------
Created on Tue Apr 23rd 15:43:01 2019


Required arguments: 1. How many partitions you require the Ngrams to split into (1,2,3,4,5 etc) 
                    2. Dataset. (Singular free text column - No headers)
                    
@author: MWorthington
-------------------------------------------------------------------------------
"""
def Ngrams(partition, data):
    import nltk
    nltk.download('punkt')
    from nltk import ngrams
    from collections import Counter
    from nltk.corpus import stopwords
    import re
    
    words = open(data,encoding="utf8").read().lower()
    words = re.sub(r'[^\w\s]','', words)
    words = re.sub(r'\d+','', words).split(" ")
    stop_words = stopwords.words('english')
    words = [word for word in words if word not in stop_words]
    ngram_counts = Counter(ngrams(words, partition))
    print(ngram_counts.most_common(200))
    with open('.csv', 'w') as f:
        for key in ngram_counts.keys():
            f.write("%s,%s\n"%(key,ngram_counts[key])) 