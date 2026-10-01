class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False

        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if stack==[]:
                    return False
                elif i==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif i==']':
                    if stack[-1]=='[':
                        stack.pop()
                    else:
                        return False 
                elif i=='}':
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False   
        
        if stack==[]:
            return True   
        else:
            return False                             



        