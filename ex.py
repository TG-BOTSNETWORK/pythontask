#keyword list
import keyword
print(keyword.kwlist)

print(len(keyword.kwlist))

# variable define
a = 7
print(a)
santhu, podili, = 15, 23
print(santhu,podili)
a = 45
b = 55
print("c is:", a+b)

#work with intiger
i = 2
print(i)
hmm = type(i)
print(hmm)
#work with float
f = 2.5
print(f)
tmm = type(f)
print(tmm)
f3 = 3e2
print(f3)
#work with bool
b = True
print(b)
b1 = False
print(b1)
b2 = None
print(b2)
ttt = type(b)
print(ttt)
tf = True + True + False - True
print(tf)
ff = True * False
print(ff)
# complex work
c = 20+4j
print(c)
print(type(c))
ss = c.real
print(ss)
ffff = c.imag
print(ffff)
c1 = 5+5j
print(c+c1)
ok = c.conjugate
print(ok)
print(c-c1)
print(c*c1)
c2 = 10+2.5j
print(c2) 
c3 = 2.0+34j
print(c3)
# work with string
s = "genrative ai & llm model great career ahead. also it is research domain"
print(s)
s = 'genrative ai & llm model great career ahead. also it is research domain'
print(s)
s = """genrative ai & llm model great career ahead. also it is research domain"""
print(s)
s = '''genrative ai & llm model great career ahead. also it is research domain'''
print(s)

#work with type casting
gandu = int(2.3)
print(gandu)
dan = int(True)
omm = int("10")
print(dan)
print(omm)
ss = float(10)
print(ss)
fffff = float(True)
print(fffff)
aa = float('20')
print(aa)
print(bool(9))
print(bool(9.9))
print(bool('9'))
print(bool(9+9j))
print(bool())

ggg = str(2)
print(ggg)
fffff = str(2.2)
print(fffff)
sasa = str(True)
print(sasa)
dd = str(10+10j)
print(dd)
com = 'milk'
print(com[0])
print(com[1])
print(com[2])
print(com[3])

#27-01-2025
#list ds
i = 64
print(type(i))
l = []
print(l)
print(len(l))
sa = l.append(10)
print(sa)
ds = l.append(10)
ds1 = l.append(20)
ds2 = l.append(30)
ds3 = l.append(40)
print(ds)
print(ds1)
print(ds2)
print(ds3)
print(id(l))

l2 = l.copy()
print(l2)
l == l2
print(l)
print(l2)
print(id(l)) == print(id(l2))


l.remove(10)
print(l)

#string indexing
s7 = 'santhu'
print(s7)
print(s7[0])
print(s7[1]) 
print(s7[2]) 
print(s7[3])
print(s7[4])
print(s7[5])
print(s7[-1])
print(s7[-2])
print(s7[-3])
print(s7[-4])
print(s7[-5])
#slicing
print(s7[0:5])
print(s7[1:4])
print(s7[-1:-4])
