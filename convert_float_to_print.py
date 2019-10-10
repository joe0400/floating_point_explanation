
def get_mantissa(s: str) -> float:
	
	ret = 0
	
	for radix, char in zip(range(-1,-len(s),-1),s):
		
		if(char == '1'):
			ret += 2**radix
				# the radix is the decimal point, which
				# is after the first bit of the bitstring
				# so goes from that on
	return ret

def get_exponent(s: str) -> int:
	
	ret = 0
	
	bias = 2**(len(s)-1)-1 # this bias function figures out 
			       # max_uint for size - 1
	
	for radix, char in zip(range(len(s)-1,-1,-1), s):
	
		if(char == '1'):
			ret += 2 ** radix
			       # this calculates the number using normal
	                       # factors
	
	return ret-bias


def main():

	print(" THIS IS FOR SINGLE_PRECISION FLOATING POITNS ONLY!!\n")

	s = input("input the floating point number: ")
	
	neg = s[0] == '1' 
	# sets negative bit, to figure out if negative is true
	
	exponent = s[1:9]
	# slices string to figure out digits from 1, to 9

	mantissa = s[9:]
	# mantissa is 9 onwards
	
	
	mantiss: float      = get_mantissa(mantissa)
	exponent_state: int = get_exponent(exponent)
	if(exponent_state != -127): # all zeros is up one, with a repeat
				    # -ing state of previous ones
		mantiss += 1	    # zero state is a special mode, 
				    # hidden bit is zero, vs 1
	else:
		exponent_state += 1
	if(exponent_state == 128): # all 1s are NaN, unless fractional
				   # bits are all zero, in which its 
				   # signed inifinity
		if('1' not in mantissa):
			if(neg):
				print("-",end="")
			print("infinity")
		else:
			print("NaN")
		return
	if(neg):
		print("-",end="")
	print(mantiss*2**exponent_state)

main()
