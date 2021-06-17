'''

 Backjoon _ exampels #

  "Baek 2437 - 저울 "

 by Jinwoo Lee ( 2021/06/17 )


 # Attention for Implementation

  - 그리디 알고리즘의 해는 최적해를 보장하지는 못하지만, 해당 문제에서의 해는 제공이 가능하다

  -> 이 문제는 주어진 리스트에서 만들 수 없는 수중 최소를 구하는 문제이기 때문에

    주어진 리스트에서만 성립이 되면 풀이가 될 수 있다 ( 그리디를 설계할떄 너무 생각해서 문제를 못푸는 경우가 많았다)


  =>  list = [1,2,3]         =>   1. 더하는 수가 목표하는 수보다 크면 안된다 
      1                           2. target 을 1씩 증가시키는게 아니라 list원소 순서대로 더한다 
      2
      3
      4 = 1 +3
      5 = 2 + 3
      6 = 3 + 3
      

'''

num = int(input())

nums = sorted(list(map(int,input().split())))

target = 1

for value in nums:

    if target < value:
        break

    target+=value

print(target)



