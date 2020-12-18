Reverse String (로그 파일 재정렬)
====

#### https://leetcode.com/problems/reorder-data-in-log-files/

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

- Each word after the identifier will consist only of lowercase letters, or;
- Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

1. 로그의 가장 앞 부분은 식별자다
2. 문자로 구성된 로그가 숫자 로그보다 앞에온다.
3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

# Example 1
1. Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
2. Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

# Constraints
0 <= logs.length <= 100  
3 <= logs[i].length <= 100  
logs[i] is guaranteed to have an identifier, and a word after the identifier.  
