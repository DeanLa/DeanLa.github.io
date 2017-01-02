import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([[1,5],[2,60], [3,11]], columns=['x','y'])
print (df)
df.to_json('./data.json', orient='values')
# {'split','records','index','columns','values'}
# plt.plot (df.x, df.y)
# plt.show()
