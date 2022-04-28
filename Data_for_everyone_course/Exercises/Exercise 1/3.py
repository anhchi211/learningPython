#Cho 1 dãy số các số nguyên bất kỳ, in ra số lượng các số chẵn, số lượng các số lẽ xuất hiện trong
#dãy. Lưu ý: số 0 ko phải là số chẵn cũng không phải là số lẽ.


         

lis1= int (input('Nhập 1 dãy số bất kỳ: ')) 
chan, le = 0, 0
for i in list1:  
    if i % 2 == 0 and i !=0:
        chan += 1
    elif i % 2 == 1 and i !=0:
        le += 1
          
print("số lượng số chẵn trong dãy: ", chan)
print("số lượng số lẻ trong dãy: ", le)