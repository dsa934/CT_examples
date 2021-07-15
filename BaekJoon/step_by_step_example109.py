'''

 Backjoon _ exampels #

  "Baek 1969 -DNA"(string)   by Jinwoo Lee


 # Algorithm 

  0. 주어진 배열을 transpose 하여, 염색체 구성 [A,C,G,T] 중 가장 counting이 많이 되는 알파벳과 수를 추출

  1. 추출된 알파벳을 이어붙여 염색체를 만들고, 전체 문자열 길이 - 각 알파벳에 해당하는 개수를 통해 hamming distance를 계산

  2. hamming distance가 동일한 경우 사전순으로 앞서는것을 출력하기 때문에 counting 시 사전순 counting


'''


n,m = list(map(int,input().split()))

DNA = [list(input()) for _ in range(n)]

cnt = 0
result = []

# transpose
trans_DNA = list(zip(*DNA))

for value in trans_DNA:

    information = max( [value.count('A'),'A'], [value.count('C'),'C'], [value.count('G'),'G'], [value.count('T'),'T'], key = lambda x: x[0])
    


    result.append(information[1])

    cnt += (n - information[0])

print(''.join(result))
print(cnt)