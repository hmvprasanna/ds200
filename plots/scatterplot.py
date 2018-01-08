import pandas as pd
import matplotlib.pyplot as plt
import sys

#create dataframe from input csv
df=pd.read_csv(sys.argv[1], header='infer')

# plot scatter with first column as per capita R&D expenditure values
# and second column as per capita GDP values, both in US $
plt.scatter(df['Per Capita R&D in US $'],df['Per Capita GDP in US $'],color='#dd12dd',label="Per Capita R&D expenditure by countries vs GDP")

#specifying labels for the axes
plt.xlabel("Per Capita R&D in US $")
plt.ylabel("Per Capita GDP in US $")

plt.legend()
plt.show()
