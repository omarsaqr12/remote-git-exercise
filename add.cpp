#include <iostream>

int main() {
    int left = 0;
    int right = 0;
    if (!(std::cin >> left >> right)) {
        std::cerr << "Expected two integers.\n";
        return 1;
    }

    // Widen before addition so adding two valid int values cannot overflow.
    const long long sum = static_cast<long long>(left) + right;
    std::cout << "the addition result = " << sum << '\n';
    return 0;
}
