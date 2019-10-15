n=int(input("Enter nth term : "))

def summ(a):
	if a<=1:
		return a
	else:
		return a + summ(a-1)

ans=summ(n)

print(ans)