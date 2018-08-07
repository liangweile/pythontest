#coding:utf-8
#列表推导式
multiples1 = [i for i in range(30) if i%3 is 0]
print multiples1

def squared(x):
    return x*x
multiples2 = [squared(i) for i in range(30) if i%3 is 0]
print multiples2

#生成器
multiples3 = (i for i in range(30) if i%3 is 0)
print(type(multiples3))

#字典推倒式
mcase = {'a':10, 'b':34, 'A':7,'Z':3}
mcase_frequency = {
    k.lower():mcase.get(k.lower(), 0)+mcase.get(k.upper, 0)
    for k in mcase.keys()
    if k.lower() in ['a', 'b']
}
print mcase_frequency

mcase = {'a':10,'b':34}
mcase_frequency1 = {v:k for k,v in mcase.items()}
print mcase_frequency1