class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            res += f"{len(s):03d}{s}"

        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        res = []
        # loop over entire arr
        pointer = 0
        while pointer < len(s):
            # take three characters to find n
            num = s[pointer:pointer + 3]
            word_len = int(num)
            pointer += 3
            # take next n characters
            word = s[pointer:pointer + word_len]
            res.append(word)
            pointer += word_len

        return res




