# Remote Git exercise: two-integer addition

A small C++ command-line exercise kept as an example of a project stored in a remote Git repository. The program in [`add.cpp`](add.cpp) reads **two integers** from standard input and prints their sum. This is a learning exercise, not a general-purpose calculator or a substantial software system.

## Run it

Requires a C++17 compiler (the examples use `g++`). From the repository root:

```sh
g++ -std=c++17 -Wall -Wextra -pedantic add.cpp -o add
printf '2 3\n' | ./add
# the addition result = 5
```

The original successful output format is preserved. The revised program reports missing or invalid operands to standard error and exits unsuccessfully. It widens the two `int` operands before addition so their sum does not overflow a signed `int`.

## Verify

With Python 3 and `g++` installed:

```sh
python3 -m unittest discover -s tests -v
```

The tests compile the source with strict warnings and check positive, negative, boundary, and invalid inputs. They do not test a Git remote workflow; the repository's name describes its exercise context, not a feature implemented by the C++ program.

## Repository map and limits

- [`add.cpp`](add.cpp): complete program.
- [`tests/test_add.py`](tests/test_add.py): executable command-line checks.
- [`Mohamed.txt`](Mohamed.txt): empty file retained from the original repository; its purpose and authorship are not documented.

The application handles exactly two `int` operands; it does not parse expressions, support arbitrary-precision integers, or demonstrate Git networking commands. Its educational scope is intentionally narrow.
