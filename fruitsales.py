# Importing pandas library
import pandas as pd
# Creating dataframe
df = pd.DataFrame({'Apples':[35,41],'Bananas':[21, 34]})
# Changing index to that requested by assignment
df.index = ['2017 Sales', '2018 Sales']
# outputting df dataframe to csv
df.to_csv('fruit.csv', index=True)
