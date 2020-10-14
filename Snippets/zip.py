######################################ZIP########################################
# zip ( <iterables> )
# Alinea los valores de varios iterables en uno solo (tuplas)
# Alinea los valores con el mismo número de índice. No importa si el imput de 
# zip es de estructuras de datos distintas mientras sean iterables 

###################################EJEMPLO1######################################

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
zipped = list(zip(lst_1, lst_2))
print(zipped)
# [(1, 4), (2, 5), (3, 6)]

lst_1_new, lst_2_new = zip(*zipped)
print(list(lst_1_new))
print(list(lst_2_new))
# [1, 2, 3]
# [4, 5, 6]

###################################EJEMPLO2######################################

column_names = ['name', 'salary', 'job']

db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]

db = [ dict( zip(column_names, row) ) for row in db_rows ]

print(db)

