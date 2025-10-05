#include <stdio.h>

// Function to compute lambda for intersection with XY plane
double computeLambda(double Az, double mz) {
    return -Az / mz;
}

// Function to compute X-coordinate of intersection
double xIntersect(double Ax, double mx, double lambda) {
    return Ax + lambda * mx;
}

// Function to compute Y-coordinate of intersection
double yIntersect(double Ay, double my, double lambda) {
    return Ay + lambda * my;
}

// Function to compute Z-coordinate of intersection (XY plane)
double zIntersect() {
    return 0; // Z = 0 for XY plane
}

int main() {
    // Given points A and B
    double Ax = 3, Ay = 4, Az = 1;
    double Bx = 5, By = 1, Bz = 6;

    // Direction vector m = B - A
    double mx = Bx - Ax;
    double my = By - Ay;
    double mz = Bz - Az;

    // Compute lambda
    double lambda = computeLambda(Az, mz);

    // Compute intersection coordinates
    double X = xIntersect(Ax, mx, lambda);
    double Y = yIntersect(Ay, my, lambda);
    double Z = zIntersect();

    // Print result
    printf("Intersection with XY plane: (%.2lf, %.2lf, %.2lf)\n", X, Y, Z);

    return 0;
}