#include <stdio.h>

// Section formula for a point dividing line AB in ratio m:n
void section_formula(float *P, float *A, float *B, int m, int n, int k) {
    for (int i = 0; i < k; i++) {
        P[i] = (m * B[i] + n * A[i]) / (float)(m + n);
    }
}

// Area of triangle given 3 points in 2D
float triangle_area(float *A, float *B, float *C) {
    float det = (B[0] - A[0]) * (C[1] - A[1]) - 
                (B[1] - A[1]) * (C[0] - A[0]);
    if (det < 0) det = -det;
    return 0.5f * det;
}

int main() {
    // Example points
    float A[2] = {2, -4};
    float B[2] = {3, 8};
    float C[2] = {-10, -3};

    // Use section formula (divide AB in ratio 2:3)
    float P[2];
    section_formula(P, A, B, 2, 3, 2);

    printf("Point dividing AB in ratio 2:3 is: (%.2f, %.2f)\n", P[0], P[1]);

    // Compute area of triangle ABC
    float area = triangle_area(A, B, C);
    printf("Area of triangle ABC is: %.2f\n", area);

    return 0;
}
