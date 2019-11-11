import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from copy import deepcopy
from sklearn.preprocessing import StandardScaler

'loading data'
data = pd.read_csv('shot_logs.csv')

'removing unnecessary columns: GAME ID, Matchup'
data = data.drop(['GAME_ID','MATCHUP'], axis = 1)

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

#plt.savefig('test.pdf')

'Clutch players'
#print(data['SHOT_CLOCK'])
print(data.shape)
clutch = data[data['SHOT_CLOCK'] > 20.0]
print('here .. ')
print(clutch['player_name'].value_counts()[0:10])
#players_list = 
#print(data_slice['SHOT_CLOCK'])

'Normalizing Data'
'Location'
#there are problems here
#data[data['LOCATION'] == 'A'] = 1
#data[data['LOCATION'] == 'H'] = 0
#azdias[azdias['OST_WEST_KZ'] == 'W'] = 1

players = {}

for index, player in enumerate(clutch['player_name'].value_counts()):
	players[player] = data[data['player_name'] == player]
	print(player)
	if index>8:
		break

print(players['deandre jordan'])
#DJ = data[data['player_name'] == 'deandre jordan']



'''
'Margin'#scaler = StandardScaler()
#data_scaled = scaler.fit_transform(data)
numerical = ['DRIBBLES']
scaler = MinMaxScaler()
scaler.fit(data)
scaler.transform(data)
#data[numerical] = scaler.fit_transform(data[numerical],feature_range=(0, 1))
print(data['DRIBBLES'][0:20])
#a = deepcopy(data['PERIOD'])
#print(a.shape)
#data['PERIOD'].reshape(-1,1)
#a = np.reshape(data['PERIOD'], (-1, 1))
#print(a.shape)
#print(scaler.fit_transform(a))
#data['PERIOD'] = scaler.fit_transform(data['PERIOD'])
#print(data['PERIOD'])
'''
