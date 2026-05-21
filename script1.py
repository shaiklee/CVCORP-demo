''''#keyword arguments

def fun3(a,b,c,d):
    print(a,b,c,d)

def fun2(**b):
    print(b)
    print(**b)
fun2(a=30,b=75,c=40,d=70)
def fun4(*a,*b):
    print(a,b,sep="\n")
fun4(10,1,7,3,8,6,7,10)
def fun5(*a,**b):
    print(a,b,sep="\n")
fun4(10,1,7,3,8,6,7,10)

fun4(10,1,7,3,8,6,a=75,'b'=10)
fun4(10,1,7,3,8,6,a=75,'b'=10)'''

def fun6(*a):
    print(sum(a))
fun6(1,7,8,25,30,60,70)

def fun7(*a):
    i=0;s=0;
    while i<len(a):
        if a[i]%2==0:
              s+=a[i]
        i+=1
    print(s)
fun7(1,7,8,25,30,60,70)
def fun8(*a):
    i=0
    s=0
    while i<len(a):
          if i%2==0:
             s += a[i]
          i+=1
    print(s)
fun8(1,2,3,4,5,7,7,8,8,10)
'''def fun9(*a):
    i=0
    s=0
    while i%2==0:
        s += a[i]
        i+=1
    print(s)
fun9(1,2,3,4,5,7,7,8,8,10)'''
print(sum(a[::2]))
