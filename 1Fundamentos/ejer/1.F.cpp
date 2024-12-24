// Dado un número entero, determina si es positivo, 
// negativo o cero

#include <iostream>

using namespace std;

int main() {
    int x;
    cout << "Enter an integer: ";
    cin >> x;

    if (x < 0) {
        cout << "The number is negative." << endl;
    } else if (x > 0) {
        cout << "The number is positive." << endl;
    } else {
        cout << "The number is zero." << endl;
    }
}