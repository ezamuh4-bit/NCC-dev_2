x=input()
y=list(x)
y.reverse()
y="".join(y)
if y==x:
    return True
else:
    return False
