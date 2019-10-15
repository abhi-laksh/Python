global ch
a = str(input("Enter String : "))
a += "#"
ch = 0
h = []
tp = []
count = 0
for i in a:
	try:
		elem = h.index(i)
		count+=1
		ch = 1 
	except ValueError:
		if ch == 1:
			tp.append((count , h[0]))
			count = 0
			while len(h) !=0 :
				h.remove(h[0])
		if len(h) == 1:
			tp.append((count , h[0]))
			count = 0
			h.remove(h[0])
			h.append(i)
			count+=1
			
		else:
			h.append(i)
			count+=1





print(tp)