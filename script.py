def display(n,a,b):
  print(f"name:{n}")
  print(f"age:{a}")
  print(f"branch:{b}")

display("leeyaz",23,"agri")# This is a sample Python script.
n="Lee"
a=24
b="ag"
def display():
    print(f"name:{n}")
    print(f"age:{a}")
    print(f"branch:{b}")
display()

"""#keyword arguments

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
fun4(10,1,7,3,8,6,a=75,'b'=10)"""

def fun6(*a):
    print(sum(a))
fun6(1,7,8,25,30,60,70)

def fun7(*a):
    i=0;s=0
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

def fun(x,y):
   print(x,y)
   return x+y
   print(x+x)
   return y+y
print(fun(10,20))
def great(a,b):
    if a>b:
        return a
    else:
        return b
print(great(75,77))
def fun(*a):
    b=sum(a)
    return b
if fun(1,7,8,6,5,3,2,8)%2==0:
    print("even")
else:
    print("odd")

class book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        if cls.valid_title(t):
            return cls(t,a)
        else:
            return "invalid bookstring"

    @staticmethod
    def valid_title(title):
        return len(title)>=3
bts="Harry potter-J.K.Rowling"
b1=book.from_string(bts)
b2=book("the song of ice and fire","R.R.Martin")