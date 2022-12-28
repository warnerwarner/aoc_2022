#%%
import numpy as np
# %%
data = open('Day2_input.txt', 'r').readlines()
# %%
print(data[:10])
# %%
scores = []
for line in data:
    line_score = 0
    split_line = line.split(' ')
    split_line = [split_line[0], split_line[1][:-1]]
    if split_line[0] == 'A':
        if split_line[1] == "Y":
            line_score += 6
        if split_line[1] == 'X':
            line_score += 3
    if split_line[0] == "B":
        if split_line[1] == 'Z':
            line_score += 6
        if split_line[1] == 'Y':
            line_score += 3
    if split_line[0] == 'C':
        if split_line[1] == 'X':
            line_score += 6
        if split_line[1] == 'Z':
            line_score += 3
    
    if split_line[1] == 'X':
        line_score += 1
    if split_line[1] == 'Y':
        line_score += 2
    if split_line[1] == 'Z':
        line_score += 3
    
    scores.append(line_score)
# %%
print(scores)
# %%
print(sum(scores))
# %%
print(data[-1])
# %%

## Part 2
loose_dict = {'A':3, 'B':1, 'C':2}
win_dict = {'A':2, 'B':3, 'C':1}
draw_dict = {'A':1, 'B':2, 'C':3}
scores = []
for line in data:
    line_score = 0
    split_line = line.split(' ')
    split_line = [split_line[0], split_line[1][:-1]]
    if split_line[1] == 'X':
        line_score += loose_dict[split_line[0]]
    if split_line[1] == 'Y':
        line_score += 3
        line_score += draw_dict[split_line[0]]
    if split_line[1] == 'Z':
        line_score += 6
        line_score += win_dict[split_line[0]]
    scores.append(line_score)



# %%
print(scores)
# %%
print(sum(scores))
# %%
