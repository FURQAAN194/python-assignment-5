# task2_list_slicing.py

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
extracted_list = numbers[:5]

# Step 3: Reverse the extracted list
reversed_list = extracted_list[::-1]

# Step 4: Print both lists
print("Extracted list (first 5 elements):", extracted_list)
print("Reversed extracted list:", reversed_list)

# Output:
# Extracted list (first 5 elements): [1, 2, 3, 4, 5]
# Reversed extracted list: [5, 4, 3, 2, 1]
