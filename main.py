#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from functions import Lot


def query(lot, _line):
    _line = _line.split(" ")
    if _line[0]=="exit":
        exit()
    if _line[0]=="create_parking_lot":
        lot.reinit(int(_line[1]))
        return
    if _line[0]=="park":
        lot.park(str(_line[1]),str(_line[2]))
        return
    if _line[0]=="leave":
        lot.leave(int(_line[1]))
        return
    if _line[0]=="status":
        lot.status()
        return
    if _line[0]=="registration_numbers_for_cars_with_colour":
        lot.reg_by_color(str(_line[1]))
        return
    if _line[0]=="slot_numbers_for_cars_with_colour":
        lot.slots_by_color(str(_line[1]))
        return
    if _line[0]=="slot_number_for_registration_number":
        lot.find_reg(str(_line[1]))
        return
    print("Query string not recognized")


if __name__ == "__main__":
    lot_main = Lot()
    if len(sys.argv)==1:
        print("This is the interactive terminal, please type in commands and use command exit to stop taking inputs.")
        while True:
            line = input()
            query(lot_main, line)
    else:
        f = open(sys.argv[1], "r")
        lines = [line.rstrip() for line in f]
        for item in lines:
            query(lot_main,item)

# In[5]:





# In[ ]:




