from hashtable import HashTable

class HashSet(object):
    def __init__(self, elements=None):
        '''Create new empty set and adds elements'''
        self.hash = HashTable()
        self.size = 0
        
        if elements is not None:
            for item in elements:
                self.add(item)


    def size(self):
        '''Tracks items in constant time
        Time complexity: O(1)'''
        return self.size

    def contains(self, element):
        '''Returns True or False if item is in set.
        Time Complexity: O(1) (avg. case)'''
        return self.hash.contains(element)

    def add(self, element):
        '''Adds element, if exist, raise KeyError
        Time Complexity: O(1) avg, but O(n) when resizing'''
        if self.contains(element):
            self.hash.set(element,element)
            self.size += 1

    def remove(self, element):
        '''Remove element, Raise Error if not present
        Time Complexity: O(1) avg, O(n) if resizing'''
        if not self.contains(element):
            raise KeyError("Element does not exist")
        else:
            self.hash.delete(element)
            self.size -= 1

    def union(self, other_set):
        '''Return new set with values from all sets
        Time Complexity: O(m + n)'''
        new_set = HashSet()
        
        for i in self.hash.values(): # O(n)
            new_set.add(i) 
        
        for i in other_set.hash.values():
            new_set.add(i)

        return new_set

    def intersection(self, other_set):
        '''Return a set that contains values that are in both sets
        Time Complexity: O(m) going through each element'''
        
        new_set = HashSet()
        for i in self.hash.values():  
            if other_set.contains(i): #log m; m=self, n=other
                new_set.add(i)  #log(min(m,n))    
        return new_set

    def difference(self, other_set):
        '''Return set that has value from only one set and not in the other
        Time Complexity: O(n)'''
        
        new_set = HashSet()
        
        for i in self.hash.values():
            if not other_set.contains(i):
                new_set.add(i)
        return new_set

    def subset(self, other_set):
        """Checks if set is a subset or not
        Time Complexity: O(1) best case if bigger, O(n) avg case going through all items"""
        var = 0
        if self.size > other_set.size: #If first set is bigger, it is anever a subset
            return False
        
        for i in self.hash.values():
            if other_set.contains(i):
                var += 1
                
        
        return self.size == var

def test_set():
    elements = ['A', 'B', 'D', 'F']
    elements2 = ['A', 'B', 'D', 'F', 'G', 'H']
    set = HashSet(elements)
    set2 = HashSet(elements2)
    # print(set.union(set2).hash.values())
    # print(set.intersection(set2).hash.values())
    # print(set.difference(set2).hash.values())
    print(set.subset(set2))


if __name__ == '__main__':
    test_set()


