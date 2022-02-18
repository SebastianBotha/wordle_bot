import pandas as pd


data = pd.read_excel (r'/Users/sebastianbotha/Documents/Python Projects/wordle_bot/Wordle database.xlsx')
print (data)

# Visualize the dataframe
print(data.head(5))
  
# Print the shape of the dataframe
print(data.shape)


# Filter all rows for which the player's
# age is greater than or equal to 25
df_filtered = data[data['Completley unique '] == 1]

print("----------------\n")

# Print the new dataframe
print(df_filtered.head(15))
  
# Print the shape of the dataframe
print(df_filtered.shape)



# find maximum value of a
# single column 'x'
maxClm = df_filtered['Full P'].idxmax()
 
print("Maximum value in column 'Full P': " )
print(maxClm)

# row then column 

df_filtered.sort_values(by=['Full P'], inplace=True, ascending=False)

wordle_next = df_filtered.iloc[0][0]
print(wordle_next)