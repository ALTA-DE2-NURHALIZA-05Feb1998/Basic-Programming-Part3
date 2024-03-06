bilangan = int(input('masukkan bilangan : '))
hasil=[]
for i in range (1, bilangan+1) :
    if bilangan %i==0 :
        hasil.append(i) 
for hasil in reversed(hasil):
    print(hasil)