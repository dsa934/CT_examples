'''

 Backjoon _ exampels #

  ""

 by Jinwoo Lee ( 2021/06/11 )


 # Attention for Implementation

  - 에라토스테네스의 체 ( 소수판별 알고리즘)

    => 어떤 수의 소수 여부 판별시, 특정한 숫자의 제곱근 까지만 약수의 여부를 검증하면 O(N^(0.5)) 소모

    => 즉, 코딩에서 range(2, int(value**0.5)+1) 까지만 소수를 판별하면 시간복잡도를 더욱 줄일 수 있음 


'''

m, n = list(map(int, input().split()))

result = []

for value in range(m,n+1):

    cnt = 0

    if value == 1:
        continue

    for chk_value in range(2,int(value**0.5)+1):

        if value % chk_value == 0:

            cnt+=1
            break

    if cnt == 0:

        result.append(int(value))

for value in result:

    print(value)