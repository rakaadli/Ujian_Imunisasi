
# kaggle datasets download -d karangadiya/fifa19 --unzip
# lintangwisesa/balita-terimunisasi-di-indonesia-bps-19952017/version/1

import matplotlib.pyplot as plt
import csv
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

x = []
y = []

# with open('Balita Terimunisasi BCG 1995-2017.csv','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))

# plt.plot(x,y, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()

import pandas as pd 

BCG = pd.read_csv('Balita Terimunisasi BCG 1995-2017.csv',na_values='n.a')
DPT =  pd.read_csv('Balita Terimunisasi DPT 1995-2017.csv',na_values='n.a')
Campak = pd.read_csv('Balita Terimunisasi Campak 1995-2017.csv',na_values='n.a')
polio =  pd.read_csv('Balita Terimunisasi Polio 1995-2017.csv',na_values='n.a')

BCG = BCG.interpolate()
DPT = DPT.interpolate()
Campak = Campak.interpolate()
polio = polio.interpolate()

plt.figure('Persentasi balita terimunisasi 1995-2017', figsize =(15,9))
plt.subplot(2,2,1)
plt.bar(BCG['Tahun'],BCG['% Balita yang pernah mendapat imunisasi BCG'],color ='red')
plt.title('BCG')

plt.xticks(BCG['Tahun'],np.arange(1995,2018),rotation = 90)
plt.subplot(2,2,2)
plt.bar(Campak['Tahun'],Campak['% Balita yang pernah mendapat imunisasi Campak'],color ='green')
plt.title('Campak')
plt.xticks(Campak['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,3)
plt.bar(DPT['Tahun'],DPT['% Balita yang pernah mendapat imunisasi DPT'],color ='yellow')
plt.title('DPT')
plt.xticks(DPT['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,4)
plt.bar(polio['Tahun'],polio['% Balita yang pernah mendapat imunisasi Polio'],color ='blue')
plt.title('Polio')
plt.xticks(polio['Tahun'],np.arange(1995,2018),rotation = 90)
plt.tight_layout()

plt.figure('Persentase balita tak terimunisasi 1995-2017', figsize =(13,9))
plt.subplot(2,2,1)
plt.bar(BCG['Tahun'],100 - BCG['% Balita yang pernah mendapat imunisasi BCG'],color ='red')
plt.title('BCG')
plt.xticks(BCG['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,2)
plt.bar(Campak['Tahun'],100 - Campak['% Balita yang pernah mendapat imunisasi Campak'],color ='green')
plt.title('Campak')
plt.xticks(Campak['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,3)
plt.bar(DPT['Tahun'],100 - DPT['% Balita yang pernah mendapat imunisasi DPT'],color ='yellow')
plt.title('DPT')
plt.xticks(DPT['Tahun'],np.arange(1995,2018),rotation = 90)

plt.subplot(2,2,4)
plt.bar(polio['Tahun'],100 - polio['% Balita yang pernah mendapat imunisasi Polio'],color ='blue')
plt.title('Polio')
plt.xticks(polio['Tahun'],np.arange(1995,2018),rotation = 90)
plt.tight_layout()
plt.show()

