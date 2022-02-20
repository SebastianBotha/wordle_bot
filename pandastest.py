# Import pandas package 
import pandas as pd
import numpy as np
  
# create a dictionary with five fields each
data = {
    'Letter 1':['a', 'b', 'c', 'd', 'e'], 
    'Letter 2':['f', 'g', 'h', 'i', 'j'], 
    'Letter 3':['c', 'a', 'b', 'd', 'e'], 
    'Letter 4':['a', 'b', 'c', 'd', 'e'], 
    'Letter 5':['a', 'b', 'c', 'd', 'e'] }
  
letter ='c'
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 # remove all words that dont contain eval letter 
 

df['has_letter'] = np.where((df['Letter 1']== letter) | (df['Letter 2'] == letter)| (df['Letter 3'] == letter)| (df['Letter 4'] == letter)| (df['Letter 5'] == letter), True, False)
df.head()

df.drop(df.index[df['has_letter'] == False], inplace=True)
df.head()



#column_index = 2
#evalue_column = "Letter {}".format(column_index)
#df.drop(df.index[df[evalue_column] != "c"],inplace=True)



#df.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=True, errors='raise')
print(df)