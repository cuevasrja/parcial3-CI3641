# Estructura de archivos
#       main.c
#         |
#         |
#       matrixSum.h/.c

# Compilador
CC = gcc

# Opciones de compilación
CFLAGS = -Wall -Wextra -Werror

# Dependencias
DEPS = matrixSum.h

# Objetivo
TARGET = main.out

.PHONY: all clean run

# Regla de construcción
$(TARGET): main.o matrixSum.o
	$(CC) $(CFLAGS) -o $@ $^
	rm -f *.o

# Regla de construcción
main.o: main.c $(DEPS)
	$(CC) $(CFLAGS) -c $<

# Regla de construcción
matrixSum.o: matrixSum.c $(DEPS)
	$(CC) $(CFLAGS) -c $<

# Regla de limpieza
clean:
	rm -f *.o $(TARGET)

# Regla de ejecución
run:
	./$(TARGET)
