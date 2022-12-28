#%%
import numpy as np
import string
# %%
data = open('Day3_input.txt').read()
data = data.split('\n')
data = data[:-1]

# %%
def find_priority(item):
    if item.isupper():
        priority = string.ascii_uppercase.index(item) + 27
    else:
        priority = string.ascii_lowercase.index(item) + 1
    return priority

# %%
priorities = []
for line in data:
    first_comp = line[:int(len(line)/2)]
    sec_comp = line[-int(len(line)/2):]
    first_comp = list(first_comp)
    sec_comp = list(sec_comp)
    for i in first_comp:
        if i in sec_comp:
            same_item = i
            priority  = find_priority(same_item)
            priorities.append(priority)
            break

    # print(string.ascii_uppercase.index(first_comp[0])+27)
    # print(string.ascii_lowercase.index(first_comp[1])+1)
# %%
print(sum(priorities))
# %%
## Part 2
priorities = []
for lines in zip(list(data[::3]), list(data[1::3]), list(data[2::3])):
    #print(lines)
    for i in lines[0]:
        if i in lines[1]:
            if i in lines[2]:
                same_item = i
                priority = find_priority(same_item)
                priorities.append(priority)
                break

# %%
print(sum(priorities))
# %%
