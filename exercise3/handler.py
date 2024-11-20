import itertools
from typing import Dict, List, Tuple

class Atom:
    """
    ### Description
    Class to represent atomic types

    ### Attributes
    - `representation`: int, representation of the type
    - `alignment`: int, alignment of the type
    """
    def __init__(self, representation: int, alignment: int):
        self.representation: int = representation
        self.alignment: int = alignment

class Struct:
    """
    ### Description
    Class to represent structured types

    ### Attributes
    - `nombre`: str, name of the type
    - `types`: list, list of types that the structure contains
    """
    def __init__(self, name: str, types: List[str]):
        self.nombre: str = name
        self.types: List[str] = types

class Union:
    """
    ### Description
    Class to represent union types

    ### Attributes
    - `name`: str, name of the type
    - `types`: list, list of types that the union contains
    """
    def __init__(self, name: str, types: List[str]):
        self.name: str = name
        self.types: List[str] = types

atomic_types: Dict[str, Atom] = {}   # Atomic types dictionary
struct_types: Dict[str, Struct] = {}  # Struct types dictionary
union_types: Dict[str, Union] = {}   # Union types dictionary

def add_atomic_type(name: str, representation: int, alignment: int) -> bool:
    """
    ### Description
    Function to add an atomic type to the corresponding dictionary

    ### Parameters
    - `name`: str, name of the type
    - `representation`: int, representation of the type
    - `alignment`: int, alignment of the type

    ### Returns
    - `bool`, True if the type was added successfully, False otherwise
    """
    # If the type was previously defined, an error message is displayed
    if atomic_types.get(name) or struct_types.get(name) or union_types.get(name):
        print(f"El tipo {name} ya se definió previamente")
        return False
    # Otherwise, the type is added to the dictionary
    atomic_types[name] = Atom(representation, alignment)
    return True

def add_struct_type(name: str, types: List[str]) -> bool:
    """
    ### Description
    Function to add a structured type to the corresponding dictionary

    ### Parameters
    - `name`: str, name of the type
    - `types`: list, list of types that the structure contains

    ### Returns
    - `bool`, True if the type was added successfully, False otherwise
    """
    # If the type was previously defined, an error message is displayed
    if atomic_types.get(name) or struct_types.get(name) or union_types.get(name):
        print(f"{name} ya se definió previamente")
        return False
    # Otherwise, it is verified that the types of the fields are previously defined
    type_list: List[str] = []
    for type in types:
        # If any of the types is not defined, an error message is displayed
        if atomic_types.get(type) is None:
            print(f"El tipo {type} no está definido previamente")
            return False
        # Otherwise, the type is added to the list
        type_list.append(type)
    # The type is added to the dictionary
    struct_types[name] = Struct(name, type_list)
    return True

def add_union_type(union_name: str, types: List[str]) -> bool:
    """
    ### Description
    Function to add a union type to the corresponding dictionary

    ### Parameters
    - `union_name`: str, name of the type
    - `types`: list, list of types that the union contains

    ### Returns
    - `bool`, True if the type was added successfully, False otherwise
    """
    # If the type was previously defined, an error message is displayed
    if atomic_types.get(union_name) or struct_types.get(union_name) or union_types.get(union_name):
        print(f"{union_name} ya se definió previamente")
        return False
    # Otherwise, it is verified that the types of the fields are previously defined
    for type in types:
        # If any of the types is not defined, an error message is displayed
        if atomic_types.get(type) is None:
            print(f"El tipo {type} no está definido previamente")
            return False
    # The type is added to the dictionary
    union_types[union_name] = Union(union_name, types)
    return True

