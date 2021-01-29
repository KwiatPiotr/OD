from typing import List

flag = 'CTF{0123456789}\x00'
#print(list(flag))
#print(bytes(list(flag)))

end = False
shuffle =   [0x02, 0x06, 0x07, 0x01, 0x05, 0x0B, 0x09, 0x0E, 0x03, 0x0F, 0x04, 0x08, 0x0A, 0x0C, 0x0D, 0x00]
add =       [0xEF, 0xBE, 0xAD, 0xDE, 0xAD, 0xDE, 0xE1, 0xFE, 0x37, 0x13, 0x37, 0x13, 0x66, 0x74, 0x63, 0x67]
xor =       [0x76, 0x58, 0xB4, 0x49, 0x8D, 0x1A, 0x5F, 0x38, 0xD4, 0x23, 0xF8, 0x34, 0xEB, 0x86, 0xF9, 0xAA]

def my_shuffle(s: str) -> str:
    l2 = list(s)
    l1 = s
    for i in range(len(shuffle)):
        l2[i] = l1[shuffle[i]]

    return ''.join([x for x in l2]).encode('utf-8')
    
def to_int_32(tab: List[int]) -> int:
    num = 0
    num += tab[3] * 0x1000000
    num += tab[2] * 0x10000
    num += tab[1] * 0x100
    num += tab[0]
    
    return num & 0xFFFFFFFF

def from_int_32(i: int) -> List[int]:
    i = i & 0xFFFFFFFF
    res = []

    res.append(i % 0x100)
    res.append((i % 0x10000) // 0x100)
    res.append((i // 0x10000) % 0x100)
    res.append(i // 0x1000000)
    
    return res

def my_add(s):
    s = list(s)
    res = []

    for x in range(0, 16, 4):
        res.extend(from_int_32(to_int_32(add[x:x+4]) + to_int_32(s[x:x+4])))

    print([hex(x) for x in res])
    return res


def my_xor(s: List[int]) -> str:
    res = ''
    print(len(s))

    for i in range(len(s)):
        res += chr(s[i] ^ xor[i])

    return res, [chr(x) for x in list(res)]


flag = my_shuffle(flag)
print(flag)
print('-----------------')
flag = my_add(flag)
print(flag)
flag = my_xor(flag)
print(flag)

flag = 'CTF{0123456789}\x00'
#flag2 = my_shuffle(flag)
#print(flag2)
#flag2 = my_add2(flag2)
#print([hex(x) for x in flag2])
#print('-----------------')
#flag, l = my_xor(flag)
#print(flag)
#print(l)

