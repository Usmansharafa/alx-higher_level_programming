#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):

    new_list = []
    try:
        for i in range(list_length):
            try:
                new_element = my_list1[i] / my_list2[i]
            except ZeroDivisionError:
                new_element = 0.0
                print("division by 0")
            except TypeError:
                new_element = 0.0
                print("wrong type")
            finally:
                new_list.append(new_element)
    except IndexError:
        new_element = 0.0
        print("out of range")
        new_list.append(new_element)
    return new_list
