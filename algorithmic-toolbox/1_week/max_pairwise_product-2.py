#"python3"

def apply(n, a): 
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n) 
    print(apply(n, a))