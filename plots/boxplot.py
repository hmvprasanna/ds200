import pandas as pd
import matplotlib.pyplot as plt
import sys

#create dataframe from input csv
df=pd.read_csv(sys.argv[1], header='infer')
plotMap=[]

# creating a list of lists where each list will have a corresponding box plot 
# for the three census years, 1991, 2001, and 2011
plotMap.append(df['1991'].dropna().tolist())
plotMap.append(df['2001'].dropna().tolist())
plotMap.append(df['2011'].dropna().tolist())

plt.boxplot(plotMap)

# specifying labels for the axes
plt.xticks([1,2,3],["1991","2001", "2011"])
plt.xlabel("Census Year")
plt.ylabel("Disrtibution of Literacy Percentage across Indian States")

plt.legend()
plt.show()
