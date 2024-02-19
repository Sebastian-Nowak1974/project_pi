In this project three methods of calculating pi value are tested. 
The outcome table shows results depending on number of steps calculated. 
Each step is an increase by magnitude of 10. Comparing results gives an idea of 
how many terms of infinite series need to be calculated to get value of pi with a specific accuracy. 
1. Wallis product is an infinite product:
    pi/2 = (2/1 * 2/3) * (4/3 * 4/5) * ... *(2n/(2n - 1) * 2n/(2n + 1)) * ...
2. Gregory-Leibnitz series:
    pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
3. Nilakantha series:
    pi = 3 + 4/(2 * 3 * 4) - 4/(4 * 5 * 6) + 4/(6 * 7 * 8) - ...
The outcome figures come after calculation of (10 ** step) terms in each series.
The default number of steps is set to five, which means n = 100 000 terms.
The figures show the difference between calculations and the value of pi (up to 20 decimal places).
