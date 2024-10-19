class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        s_index = 0
        p_index = 0
        match = False
        while True:
            if s_index == len(s):
                break

            if s[s_index] == p[p_index] or p[p_index] == "*" or p[p_index]== ".":
                match = True
            else:
                match = False
                if len(p[p_index:]) < len(s):
                    return match
                s_index = -1
            
            # check if p has reached its end
            if p_index == len(p) - 1:
                # last character is either * or .
                if p[p_index] == "*" or p[p_index] == "." or (p[p_index].isalpha() and len(s) == len(p)):
                    match = True
                else:
                    match = False
                break
                
            s_index += 1 # move to next index of s
            p_index += 1 # move to next index of p
        
        return match
