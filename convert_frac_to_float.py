
from math import log

def calculate_expon(exponent):
				#calculate bias offset for exponent
	exponent += 2**7-1	#2^(exponent_size-1)-1
	return exponent

def remove_first(exponent,val): #remove the hidden bit from fraction
	return val - 2**exponent

def calculate_n_bits(exponent,val): #calculate the fractional segment by
				    #by going from 1/2->1/2^24
	val = remove_first(exponent,val)
	val /= 2**exponent
	s = ''
	for i in range(-1,-24,-1):
		if(val - 2**i >= 0):
			s += '1'
			val -= 2**i
		else:
			s += '0'
	return s

def s_expon(exponent):
	s = ''					# simple dec to binary 
						# conversion
	exponent = calculate_expon(exponent)
	for i in range(7,-1,-1):
		if(exponent - 2**i >= 0):
			s += '1'
			exponent -= 2**i
		else:
			s += '0'
	return s


def main():
	# ignore this, its just input handling
	number = input("place the floating point to get its representation: ")
	if("/" in number):
		
		num = number.split('/')[0]
		den = number.split('/')[1]
		number = int(num)/int(den)
	number = float(number)


	if(number == 0):				#if number is zero
							#print all zeros
		print(''.join(['1' for i in range(32)]))
		return
	if(number < 0):					#if less than zero
							#print 1 sign bit
		print('1',end='')
		number = -number
	else:						#print 0 sign bit
		print('0',end='')
							# find the value 
							# of the hidden
							# bit
	exponent = int(log(number,2))
	
	print(s_expon(exponent),end='')
	print(calculate_n_bits(exponent,number))


main()
