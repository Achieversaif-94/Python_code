class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def build(values):
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

head = build([1, 2, 3, 4, 5])
print(to_list(reverse(head)))