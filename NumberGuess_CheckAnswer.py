Q1 = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
Q2 = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
Q3 = [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
Q4 = [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
Q5 = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
ans = 0
print(Q1)
a = input("y/n: ")
if a == 'y':
    ans = ans +1
print(Q2)
b = input("y/n: ")
if b == 'y':
    ans = ans +2
print(Q3)
c = input("y/n: ")
if c == 'y':
    ans = ans + 4
print(Q4)
d = input("y/n: ")
if d == 'y':
    ans = ans+8
print(Q5)
e = input("y/n: ")
if e == 'y':
    ans = ans+ 16
print("The Number in Your Mind is {}".format(ans))