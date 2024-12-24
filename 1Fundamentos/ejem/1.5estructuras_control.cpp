#include <iostream>

int main() {
    int x=10;

    std::cout << "El numero es: " << x << std::endl;
    if (x>5) {
        std::cout << "x es mayor que 0" << std::endl;
    } else {
        std::cout << "x es menor que 0" << std::endl;
    }

    switch (x) {
        case 10:
            std::cout << "x es 10" << std::endl;
            break;
        default:
            std::cout << "x no es 10" << std::endl;
    }

    return 0;
}