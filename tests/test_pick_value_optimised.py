from game_functions import pick_value

def test_pick_value():
    mylist = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    middle_items = []
    n = len(mylist) 
    middle_items.append(mylist[n//2])
    if n%2 == 0:
       middle_items.append(mylist[(n+1)//2])
    assert pick_value(mylist) in middle_items

    mylist = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    middle_items = []
    n = len(mylist) 
    middle_items.append(mylist[n//2])
    if n%2 == 0:
       middle_items.append(mylist[(n+1)//2])
    assert pick_value(mylist) in middle_items

