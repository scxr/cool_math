def conjecture(n):
    cnt = 0
    while n!=1:
        if n <= 0:
            break
        if n % 2 == 0:
            n /=2
        else:
            n = n*3 + 1
        cnt += 1
    return cnt
tof = int(input('Enter a number '))
print(f'It will take {conjecture(tof)} iterations to conform with collatz conjecture')
