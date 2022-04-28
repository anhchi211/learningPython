#Tìm giá trị lớn nhất và giá trị nhỏ nhất xuất hiện trong dãy số bất kỳ.

a = int(input('Nhập dãy số bất kỳ : '))
A=[]
for i in range (0,a):
  x = int(input())
  A.append(x)
Max=A[0]
Min=A[0]
for i in range(0,a):
  if A[i]>=Max:
    Max = A[i]
  if A[i]<=Min:
    Min = A[i]
print('Giá trị lớn nhất là: ')
input(Max)
print('Giá trị bé nhất là: ')
input(Min)

A=[]
n = int(input("Nhap chieu dai cua day so nguyen A: "))
for i in range(0,n):
  A.append(int(input("Nhập phần tử thứ %d :  " %i)))
max = A[0] 
min = A[0]
for i in range(0,n):
  if max <= A[i]:
    max = A[i]
  if min >= A[i]:
    min = A[i]
print("So Lon nhat la: %d, so Nho nhat la: %d" %(max, min))