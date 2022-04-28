#Cho một số nguyên dương a bất kỳ (a nằm trong đoạn [0,1000]). Liệt kê tất các bội số của a nằm
#trong đoạn [0,1000].

a = int(input("Nhap so nguyen duong a: "))
if a >=0 and a <=1000:
  for i in range(0,1001):
    if i%a == 0:
      print(i)
else:
  print("a khong thuoc [0,1000]")
