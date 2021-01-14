# 주연겨
from collections import Counter

counter = Counter(s)
# print(counter)
stack = []

for ch in s :
    #print(ch)
    counter[ch] -= 1
    if ch in stack:
        continue

    while stack and ch < stack[-1] and counter[stack[-1]] > 0:
        stack.pop()
    stack.append(ch)

print(''.join(stack))
