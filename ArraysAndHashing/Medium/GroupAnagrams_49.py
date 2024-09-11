def groupAnagrams(strs):
    anagrams = dict()
    for s in strs:
        sorted_s = str(sorted(s))
        if sorted_s not in anagrams.keys():
            anagrams[sorted_s] = [s]
        else:
            anagrams[sorted_s].append(s)
    res = []
    for lst in anagrams.values():
        res.append(lst)

    return res