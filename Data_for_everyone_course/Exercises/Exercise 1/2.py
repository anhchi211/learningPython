##Cho ba số a, b, c. Kiểm tra xem ba số a, b ,c có phải là độ dài của một tam giác vuông hay không?
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
