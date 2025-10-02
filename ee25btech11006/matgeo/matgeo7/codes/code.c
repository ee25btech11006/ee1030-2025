#include <stdio.h>

int main() {
    // Vectors
    double a1 = 3, a2 = -6, a3 = 1;   // Vector A
    double b1 = 2, b2 = -4, b3;       // Vector B, lambda is unknown

    // Scalar multiple t from first component
    double t = b1 / a1;

    // Calculate lambda
    b3 = t * a3;

    printf("Vector A = (%.1f, %.1f, %.1f)\n", a1, a2, a3);
    printf("Vector B = (%.1f, %.1f, lambda)\n", b1, b2);
    printf("\nSince B is parallel to A:\n");
    printf("B = t*A with t = %.2f\n", t);
    printf("=> lambda = %.2f\n", b3);

    return 0;
}