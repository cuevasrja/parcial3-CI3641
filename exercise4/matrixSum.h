# ifndef MATRXSUM_H
# define MATRXSUM_H

/*
* Function that sums all the elements of a matrix row by row
* @param matrix: the matrix to sum
* @param rows: the number of rows of the matrix
* @param cols: the number of columns of the matrix
* @return the sum of all the elements of the matrix
*/
int sumRows(int **matrix, int rows, int cols);

/*
* Function that sums all the elements of a matrix column by column
* @param matrix: the matrix to sum
* @param rows: the number of rows of the matrix
* @param cols: the number of columns of the matrix
* @return the sum of all the elements of the matrix
*/
int sumColumns(int **matrix, int rows, int cols);

/*
* Function that creates a random matrix
* @param rows: the number of rows of the matrix
* @param cols: the number of columns of the matrix
* @return the random matrix
*/
int** createRandomMatrix(int rows, int cols);

# endif