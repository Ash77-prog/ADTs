class arrays:
# a rep arrays
# basic array operations:
    def __init__(self):
        """
        [Creates an array using a list]
        """
        self.testd = []

    def insert_a(self, index, element):
        """
        [inserts a new object into an array]
        
        Args:
            index ([int]): [unique, descibes location of an item in an array]
            element ([int/str]): [item stored in an array]
        
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
        """
        self.testd.append(element)

    def delete_a(self, element):
          """
        [deletes an element from an array]
        
        Args:
            index ([int]): [unique, descibes location of an item in an array]
            element ([int/str]): [item stored in an array]
        
        Runtime:
            Time complexitiy: O(1)
            Name: Constant
            """
        self.testd.remove(element)

    def search_a(self, index):
          """
        [searches for a specific element an array]
        
        Args:
            index ([int]): [unique, descibes location of an item in an array]
        
        Runtime:
            Time complexitiy: O(n)
            Name: Linear
            """
        self.testd.index('Element')

