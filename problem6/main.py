def prime_number(N) : 
    if N == 1 or N== 0 :
        return False
    elif N > 1:
        for i in range (2, N ) :
            if N % i == 0 :
                return False
        else :
            return True
def cekdigitsatuan(N):
    while (N) :
        modulus10=N%10
        if (modulus10 != 2 and modulus10 !=3 and modulus10 !=5 and modulus10 !=7 ):
            return False
        else :
            return True
    return True
def cekdigitpuluhan(N):
    str_angka =str(N)
    #panjang= len(str_angka)
    if len(str_angka) == 2 :
        if str_angka[0] == '2' or str_angka[0] == '3' or str_angka[0] =='5' or str_angka[0] =='7' :
            return True
        else :
            return False
    else :
        return True            
def full_prima(N):
    if prime_number(N) and cekdigitsatuan(N) and cekdigitpuluhan(N) :
        return True
    else :
        return False

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True