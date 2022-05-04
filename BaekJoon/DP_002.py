

'''

 Backjoon _ exampels 9184

  "�ų��� �Լ� ���� "   by Jinwoo Lee

  < algorithm >
 
  1. Memoization & bottom - up 

  2. table�� ���������� ����ؾ� �ð��ʰ� �������� ���� �� �� ����

     * �������� �ִ� ĭ��(20)���� ����������, max_value = 21�� ���� 



'''


def w(a,b,c):

    if a <= 0 or b <=0 or c <=0 : return 1

    elif a >20 or b >20 or c >20 : return w(20,20,20)

    if table[a][b][c] != 0 :

        return table[a][b][c]

    else:
        
        if a < b and b < c :

            table[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

        else:
            table[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b, c-1) - w(a-1, b-1, c-1) 

        return table[a][b][c]


max_value = 21

table = [ [ [0 for _ in range(max_value)] for _ in range(max_value) ] for _ in range(max_value) ]


while True:

    a,b,c = list(map(int, input().split()))

    if a == -1 and b == -1 and c == -1 : break

    else:
        
        result = w(a,b,c)
    
        print(f"w({a}, {b}, {c}) = {result}")
