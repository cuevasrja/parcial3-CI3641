import handler
import sys


def menu():
    print("\033[1;92mMenu\033[0m")
    print("\033[92mATOMICO\033[0m <nombre> <representación> <alineación>")
    print("\033[92mSTRUCT\033[0m <nombre> [<tipo>]")
    print("\033[92mUNION\033[0m <nombre> [<tipo>]")
    print("\033[92mDESCRIBIR\033[0m <nombre>")
    print("\033[92mSALIR\033[0m")

continue_loop = True

# Main loop
while continue_loop:
    # Print menu
    menu()
    # Read command
    command = input("> ")

    # Check if command is empty
    if command == '':
        continue

    # Split command
    args = command.split()

    # If command is "salir" then exit
    if args[0].lower() == "salir":
        continue_loop = False
    # If command is "atomico" then add atomic type
    elif args[0].lower() == "atomico":

        if len(args) < 4:
            print("Accion invalida")
        else:
            type_name = args[1]
            representation_value = int(args[2])
            alignment = int(args[3])

            handler.add_atomic_type(type_name, representation_value, alignment)
    # If command is "struct" then add struct type
    elif args[0].lower() == "struct":
        if len(args) < 3:
            print("Accion invalida")
        else:
            type_name = args[1]
            type_list = args[2:]
            handler.add_struct_type(type_name, type_list)
    # If command is "union" then add union type
    elif args[0].lower() == "union":
        if len(args) < 3:
            print("Accion invalida")
        else:
            type_name = args[1]
            type_list = args[2:]
            handler.add_union_type(type_name, type_list)
    # If command is "describir" then describe type
    elif args[0].lower() == "describir":
        if len(args) != 2:
            print("Accion invalida")
        else:
            type_name = args[1]
            handler.describe_type(type_name)
    # Else print invalid action
    else:
        print("Accion invalida")