def selection_sort(the_list):
    n = len(the_list)     # makes it easy to denote the length of the list

    for i in range(n - 1):
        # Find the minimum value in the sublist starting at index i.
        # smallest will hold the index of the smallest value we have found
        # so far in the sublist.
        smallest = i

        for j in range(i, n):
            if the_list[j] < the_list[smallest]:
                smallest = j

        # After the inner loop, smallest has the index of the smallest
        # value in the sublist starting at index i.  Swap the values
        # at index i and smallest.
        (the_list[i], the_list[smallest]) = (the_list[smallest], the_list[i])

the_list = [89, 45, 85, 81, 77, 94, 22, 79, 92, 91]
selection_sort(the_list)
print("grade_list after sorting:  " + str(the_list))