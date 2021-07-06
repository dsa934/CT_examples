'''

 Backjoon _ exampels #

  "Baek 11723 - 집합 (Implementation)"   by Jinwoo Lee


 # Algorithm 

  0. 

  1. 

  2.

  3.


 # Attention for Implementation



'''

def functions(oper, num, stack):

    if oper == 'add' and int(num) not in stack : stack.append(int(num))

    elif oper == 'remove' and int(num) in stack  : stack.remove(int(num))

    elif oper =='check' : 

        if int(num) in stack : print(1)
        else : print(0)
         
    elif oper =='toggle' :

        if int(num) in stack : stack.remove(int(num))

        else : stack.append(int(num))

    elif oper =='empty' : stack = []

num_oper = int(input())

stack = [] 


for _ in range(num_oper):

    oper = input().split()

    if oper[0] == 'all' : stack = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 

    elif oper[0] =='empty' : stack = []

    else : functions(oper[0],oper[1],stack)
