#!/usr/bin/env python
# coding: utf-8

# In[131]:


class Lot:

    def __init__(self, size = -1):
        self.size = size
        self.slots = ["Empty"]*size

    def reinit(self, size):
        self.size = size
        self.slots = ["Empty"]*size
        
        

    def park(self, reg_no, color):
        temp = 1
        
        for x in self.slots:
            if x!="Empty" and x[0].lower()==reg_no.lower():
                print("Registration no "+reg_no+" already present, duplicate registration number not allowed")
                return
            
        for x in self.slots:
            if x=="Empty":
                self.slots[temp-1]=[reg_no, color]
                print("Allocated slot number: "+str(temp))
                return 
            temp=temp+1
            
        print("Sorry, parking lot is full")
        
    def leave(self, slot):
        
        if slot>self.size or slot<=0:
            print("Invalid/Out of bounds slot number to leave")
            return
        
        if self.slots[slot-1] == "Empty":
            print("Slot number "+str(slot)+" already free")
            return 
        
        self.slots[slot-1]="Empty"
        print("Slot number "+str(slot)+" is free")
    
    def find_reg(self, reg_no):
        temp = 1
        for x in self.slots:
            if x!="Empty" and x[0].lower()==reg_no.lower():
                print(temp)
                return
            temp = temp+1
        print("Not found")
        
    def slots_by_color(self, color):
        first = True
        temp = 1
        final = ""
        for x in self.slots:
            if x!="Empty" and x[1].lower()==color.lower():
                if first:
                    first = False
                else:
                    final = final+", "
                final = final + str(temp)
            temp=temp+1
        if first:
            print("No cars of specified color: "+color)
            return 
        print(final)
        
            
    def reg_by_color(self, color):
        first = True
        final=""
        for x in self.slots:
            if x!="Empty" and x[1].lower()==color.lower():
                if first:
                    first = False
                else:
                    final=final+ ", "
                final=final+x[0]
        if first:
            print("No cars of specified color: "+color)
            return 
        print(final)
    
    def status(self):
        temp = 1
        print("Slot number | Registration No. | Color ")
        for x in self.slots:
            if x!="Empty":
                print(str(temp)+"  "+x[0]+"  "+x[1])
            temp=temp+1
                
            
                    


# In[ ]:




