#include <iostream>

#pragma pack(4)
struct A {
    uint8_t m1;
    double m2;
};
#pragma pack()

#pragma pack(8)
struct B {
    uint8_t m1;
    double m2;
};
#pragma pack()

void printBinary(unsigned int value) {
    for (int i = 31; i >= 0; --i) {
        std::cout << ((value >> i) & 1);
    }
    std::cout << std::endl;
}

int main() {
    A a;
    B b;
    sizeof(a);
    sizeof(b);
    //
    float f_raw = -0.1f;
    uint8_t uint8 = f_raw / 10.f;
    int8_t int8 = f_raw / 10.f;
    printBinary(uint8);
    printBinary(int8);

    return 0;
}