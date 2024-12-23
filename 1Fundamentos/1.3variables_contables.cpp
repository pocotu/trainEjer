#include <iostream>

int main() {
    int variable = 10;
    const int CONSTANTE = 20;

    variable = 15; //se puede cambiar el valor

    std::cout << "Variable: " << variable << std::endl;
    std::cout << "Constante: " << CONSTANTE << std::endl;

    return 0;
}