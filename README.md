# CF_Solver

This script performs autonomous testing on given tests in any codeforces problem !


## Usage

```
$ python3 CF_test.py --help
usage: CF_test.py [-h] code_path problem

This tool automates the test cases in a given problem from codeforces

positional arguments:
  code_path   Path of the c++ code
  problem     Problem code , ex: 677/A

optional arguments:
  -h, --help  show this help message and exit
```
________________
## Examples
* Accepeted Solution
```
$ python3 CF_test.py ~/Problem-Solving/CF/main.cpp 734/A

Compiled Successfully
Accepted, you are a Super HERO <3
Test Number 1 Passed, Input : 6 ADAAAA , Expected : Anton , Result : Anton
Test Number 2 Passed, Input : 7 DDDAADA , Expected : Danik , Result : Danik
Test Number 3 Passed, Input : 6 DADADA , Expected : Friendship , Result : Friendship
```

* Rejected Solution
```
$ python3 CF_test.py ../Problem-Solving/CF-734A/main.cpp 734/A

Compiled Successfully
Failed, you are a Big Dump IDIOT!!!!!!
Test Number 1 Failed, Input : 6 ADAAAA , Expected : Anton , Result : Friendship
Test Number 2 Failed, Input : 7 DDDAADA , Expected : Danik , Result : Anton
Test Number 3 Passed, Input : 6 DADADA , Expected : Friendship , Result : Friendship
```
