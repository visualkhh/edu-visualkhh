# 민호
import collections
def palinCheck(s)-> bool:
    strs = collections.deque()
    for char in s:
        #문자열을 단어로 분리해서 덱에 저장
        # #영문자의 경우소문자로 통일(미구분)
        if char.isalnum():
            strs.append(char.lower())
    #확인작업
    while len(strs) > 1:
        if strs.pop() != strs.popleft():
            # popleft 사용시 시간복잡도 O(1)
            # 리스트의 pop(0) 사용시 시간복잡도 O(n)과 비교해서 더 빠름
            return False
    return True

if __name__ == '__main__':
    palindrome = palinCheck('A man, a plan, a canal: Panama')
    print(palindrome)
