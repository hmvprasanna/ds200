# DS200 - Research Methods
Contains all the code written for the completion of assignments of DS 200 Course of 2017-18, IISc CDS

TO DO: Select datasets from https://data.gov.in/ and create (a) a scatter plot, (b) a box plot, and (c) a bar or line plot from them using matplotlib library. Include a Readme.md documentation for the same listing the data sources and the observations from the plots, including citations. Use the git or svn commandline clients to perform these operations.

## Scatter Plot

The data considered for the scatter plot is the "R&D Expenditure Per Capita and as Percentage of GDP for Selected Countries fyear or the 2009 (in US$)", as shared here by the Open Government Data Platform India: https://data.gov.in/resources/rd-expenditure-capita-and-percentage-gdp-selected-countries-2009-us

The data from the CSV was cleaned up to retain only 3 columns that are necessay for the plot, i.e., the columns of Country, Per Capita R&D in US $, and Per Capita GDP in US $ (scatterplot_data.csv). Once done, we can call scatterplot.py on this data to obtain the plot seen in scatterplot.png.

The plot clearly indicates dependency of these two data points. That is, the lower (higher) the per capita GDP, the lower (higher) is the per capita R&D expenditure and vice versa, in general.

## Box Plot

The data considered for the box and whisker plot is the "State level Literacy rate in % from 1951-2011", as shared here by the Open Government Data Platform India: https://data.gov.in/resources/state-level-literacy-rate-1951-2011

The data contains the progressive literacy percentage of each state of India from the data available from each census data from 1951 to 2011. For the purpose of data cleanup (to exclude cases of unavailable data for certain states), the plot here considered the last 3 census information, that of 1991, 2001 and 2011, for each state / union terrotory of India. This data is in file boxplot_data.csv and the plotting is carried out through boxplot.py. 

The plot obtained, boxplot.png, shows the trend in literacy rates over the last 3 decades. Clearly, the mean literacy rate across states is on the up constantly, moving from around 58% in 1991 to 75% in 2011. Even the deviation from the median has reduced over the 3 decades as most states have been improving the literacy rates rapidly.

## Bar Plot

Here, the data considered provides the "Number of teachers(Male/Female) in secondary school at all India level from year 2001 to 2010" as shared here by the Open Government Data Platform India: https://data.gov.in/resources/number-teachersmalefemale-secondary-school-all-india-level-year-2001-2010

While this data has separate entries for each state, for the purpose of this plot, I have considered only the overall country level data for India - for each of the 10 years in consideration. The considered data is stored in barplot_data.csv and its plotting code is in barplot.py.

The plot in barplot.png clearly indiactes a constant increase in the number of secondary school teachers over these 10 years, although there was one slight dip from 2006 to 2007.
