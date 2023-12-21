import re

class Node:
    # Node of a singly linked list initialization
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # A simple linked list class to handle collisions  #separate chaining
    def __init__(self):
        self.head = None

    def linked_insert(self, data):
        """
        insert function with data repeat avoidance and hash collision avoidance
        :param data:
        :return:
        """
        if not self.exists(data): # check repeat data
            node = Node(data)   # front insertion
            node.next = self.head
            self.head = node

    def exists(self, data):
        """
        check repeat data
        :param data:
        :return:
        """
        current = self.head
        while current:                      # jump out loop when there is no data or reach the end of linked list
            if current.data == data:        # check repeat data
                return True
            current = current.next
        return False

class HashTable:
    # HashTable with fixed size
    def __init__(self, size):
        """
        :param size: size of the hash table
        """
        self.size = size
        self.table = [LinkedList() for _ in range(self.size)]    #generate same amount of size linked list inside the hash table
        self.count = 0

    def hash(self, x):
        """
        calculate hash key
        :param x: string, original data
        :return: hash key
        """

        # A simple hash function that sums the ASCII values of the characters in the string
        # and uses the modulo operator to find the index for the hash table
        return sum(ord(char) for char in x) % self.size

    def hash_insert(self, x):
        """
        hash insert function with insertion count
        :param x:string
        :return: None
        """
        index = self.hash(x)

        if not self.table[index].exists(x):    # judge for easy count  # if repeat exist skip
            self.table[index].linked_insert(x)
            self.count += 1

# Test cases

def hash_tests():
    # Sample size for the hash table
    hash_table = HashTable(100)

    # Inserting elements
    hash_table.hash_insert("apple")
    hash_table.hash_insert("banana")
    hash_table.hash_insert("cherry")
    hash_table.hash_insert("date")

    # Inserting an element that should result in a collision with "banana"
    hash_table.hash_insert("ananab")


    # Inserting an existing element, size should not increase
    hash_table.hash_insert("apple")

    # Checking the size (should be 5)
    print(f"Size of hash table: {hash_table.count}")


hash_tests()





def read_and_process_file(file_name):
    # Initialize a hash table with a reasonably large size
    hash_table = HashTable(10000)

    with open(file_name, 'r') as file:
        for line in file:
            # Split the line into words using non alpha-numeric characters as delimiters
            words = re.split('[^a-zA-Z0-9]', line)  # regular expression
            for word in words:
                if word:  # This check ensures that we don't process empty strings
                    # Sort the characters in the word to find the anagram root
                    sorted_word = ''.join(sorted(word))    # sorted func: result will be order ASCII
                    # Insert the anagram root into the hash table
                    hash_table.hash_insert(sorted_word.lower())  # Convert to lower case to avoid duplicates due to case

    # Return the number of unique anagram roots
    return hash_table.count

read_and_process_file("pride-and-prejudice.txt")

print(f'Number of unique anagram roots: {read_and_process_file("pride-and-prejudice.txt")}')


