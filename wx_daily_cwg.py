# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:04:08 2019
@author: harshit.mahajan
"""
import os
import pandas as pd 
from datetime import date, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.gridspec as gridspec

today = date.today()

year = str(today.year)
month = '0'+ str(today.month) if today.month < 10 else str(today.month)
day = '0'+ str(today.day) if today.day < 10 else str(today.day)

offset = max(1, (today.weekday() + 6) % 7 -3)

previous_date  = today - timedelta(offset)

previous_year = str(previous_date.year)
previous_month = '0'+ str(previous_date.month) if previous_date.month < 10 else str(previous_date.month)
previous_day = '0'+ str(previous_date.day) if previous_date.day < 10 else str(previous_date.day)

#nationalurl = 'XXXX'
#nationaldd = pd.read_csv(nationalurl).dropna()

# National Forecast 
nationalurl = 'XXXX'
nationaldd = pd.read_csv(nationalurl).dropna()
nationaldd['vintage_id'] = today
nationaldd.columns
nationaldd['totaldd'] = nationaldd['NG_HDD'] + nationaldd['POP_CDD']
nationaldd['totalddlastyear'] = nationaldd['LAST_Y_NG_HDD'] + nationaldd['LAST_Y_POP_CDD']
nationaldd['totaldd10year'] = nationaldd['10Y_NG_HDD'] + nationaldd['10Y_POP_CDD']
    
# 9Region Forecast 
nineregionurl = 'XXXX'+ year + month + day + '.csv'
nineregiondd = pd.read_csv(nineregionurl).dropna()
nineregiondd['vintage_id'] = today
nineregiondd['totaldd'] = nineregiondd['NG_HDD'] + nineregiondd['POP_CDD']
nineregiondd['totalddlastyear'] = nineregiondd['LAST_Y_NG_HDD'] + nineregiondd['LAST_Y_POP_CDD']
nineregiondd['totaldd10year'] = nineregiondd['10Y_NG_HDD'] + nineregiondd['10Y_POP_CDD']

# 5Region Forecast 
fiveregionurl = 'XXXX' + year + month + day + '.csv'
fiveregiondd = pd.read_csv(fiveregionurl).dropna()
fiveregiondd['vintage_id'] = today
fiveregiondd['totaldd'] = fiveregiondd['NG_HDD'] + fiveregiondd['POP_CDD']
fiveregiondd['totalddlastyear'] = fiveregiondd['LAST_Y_NG_HDD'] + fiveregiondd['LAST_Y_POP_CDD']
fiveregiondd['totaldd10year'] = fiveregiondd['10Y_NG_HDD'] + fiveregiondd['10Y_POP_CDD']

# ISO Forecast 
isourl = 'XXXX' + year + month + day + '.csv'
isodd = pd.read_csv(isourl).dropna()
isodd['vintage_id'] = today
isodd['totaldd'] = isodd['POP_HDD'] + isodd['POP_CDD']
isodd['totalddlastyear'] = isodd['LAST_Y_POP_HDD'] + isodd['LAST_Y_POP_CDD']
isodd['totaldd10year'] = isodd['10Y_POP_HDD'] + isodd['10Y_POP_CDD']

# Monthly Degree Days
monthlyddurl = 'XXXX'
monthlydd = pd.read_csv(monthlyddurl).dropna()
monthlydd ['vintage_id'] = today

# Europe Degree Days 
europeurl = 'XXXX' + year + month + day + '.csv'
europedd = pd.read_csv(europeurl).dropna()
europedd['vintage_id'] = today
europedd['totaldd'] = europedd['POP_HDD'] + europedd['POP_CDD']
europedd['totalddlastyear'] = europedd['LAST_Y_POP_HDD'] + europedd['LAST_Y_POP_CDD']
europedd['totaldd10year'] = europedd['10Y_POP_HDD'] + europedd['10Y_POP_CDD']

# Asia Degree Days 
asiaurl = 'XXXX' + year + month + day + '.csv'
asiadd = pd.read_csv(asiaurl).dropna()
asiadd['vintage_id'] = today
asiadd['totaldd'] = asiadd['POP_HDD'] + asiadd['POP_CDD']
asiadd['totalddlastyear'] = asiadd['LAST_Y_POP_HDD'] + asiadd['LAST_Y_POP_CDD']
asiadd['totaldd10year'] = asiadd['10Y_POP_HDD'] + asiadd['10Y_POP_CDD']

##############################################################################
##############################################################################
# Saving the data to xlsx file with today's date 
path = 'XXXX'
name = 'temperatures_fsct_' + str(today) + '.xlsx'
filepath = path + name 

dfs = {'nationaldd': nationaldd, 'nineregiondd':nineregiondd, 'fiveregiondd': fiveregiondd, 'isodd': isodd , 'monthlydd' : monthlydd , 'europedd' : europedd , 'asiadd' : asiadd}
writer = pd.ExcelWriter(filepath, engine = 'xlsxwriter')

for sheetname in dfs.keys():
    print(sheetname)
    dfs[sheetname].to_excel(writer, sheet_name=sheetname, index = False)
writer.save()    
    
##############################################################################
##############################################################################

### Plotting 
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15,6))
nationaldd = nationaldd[pd.to_datetime(nationaldd['DATES'])> pd.to_datetime(today)]
europedd = europedd[pd.to_datetime(europedd['DATES'])> pd.to_datetime(today)]
asiadd = asiadd[pd.to_datetime(asiadd['DATES'])> pd.to_datetime(today)]

ax[0].plot(nationaldd['DATES'].astype('datetime64[ns]'),nationaldd['totaldd'], marker = 'o')
ax[0].plot(nationaldd['DATES'].astype('datetime64[ns]'),nationaldd['totalddlastyear'], marker = '')
ax[0].plot(nationaldd['DATES'].astype('datetime64[ns]'),nationaldd['totaldd10year'], marker = '.')
ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
ax[0].set_title('US National Degree Days')

ax[1].plot(europedd['DATES'].astype('datetime64[ns]'),europedd['totaldd'], marker = 'o')
ax[1].plot(europedd['DATES'].astype('datetime64[ns]'),europedd['totalddlastyear'], marker = '')
ax[1].plot(europedd['DATES'].astype('datetime64[ns]'),europedd['totaldd10year'], marker = '.')
ax[1].xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
ax[1].set_title('Europe Degree Days')

ax[2].plot(asiadd['DATES'].astype('datetime64[ns]'),asiadd['totaldd'], marker = 'o')
ax[2].plot(asiadd['DATES'].astype('datetime64[ns]'),asiadd['totalddlastyear'], marker = '')
ax[2].plot(asiadd['DATES'].astype('datetime64[ns]'),asiadd['totaldd10year'], marker = '.')
ax[2].xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
ax[2].set_title('Asia Degree Days')
fig.legend([year, 'Last Year', '10 Year Norms'])

## Regional Degree Days
fig, ax = plt.subplots(nrows=1, ncols = 5, figsize=(25,6))
i = 0
for region in fiveregiondd.REGION_NAME.unique():   
   fiveregiondd = fiveregiondd[pd.to_datetime(fiveregiondd['DATES'])> pd.to_datetime(today)]
   ax[i].plot(fiveregiondd[fiveregiondd['REGION_NAME'] == region][['DATES']].astype('datetime64[ns]'), fiveregiondd[fiveregiondd['REGION_NAME'] == region][['totaldd']])
   ax[i].plot(fiveregiondd[fiveregiondd['REGION_NAME'] == region][['DATES']].astype('datetime64[ns]'), fiveregiondd[fiveregiondd['REGION_NAME'] == region][['totalddlastyear']])
   ax[i].plot(fiveregiondd[fiveregiondd['REGION_NAME'] == region][['DATES']].astype('datetime64[ns]'), fiveregiondd[fiveregiondd['REGION_NAME'] == region][['totaldd10year']])
   ax[i].xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
   ax[i].set_title(region + 'Degree Days')
   i+= 1
fig.legend([year, 'Last Year', '10 Year Norms'], loc ='best')    #plt.title('Heating Degree Days') 
plt.show()
##############################################################################
##############################################################################
