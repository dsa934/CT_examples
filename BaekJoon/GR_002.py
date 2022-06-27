

'''

 Backjoon _ exampels 14720

  "우유 축제"   by Jinwoo Lee

  < algorithm >

  * 0->1->2 가 순환되는 구조를 보고, 3으로 나눈 나머지 값들이라는 아이디어를 이용
 

'''

def solution():

    num = int(input())

    candidate = list(map(int ,input().split()))

    cnt, answer = 0, 0


    for idx in range(num):

        if candidate[idx] == cnt%3:

            cnt+=1

            answer +=1

    print(answer)

solution()