def describe_type(type_name: str) -> bool:
    """
    ### Description
    Function to describe a type

    ### Parameters
    - `type_name`: str, name of the type
    
    ### Returns
    - `bool`, True if the type was described successfully, False otherwise
    """
    # If the type is not previously defined, an error message is displayed
    if type_name not in union_types and type_name not in struct_types and type_name not in atomic_types:
        print(f"{type_name} no está definido previamente")
        return

    # Get the type
    type: Atom|Union|Struct = get_type(type_name)

    # If the type is atomic, it is displayed as an atomic type
    if isinstance(type, Atom):
        print(f"Tipo Atomo {type_name}")
    # If the type is a struct, it is displayed as a struct type
    elif isinstance(type, Struct):
        print(f"Tipo Struct {type_name}")
    # If the type is a union, it is displayed as a union type
    elif isinstance(type, Union):
        print(f"Tipo Union {type_name}")

    # Calculate the size and alignment of the type
    size: int = calculate_size(type)
    alignment: int = get_alignment(type)
    # Display the packed representation and alignment of the type
    print("Empaquetados:")
    print(f"Ocupacion: {size}\nAlineacion: {alignment}\nDesperdicio: 0")

    # Calculate the unpacked size and waste of the type
    size, waste = calculate_unpacked_size_and_waste(type)
    print("Sin empaquetar:")
    print(f"Ocupacion: {size + waste}\nAlineacion: {alignment}\nDesperdicio: {waste}")

    # Optimize the field order of the type
    size, waste = optimize_field_order(type)
    print("Reordenamiento de los campos de manera óptima:")
    print(f"Ocupacion: {size}\nAlineacion: {alignment}\nDesperdicio: {waste}")
    return True

def calculate_unpacked_size_and_waste(data_type: Atom|Union|Struct) -> Tuple[int, int]:
    """
    ### Description
    Function to calculate the unpacked size and waste of a type

    ### Parameters
    - `data_type`: Atom|Union|Struct, type to calculate the unpacked size and waste

    ### Returns
    - `Tuple[int, int]`, size and waste of the type
    """
    # If the type is atomic, the representation and waste are calculated
    if isinstance(data_type, Atom):
        waste: int = get_alignment(data_type) - data_type.representation
        return data_type.representation, waste
    # If the type is a union, the representation and waste of the atomic type with the highest representation are calculated
    elif isinstance(data_type, Union):
        types: List[str] = data_type.types
        type_list: List[Atom] = [atomic_types[elem] for elem in types]
        atomic_type: Atom = max(type_list, key=lambda Atomo: Atomo.representation)
        waste: int = get_alignment(atomic_type) - atomic_type.representation
        return atomic_type.representation, waste
    # If the type is structured, the size and waste of each field are calculated
    else:
        size: int = 0
        waste: int = 0
        # For each field, the size and waste are calculated
        for data_type in data_type.types:
            atomic_type: Atom = atomic_types[data_type]
            # Calculate the waste
            current_waste: int = get_alignment(atomic_type) - atomic_type.representation
            current_size: int = atomic_type.representation
            size += current_size
            waste += current_waste
        return size, waste

def optimize_field_order(field_type: Atom|Union|Struct) -> Tuple[int, int]:
    """
    ### Description
    Function to optimize the field order of a type

    ### Parameters
    - `field_type`: Atom|Union|Struct, type to optimize the field order

    ### Returns
    - `Tuple[int, int]`, size and waste of the type
    """
    # If the type is atomic, the representation and waste are calculated
    if isinstance(field_type, Atom):
        waste: int = get_alignment(field_type) - field_type.representation
        return field_type.representation, waste
    # If the type is a union, the representation and waste of the atomic type with the highest representation are calculated
    elif isinstance(field_type, Union):
        types: List[str] = field_type.types
        # Get the atomic type with the highest representation
        type_list: List[Atom] = [atomic_types[elem] for elem in types]
        # Get the atomic type with the highest representation
        max_atomic_type: Atom = max(type_list, key=lambda Atomo: Atomo.representation)
        # Calculate the waste
        waste: int = get_alignment(max_atomic_type) - max_atomic_type.representation
        return max_atomic_type.representation, waste
    # If the type is structured, the size and waste of each field are calculated
    else:
        type_permutations: List[itertools.permutations] = list(itertools.permutations(field_type.types))
        size_waste_combinations: List[Tuple[int, int]] = []
        # For each permutation of the fields, the size and waste are calculated
        for permutacion in type_permutations:
            field_type.types = permutacion
            size: int = 0
            waste: int = 0
            # For each field, the size and waste are calculated
            for current_type in field_type.types:
                current_size, current_waste = optimize_field_order(get_type(current_type))
                size += current_size
                waste += current_waste
            size_waste_combinations.append((size, waste))
        return min(size_waste_combinations)

