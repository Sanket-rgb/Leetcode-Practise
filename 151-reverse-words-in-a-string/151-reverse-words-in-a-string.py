class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        length = len(s)
        result = ""
        
        while i < length:
            while i < length and s[i] == " ":
                i += 1
            j = i + 1
            while j < length and s[j] != " ":
                j += 1
            if i > length or j > length:
                break
            w = s[i:j]
            result = w + " " + result if result != "" else w
            i = j + 1
            
            # i += 1

        return result
#             temp = s[i]
#             s[i] = s[length]
#             s[length] = temp
            
#             i += 1
#             length -= 1
        # return s