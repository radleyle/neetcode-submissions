class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # count the ocurrences of each value
        freq = [[] for i in range(len(nums) + 1)] # the freq array to store the index (the occurences of each value) and the values (list of values in the input array that has the same occurences)

        for n in nums:
            count[n] = 1 + count.get(n, 0) # count how many times each value occurs

        for n, c in count.items():
            freq[c].append(n) # add the value that occurs c times to the freq array, after this we gonna have the table looks like the notes

        res = []

        # loop through the table index from top to bottom index
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: # each freq[i] is a sublist so we're looping through each of those sublists
                res.append(n)
                if len(res) == k:
                    return res
