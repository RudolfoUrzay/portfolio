import num_funcs

option = int(input("Please select one: 1(equal) 2(lower) 3(grater) 4(in range) 5(even) 6(ood) 7(is in a list) "))
print(option, "selected")

if option == 1:
    print(num_funcs.is_equal(5,7))

elif option == 2:
    print(num_funcs.is_lower(5, 7))

elif option == 3:
    print(num_funcs.is_grater_than(5, 7))

elif option == 4:
   print(num_funcs.is_in_range(5, 1, 10))

elif option == 5:
    print(num_funcs.is_even(5))

elif option == 6:
    print(num_funcs.is_ood(5))

elif option == 7:
    print(num_funcs.is_in_list(5,20))








