# include <stdio.h>  // funcion printf
# include <time.h>   // funcion clock
# include <stdlib.h> // funcion free

# include "matrixSum.h"


/*
* Function that measures the time of a function
* @param attemp: the number of the attemp
* @param matrix: the matrix to sum
* @param rows: the number of rows of the matrix
* @param cols: the number of columns of the matrix
* @param function: the function to measure
* @param operation: the operation to measure
*/
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
    // Array with the sizes of the matrices
    int sizes[5] = {100, 1000, 10000, 100000, 1000000};
    int atemps = 3;

    // Check the time of the functions
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            int rows = sizes[i];
            int cols = sizes[j];
            // Skip some cases that was proved don't finish
            if ((rows >= 100 && cols == 1000000) || (rows == 10000 && cols == 100000) || (rows == 100000 && cols >= 10000) || (rows == 1000000 && cols >= 1000)){
                continue;
            }
            // Create the matrix and measure the time 3 times
            for(int k = 0; k < atemps; k++){
                int **matrix = createRandomMatrix(rows, cols);
                measureTime(k, matrix, rows, cols, sumRows, 0);
                measureTime(k, matrix, rows, cols, sumColumns, 1);
                free(matrix);
            }
        }
    }
}