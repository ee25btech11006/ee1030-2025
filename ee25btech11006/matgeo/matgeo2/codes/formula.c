#include <stdio.h>
#include <math.h>

// Function to calculate discriminant
int getDiscriminant(int a, int b, int c) {
    return b * b - 4 * a * c;
}

// Function to find roots of quadratic equation
void findRoots(int a, int b, int discrim, int *y1, int *y2) {
    *y1 = (-b + (int)sqrt(discrim)) / (2 * a);
    *y2 = (-b - (int)sqrt(discrim)) / (2 * a);
}

// Function to calculate distance between two points
double getDistance(int x1, int y1, int x2, int y2) {
    return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}

int main() {
    int Ax = 2, Ay = -4;
    int Px = 3, Py = 8;
    int Qx = -10;

    // From equation ||A-P||^2 = ||A-Q||^2
    int a = 1, b = 8, c = 15;
    int discrim = getDiscriminant(a, b, c);

    int y1, y2;
    findRoots(a, b, discrim, &y1, &y2);

    // Calculate distances
    double d1 = getDistance(Px, Py, Qx, y1);
    double d2 = getDistance(Px, Py, Qx, y2);

    printf("Roots: y1 = %d, y2 = %d\n", y1, y2);
    printf("Distances: d1 = %.2f, d2 = %.2f\n", d1, d2);

    return 0;
}
