numbers = list(map(int,input().split()))

def my_len(list):
    count = 0
    for a in list:
        count += 1
    return count

K = my_len(numbers)

def bubblesort(x):
    for i in range(K-1):
        for j in range(K-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x
	
bubblesort(numbers)

print(numbers[K//2])


