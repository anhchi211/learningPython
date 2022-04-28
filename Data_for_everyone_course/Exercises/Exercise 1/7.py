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
