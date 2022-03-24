import re
import collections
from typing import List
# run main
if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5];
    # print(arr[::-5])
    # print(arr[1:2])
    # a = len([1,2,3,3])//3
    # l = [1, 2, 3, 3]
    # l.__len__()
    # a = len(l) / 3
    # print(a)
    # s = 'Show me the money 0 a good f'
    # s = re.sub('[^a-z0-9]', '', s.lower()) # 정규식으로 불필요한 문자 필터링
    # s = re.subn('[^a-z0-9]', '', s.lower(),2 ) # 정규식으로 불필요한 문자 필터링
    # print(s)
    # print(range(76));

    # for enumerate
    # l = [1, 2, 3, 3]
    # for i, v in enumerate(l):
    #     print(i, v)

    # list sort lambda
    # l = [1, 2, 3, 3]
    # l.sort(key=lambda x: x)
    # print(l)
    # sorted
    # l = [1, 2, 3, 3]
    # l = sorted(l, key=lambda x : x[1])
    # print(l)

    # num_list = [15, 22, 8, 79, 10]
    # num_list.sort(reverse=True)
    # print(num_list)
    # print(sorted(['좋은하루','good_morning','굿모닝','niceday'], reverse=True))

    # str_list = ['좋은하루','good_morning','굿모닝','niceday']
    # print(sorted(str_list, key=len))  # 함수

    # print(sorted(str_list, key=lambda x : x[1], reverse=True))  # 람다
    # tuple_list = [('좋은하루', 0, 45),
    #               ('niceday', 1),
    #               ('좋은하루', 5),
    #               ('good_morning', 3),
    #               ('niceday',5)]
    #
    # tuple_list.sort(key=lambda x : (x[0], x[1]), reverse=True)  # '-'부호를 이용해서 역순으로 가능
    # print(tuple_list)

    # split string
    # s = '좋은하루,goo d_morning,굿모 닝,ni ceday'
    # print(s.split())

    # print('---') if False else print('--22-')

    # s = "dig1 8 1 5 1";
    # print(s.split())
    # print(s.split()[1:])
    # print(s.split()[0])

    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.";
    # banned = ["hit"];
    # # words = re.sub(r'[^\w]', ' ', paragraph);
    # # for word in words:
    # #     print(word, end='')
    # words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
    #     .lower().split()
    #          if word not in banned]
    #
    # counts = collections.Counter(words)
    # print(counts)
    # print(counts.most_common(1))
    # print(counts.get('ball'))
    # print(counts['ball'])
    # print(words)

    # anagrams = collections.defaultdict(list);
    # anagrams['s'].append('22')
    # print(anagrams);
    #
    # baseline = {'music': 'bach', 'art': 'rembrandt'}
    # adjustments = {'art': 'van gogh', 'opera': 'carmen'}
    # at = list(collections.ChainMap(adjustments, baseline))
    # print(at);

    print ('1234567891abc'[-2:5])
    # print(max('ddd2', 'ddd5', 'ddd', 'ddd', key=len));
