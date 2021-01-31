class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if not head == None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print()

def palindrome(head, start = None):
    # Returns True if LL is of length 0 or 1
    if not start:
        if not head or not head.next: # BASE CASE
            return True 
        start = head # Keeps track of head
    
    # Iterates through LL to the last value, updating var head
    elif not head.next:
        return start.next, True
    
    compere, result = palindrome(head.next, start) # RECURSIVE STEP

    # Checks if head and compere are equal, once False, output will be False
    if result is True:
        result = head.data == compere.data
    
    # Checks if backtracking is done
    if head is start: # BASE CASE
        return result 
    
    # Iterates through LL to the last value, updating var compere
    return compere.next, result

if __name__ == "__main__":
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)
    print("\n")


    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")