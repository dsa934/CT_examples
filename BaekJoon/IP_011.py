

'''

 Backjoon _ exampels 1817

  " �� ì��� �� "   by Jinwoo Lee

  < algorithm >

  1 . å�� žó�� �׿� �ֱ� ������ sort ��� ����, �迭�� ���������� ������ �� 

  2. pop �� å�� ���԰� �ڽ� ���ġ�� �ʰ��� ��� 

    a) �ڽ��� �߰��ϰ� ( answer +=1 )

    b) pop �� value�� �ٽ� �־��ְ� info,append(value)

    c) ���ο� �ڽ��� �־�� ������ total = 0 ���� �ʱ�ȭ 


 

'''



def solution():

    num, weight = map(int, input().split())

    if num == 0 : print(0)

    else:
        info = list(map(int , input().split()))
        
        total, answer  = 0, 0

        while True:

            value = info.pop()
            
            total += value 

            if total == weight : 

                answer += 1

                total = 0

            # algorithm 2 
            elif total > weight :

                answer +=1 

                total = 0

                info.append(value)

            elif total < weight and len(info) == 0 :

                answer+=1

            if len(info) == 0 : break

        print(answer)




        
solution()