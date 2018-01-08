import pandas as pd
import matplotlib.pyplot as plt
import sys

#create dataframe from input csv
df=pd.read_csv(sys.argv[1], header='infer')

#plot bar plot with years as the x-axis argument and count of teachers as the y-axis argument
plt.bar(df['year'],df['teacher_count'],color='#afaf00',label="Secondary school teachers in India over the years")

# specifying labels for the axes
plt.xlabel("Year")
plt.ylabel("No. of Secondary School Teachers across India")

plt.legend()
plt.show()
