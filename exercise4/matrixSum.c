#include <stdlib.h>

int sumRows(int **matrix, int rows, int cols){
    int sum = 0;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            sum += matrix[i][j];
        }
    }
    return sum;
}

int sumColumns(int **matrix, int rows, int cols){
    int sum = 0;
    for(int i = 0; i < cols; i++){
        for(int j = 0; j < rows; j++){
            sum += matrix[j][i];
        }
    }
    return sum;
}

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