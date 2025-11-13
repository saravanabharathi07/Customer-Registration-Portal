stack=[]
stack.append("a")
stack.append("b")
stack.append("c")
print("Stack",stack)

'''top_element=stack[-1]
print(top_element)'''

popped_element=stack.pop()
print(popped_element)

print(stack)

isEmpty=not bool(stack)
print(isEmpty)

print("Size: ",len(stack))
