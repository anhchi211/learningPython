# Cho hai số nguyên dương bất kỳ a và b, kiểm tra xem a có chia hết cho b hoặc b có chia hết cho a không.
# Nếu a chia hết cho b, in ra màn hình: “a chia hết cho b”, nếu b chia hết cho a thì in ra màn hình:
#“b chia hêt cho a”, những trường hợp còn lại thì in ra: “a và b không có mối liên hệ với nhau thông qua phép chia”.

a = int(input ('Nhập 1 số nguyên dương bất kì: '))
b = int(input ('Nhập 1 số nguyên dương bất kì: '))

if a%b == 0:
    print('a chia hết cho b')
elif a%b != 0:
    print('a không chia hết cho b')
else:
    print('a và b không có mối liên hệ với nhau thông qua phép chia')
    
#Cho ba số a, b, c. Kiểm tra xem ba số a, b ,c có phải là độ dài của một tam giác vuông hay không?
#Nếu đúng thì in ra màn hình: ‘độ dài ba cạnh a, b,c có thể tạo thành 1 tam giác vuông’, nếu sai in ra màn
#hình: ‘độ dài ba cạnh a,b,c không thể tạo thành 1 tam giá vuông’ (Gợi ý: Định lý pytago)

a = float(input('Nhập 1 số nguyên dương: '))
b = float(input('Nhập 1 số nguyên dương: '))
c = float(input('Nhập 1 số nguyên dương: '))

if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print('độ dài ba cạnh a, b,c có thể tạo thành 1 tam giác vuông')
    else:
        print('độ dài ba cạnh a,b,c không thể tạo thành 1 tam giá vuông')
        

#Cho hai số a và b bất kỳ, thực hiện phép hoán đổi giá trị của hai số a và b.
#Ví dụ: a = 5, b = 10. Out put: a = 10, b = 5

a = int(input("Nhập giá trị a:"))
b = int(input("Nhập giá trị b:"))
a, b = b, a
print("Giá trị a:",a)
print("Giá trị b:",b)

#Cho một dãy số nguyên bất kỳ, và một số d. 
#Liệt kê trong dãy số đó có bao nhiêu số là bội số của d.

a=[]
a = int(input('Nhập dãy số nguyên: '))
A = input('Nhập dãy số nguyên có khoảng trắng: ')
d = float(input('Nhập số d: '))
A = A.split(' ')
for i in range(0,a):
  A[i] = int(A[i])
  if A[i] % d == 0:
    print(A[i], ' chia hết cho', d)
  else:
    print('')

#Cho một chuỗi ký tư bất kỳ (bao gồm các ký tự: ‘A’->’Z’,’a’-> ‘z’). 
# Đếm trong chuỗi đó có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường?

A=''
A=input('Nhập chuỗi ký tự cần đếm: ')
inhoa =0
inthuong=0

for i in range (0,len(A)):
 if A[i].isupper():
        inhoa += 1
 if A[i].islower():
        inthuong += 1

print("Số ký tư in hoa: ", inhoa)
print("Số ký tự in thường: ", inthuong)

#Cho một số nguyên dương a bất kỳ (a nằm trong đoạn [0,1000]). Liệt kê tất các bội số của a nằm
#trong đoạn [0,1000].

a = int(input("Nhap so nguyen duong a: "))
if a >=0 and a <=1000:
  for i in range(0,1001):
    if i%a == 0:
      print(i)
else:
  print("a khong thuoc [0,1000]")
  
#Cho hai số a và b (a <> 0, b <> 0). Liệt kê tất các các ước chung > 0 của hai số a và b.

a = int(input("Nhập số nguyên dương a = "))
b = int(input("Nhập số nguyên dương b = "))