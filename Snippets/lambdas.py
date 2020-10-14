####################################LAMBDAS######################################
# lambda <arguments> : <return expression>
# lambda es una pequeña función anónima
# Puede tener varios argumento pero solo una expresión
# Siempre tiene que regresar un valor, a diferencia de una funcion normal

# Ejemplo simple
print( (lambda x: x + 3)(3) )

# Varios argumentos
x = lambda a, b: a * b
print( x(5,4) )

# Dentro de una función
def test(n):
    return lambda x: x ** n
valor = test(3) # segundo argumento de la expresión (n)
print( valor(5) ) # primer argumento de la expresión (x)

###################################EJEMPLO1######################################

txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

print(list(mark))

###################################EJEMPLO2######################################

txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

test = [ ('anonymous' in line, line) for line in txt]
print(test)