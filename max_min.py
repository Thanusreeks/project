lst=[1,2,3,4,5,6,5,8,11,10]
f=max(lst,key=lambda x:x)
p=min(lst,key=lambda x:x)
s=sorted(lst,key=lambda x:x)
print(f,p,s)