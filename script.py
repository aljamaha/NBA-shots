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
print('Data Size: ', data.shape)

'remove nan data'
data = data.dropna()

'''
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
'''

'Clutch players'
clutch_data = data[data['SHOT_CLOCK'] > 20.0]
print('Players with most shots ...')
print(clutch_data['player_name'].value_counts()[0:10])
clutch_players = ['andre drummond','deandre jordan','goran dragic','russell westbrook','lebron james','eric bledsoe','enes kanter','stephen curry']

'data frame for each clutch player in a dictionary'
players = {}
for player in clutch_players:
	players[player] = clutch_data[clutch_data['player_name'] == player]

'Mean data for each clutch player'
mean_clutch = {}
for player in players:
	mean_clutch[player] = players[player].mean()

'choices I made for descriptors'
descriptors = ['SHOT_DIST','DRIBBLES','TOUCH_TIME','PTS']

def sort_data(players, desc):
	'sort data of players from lowest to highest'
	data = {}
	sorted_data = {}
	for player in players:
		data[player] = mean_clutch[player][desc]
	for i in sorted (data.values()):
		for p in players:
			if data[p] == i:
				sorted_data[p] = i
				break
	return sorted_data

'Data Analysis'
for d in descriptors:
	print('----'+d+'----')
	new_data = sort_data(players, d)
	for i in new_data:
		print(i, new_data[i])


'''
#print(clutch_data.groupby(['player_name']).mean())
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
'Normalizing Data'
'Location'
#there are problems here
#data[data['LOCATION'] == 'A'] = 1
#data[data['LOCATION'] == 'H'] = 0
#azdias[azdias['OST_WEST_KZ'] == 'W'] = 1''
'''
