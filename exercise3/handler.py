import itertools

# Implementación del manejador de tipos de datos
atomic_types = {}   # Diccionario para tipos atómicos
struct_types = {}  # Diccionario para tipos estructurados
union_types = {}   # Diccionario para tipos de unión

# Definición de la clase para tipos atómicos
class Atomo:
    def __init__(self, representation, alignment):
        self.representation = representation
        self.alignment = alignment

# Definición de la clase para tipos estructurados
class Struct:
    def __init__(self, name: str, types: str):
        self.nombre = name
        self.types = types

# Definición de la clase para tipos de unión
class Union:
    def __init__(self, name: str, types: str):
        self.name = name
        self.types = types

# Función para agregar un tipo atómico al diccionario correspondiente
def add_atomic_type(name, representation, alignment):
    # Si el tipo ya se definió previamente, se muestra un mensaje de error
    if atomic_types.get(name) or struct_types.get(name) or union_types.get(name):
        print(f"El tipo {name} ya se definió previamente")
        return False
    # Caso contrario, se agrega el tipo al diccionario
    atomic_types[name] = Atomo(representation, alignment)
    return True

# Función para agregar un tipo estructurado al diccionario correspondiente
def add_struct_type(name, types):
    # Si el tipo ya se definió previamente, se muestra un mensaje de error
    if atomic_types.get(name) or struct_types.get(name) or union_types.get(name):
        print(f"{name} ya se definió previamente")
        return False
    # Caso contrario, se verifica que los tipos de los campos estén definidos previamente
    type_list = []
    for type in types:
        # Si alguno de los tipos no está definido, se muestra un mensaje de error
        if atomic_types.get(type) is None:
            print(f"El tipo {type} no está definido previamente")
            return False
        # Caso contrario, se agrega el tipo a la lista de tipos
        type_list.append(type)
    # Se agrega el tipo al diccionario
    struct_types[name] = Struct(name, type_list)
    return True

# Función para agregar un tipo de unión al diccionario correspondiente
def add_union_type(union_name, types):
    # Si el tipo ya se definió previamente, se muestra un mensaje de error
    if atomic_types.get(union_name) or struct_types.get(union_name) or union_types.get(union_name):
        print(f"{union_name} ya se definió previamente")
        return False
    # Caso contrario, se verifica que los tipos de los campos estén definidos previamente
    for type in types:
        # Si alguno de los tipos no está definido, se muestra un mensaje de error
        if atomic_types.get(type) is None:
            print(f"El tipo {type} no está definido previamente")
            return False
    # Se agrega el tipo al diccionario
    union_types[union_name] = Union(union_name, types)
    return True

# Función para describir un tipo
def describe_type(type_name):
    # Si el tipo no está definido, se muestra un mensaje de error
    if type_name not in union_types and type_name not in struct_types and type_name not in atomic_types:
        print(f"{type_name} no está definido previamente")
        return

    # Se obtiene el tipo
    type = get_type(type_name)

    # Se muestra el tipo
    if isinstance(type, Atomo):
        print(f"Tipo Atomo {type_name}")
    elif isinstance(type, Struct):
        print(f"Tipo Struct {type_name}")
    elif isinstance(type, Union):
        print(f"Tipo Union {type_name}")

    # Se muestra la representación y alineación del tipo
    size = calculate_size(type)
    alignment = get_alignment(type)
    # En el caso de empacaquetados, el desperdicio es 0
    print("Empaquetados:")
    print(f"Ocupacion: {size}\nAlineacion: {alignment}\nDesperdicio: 0")

    # Se muestra la representación y alineación del tipo sin empaquetar
    size, waste = calculate_unpacked_size_and_waste(type)
    print("Sin empaquetar:")
    print(f"Ocupacion: {size + waste}\nAlineacion: {alignment}\nDesperdicio: {waste}")

    # Se muestra la representación y alineación del tipo reordenado
    size, waste = optimize_field_order(type)
    print("Reordenamiento de los campos de manera óptima:")
    print(f"Ocupacion: {size}\nAlineacion: {alignment}\nDesperdicio: {waste}")
    return True

