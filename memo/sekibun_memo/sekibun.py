#区分求積で円周率計算

def f(x):
    return 4/(1+x*x)

def integral(f,a,b,n):
    h=(b-a)/n
    s=0
    x=0
    for i in range(n):
        s=s+f(x)
        x=x+h
    return s*h

print(integral(f,0,1,10))
print(integral(f,0,1,100))
print(integral(f,0,1,1000))
