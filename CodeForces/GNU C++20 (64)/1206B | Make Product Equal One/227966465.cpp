#include <iostream>
#include <vector>
 
int main() {
    int n;
    std::cin >> n;
    std::vector<long long> arr(n);
    int pos = 0, neg = 0, zero = 0;
    long long op = 0;
 
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
        if (arr[i] < 0) {
            neg++;
            op += -arr[i] - 1;
        } else if (arr[i] > 0) {
            pos++;
            op += arr[i] - 1;
        } else {
            zero++;
        }
    }
 
    if (neg % 2 == 1 && zero == 0) {
        op += 2;
    } else if (zero > 0) {
        op += zero;
    }
 
    std::cout << op << std::endl;
 
    return 0;
}