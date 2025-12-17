def sort_array(source_array):
    
    new_list = [x for x in source_array if x % 2 != 0]
    new_list.sort()
    
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
                source_array[i] = new_list[0]
                new_list.remove(new_list[0])
    return source_array
   
print(sort_array([5, 8, 6, 3, 4]))

 
