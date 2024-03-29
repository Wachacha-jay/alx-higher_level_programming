#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except (TypeError, ZeroDivisionError):
            print("division by zero")
        except IndexError:
            print("out of range")
        finally:
            newlist.append(div)
    return newlist
