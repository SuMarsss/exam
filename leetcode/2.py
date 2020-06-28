# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def list2num(root):
            num,mult = 0,1
            cur = root
            while cur :
                num += cur.val * mult
                mult *= 10
                cur = cur.next
            return num

        num1,num2 = map(list2num, (l1,l2))
        tot_num = num1 + num2
        tmp = tot_num

        def num2list(num,mult=10):
            print("num",num)
            g = num % mult 
            num = num // mult
            ln = ListNode(g)
            if num > 0 :
                print("ListNode",ln)
                ln.next = num2list(num,mult)
            else:
                print(ln)
                ln.next = None
            return ln
        return num2list(tot_num, 10)