def calculate_size(data_structure: Union|Struct) -> int:
    """
    ### Description
    Function to calculate the size of a type

    ### Parameters
    - `data_structure`: Atom|Union|Struct, type to calculate the size

    ### Returns
    - `int`, size of the type
    """
    # If the type is atomic, the representation is returned
    if isinstance(data_structure, Struct):
        # Si el objeto es estructurado, se calcula el tamaño de cada campo
        acc: int = 0
        for type in data_structure.types:
            acc += atomic_types.get(type).representation
        return acc
    elif isinstance(data_structure, Union):
        # Si el objeto es de unión, se obtiene el tipo atómico de mayor representación
        type_representation_list: List[int] = [atomic_types.get(tipo).representation for tipo in data_structure.types]
        return max(type_representation_list)
    else:
        return data_structure.representation

def get_type(type_name: str) -> Atom|Union|Struct|None:
    """
    ### Description
    Function to get the type information

    ### Parameters
    - `type_name`: str, name of the type

    ### Returns
    - `Atom|Union|Struct`, type information
    - `None`, if the type is not defined
    """
    # If the type is atomic, it is returned
    if type_name in atomic_types:
        return atomic_types[type_name]
    # If the type is structured, it is returned
    elif type_name in struct_types:
        return struct_types[type_name]
    # If the type is a union, it is returned
    elif type_name in union_types:
        return union_types[type_name]
    # Otherwise, an error message is displayed
    else:
        print(f"{type_name} no está definido")
        return None

def compute_lcm_list(number_list: List[int]) -> int:
    """
    ### Description
    Function to compute the least common multiple of a list of numbers

    ### Parameters
    - `number_list`: List[int], list of numbers

    ### Returns
    - `int`, least common multiple of the numbers
    """
    # If the list has only one element, the element is returned
    if len(number_list) == 1:
        return number_list[0]
    i = 1
    # Calculate the least common multiple of the first two elements
    current_lcm: int = lcm(number_list[0], number_list[1])
    # While there are more elements in the list, the least common multiple is calculated
    while i < len(number_list) - 1:
        current_lcm = lcm(current_lcm, number_list[i + 1])
        i += 1
    return current_lcm

def gcd(a: int, b: int) -> int:
    """
    ### Description
    Function to calculate the greatest common divisor of two numbers

    ### Parameters
    - `a`: int, first number
    - `b`: int, second number

    ### Returns
    - `int`, greatest common divisor of the numbers
    """
    current_b: int = 0
    # While the second number is not zero, the greatest common divisor is calculated
    while b != 0:
        current_b = b
        b = a % b
        a = current_b
    return a

def lcm(a: int, b: int) -> int:
    """
    ### Description
    Function to calculate the least common multiple of two numbers

    ### Parameters
    - `a`: int, first number
    - `b`: int, second number

    ### Returns
    - `int`, least common multiple of the numbers
    """
    return int((a * b) / gcd(a, b))

def get_alignment(type_info: Atom|Union|Struct) -> int:
    """
    ### Description
    Function to get the alignment of a type

    ### Parameters
    - `type_info`: Atom|Union|Struct, type information

    ### Returns
    - `int`, alignment of the type
    """
    # If the type is atomic, the alignment is returned
    if isinstance(type_info, Atom):
        return type_info.alignment
    # If the type is a union, the alignment of the atomic type with the highest representation
    elif isinstance(type_info, Union):
        types: List[str] = type_info.types
        alignment_list: List[Atom] = [atomic_types[elem].alignment for elem in types]
        return compute_lcm_list(alignment_list)
    # If the type is structured, the alignment of the atomic type with the highest alignment is returned
    else:
        types: List[str] = type_info.types
        return atomic_types[types[0]].alignment
