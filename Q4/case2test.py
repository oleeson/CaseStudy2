import pandas as pd
import csv
from datetime import datetime,date
import matplotlib.pyplot as plt

#import warnings
#warnings.filterwarnings("ignore")

temp = pd.read_csv('TEMP.csv')

#Create new data file with dates greater than 1900
temp2 = temp[temp.Date.str.len() <= 8]
#temp2.Date = temp2.Date.apply(lambda d: datetime.strptime(d, "%m/%d/%y"))

#Grouped by data file
tempgroup=temp2.groupby("Country")
#tempgroup.describe()
#find different in temperature for each country
tempgroup.tempdiff = tempgroup['MAverageTemp'].max() - tempgroup['MAverageTemp'].min()
tempgroup.tempdiff = tempgroup.tempdiff.order(ascending=False)
tempgroup.tempdiff = tempgroup.tempdiff.dropna()
top20 = tempgroup.tempdiff[0:20]
top20.plot.bar()

##import new clean dates dataset for US temps

usa = pd.read_csv('usaclean.csv')
print usa.head()


#UStemp = temp2[temp2.Country ==  "United States"]
#UStemp.FMAverageTemp = 9.0/5.0*(UStemp.MAverageTemp) + 32

citytemp=pd.read_csv("CityTemp.csv")
citytemp2=citytemp[citytemp.Date.str.len()<=8]
citytempgroup=citytemp2.groupby("City")
citytempgroup.tempdiff = citytempgroup['MAverageTemp'].max() - citytempgroup['MAverageTemp'].min()
citytempgroup.tempdiff = citytempgroup.tempdiff.order(ascending=False)
citytempgroup.tempdiff = citytempgroup.tempdiff.dropna()
citytop20 = citytempgroup.tempdiff[0:20]
citytop20.plot.bar()
plt.show()
