#%%
import numpy as np
import itertools
# %%

data = open('Day5_input.txt', 'r').read().splitlines()
for i in data[:10]:
    print(i)
# %%
init_crates = data[:8]
[print(i) for i in init_crates]
init_crates = init_crates[::-1]


sliced_list = [[j[4*i:4*i+3] for i in range(9)] for j in init_crates]


rotated_list = [[sliced_list[i][j] for i in range(len(sliced_list))] for j in range(9)]
print(rotated_list)

# %%
trimmed_list = [[i for i in j if i != '   '] for j in rotated_list]
[print(i) for i in trimmed_list]

#%%
print(data[10])
# %%
[print(i) for i in trimmed_list]
for line in data[10:]:
    #print(line)
    split_line = line.split(' ')
    num_of_boxes = int(split_line[1])
    from_col = int(split_line[3])-1
    to_col = int(split_line[-1])-1
    #print(num_of_boxes, from_col, to_col)
    moved_boxes = trimmed_list[from_col][-num_of_boxes:]
    trimmed_list[from_col] = trimmed_list[from_col][:int(len(trimmed_list[from_col])-num_of_boxes)]
    [trimmed_list[to_col].append(i) for i in moved_boxes[::-1]]
    #[print(i) for i in trimmed_list]
#    trimmed_list[to_col].append(moved_boxes[::-1])
# %%
top_crates = [i[-1][1:-1] for i in trimmed_list]
print(''.join(top_crates))
# %%
trimmed_list = [[i for i in j if i != '   '] for j in rotated_list]

## Part 2
[print(i) for i in trimmed_list]
for line in data[10:]:
    #print(line)
    split_line = line.split(' ')
    num_of_boxes = int(split_line[1])
    from_col = int(split_line[3])-1
    to_col = int(split_line[-1])-1
    #print(num_of_boxes, from_col, to_col)
    moved_boxes = trimmed_list[from_col][-num_of_boxes:]
    trimmed_list[from_col] = trimmed_list[from_col][:int(len(trimmed_list[from_col])-num_of_boxes)]
    [trimmed_list[to_col].append(i) for i in moved_boxes]

# %%
top_crates = [i[-1][1:-1] for i in trimmed_list]
print(''.join(top_crates))
# %%
