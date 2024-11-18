import handler
import sys

while True:

    print("USO:")
    print("ATOMICO <nombre> <representación> <alineación>")
    print("STRUCT <nombre> [<tipo>]")
    print("UNION <nombre> [<tipo>]")
    print("DESCRIBIR <nombre>")

    print("SALIR")
    command = input("> ")

    if command == '':
        continue

    args = command.split()

    if args[0].lower() == "salir":
        sys.exit()
    elif args[0].lower() == "atomico":

        if len(args) < 4:
            print("Accion invalida")
        else:
            type_name = args[1]
            representation_value = int(args[2])
            alignment = int(args[3])

            handler.add_atomic_type(type_name, representation_value, alignment)
    elif args[0].lower() == "struct":

        if len(args) < 3:
            print("Accion invalida")
        else:
            type_name = args[1]
            type_list = args[2:]
            handler.add_struct_type(type_name, type_list)

    elif args[0].lower() == "union":

        if len(args) < 3:
            print("Accion invalida")
        else:
            type_name = args[1]
            type_list = args[2:]
            handler.add_union_type(type_name, type_list)

    elif args[0].lower() == "describir":

        if len(args) != 2:
            print("Accion invalida")
        else:
            type_name = args[1]
            handler.describe_type(type_name)


    else:
        print("Accion invalida")