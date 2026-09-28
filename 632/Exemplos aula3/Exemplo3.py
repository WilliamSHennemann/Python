def dividir(n1, n2):
    if n2==0:
        raise ZeroDivisionError('Não é possivel dividir por zero')
    return n1/n2

v1 = 10
v2 = 0

try:
    dividir(v1,v2)
except Exception as e:
    print(e)
