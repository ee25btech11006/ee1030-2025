// rectangle_solver.c
void calculate_dimensions(float perimeter, float difference, float* length, float* breadth) {
    /*
      Given:
      P = 2 × (L + B)
      D = L - B

      Solving:
      L + B = P / 2
      L = B + D

      Substitute:
      (B + D) + B = P / 2 → 2B + D = P / 2 → B = ((P / 2) - D) / 2
      Then: L = B + D
    */
    *breadth = ((perimeter / 2) - difference) / 2;
    *length = *breadth + difference;
}