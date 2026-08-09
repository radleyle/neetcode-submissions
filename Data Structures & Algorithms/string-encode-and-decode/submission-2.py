class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # the encoded string would look like 4#neet5#code
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0  # i is the index to keep track of where we at in the input string

        while i < len(s):
            j = i

            # read each word
            while s[j] != "#":
                j += 1 # check if that character is the # sign 
            length = int(s[i:j]) # the length of the string starts from i and ends at j but not including j (which is #), and this length is the encoded integer
            res.append(s[j + 1 : j + 1 + length]) # get the rest of the word excluding the integer length and the # sign and append that word to the res list
            i = j + 1 + length # update i to the beginning of the next string once done with the previous one
        return res

