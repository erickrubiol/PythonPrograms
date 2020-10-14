# [ <expresión> +  <contexto> ]
# La expresión dice que hacer con cada elemento de la lista.
# El contexto empieza a partir del "for", dice que elementos de la lista seleccionar: 
# consiste en un número arbitrario de declaraciones for, in, if.
# Siempre va encerrada en [] la listComprehension.

###################################EJEMPLO1######################################

letras = [letra for letra in 'betito']
print(letras)

###################################EJEMPLO2######################################

# Lista 'clientes' con estructura [nombre, ingreso]
clientes = [("John", 240000),
             ("Alice", 120000),
             ("Ann", 1100000),
             ("Zach", 44000),
             ("Erick", 1050000)
            ]

# Lista de clientes con ingreso >$1M
#mejores_clientes = [nombre for nombre,ingreso in clientes if ingreso>1000000]
#print(mejores_clientes)

# Si no se usa listComprehension el código se vería algo así
mejores_clientes = []
for key, val in clientes:
    if val > 1000000:
        mejores_clientes.append(key)
print(mejores_clientes)


###################################EJEMPLO3######################################

print( [ (x, y) for x in range(3) for y in range(3)] )

print( [x ** 2 for x in range(10) if x % 2 > 0] )

print( [x.lower() for x in ['DILE', 'A', 'ESA', 'VIEJITA', 'QUE SE', 'VAYA']] )


###################################EJEMPLO4######################################

employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}

top_earners = [(key, value) for key, value in employees.items() if value >= 100000]

print(top_earners)

###################################EJEMPLO5######################################

# given a multiline string, create a list of lists—each consisting of all the words 
# in a line that have more than three characters. Listing 2-2 provides the data and 
# the solution.

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

w = [ [ word for word in line.split() if len(word) > 3 ] for line in text.splitlines() ]
print(w)

###################################EJEMPLO6######################################

companies = {
    'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
    'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
    'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18} }

illegal = [x for x in companies if any(y<9 for y in companies[x].values())]

print(illegal)