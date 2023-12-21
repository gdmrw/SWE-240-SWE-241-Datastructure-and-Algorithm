class User:
    def __init__(self, name, address, ssn, initial_deposit):   # create a user node
        self.name = name
        self.address = address
        self.ssn = ssn
        self.initial_deposit = initial_deposit
        self.next_user = None


class Bank:                         # create a linked list
    def __init__(self):
        self.head = None                # initialize head
        self.last_unique_id = 0         # initialize unique id
        self.free_up_ids = set()        # create an empty set to store free up id

    def addUser(self, name, address, ssn, initial_deposit):    #add user function start
        """
        add user into bank(linkedlist)
        :param name: str
        :param address: str
        :param ssn: str
        :param initial_deposit: int
        :return:
        """
        new_user = User(name, address, ssn, initial_deposit)

        if self.free_up_ids:                        # judge if any free up id exist, if yes use free up id first
            new_user.id = self.free_up_ids.pop()    # take out free id from set and assign to new user

            current_user = self.head
            previous_user = None

            while current_user and current_user.id > new_user.id:
                previous_user = current_user
                current_user = current_user.next_user
            if previous_user is None:  # This means the new user has the smallest ID
                new_user.next_user = self.head
                self.head = new_user
            else:
                new_user.next_user = previous_user.next_user
                previous_user.next_user = new_user
        else:
            self.last_unique_id += 1                # if no free up id exist, increment unique id and assign to new user
            new_user.id = self.last_unique_id
            new_user.next_user = self.head      # start link linked list
            self.head = new_user                # In this case, use head insertion method to make up a single linked list

    def deleteUser(self, user_id):
        """
        :param user_id: int
        :return:
        """
        current_user = self.head     #
        previous_user = None         #

        while current_user:    # traverse start until the end of the linked list
            if current_user.id == user_id:
                # Remove the user from the list
                if previous_user:   # if match node not the first node
                    previous_user.next_user = current_user.next_user # link the node between delete node
                else:
                    self.head = current_user.next_user   # if match node the first node
                self.free_up_ids.add(user_id)  # Free up the unique ID
                return

            previous_user = current_user
            current_user = current_user.next_user  # traverse until the end of list

    def printUsers(self):
        current_user = self.head
        while current_user:         # traverse and print out the node data
            print(
                f"ID: {current_user.id}, Name: {current_user.name}, Address: {current_user.address}, SSN: {current_user.ssn}, Initial Deposit: {current_user.initial_deposit}")
            current_user = current_user.next_user

    def findUser(self, user_id):
        """
        find target user using unique id, find user is a function create for pay to user function
        :param user_id: int
        :return: target user node
        """
        current_user = self.head
        while current_user:
            if current_user.id == user_id:
                return current_user
            current_user = current_user.next_user
        return None

    def payUserToUser(self, payer_id, payee_id, amount):
        payer = self.findUser(payer_id)
        payee = self.findUser(payee_id)

        if payer == None or payee == None:
            print("Payment failed, invalid payer or payee ID")
            return

        if payer.initial_deposit >= amount:  # check payer have enough money to pay
            payer.initial_deposit -= amount
            payee.initial_deposit += amount
            print(f"Payment of ${amount} from User ID {payer.id} to User ID {payee.id} was successful.") # hint
        else:
            print("Payment failed. Please check the user IDs and the payer's balance.")

    def getMedianID(self):
        """
        Returns the median of all the account IDs
        :return: int or float
        """
        length = 0
        current_user = self.head
        ids = []

        # Traverse the linked list to get all IDs and the total count
        while current_user:
            ids.append(current_user.id)
            current_user = current_user.next_user
            length += 1

        # Sort the IDs to find the median
        ids.sort()

        # If the length of the list is even, return the average of the two middle elements
        if length % 2 == 0:
            return (ids[length // 2 - 1] + ids[length // 2]) / 2
        # If the length of the list is odd, return the middle element
        else:
            return ids[length // 2]

    def mergeAccounts(self, id1, id2):
        """
        user with higher id will be merged into same user with lower id
        :param id1:
        :param id2:
        :return:
        """
        user1 = self.findUser(id1)
        user2 = self.findUser(id2)

        if user1 and user2:  # make sure there are users existed
            if (
                    user1.name == user2.name                    # make sure all the require information match
                    and user1.address == user2.address
                    and user1.ssn == user2.ssn
            ):
                # Merge the accounts
                # Delete the account with the higher ID
                if user1.id < user2.id:
                    user1.initial_deposit += user2.initial_deposit  # add on
                    self.deleteUser(user2.id)
                else:
                    user2.initial_deposit += user1.initial_deposit
                    self.deleteUser(user1.id)
                print(f"Accounts with IDs {id1} and {id2} have been merged.")
            else:
                print("Accounts cannot be merged. Owner information does not match.")
        else:
            print("One or both accounts not found.")

    def mergeBanks(self, bank1, bank2):
        """
        Merges two banks into a single bank with unique and incremental IDs
        :param bank1: Bank
        :param bank2: Bank
        :return: Bank
        """
        merged_bank = Bank()
        current_user_1 = bank1.head
        current_user_2 = bank2.head

        # Merge all users from bank1 to merged_bank
        while current_user_1:
            merged_bank.addUser(current_user_1.name, current_user_1.address, current_user_1.ssn,
                                current_user_1.initial_deposit)
            current_user_1 = current_user_1.next_user

        # Merge all users from bank2 to merged_bank, checking for duplicate IDs
        while current_user_2:
            if current_user_2.id in merged_bank.free_up_ids or current_user_2.id <= merged_bank.last_unique_id:
                # If duplicate ID, create a new ID for this user
                merged_bank.last_unique_id += 1
                new_id = merged_bank.last_unique_id
            else:
                # If no duplicate, use the existing ID
                new_id = current_user_2.id

            merged_bank.addUser(current_user_2.name, current_user_2.address, current_user_2.ssn,
                                current_user_2.initial_deposit)
            # Manually set the ID of the newly added user to the correct ID (new or existing)
            merged_bank.head.id = new_id
            current_user_2 = current_user_2.next_user

        # Now, merged_bank contains all users from both banks with unique IDs
        return merged_bank


# Sample test cases
if __name__ == '__main__':
    bankoc = Bank()
    bankla = Bank()


    bankla.addUser("Carol", "789 Oak St", "543-21-9876", 1000)
    bankoc.addUser("Alice", "123 Main St", "123-45-6789", 800)
    bankoc.addUser("Bob", "456 Elm St", "987-65-4321", 2000)
    bankoc.addUser("Carol", "789 Oak St", "543-21-9876", 1000)
    bankoc.addUser("lutos", "123 badminton St", "949-13-5678", 1500)
    bankoc.addUser("lutos", "123 badminton St", "949-13-5678", 1500)
    bankoc.deleteUser(2)
    bankoc.addUser("lutos", "123 badminton St", "949-13-5678", 1500)
    bankoc.deleteUser(3)
    bankoc.addUser("Bob", "456 Elm St", "987-65-4321", 2000)
    bankoc.printUsers()
    # bankoc.mergeAccounts(4,5)
    # bankoc.payUserToUser(4,6, 2000)
    # banksc = bankoc.mergeBanks(bankoc,bankla)
    # banksc.printUsers()
    # bankla.printUsers()
    # print("user list in bank oc:")
    # bankoc.printUsers()

    # print("user list after  delete bob:")
    # bankoc.deleteUser(2)
    # bankoc.printUsers()
    # print("new user add back after deletion:")
    # bankoc.addUser("Taylor", "456 Elm St", "987-65-4321", 2000)
    # bankoc.printUsers()
    # print("user transfer function test:")
    # bankoc.payUserToUser(2, 1, 1000)  # taylor transfer 1000 to alice
    # bankoc.printUsers()
    # print("bank get median ID test")
    # print(f"bankoc mideian id is {bankoc.getMedianID()}")
    # print("bank merging test")  # merge bank bankoc and bankla into bank sc
    # print("bankoc user list")
    # bankoc.printUsers()
    # print("bankla user list")
    # bankla.printUsers()
    # print("banksc user list after merge bankoc and bankla")
    # banksc = bankoc.mergeBanks(bankoc, bankla)
    # banksc.printUsers()
    # print("merge account function test")
    # banksc.mergeAccounts(3, 5)
    # print("banksc user list after merge account")
    # banksc.printUsers()


