
letters = ["l", "a", "v", "v", "a", "g", "m", "a", "n", "a"]
freq = {}


for ch in letters:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

max_freq = 0
for key in freq:
    print(freq[key])
    if freq[key] > max_freq:
        max_freq = freq[key]
        max_key = key
        
print("Valoarea maxima:", max_freq)
print("Litera care se intalneste cel mai des este", max_key)