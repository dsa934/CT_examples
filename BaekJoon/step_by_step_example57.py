'''

 Backjoon _ exampels #

  "Baek 10610 - 30 (문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 양수 N을 구성하는 숫자들을 섞어서 30의 배수중 가장 큰값을 만들자 안되면 -1 ( 입력은 0이상)

  1'. 현재 주어진 수의 길이중에 가장 큰값을 만들어야 함 -> 내림차순 정렬 

  2'. 30의 배수 : 3의 배수이면서, 일의자리가 0인 수


  # first try 
  #1. itertools 의 permuatation 사용하여 모든 순열을 구하고 그 중에 30의 배수가 있는지 없는지 check

  #2. len(string)의 길이를 고정하고, 숫자들을 조합해야 하기 떄문에 순열이 적합 => 이거하니까 시간초과 판정




'''

number = sorted(list(input()), reverse=True)

sum(list(map(int,number)))

if sum(list(map(int,number))) % 3 == 0 and int(number[-1]) == 0 : print(''.join(number))
else: print(-1)

