# At first I define a "Numbers" variable and use "list" & "map" & "slpit".
Numbers = list(map(int, input("Please enter numbers separated by spaces:").split()))

# Define "largest" & "minimum" variables and use "max" & "min" to choose maximum & minimum numbers.
largest = max(Numbers)
minimum = min(Numbers)

# Output the result
print(f"the largest number is: {largest}")
print(f"the minimum number is: {minimum}")