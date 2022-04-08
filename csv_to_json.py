import json 
import time
import pandas as pd 
## WARNING : csv file name
csv_file='DBPEDIA_test.csv'
df=pd.read_csv(csv_file)
df=df.to_dict(orient='records')
j_file=json.dumps(df)
with open('DBPedia.json', 'w') as outfile:
    outfile.write(j_file)