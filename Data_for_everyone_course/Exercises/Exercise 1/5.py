#Cho một dãy số nguyên bất kỳ, và một số d. 
#Liệt kê trong dãy số đó có bao nhiêu số là bội số của d.

a=[]
a = int(input('Nhập dãy số nguyên: '))
A = input('Nhập dãy số nguyên có khoảng trắng: ')
d = float(input('Nhập số d: '))
A = A.split(' ')
for i in range(0,a):
  A[i] = int(A[i])
  if d!=0A[i] % d == 0:
    print(A[i], ' chia hết cho', d)
  else:
    print('')  