# Función para obtener el espacio y desperdicio sin empaquetar de un tipo
def calculate_unpacked_size_and_waste(data_type):
    # Si el tipo es atómico, se devuelve su representación y desperdicio
    # el cual se calcula como la alineación del tipo menos su representación
    if isinstance(data_type, Atomo):
        waste = get_alignment(data_type) - data_type.representation
        return data_type.representation, waste
    # Si el tipo es de unión, se obtiene el tipo atómico de mayor representación
    elif isinstance(data_type, Union):
        types = data_type.types
        type_list = [atomic_types[elem] for elem in types]
        atomic_type = max(type_list, key=lambda Atomo: Atomo.representation)
        waste = get_alignment(atomic_type) - atomic_type.representation
        return atomic_type.representation, waste
    else:
        # Si el tipo es estructurado, se calcula el tamaño y desperdicio de cada campo
        size = 0
        waste = 0
        for data_type in data_type.types:
            atomic_type = atomic_types[data_type]
            current_waste = get_alignment(atomic_type) - atomic_type.representation
            current_size = atomic_type.representation
            size += current_size
            waste += current_waste
        return size, waste

# Función para reordenar campos de manera óptima
def optimize_field_order(field_type):
    # Si el tipo es atómico, se devuelve su representación y desperdicio
    if isinstance(field_type, Atomo):
        waste = get_alignment(field_type) - field_type.representation
        return field_type.representation, waste
    # Si el tipo es de unión, se obtiene el tipo atómico de mayor representación
    elif isinstance(field_type, Union):
        types = field_type.types
        type_list = [atomic_types[elem] for elem in types]
        max_atomic_type = max(type_list, key=lambda Atomo: Atomo.representation)
        waste = get_alignment(max_atomic_type) - max_atomic_type.representation
        return max_atomic_type.representation, waste
    # Si el tipo es estructurado, se calcula el tamaño y desperdicio de cada campo
    else:
        type_permutations = list(itertools.permutations(field_type.types))
        size_waste_combinations = []
        for permutacion in type_permutations:
            field_type.types = permutacion
            size = 0
            waste = 0
            for current_type in field_type.types:
                current_size, current_waste = optimize_field_order(get_type(current_type))
                size += current_size
                waste += current_waste
            size_waste_combinations.append((size, waste))
        return min(size_waste_combinations)

# Función para obtener el espacio de un objeto
def calculate_size(data_structure):
    # Si el objeto es atómico, se devuelve su representación
    if isinstance(data_structure, Struct):
        # Si el objeto es estructurado, se calcula el tamaño de cada campo
        acc = 0
        for type in data_structure.types:
            acc += atomic_types.get(type).representation
        return acc
    elif isinstance(data_structure, Union):
        # Si el objeto es de unión, se obtiene el tipo atómico de mayor representación
        type_representation_list = [atomic_types.get(tipo).representation for tipo in data_structure.types]
        return max(type_representation_list)
    else:
        return data_structure.representation

# Función para obtener el tipo asociado a un nombre
def get_type(type_name):
    # Si el nombre está definido, se devuelve el tipo asociado
    if type_name in atomic_types:
        return atomic_types[type_name]
    elif type_name in struct_types:
        return struct_types[type_name]
    elif type_name in union_types:
        return union_types[type_name]
    else:
        print(f"{type_name} no está definido")
        return None

# Función para calcular el MCM de una lista de números
def compute_lcm_list(number_list):
    # Si la lista es vacía, se devuelve 0
    if len(number_list) == 1:
        return number_list[0]
    i = 1
    # Se calcula el MCM de los dos primeros elementos
    current_lcm = lcm(number_list[0], number_list[1])
    while i < len(number_list) - 1:
        current_lcm = lcm(current_lcm, number_list[i + 1])
        i += 1
    return current_lcm

# Función para calcular el MCD de dos números
def gcd(a, b):
    # Se calcula el MCD de dos números usando el algoritmo de Euclides
    current_b = 0
    while b != 0:
        current_b = b
        b = a % b
        a = current_b
    return a

# Función para calcular el MCM de dos números
def lcm(a, b):
    # Se calcula el MCM de dos números usando la propiedad de que
    # el MCM de dos números es igual al producto de los dos números
    # dividido entre el MCD de los dos números
    return int((a * b) / gcd(a, b))

# Función para obtener la alineación de un tipo
def get_alignment(type_info) -> int:
    # Si el tipo es atómico, se devuelve su alineación
    if isinstance(type_info, Atomo):
        return type_info.alignment
    elif isinstance(type_info, Union):
        # Si el tipo es de unión, se obtiene el tipo atómico de mayor representación
        types = type_info.types
        alignment_list = [atomic_types[elem].alignment for elem in types]
        return compute_lcm_list(alignment_list)
    else:
        # Si el tipo es estructurado, se calcula la alineación de cada campo
        types = type_info.types
        return atomic_types[types[0]].alignment
