'''

 Backjoon _ exampels #

  "Baek 1343 - 폴리오미노 (Greedy)"   by Jinwoo Lee

'''


string = input()

string = string.replace('XXXX', 'AAAA')
string = string.replace('XX', 'BB')


if 'X' in string : print(-1)
else: print(string)