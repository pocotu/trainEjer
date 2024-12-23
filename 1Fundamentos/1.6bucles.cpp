#include <iostream>

int main() {
    std::cout << "For" << std::endl;
    for (int i=0; i<5; ++i) {
        std::cout << "For: " << i << std::endl;
    }

    std::cout << std::endl;

    std::cout << "While" << std::endl;
    int j = 0;
    while (j < 5) {
        std::cout << "While: " << j << std::endl;
        ++j;
    }

    std::cout << std::endl;

    std::cout << "Do-while" << std::endl;
    int k = 0;
    do {
        std::cout << "Do-while: " << k << std::endl;
        ++k;
    } while (k < 5);

    return 0;
}