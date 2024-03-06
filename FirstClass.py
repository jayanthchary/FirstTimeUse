class pqueue:
    def __init__(self):
        self.list1 = []

    def insert1(self, el, pi):
        index = 0
        if len(self.list1) == 0:
            print(f"-> Added Element -> Element {el}  Priroty {pi}")
            self.list1.append((el, pi))
            # print("added element",self.list1)
        else:
            print(f"-> Added Element -> Element {el}  Priroty {pi}")
            while index < len(self.list1) and self.list1[index][1] <= pi:
                index += 1
            self.list1.insert(index, (el, pi))
            # print("added element",self.list1)

    def delete1(self):
        if self.is_empty():
            print("-> Queue is Empty")
        else:
            a = self.list1.pop(0)[0]
            print("-> Delete Element", a)

    def display1(self):
        if self.is_empty():
            print("-> Queue has No Element")
        else:
            place = 0
            print("-> Element in Queue ", end="")
            while place < len(self.list1):
                print("-> ", self.list1[place][0], end="")
                place += 1
            print("")

    def is_empty(self):
        return len(self.list1) == 0

    def product(self, n):
        l = 1
        if n <= len(self.list1):
            for i in range(len(self.list1)):
                if i < n:
                    l *= self.list1[i][0]
            print(l)
        else:
            print("Entered number out of bond in queue")


def main():
    pq = pqueue()
    while True:
        print("\nPriority Queue Operations:")
        print("1. Insert Element")
        print("2. Delete Element")
        print("3. Display Priority Queue")
        print("4. Display the Product of Queue")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            element = int(input("Enter the element to insert: "))
            priority = int(input("Enter the priority of the element: "))
            pq.insert1(element, priority)
        elif choice == '2':
            pq.delete1()
        elif choice == '3':
            pq.display1()
        elif choice == '4':
            n = int(input("How many elements do you want product"))
            pq.product(n)
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()