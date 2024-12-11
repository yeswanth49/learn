def main():
	number = int(input("whats factorial you want?"))
	print(fact(number))

def fact(n):
	if (n==1) or(n==0) :
		return 1
	else:
		return  n*fact(n-1)

if __name__ =="__main__":
	main()
