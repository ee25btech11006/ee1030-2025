#include <stdio.h>
#include <math.h>

// Function to compute the radius of required circle
double find_radius(double g, double f, double c) {
    return sqrt(g*g + f*f - c);
}

// Function to compute f (from tangency condition)
double find_f(double g) {
    // From condition: g^2 + f^2 = (1.5)^2 = 9/4
    return sqrt(9.0/4.0 - g*g);
}

// Function to print circle center and radius
void print_circle(double g, double f, double c) {
    double h = -g;
    double k = -f;
    double r = find_radius(g, f, c);
    printf("Center : (%.2f , %.2f)\n", h, k);
    printf("Radius : %.2f\n\n", r);
}

int main() {
    // Given circle: x^2 + y^2 = 9
    double r1 = 3.0; // radius of given circle
    double c1x = 0.0, c1y = 0.0; // center of given circle

    // Required circle passes through (0,0) and (1,0)
    // Equation: x^2 + y^2 + 2gx + 2fy + c = 0
    // From (0,0): c = 0
    // From (1,0): 1 + 2g(1) = 0 -> g = -1/2
    double g = -0.5;
    double c = 0.0;

    // From tangency condition: internal touch with x^2 + y^2 = 9
    double f = find_f(g);   // +√2
    double f_neg = -find_f(g); // -√2

    printf("Centers of the required circles:\n\n");

    print_circle(g, f, c);      // Circle 1: (1/2, -√2)
    print_circle(g, f_neg, c);  // Circle 2: (1/2, +√2)

    return 0;
}