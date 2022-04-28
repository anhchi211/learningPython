# Cho hai số nguyên dương bất kỳ a và b, kiểm tra xem a có chia hết cho b hoặc b có chia hết cho a không.
# Nếu a chia hết cho b, in ra màn hình: “a chia hết cho b”, nếu b chia hết cho a thì in ra màn hình:
#“b chia hêt cho a”, những trường hợp còn lại thì in ra: “a và b không có mối liên hệ với nhau thông qua phép chia”.

a = int(input ('Nhập 1 số nguyên dương bất kì: '))
b = int(input ('Nhập 1 số nguyên dương bất kì: '))



if b!=0  and  a%b == 0:
    print('a chia hết cho b')
elif a!=0 and a%b != 0:
    print('a không chia hết cho b')
else:
    print('a và b không có mối liên hệ với nhau thông qua phép chia')
    
