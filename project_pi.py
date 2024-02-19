''' In this project three methods of calculating pi value are tested.
The outcome table shows results depending on number of steps calculated.
Each step is an increase by magnitude of 10. Comparing results gives 
an idea of how many terms of infinite series need to be calculated
to get value of pi with a specific accuracy.  '''
import sys
sys.setrecursionlimit(1100)    
    

def pi_Wallis(n):
    ''' Wallis product is an infinite product:
    pi/2 = (2/1 * 2/3) * (4/3 * 4/5) * ... *(2n/(2n - 1) * 2n/(2n + 1)) * ... 

    n: number of terms calculated in expression
    '''
    def recursion(n, i, init):        
        if n == 1000 * i :
            return init
        else:
            return ((2 * n) ** 2)/((2 * n -1) * (2 * n +1)) * recursion(n -1, i, init)
    # Recursion is split into steps of 1000 each to prevent memory issues.     
    m = n // 1000    
    init = 2
    for i in range(m):
        res = recursion(1000 * (i + 1), i, init)
        init = res        
    else:
        res = recursion(n, m, init)
        return res


def pi_Gregory_Leibnitz(n):
    ''' Gregory-Leibnitz series:
    pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
    '''
    value = 0
    i = 0
    x = 1
    while i <= n:
        value += x/(2 * i +1)
        x = -x
        i += 1
    return value * 4


def pi_Nilakantha(n):
    ''' Nilakantha series:
    pi = 3 + 4/(2 * 3 * 4) - 4/(4 * 5 * 6) + 4/(6 * 7 * 8) - ...
    '''
    value = 3
    i = 1
    x = 1    
    while i <= n:
        value += 4 * x/(2 * i * (2 * i +1) * (2 * i + 2))
        x = -x
        i += 1
    return value


def my_data(step = 5):   
    ''' The outcome figures come after calculation of 10 ** step terms
    in each series. The default number of steps is set to five,
    which means n = 100 000 terms. The figures show the difference
    between calculations and the value of pi (up to 20 decimal places).
    '''
    pi = 3.14159265358979323846
    my_data = {'Wallis': [], 'Gregory-Leibnitz': [], 'Nilakantha': [] }
    for j in range(step +1):
        i = 10 ** j
        pi_dif = pi - pi_Wallis(i)         
        my_data['Wallis'].append(pi_dif)
        pi_dif =pi - pi_Gregory_Leibnitz(i)        
        my_data['Gregory-Leibnitz'].append(pi_dif)
        pi_dif = pi - pi_Nilakantha(i)        
        my_data['Nilakantha'].append(pi_dif)
    string = 'step\t\t'
    for key in my_data:
        string += f'{key}\t\t'
    string += '\n\n'
    i = 1    
    while i <= step:
        string += f'{i}\t'
        for key in my_data.keys():
            string += f'{my_data[key][i]:.17f}\t'
        string += '\n'
        i += 1    
    print(string)

my_data()
    
    
    

