import pandas as pd
import json

df = pd.read_csv('data.csv', delimiter='\t')

d = df.to_dict('series')
print(d.keys())
d = {k: v.str.strip(' ').dropna().tolist() for k, v in d.items()}
# d['type']
# d['establishment_prefix']
with open('data.json', 'w', encoding='latin-1') as f:
    json.dump(d, f)
print
