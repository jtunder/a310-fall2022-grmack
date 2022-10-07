class LinkedList:
    def __init__(self, num, rest):
        self.num = num
        self.next = rest
    def show(self):
        print(self.num, end=' ')
        if self.next == None:
            print()
        else:
            self.next.show()

def insert(lon, num):
    if lon == None:
        return LinkedList(num, None)
    elif lon.num < num:
        # return lon.insert(num)
        return LinkedList(lon.num, insert(lon.next, num))
    else:
        return LinkedList(num, lon)

def delete(lon, num):
    if lon == None:
        return None
    else:
        if lon.num == num:
            return lon.next
        else:
            return LinkedList(lon.num, delete(lon.next, num))

def show(lon):
    if lon == None:
        print(None)
    else:
        lon.show()

lon = None
show(lon) # None 
lon = insert(lon, 5)
show(lon) # 5
lon = insert(lon, 7)
show(lon) # 5 7 
lon = insert(lon, 9)
show(lon) # 5 7 9 
lon = insert(lon, 6)
show(lon) # 5 6 7 9
lon = insert(lon, 3)
show(lon) # 3 5 6 7 9
lon = delete(lon, 7)
show(lon) # 3 5 6 9
lon = delete(lon, 8)
show(lon) # 3 5 6 9
lon = delete(lon, 9)
show(lon) # 3 5 6 
lon = delete(lon, 3)
show(lon) # 5 6 
lon = delete(lon, 5)
show(lon) # 6 
lon = delete(lon, 6)
show(lon) # None 
lon = delete(lon, 10)
show(lon) # None 


