import pandas as pd
import numpy as np
from collections import Counter

path = ''

stimuli = pd.read_excel(path+'stimuli.xlsx')

chars = [_ for _ in ''.join(list(stimuli.words)).replace(' ', '')]

# bool(np.random.randint(2))

# prime,target,same_category,wordness,block
def make_trials(trial_count, blockID): 

    count_of_each_condtion = trial_count//2

    'same_category'
    results1 = []
    for i in range(count_of_each_condtion):
        candidate = stimuli.sample(n=1)
        candidate = candidate.iloc[0].words.split(' ')

        prime,target = np.random.choice(candidate,2,replace=False)

        results1.append([prime, target, True, True, np.random.choice([0.150,0.350]), blockID])

    for i in np.random.choice(range(count_of_each_condtion),
        count_of_each_condtion//4,replace=False):

        results1[i][1] = ''.join(np.random.choice(chars,2))
        results1[i][3] = False

    'diff_category'
    results2 = []
    for i in range(count_of_each_condtion):
        candidate = stimuli.sample(n=2)
        c1 = candidate.iloc[0].words.split(' ')
        c2 = candidate.iloc[1].words.split(' ')

        prime = np.random.choice(c1,1,replace=False)[0]
        target = np.random.choice(c2,1,replace=False)[0]

        results2.append([prime, target, False, True, np.random.choice([0.150,0.350]), blockID])

    for i in np.random.choice(range(count_of_each_condtion),
        count_of_each_condtion//4,replace=False):

        results2[i][1] = ''.join(np.random.choice(chars,2))
        results2[i][3] = False

    results = results1 + results2
    np.random.shuffle(results)

    return results

def check_trials(trial_list):
    return True

def make_block(trial_count,blockID): 
    while 1: 
        trial_list = make_trials(trial_count, blockID)
        if check_trials(trial_list) == True:
            break
    return trial_list

all_trials = []
for blockID in range(4):
    all_trials.extend(make_block(90,blockID+1))

all_trials = pd.DataFrame(all_trials,
    columns=['prime','target','same_category','wordness','soa','block'])
all_trials.to_csv(path+'trial_list.csv',index=None)

# def make_trials(normal_list,outlier_list,blockID): 
#     if normal_list == Tt:
#         tag = 'Tt'
#     else:
#         tag = 'Ft'

#     while 1:
#         trial_list = [set([s for s in np.random.choice(normal_list,10,replace=False)])]
#         for i in range(1,30):
#             while 1:
#                 trial = set([s for s in np.random.choice(normal_list,10,replace=False)])
#                 if trial&trial_list[i-1]==set():
#                     trial_list.append(trial)
#                     break

#         if Counter([s for i in trial_list for s in list(i)]).most_common(1)[0][1]<8:
#             break

#     trial_list = [[list(i),tag,True,blockID] for i in trial_list]
    
#     for i in np.random.choice(range(30),10,replace=False):
#         for j in np.random.choice(range(10),2,replace=False):
#             trial_list[i][0][j] = np.random.choice(outlier_list,1)[0]
#             trial_list[i][2] = False
    
#     trial_list = [(''.join(i[0]),i[1],i[2],i[3]) for i in trial_list]
            
#     return trial_list


# trials = np.concatenate([make_trials(Tt,Ft,1),
#                          make_trials(Ft,Tt,2),
#                          make_trials(Ft,Tt,3),
#                          make_trials(Tt,Ft,4)])

# pd.DataFrame(trials,columns=['content','type','normal','block']).to_csv(path+'trial_list.csv',index=None)
