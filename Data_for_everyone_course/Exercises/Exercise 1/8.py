#Cho một dãy ký tự được xem là một password. Kiểm tra password có hợp lệ hay không.
#Một password hợp lệ khi và chỉ khi thỏa mãn tất cả các điều kiện sau:
#1.Ít nhất 1 chữ cái nằm trong [a-z]
#2. Ít nhất 1 số nằm trong [0-9]
#3. Ít nhất 1 kí tự nằm trong [A-Z]
#4. Ít nhất 1 ký tự nằm trong [$ # @]
#5. Độ dài mật khẩu tối thiểu: 6
#6. Độ dài mật khẩu tối đa: 12


def check_password(a):
      KTDB = '@#!'
  dem1 = dem2 = dem3 = dem4 = False
  if 12 < len(a) and len(a) < 6 :
    return False
  for i in a:
    if i.islower():
      dem1 = True
    if i.isupper():
      dem2 = True
    if i.isdigit():
      dem3 = True
    if i in KTDB:
      dem4 = True 
  if dem1 and dem2 and dem3 and dem4:
    return True
  else:
    return False

A=input("Nhap chuoi cac password cach nhau bang dau phay")
A = A.split(',')
for i in A:
  check_password(i)
    
