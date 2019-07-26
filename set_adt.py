class Setm:
    
    def __init__(self):
        pass

    def create_set(self, set_name):
        """
        Creates a set  

        Arguments:
            set_name {list} -- creates a list of elements

        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        self.set_name = []

    def access_elements(self, set_name):
        """
        Outputs the set
        
        Arguments:
            set_name {list} -- outputs the elements in the set

        
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        for i in set_name:
            print(i)

    def add_elements(self, set_name):
        """
        Adds elements to a set
        
        Arguments:
            set_name {list} -- adds an element to a set
        
        Returns:
            set -- set of elements including the added element

        
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        self.set_name.add('element')
        return set_name

    def remove_elements(self, set_name):
        """
        Deletes an element from a set
        
        Arguments:
            set_name {list} -- a list of elements
        
        Returns:
            set -- a set not including the removed item

        
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        self.set.remove('element')
        return set_name

    #def __len__(self, set_name)
    def length_set(self, set_name):
        """
        Function returns the length of set
        
        Arguments:
            set_name {list} -- a list of elements
        
        
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        for i in set_name:
            print(len(i))

    def compare_set(self, set_name, set2_name):
        # if set_name <= set2_name:
        #     print("The sets are equal")
        # else:
        #     print("Not equal")
        """
        Compares two sets
        
        Returns:
            list -- returns subset of both items
        
        
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        sub_set = self.set_name.issubset(set2_name)
        return sub_set
    
    def set_union(self, set_name, set2_name):
        """
        Gives an output of items contained in two list but not redundant in both

        Arguments:
            set_name {[list]} -- [first list]
            set2_name {[list]} -- [second list]
        
        Returns:
            [list] -- [returns union of items in both lists]

    
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        set_union_var = self.set_name.union(set2_name)
        return set_union_var

    def set_intersection(self,set_name,set2_name):
         """
        Gives an output of items common in both lists

        Arguments:
            set_name {[list]} -- [first list]
            set2_name {[list]} -- [second list]
        
        Returns:
            [list] -- [returns list of items common in both lists if there is any]

    
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        var_intesection = self.set_name.intersection(set2_name)
        return var_intesection

    def set_diff(self, set_name, set2_name):
         """
        Returns a list that is the difference of the two lists

        Arguments:
            set_name {[list]} -- [first list]
            set2_name {[list]} -- [second list]
        
        Returns:
            [list] -- [returns difference of items in both lists]

    
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        var_difference = self.set_name.difference(set2_name)
        return var_difference