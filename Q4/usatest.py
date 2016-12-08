import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#import warnings
#warnings.filterwarnings("ignore")

usa = pd.read_csv('usaclean.csv')
#print usa.head()

usa["FMAverageTemp"] = 9.0/5.0*(usa.MAverageTemp) + 32
#print usa.FMAverageTemp

usa["newdate2"] = usa.newdates.apply(lambda d: datetime.strptime(d, "%m/%d/%Y"))
after1990 = usa[usa.newdate2 >= "1/1/1990"]
#print after1990.head()
#print usa.newdate2.head()

after1990['year'] = [t.year for t in after1990.newdate2]
#print usa.year.head()
#print usa.head()

byyear = after1990.groupby('year')
#print byyear.head()

byyear.avg = byyear['FMAverageTemp'].mean()
#print byyear.avg
#print after1990.head()

byyear.avg.plot.line()
#plt.show()

avgtempbyyr=[]
for i in byyear.avg:
    avgtempbyyr.append(i)
#print len(avgtempbyyr)

yearrange = []
for num in range(1990,2014):
    yearrange.append(num)
#print len(yearrange)

tempdifference = []
yeardifference = []
maximum=0
maxyear=0
for i in range(0,23):
    dex = i
    upone = dex + 1
    diff = avgtempbyyr[upone] - avgtempbyyr[dex]
    if abs(diff) > maximum:
        maximum=diff
        maxyear = yrdiff = str(yearrange[upone])+"-"+str(yearrange[dex])
    tempdifference.append(diff)
    yrdiff = str(yearrange[upone])+"-"+str(yearrange[dex])
    yeardifference.append(yrdiff)

print "The maximum difference: ",maximum,"occurs in date range: ",maxyear

import numpy as np
byyeartempdifference = np.column_stack((yeardifference,tempdifference))
print byyeartempdifference
#print byyeartempdifference
