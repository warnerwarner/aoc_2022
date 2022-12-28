# %%
import numpy as np

# %%
data = open('Day4_input.txt', 'r').read().splitlines()
# %%
print(data[0])

# %%
overlap_count = 0
for line in data:
    elf1, elf2 = line.split(',')
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')
    elf1_start, elf1_end, elf2_start, elf2_end = int(elf1_start), int(elf1_end), int(elf2_start), int(elf2_end)
    if elf1_start <= elf2_start and elf1_end >= elf2_end:
        overlap_count += 1
        continue
    if elf2_start <= elf1_start and elf2_end >= elf1_end:
        overlap_count += 1
# %%
print(overlap_count)
# %%
overlap_count = 0
for line in data:
    elf1, elf2 = line.split(',')
    elf1_start, elf1_end = elf1.split('-')
    elf2_start, elf2_end = elf2.split('-')
    elf1_start, elf1_end, elf2_start, elf2_end = int(elf1_start), int(elf1_end), int(elf2_start), int(elf2_end)
    elf1_range = list(range(elf1_start, elf1_end+1))
    elf2_range = list(range(elf2_start, elf2_end+1))
    #print(elf1_range)
    if any(i in elf2_range for i in elf1_range):
        overlap_count+= 1
        #print(elf1_range, elf2_range)
    elif any(i in elf1_range for i in elf2_range):
        overlap_count+= 1
    else:
        print(elf1_range, elf2_range)
    print('\n')
print(overlap_count)
# %%
