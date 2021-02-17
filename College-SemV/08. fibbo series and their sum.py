
#Use a recursive function to calculate and print the terms and sum of the terms of a FIBONACCI SERIES.

def fibbo_series(n):
    if n <= 1:
        #sum_fibbo = [n]
        return n
    else:
        #sum_fibbo = [fibbo_series(n-1) + fibbo_series(n-2)]
        return (fibbo_series(n-1) + fibbo_series(n-2))

n = int(input("Enter the number: "))

sum_fibbo = []
a = 0
b = 1

while n <= 0:
    print("Enter greater then 0")
    n = int(input("Enter the number: "))
if n == 1:
    print("Term: ", a)
    print("Sum of the term: ", a)
    exit()
elif n == 2:
    print("Terms: ", a, b, " ", end='')
    print("\nSum of all terms: ", a+b)
    exit()

sum_fibbo = [0,1]
print("Terms: ")
print(a, b, " ", end='')

for i in range(2,n):
    re = fibbo_series(i)
    sum_fibbo.append(re)
    print(re, " ", end='')


sum_term = 0
for i in range(len(sum_fibbo)):
    sum_term += sum_fibbo[i]

print("\nSum of all terms: ", sum_term)
