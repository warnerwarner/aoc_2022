import numpy as np

#%%
data = open('Day1_input.txt', 'r').readlines()
# %%
print(data[:100])
# %%
elf_counts = []
current_count = int(data[0][:-1])
print(current_count)

# %%
for count in data[1:]:
    if count != '\n':
        current_count += int(count[:-1])
    else:
        elf_counts.append(current_count)
        current_count = 0
# %%
print(elf_counts)
# %%
print(max(elf_counts))
# %%
sorted_elf_counts = np.sort(elf_counts)
print(sorted_elf_counts)
# %%
print(sorted_elf_counts[-3:])
print(sum(sorted_elf_counts[-3:]))
# %%
