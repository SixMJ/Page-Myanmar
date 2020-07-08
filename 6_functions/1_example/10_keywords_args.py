def simple_interest(p,r,t):
    return (p + t) - r
p,r,t = 10,20,30

#positional args
print("ptargs : ", simple_interest(p,t,r))
print("ptargs : ", simple_interest(p,r,t))

#keyword args
print ("kwargs : ",simple_interest(p=p,t=t,r=r))
print ("kwargs : ",simple_interest(p=p,r=r,t=t,))

#print ("kwargs : ",simple_interest(time=t,rate=r,prin=p))

