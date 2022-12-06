def merge(number_list, i, j, k):
    merged_size = k - i + 1
    merged_numbers = [0] * merged_size #dynamic array creation

    merge_position = 0
    left_position = i
    right_position = j + 1
    print('\nCurrent positions:',number_list[left_position:right_position+2])
    print(' Merge position:',merge_position,', Left position:',left_position,', Right position:',right_position)

    # Add smallest element from left or right partition to merged numbers
    while (left_position <= j and right_position <= k):
        print('  Current positions of merged numbers:',merged_numbers)
        print('  Merge position:',merge_position,', Left position:',left_position,', Right position:',right_position)

        if (number_list[left_position] <= number_list[right_position]):
            print('   Adding',number_list[left_position],'to merged_numbers at merge position',merge_position)
            merged_numbers[merge_position] = number_list[left_position]
            left_position += 1
        
        else:
            print('   Adding',number_list[right_position],'to merged_numbers at merge position',merge_position)
            merged_numbers[merge_position] = number_list[right_position]
            right_position += 1

        merge_position += 1

    # If left partition is not empty, add remaining elements to merged numbers
    while left_position <= j:
        print('   Current positions of merged numbers:',merged_numbers)
        print('   Left partition not empty, Adding',number_list[left_position],'to merged_numbers at merge position',merge_position)
        merged_numbers[merge_position] = number_list[left_position]
        left_position += 1
        merge_position += 1

    # If right partiion is not empty, add remaining elements to merged numbers
    while right_position <= k:
        print('   Current positions of merged numbers:',merged_numbers)
        print('   Right partition not empty, Adding',number_list[right_position],'to merged_numbers at merge position',merge_position)
        merged_numbers[merge_position] = number_list[right_position]
        right_position += 1
        merge_position += 1

    for merge_index in range(merged_size):
        print('  Merging...')
        print('  Current positions of merged numbers:',merged_numbers)
        number_list[i + merge_index] = merged_numbers[merge_index]
        print('   Current positions:',number_list)

def merge_sort(numbers, i, k):
    j = 0

    if i < k:
        j = (i + k) // 2 #finding midpoint in partition

        #recursivly sort left and right partition
        print('//...Recursive call to sort left partition')
        merge_sort(numbers, i, j)
        print('//...Recursive call to sort right partition')
        merge_sort(numbers, j + 1, k)

        #merge left and right partition in sorted order
        print('//...Merging left and right partitions')
        merge(numbers, i, j, k)

numbers = [23, 10, 9, 33, 356, 0, 27, 24, 28]

print('Unsorted:',numbers)

merge_sort(numbers, 0, len(numbers)-1)

print('\nSorted:', numbers) 