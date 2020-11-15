#Tests:
A1 = [-4, 2,3,4]
A3 = [-4, -2,-3,-4]
A4 = [2,3,4]
A2 = [0,0,0,0]
A5 = [1,2,3,4]
A6 = [10, 5, 2, 1, 13]
A7 = [2,2,2,2]
A = [1,1,2,5]

def find_min_positive_not_in_array(A):
    A.sort()
    print(A)
    res = 1
    for i in range(len(A)):
        if(A[i]) > 0:
            print("positive detected")
            if(A[i] == res): 
                print("skip")
                res = res + 1
            else: 
                if(A[i] > res):
                    break
    return res
    

# Checks
b = solution(A)
print(b)
b = solution(A1)
print(b)
b = solution(A2)
print(b)
b = solution(A3)
print(b)
b = solution(A4)
print(b)
b = solution(A5)
print(b)
b = solution(A6)
print(b)
b = solution(A7)
print(b)