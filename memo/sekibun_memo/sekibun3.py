#シンプソン則で円周率計算

def f(x):
    return 4/(1+x*x)

def integral(f,a,b,n):
    n2=n//2
    h=(b-a)/n
    h2=h*2
    s=0

    s2=0
    x=h
    for i in range(n2):
        s2=s2+f(x)
        x=x+h2
    s=s+s2*4
    
    s2=0
    x=h2
    for i in range(n2-1):
        s2=s2+f(x)
        x=x+h2
    s=s+s2*2
    s=s+f(a)+f(b)
    return s*h/3

print(integral(f,0,1,10))
print(integral(f,0,1,100))
print(integral(f,0,1,1000))
