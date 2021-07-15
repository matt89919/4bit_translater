func=input("0 or 1 : ")

def bit_dec(bit):
    count=0
    for i in range(0,4):
        count+=int(bit[i])*(2**(3-i))
 #       print(int(bit[i]),2**(3-i))
 #       print(count)
    return count

def dec_bit(dec):
    num=0
    count=0
    count=int(dec)
    for i in range(0,4):
        num+=(count%2)*(10**i)
        count=count//2
    return num

if func=='0' :
    #bit to decimal
    bit=input("bit : ")
    print(bit_dec(bit))
else :
    #decimal to bit
    dec=input("dec : ")
    print(dec_bit(dec))