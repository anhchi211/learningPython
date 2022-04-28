#Cho hai số a và b bất kỳ, thực hiện phép hoán đổi giá trị của hai số a và b.
#Ví dụ: a = 5, b = 10. Out put: a = 10, b = 5

a = int(input("Nhập giá trị a:"))
b = int(input("Nhập giá trị b:"))
a, b = b, a
print("Giá trị a:",a)
print("Giá trị b:",b)

#a=a+b
#b=a-b
#a=a-b