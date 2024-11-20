#include <stdlib.h>

/*
* Function that sums all the elements of a matrix row by row
* @param matrix: the matrix to sum
* @param rows: the number of rows of the matrix
* @param cols: the number of columns of the matrix
* @return the sum of all the elements of the matrix
*/
int sumRows(int **matrix, int rows, int cols){
    int sum = 0;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            sum += matrix[i][j];
        }
    }
    return sum;
}

/*
* Function that sums all the elements of a matrix column by column
* @param matrix: the matrix to sum
* @param rows: the number of rows of the matrix
* @param cols: the number of columns of the matrix
* @return the sum of all the elements of the matrix
*/
int sumColumns(int **matrix, int rows, int cols){
    int sum = 0;
    for(int i = 0; i < cols; i++){
        for(int j = 0; j < rows; j++){
            sum += matrix[j][i];
        }
    }
    return sum;
}

/*
* Function that creates a random matrix
* @param rows: the number of rows of the matrix
* @param cols: the number of columns of the matrix
* @return the random matrix
*/
int** createRandomMatrix(int rows, int cols){
    int** matrix = (int**) malloc(rows * sizeof(int*));
    for(int i = 0; i < rows; i++){
        matrix[i] = (int*) malloc(cols * sizeof(int));
        for(int j = 0; j < cols; j++){
            matrix[i][j] = rand() % 10;
        }
    }
    return matrix;
}