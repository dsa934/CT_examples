
def solution():
    
    n, l, k = map(int, input().split())

    score, cnt = 0, 0

    problems = sorted (  [ list(map(int, input().split())) for _ in range(n)] , key = lambda x :x[1] )


    for problem in problems:


        sub1 , sub2 = problem

        if cnt == k : break

        if sub2 <= l : 

            score += 140
            cnt +=1 

        else:
            if sub1 <= l :
                score += 100
                cnt +=1


    print(score)

solution()