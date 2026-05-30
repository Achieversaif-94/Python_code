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

def merge_sorted(l1, l2):
    dummy = Node(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

l1 = build([1, 3, 5])
l2 = build([2, 4, 6])
print(to_list(merge_sorted(l1, l2)))