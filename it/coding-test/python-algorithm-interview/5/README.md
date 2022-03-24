https://leetcode.com/problems/group-anagrams/

49. Group Anagrams
    Medium


Given an array of strings strs, group the anagrams together. You can return the answer in any order.
문자열 배열이 지정되면 애너그램을 함께 그룹화합니다. 답변은 임의의 순서로 반환할 수 있습니다.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
아나그램은 다른 단어나 구문의 글자를 정렬하여 형성된 단어나 구절이며, 일반적으로 모든 원래 글자를 정확히 한 번 사용합니다.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
Accepted
1,275,929
Submissions
2,002,136