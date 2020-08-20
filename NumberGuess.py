binArr1 = []
binArr2 = []
binArr4 = []
binArr8 = []
binArr16 = []

for binNum in range(1,32):
    binStr = format(binNum,'05b')
    
    if binStr[-1] == '1':
        binArr1.append(binNum)
    
    if binStr[-2] == '1':
        binArr2.append(binNum)
    
    if binStr[-3] == '1':
        binArr4.append(binNum)

    if binStr[-4] == '1':
        binArr8.append(binNum)
    
    if binStr[-5] == '1':
        binArr16.append(binNum)
        
print('\n')                
print(binArr1)
print('\n')
print(binArr2)
print('\n')
print(binArr4)
print('\n')
print(binArr8)
print('\n')
print(binArr16)