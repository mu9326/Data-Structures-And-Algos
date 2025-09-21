# 1. List can be empty? No
# 2. Str can be empty? Yes --> ""
# Type of chars? Any ASCII 256


class Codec:
    def encode(self, strs):
        # initialize the encoded_string = ''
        encoded_string = ""

        # iterate over strs - "neet", "code"
        for s in strs:
            # for each word:
            # 1. calculate it's length # 4
            length = str(len(s))
            # 2. we concatenate to the encoded string --> str(len) + '#' + str
            encoded_string += length
            encoded_string += "#"
            encoded_string += s

        print(encoded_string)
        return encoded_string

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            num = ""
            print("s[i]: ", s[i])
            while s[i] != "#":
                num += s[i]
                i += 1

            num = int(num)
            i += 1
            new_str = s[i : i + num]
            res.append(new_str)

            i = i + num

        return res


print(Codec().encode(["", "code"]))
print(Codec().decode("0#4#code"))
