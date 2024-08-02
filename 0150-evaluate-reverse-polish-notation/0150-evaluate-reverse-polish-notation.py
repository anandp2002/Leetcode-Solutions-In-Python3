class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        stack=[]
        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                num1=stack.pop()
                num2=stack.pop()
                res=int(eval(str(num2)+token+str(num1)))
                stack.append(res)
        return stack[-1]