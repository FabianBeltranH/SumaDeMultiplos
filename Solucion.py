sumTotal = 0 #Variable to hold the total to print at the end

for i in range(1, 1000): #We are going to test all numbers from 1 to but not including 1000
    if ((i % 3) == 0): #If it's a multiple of 3, we sum the value to our total
        sumTotal = sumTotal + i
    elif ((i % 5) == 0): #If it's a multiple of 5, we sum the value to our total
        sumTotal = sumTotal + i

print('The total of the sum is: ' + str(sumTotal) + '.') #We print the result
