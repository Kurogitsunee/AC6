import numpy as np
# create identity matrix n by n
while True:
    n = int(input('Write a number of criteries (positive integer): '))
    if n <= 0:
        print("Number of criteria must be positive")
        continue
    else:
        break

weights = np.eye(n)

# create iterator
i = 0

# cycle to input matrix values and input errors
while i != n:
    j = 0
    while j != i:
        weights[i][j] = float(input(f"Write a weight for {i+1} criteria to {j+1} criteria (number from 0 to 10 but not a 0): "))
        if weights[i][j] <= 0 or weights[i][j] > 10:  # checking range
            print("Weight must be a number from 0 to 10 but not a 0. Try again.")
            continue
        elif not (weights[i][j]).is_integer():  # checking integer
            if weights[i][j] < 1:
                if round(weights[i][j], 2) not in [0.50, 0.33, 0.25, 0.20, 0.17, 0.14, 0.12, 0.11, 0.10]:
                    print("Weights less than 1 must be an inverse number to integer number from 1 to 10")
                    continue
            else:
                print("Weights greater than (or equal to) 1 must be an integer number or equal to 1.")
                continue
            weights[j][i] = 1/weights[i][j]
        j += 1  # incrementing iterator j
    i += 1  # incrementing iterator i

# summarizing weights in rows and adding them in list
sums = []

for k in range(n):
    sums.append(sum(weights[k]))

# finding sum of summarized weights
sum_of_sums = sum(sums)

# normalizing weigths and adding them in list
result_coefs = []

for k in range(n):
    result_coefs.append(round(sums[k]/sum_of_sums, 2))

# print coefficients for each criteria
for k, coef in enumerate(result_coefs):
    print(f"Coefficient for {k+1} criteria: {coef}")