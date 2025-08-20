class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = [""]

        for d in digits:
            curr = letters[int(d)]
            next = []

            for p in result:
                for i in curr:
                    next.append(p+i)
            
            result = next
        
        return result
        
