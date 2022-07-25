
'''

 Backjoon _ exampels 5534

  "����"   by Jinwoo Lee

  < algorithm >

  1. �Է����� �־����� �� ���ǰ��� ���ؼ�, ���۰� ������ ������� �ϴ� ������ ����/�� ���� ���� idx�� ã�´�.


  2. 1�� ������ ���� �־��� ������ ����~ �� ������ �����ǰ�, 

     �ش� ���� ������  [start_idx + avg_interval*cnt] �� ���� ���� �� ���� ���ݿ� �ִ� ���ĺ���, 

     ������� �ϴ� ������ ������ ������ üũ

  
'''



def make_ganpan(name, candidate):

    length_name = len(name)

    for start_idx in range(len(candidate)):

        for end_idx in range(start_idx, len(candidate)):

            if candidate[start_idx] == name[0] and candidate[end_idx] == name[-1]:

                avg_interval = (end_idx - start_idx) // (length_name-1) 

                cnt = 0

                while cnt < length_name :

                    if candidate[start_idx + avg_interval * cnt ] == name[cnt]:

                        cnt +=1

                    else: 

                        break

                        
                if cnt == length_name : return 1

 

    return 0


def solution():

    

    num = int(input())

    name = input()

    candidates = [input() for _ in range(num)]

    answer = 0 

 
    for candidate in candidates:

        answer += make_ganpan(name, candidate)

    print(answer)

solution()