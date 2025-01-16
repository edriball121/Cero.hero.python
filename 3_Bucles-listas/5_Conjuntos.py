# Conjuntos

# Los conjuntos son colecciones desordenadas de elementos únicos. Se pueden usar para realizar operaciones matemáticas como la unión, 
# la intersección, la diferencia y la diferencia simétrica.

a = {1, 2, 3, 4}
b = {2, 3, 5, 6}
c = {3, 4, 6, 7}

# Comparar conjuntos
print(a == b) # False
print(a != b) # True
print(a == c) # False
print(a != c) # True

# Operacion de union |
print(a | b) # {1, 2, 3, 4, 5, 6}
print(a | c) # {1, 2, 3, 4, 6, 7}

# Operacion de interseccion &
print(a & b) # {2, 3}
print(a & c) # {3, 4}

# Operacion de diferencia -
print(a - b) # {1, 4}
print(a - c) # {1, 2}

# Operacion de diferencia simetrica ^
print(a ^ b) # {1, 4, 5, 6}
print(a ^ c) # {1, 2, 6, 7}
