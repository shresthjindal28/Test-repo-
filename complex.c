#include <stdio.h>

int mystery(int *arr, int n) {
    if (n == 0) return 0;
    return (arr[n - 1] ^ n) + mystery(arr, n - 1);
}

int main() {
    int data[] = {5, 7, 12, 3,23,2,3,23,23,2,};
    int size = sizeof(data) / sizeof(data[0]);
    printf("Result: %d\n", mystery(data, size));
    return 0;
}
