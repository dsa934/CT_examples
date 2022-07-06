
'''

 Backjoon _ exampels 1380

  "귀걸이"   by Jinwoo Lee

  < algorithm >
 
  1. dict 자료형을 사용하여 아래와 같이 데이터 저장

     key := student number
     value : name, A,B 


  2. A,B가 없는 학생의 이름 student[0] 을 출력 
    

'''




def solution():


    n_senario = 0

    while True:

        num = int(input())

        n_senario += 1

        if num == 0 : break

        else:

            student = {}

            for idx in range(num):

                student[idx+1] = []

                student[idx+1].append(input())


            for _ in range((2*num )-1):

                n, alpha = input().split()

                student[int(n)].append(alpha)

            for value in student.values():
                
                if 'A' not in value or 'B' not in value :

                    print(n_senario, value[0])

solution()