#comm
alfa=1
alfa="Suc"
print(alfa)
x=y=z=1
print(x,y,z)
ab="Python is better  than "
c="C"
print(ab+c)

def funz():
    print(ab+"C")
    global x 
    x= "akfa"
    print(x)
funz()

print(x)
print(type(ab))

simone=10
if(simone==10):
    simone=simone*1e2
    print(simone,"Simomm")