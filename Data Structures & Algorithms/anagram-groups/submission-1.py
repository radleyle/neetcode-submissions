class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams
        # go through each 
        for s in strs:
            count = [0] * 26 # initiate an empty array of 26 0's so that we can fill them up later
            # go through each character
            for c in s:
                # map any lowcase letter a...z to an index from 0..25
                # after mapping letters to the indices, count increments the the counter at that         letter's slot, holding the frequency of each letter, for example "aab", count[0] = 2, count[1] = 1
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())