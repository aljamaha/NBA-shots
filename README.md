# NBA-shots

## Business Understanding:
Taking and making shots late in the shot clock is an important aspect of an NBA game. In many cases the team can't generate a good shot and relies on a star player in those stressful times to bail them out. Here, I take a look at the data from the 2014-2015 NBA season, identify the players taking the most shots, and provide more insights.

## Data Understanding:
Shot logs data from the 2014-2015 NBA season area used here. It includes many information (player taking the shot, closest defender distance, the shot clock, etc.)

## Data Preparation:
Data outside the last 4 seconds of the shot clock were eliminated. >95% of the data were completely filled, and hence, <5% were not used due to incomplete inofrmation.

## Data Modeling:
Pandas was used as the primary library to analyze and disect the data.

## Evaluation:
The outcome shows many NBA centers, not traditionally critical for the offense, are taking an alarming number of shots late in the shot clock.

### Libraries needed: 
Python, Pandas , matplotlib, numpy, sklearn

### NBA_shots.ipynb:
Jupyter notebook containing the entire code, how the data is treated and analyzed

### script.py: 
Python scrip (similar to the jupyter notebok)

### shot_logs.csv: 
Data log 

