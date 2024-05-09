import pandas as pd
import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'Filtered Data.csv'
dataset = pd.read_csv(file_path)
array = dataset.values

#claculate total winnings based off random selection
index = 0
winning_index = []
for placement in array[:,1]:
    index += 1
    if placement == 1:
        winning_index.append(index - 1)

prev_index = 0
total_wins = 0 
win_count = []
for _ in range(1000):
    total_wins = 0
    for index in winning_index:
        curr_index = index
        range_for_random = curr_index - prev_index
        if range_for_random > 0:
            guess = random.randint(0, range_for_random)
        else:
            guess = 0 
        prev_index = index
        if guess == 1:
            total_wins += array[index, -1]
        else:
            total_wins -= 1
    win_count.append(total_wins)
    
df = pd.DataFrame({'Counts': range(1, len(win_count) + 1), 'Win Total': win_count})
sns.boxplot(x='Counts', y='Win Total', data=df)
plt.title('Win Total from Random Selection')
plt.show()

all_elem = []
total_sum = 0
avg_win = []
for elem in win_count:
    all_elem.append(elem)
    total_sum = sum(all_elem)
    avg_win.append(total_sum / len(all_elem))

df2 = pd.DataFrame({'Counts': range(1, len(win_count) + 1), 'Average Win Total': avg_win})
sns.lineplot(x='Counts', y='Average Win Total', data=df2)
plt.title('Average Win Total from Random Selection')
plt.show()

#calculate total winnings based off favorites
prev_index = 0
best_odd_list = []
best_odd_index_list = []
winning_index.append(3747)
for curr_index in winning_index[1:]:
    odds_list = []
    
    for num in range(prev_index, curr_index):
        odds_list.append(array[num][-1])
    
    best_odd_index = prev_index + odds_list.index(min(odds_list))
    best_odd_index_list.append(best_odd_index)
    
    best_odd_list.append(min(odds_list))
    prev_index = curr_index
winning_index.remove(3747)

winnings = 0
total_winnings = []
for  num in range(len(best_odd_index_list)):
    if best_odd_index_list[num] == winning_index[num]:
        winnings += array[best_odd_index_list[num]][-1]
    else:
        winnings -= 1
    total_winnings.append(winnings)

df3 = pd.DataFrame({'Counts': range(1, len(best_odd_index_list) + 1), 'Total Winnings': total_winnings})
sns.lineplot(x='Counts', y='Total Winnings', data=df3)
plt.title('Win Total from Betting on Favorite')
plt.show()

#calculate total winnings based off race position

mark_index = ''
race_position = []
def get_race_place(string):
    while '-' in string:
        mark_index = string.find('-')
        race_position.append(int(string[:mark_index]))
        string = string[mark_index + 1:]
    race_position.append(int(string))
    return race_position

prev_index = 0
position_list_str = []
position_list_int = []
for curr_index in winning_index[1:]:
    for num in range(prev_index, curr_index):
        position_list_str.append(array[num][-3])
        for positions in position_list_str:
            position_list_int.append(get_race_place(positions).count(1))
        position_list_str = []
    prev_index = curr_index

final_count = []
prev_elem = 0
elem_temp = 0
for elem in position_list_int:
    elem_temp = elem
    elem = elem - prev_elem
    final_count.append(elem)
    prev_elem = elem_temp







