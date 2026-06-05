class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(',']':'[','}':'{'}

        stack = []
        for bracket in s:
            if bracket in pairs.values():
                stack.append(bracket)
            if bracket in pairs.keys():
                if len(stack) == 0:
                    return False
                if stack[-1] != pairs[bracket]:
                    return False
                stack.pop()
        
        return len(stack)==0
