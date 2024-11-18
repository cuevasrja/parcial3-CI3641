# include <stdio.h>  // funcion printf
# include <time.h>   // funcion clock
# include <stdlib.h> // funcion free

# include "matrixSum.h"


void measureTime(int attemp, int **matrix, int rows, int cols, int (*function)(int**, int, int), int operation){
    clock_t start, end;
    double cpu_time_used;
    start = clock();
    function(matrix, rows, cols);
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("%d, %d, %d, %f, %d\n", rows, cols, attemp+1, cpu_time_used, operation);
}

int main(){
    int sizes[5] = {100, 1000, 10000, 100000, 1000000};
    int atemps = 3;

    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            int rows = sizes[i];
            int cols = sizes[j];
            if (rows*cols >= 100000000 || (rows >= 100000 && cols >= 1000)) continue;
            for(int k = 0; k < atemps; k++){
                int **matrix = createRandomMatrix(rows, cols);
                measureTime(k, matrix, rows, cols, sumRows, 0);
                measureTime(k, matrix, rows, cols, sumColumns, 1);
                free(matrix);
            }
        }
    }
}