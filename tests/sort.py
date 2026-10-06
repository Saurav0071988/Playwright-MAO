#numbers = [5,4,3,10,29,8,6,44,32]
#numbers.sort()
#print(numbers)

numbers = [5,4,3,10,29,8,6,44,32]
n = len(numbers)

# Outer loop: steps through each position of the list
for i in range(n):
    # Assume the current position holds the smallest number
    min_index = i
    
    # Inner loop: scans the rest of the list to find a smaller number
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j  # Update the index of the smallest number
            
    # Swap the found minimum element with the first element of the unsorted part
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Selection Sorted:", numbers)
    
    