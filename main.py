from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    ll = LinkedList()

    ll.insert_at_front(3)
    ll.insert_at_front(2)
    ll.insert_at_front(1)

    print("Original list:")
    ll.print_list()

    total = ll.sum()
    print("Sum of list:", total)

    target = 2
    found = ll.search(target)
    print(f"Search for {target}:", found)

    ll.reverse()
    print("Reversed list:")
    ll.print_list()