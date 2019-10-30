import pandas as pd
#import matplotlib
#matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

'loading data'
data = pd.read_csv('shot_logs.csv')

'removing unnecessary columns: GAME ID, Matchup, Winner/loser'
data = data.drop(['GAME_ID','MATCHUP','W'], axis = 1)

'data size'
#print 'Data Size: ', data.shape

'remove nan data'
data = data.dropna()

'Data Exploration'
ax = plt.figure(1)
plt.title('Shot Clock')
plt.hist(data['SHOT_CLOCK'], bins='auto')

ax = plt.figure(2)
plt.title('Shot Distance')
plt.hist(data['SHOT_DIST'], bins='auto')

ax = plt.figure(3)
plt.title('Dribbles')
plt.hist(data['DRIBBLES'], bins='auto')

ax = plt.figure(4)
plt.title('TOUCH_TIME' )
plt.hist(data['TOUCH_TIME'], bins='auto')
plt.xlim([0,20])

ax = plt.figure(5)
plt.title('CLOSE_DEF_DIST')
plt.hist(data['CLOSE_DEF_DIST'], bins='auto')
plt.xlim([0, 20])
#plt.show()

plt.savefig('test.pdf')
