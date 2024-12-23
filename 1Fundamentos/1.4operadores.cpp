#include <iostream>

int main() {
    int a=10, b=20;

    std::cout << "Operadores aritmeticos" << std::endl;
    std::cout << "a + b = " << (a+b) << std::endl;
    std::cout << "a - b = " << (a-b) << std::endl;

    std::cout << std::endl;
    
    std::cout << "Operadores logicos" << std::endl;
    std::cout << "(a<b) && (a>5) = " << ((a<b) && (a>5)) << std::endl;

    std::cout << std::endl;

    std::cout << "Operadores relacionales" << std::endl;
    std::cout << "a==b = " << (a == b) << std::endl;

    return 0;
}