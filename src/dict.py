freq = {}
for w in ["a","b","a"]:
    freq[w] = freq.get(w, 0) + 1
# {"a": 2, "b": 1}

groups = {}
for w in ["a", "bb", "c"]:
    groups.setdefault(len(w), []).append(w)
# {1: ["a","c"], 2: ["bb"]}
print(freq)