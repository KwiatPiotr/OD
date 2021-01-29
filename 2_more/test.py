def shuffle( in_str ):
	new_pos = [ 0x2, 0x6, 0x7, 0x1, 0x5, 0xB, 0x9, 0xE, 0x3, 0xF, 0x4, 0x8, 0xA, 0xC, 0xD, 0x0 ]
	out_str = []
	for x in range( 16 ):
		out_str.append(ord(in_str[new_pos[x]]))
	return out_str

def toInt32( num_array ):
	num = 0
	num += num_array[3] * 0x1000000
	num += num_array[2] * 0x10000
	num += num_array[1] * 0x100
	num += num_array[0]
	return num & 0xffffffff

def fromInt32( num ):
	num = num & 0xffffffff
	num_array = []
	num_array.append(num%0x100)
	num_array.append((num%0x10000)//0x100)
	num_array.append((num//0x10000)%0x100)
	num_array.append(num//0x1000000)
	return num_array

def add( in_str ):
	values = [ 0xEF, 0xBE, 0xAD, 0xDE, 0xAD, 0xDE, 0xE1, 0xFE, 0x37, 0x13, 0x37, 0x13, 0x66, 0x74, 0x63, 0x67 ]
	out_str = []
	for x in range( 0, 16, 4 ):
		out_str.extend(fromInt32(toInt32(values[x:x+4])+toInt32(in_str[x:x+4])))

	return out_str

def xor( in_str ):
	values= [ 0x76, 0x58, 0xb4, 0x49, 0x8d, 0x1A, 0x5F, 0x38, 0xD4, 0x23, 0xF8, 0x34, 0xEB, 0x86, 0xF9, 0xAA ]
	out_str = []
	for x in range( 16):
		out_str.append(in_str[x]^values[x])
	return out_str
	
result = xor(add(shuffle("CTF{0123456789}\x00")))  
print("Result of shuffle, add, and xor:")
print([chr(x) for x in result])
for x in result:  
   print( hex(x) )
