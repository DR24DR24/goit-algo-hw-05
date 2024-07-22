# goit-algo-hw-05

# Comparison of three substring search functions in a string

## Introduction

This report contains the results of testing three different substring search algorithms in a string:
1. "KMP (Knuth-Morris-Pratt)" search
2. "Boyer-Moore" search
3. "Rabin-Karp" search

For each test, various patterns and texts with different numbers of repetitions were used. The goal of the testing is to determine the performance of each algorithm.

## Description of algorithms

1. **"KMP (Knuth-Morris-Pratt)" search**:
   - This algorithm uses preprocessing of the pattern to create a partial match array. It allows avoiding re-comparison of characters, resulting in linear time complexity in the worst case.
  
2. **"Boyer-Moore" search**:
   - This algorithm searches for the substring using shift heuristics, making it very efficient in practice, especially for long patterns. On average, its runtime is better than KMP.
   
3. **"Rabin-Karp" search**:
   - This algorithm uses hashing to compare substrings. On average, it shows good performance, but in the worst case, it can be slower due to hash collisions.

## Test results

For each test, three indicators are provided:
- Runtime of "KMP" search.
- Runtime of "Boyer-Moore" search and its ratio to "KMP" search.
- Runtime of "Rabin-Karp" search and its ratio to "KMP" search.

## Tests

### Test 1

- **Pattern**: "системах. Наявність"
- **Text**: "Методи та структури даних для реалізації бази даних рекомендаційної системи соці"
- **Repetitions**: 100

| Algorithm         | Runtime (sec)             | Ratio to "KMP"   |
|-------------------|--------------------------|------------------|
| "KMP"             | 0.0012752320000436158    | 1.0              |
| "Boyer-Moore"     | 0.0002790830004960299    | 0.2188488059321634 |
| "Rabin-Karp"      | 0.0033820130000822247    | 2.6520766417142547 |

### Test 2

- **Pattern**: "системах. Наявність"
- **Text**: "Методи та структури даних для реалізації бази даних рекомендаційної системи соці"
- **Repetitions**: 1000

| Algorithm         | Runtime (sec)             | Ratio to "KMP"   |
|-------------------|--------------------------|------------------|
| "KMP"             | 0.001326635899953544     | 1.0              |
| "Boyer-Moore"     | 0.000279677499900572     | 0.21081707491133453 |
| "Rabin-Karp"      | 0.0027186625999165697    | 2.0492906908457487 |

### Test 3

- **Pattern**: "системах.  Наявність"
- **Text**: "Методи та структури даних для реалізації бази даних рекомендаційної системи соці"
- **Repetitions**: 100

| Algorithm         | Runtime (sec)             | Ratio to "KMP"   |
|-------------------|--------------------------|------------------|
| "KMP"             | 0.005353578000795096     | 1.0              |
| "Boyer-Moore"     | 0.0011381040001288056    | 0.21258754424793627 |
| "Rabin-Karp"      | 0.012649435999337584     | 2.36280035472705 |

### Test 4

- **Pattern**: "системах.  Наявність"
- **Text**: "Методи та структури даних для реалізації бази даних рекомендаційної системи соці"
- **Repetitions**: 1000

| Algorithm         | Runtime (sec)             | Ratio to "KMP"   |
|-------------------|--------------------------|------------------|
| "KMP"             | 0.005547751799924299     | 1.0              |
| "Boyer-Moore"     | 0.001137159000034444     | 0.2049765456432209 |
| "Rabin-Karp"      | 0.010706905800034291     | 1.929954004103138 |

### Test 5

- **Pattern**: "Література"
- **Text**: "Методи та структури даних для реалізації бази даних рекомендаційної системи соці"
- **Repetitions**: 100

| Algorithm         | Runtime (sec)             | Ratio to "KMP"   |
|-------------------|--------------------------|------------------|
| "KMP"             | 0.004086461999686435     | 1.0              |
| "Boyer-Moore"     | 0.0014478139998391271    | 0.35429523141294883 |
| "Rabin-Karp"      | 0.010513148000463844     | 2.5726772942634843 |

### Test 6

- **Pattern**: "Література"
- **Text**: "Методи та структури даних для реалізації бази даних рекомендаційної системи соці"
- **Repetitions**: 1000

| Algorithm         | Runtime (sec)             | Ratio to "KMP"   |
|-------------------|--------------------------|------------------|
| "KMP"             | 0.0038854594000149517    | 1.0              |
| "Boyer-Moore"     | 0.001467542099999264     | 0.3777010512562856 |
| "Rabin-Karp"      | 0.009366085000103339     | 2.4105476433667783 |

### Test 7

- **Pattern**: "Л ітература"
- **Text**: "Методи та структури даних для реалізації бази даних рекомендаційної системи соці"
- **Repetitions**: 100

| Algorithm         | Runtime (sec)             | Ratio to "KMP"   |
|-------------------|--------------------------|------------------|
| "KMP"             | 0.004845544999698177     | 1.0              |
| "Boyer-Moore"     | 0.0016237360006198286    | 0.33509873517240457 |
| "Rabin-Karp"      | 0.011027115000179038     | 2.2757223389455477 |

### Test 8

- **Pattern**: "Л ітература"
- **Text**: "Методи та структури даних для реалізації бази даних рекомендаційної системи соці"
- **Repetitions**: 1000

| Algorithm         | Runtime (sec)             | Ratio to "KMP"   |
|-------------------|--------------------------|------------------|
| "KMP"             | 0.004595146500039846     | 1.0              |
| "Boyer-Moore"     | 0.0015377939000027255    | 0.3346561203194263 |
| "Rabin-Karp"      | 0.010971449699951336     | 2.387616956250731 |

## Conclusion

Based on the given results, the following conclusions can be drawn:
1. **"Boyer-Moore" search** consistently outperforms the other two algorithms in terms of execution time, making it the most efficient algorithm for the tested cases for both texts.
2. **"KMP" search** performs well and is a reliable choice, especially considering its predictable linear time complexity in the worst case.
3. **"Rabin-Karp" search** is the least efficient of the three, largely due to the overhead of hash calculations and potential hash collisions.

These results indicate that while "KMP" and "Rabin-Karp" have their specific use cases, "Boyer-Moore" is generally the fastest for practical purposes, especially with longer patterns.
