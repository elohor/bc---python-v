Import math
Import Sqrt
def is = prime(num)
	if num <= 1
		return false
	for i in range(2,int(Sqrt(num + 1)))
	if num % i == 0
		return false
	return true