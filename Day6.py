

#%%
data = open('Day6_input.txt', 'r').read()
# %%
for i in range(int(len(data)-4)):
    buffer = data[i:i+4]
    
    unique_len = len(set(buffer))
    if unique_len == 4:
        print(i+4)
        break
#%%
def find_marker(data, marker_size=4):
    for i in range(int(len(data)-marker_size)):
        buffer = data[i:i+marker_size]
        unique_len = len(set(buffer))
        if unique_len == marker_size:
            
            break
    return i+marker_size
# %%
find_marker(data)
find_marker(data, marker_size=14)
# %%
