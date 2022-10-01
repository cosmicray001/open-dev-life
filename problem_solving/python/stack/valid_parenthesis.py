'''
    This program will check if a given string is a valid parenthesis or not
    Test case 1: (){}[] -> valid parenthesis
    Test case 2: ())[]{() -> Not valid parenthesis
'''

class Solution:
    def check_valid_parenthesis(self, given_input):
        stack = []
        mapper = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for current in given_input:
            if current == ')' or current == '}' or current == ']':
                if len(stack) == 0:
                    return False
                    
                top = stack.pop()
                if mapper[top] != current:
                    return False
            else:
                stack.append(current)
        
        if len(stack) > 0:
            return False
        return True

given_input = input("Provide the string")

result = Solution().check_valid_parenthesis(given_input)

if(result):
    print("Valid")
else:
    print("Not valid")