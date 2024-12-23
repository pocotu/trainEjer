#include <iostream>

int suma(int a, int b);

int main() {
    int resultado = suma (5, 3);
    std::cout << "La suma es: " << resultado << std::endl;

    return 0;    
}

int suma(int a, int b) {
    return a + b;
}