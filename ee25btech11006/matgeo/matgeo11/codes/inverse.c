#include <stdio.h>
#define N 2

int inverse(double A[N][N], double inv[N][N]) {
    double aug[N][2*N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            aug[i][j] = A[i][j];
            aug[i][j+N] = (i == j) ? 1 : 0;
        }
    }

    for (int i = 0; i < N; i++) {
        double pivot = aug[i][i];
        if (pivot == 0) {
            printf("Matrix is singular (no inverse).\n");
            return -1;
        }
        for (int j = 0; j < 2*N; j++) {
            aug[i][j] /= pivot;
        }
        for (int k = 0; k < N; k++) {
            if (k != i) {
                double factor = aug[k][i];
                for (int j = 0; j < 2*N; j++) {
                    aug[k][j] -= factor * aug[i][j];
                }
            }
        }
    }

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            inv[i][j] = aug[i][j+N];
    return 0;
}