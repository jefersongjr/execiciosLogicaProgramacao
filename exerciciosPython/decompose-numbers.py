# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for line in sys.stdin:
    maxDigit = int(line.rstrip())
    if 21 / maxDigit >= 4:
        print('null')
    else:
        for number in range(1000, 9999):
            sum = 0
            cont = 0
            for x in str(number):
                if int(x) <= maxDigit:
                    sum += int(x)
                    cont += 1
            if sum == 21 and cont == 4:
                print(number)

# Exercicio do HackerRank