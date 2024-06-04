class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def find_letter(i, s):
            if i == len(digits):
                res.append(s)
                return
            for alpha in c[int(digits[i])]:
                find_letter(i+1, s+alpha)

        if digits == '':
            return []
        c = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
             6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        res = []
        find_letter(0, '')
        return res
