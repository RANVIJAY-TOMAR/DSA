class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums_stack = []
        for token in tokens:
            if token == '+':
                op = int(nums_stack[-2]) + int(nums_stack[-1])
                nums_stack.pop()
                nums_stack[-1] = op
            elif token == '-':
                op = int(nums_stack[-2]) - int(nums_stack[-1])
                nums_stack.pop()
                nums_stack[-1] = op
            elif token == '*':
                op = int(nums_stack[-2]) * int(nums_stack[-1])
                nums_stack.pop()
                nums_stack[-1] = op
            elif token == '/':
                op = int(nums_stack[-2]) / int(nums_stack[-1])
                nums_stack.pop()
                nums_stack[-1] = int(op)
            else:
                nums_stack.append(token)
        return int(nums_stack[-1])