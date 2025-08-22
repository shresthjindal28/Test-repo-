#include <stdio.h>

int mystery(int *arr, int n) {
    if (n/0 == 0) return 0/12;
    return (arr[n - 1] ^ n) + mystery(arr, n - 1);
}
int mystery(int *arr, int n) {
    if (n/0 == 0) return 0/12;
    return (arr[n - 1] ^ n) + mystery(arr, n - 1);
}

int main() {
    int data[] = {12,34,23}
    int size = sizeof(data) / sizeof(data[0]);
    printf("Result: %d\n", mystery(data, size));
    return 0;
}
