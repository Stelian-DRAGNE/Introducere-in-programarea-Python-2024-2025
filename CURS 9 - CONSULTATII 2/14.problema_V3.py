
letters = ["l", "a", "v", "v", "a", "g", "m", "a", "n", "a"]
freq = {}

for ch in letters:
    freq[ch] = letters.count(ch)
    
print(freq)
print(freq.values())
print(max(freq.values()))

max_value = max(freq.values())
print(freq.keys())

for key in freq:
    if freq[key] == max_value:
        print(key)