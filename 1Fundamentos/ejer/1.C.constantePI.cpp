// Problema: Declara una constante de tipo `float` para a
// lmacenar el valor de pi, calcula el área de un círculo
// con un radio dado y muestra el resultado.

#include <iostream>

using namespace std;

int main() {
    const float pi = 3.14159;
    int r;
    cin >> r;
    cout << pi * r * r << endl;

    return 0;
}
