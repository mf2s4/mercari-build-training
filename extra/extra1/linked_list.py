# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Linked_list:
    # Time: O(N) Space: O(N)
    def getIntersectionNode1(self, headA, headB):
        hA_hashmap = {}

        while headA:
            hA_hashmap[headA] = 1
            headA = headA.next

        while headB:
            if headB in hA_hashmap:
                return headB
            headB = headB.next
        
        return None
    

    # Time: O(N) Space: O(1)
    def getIntersectionNode2(self, headA, headB):
        hA = headA
        hB = headB
        numA, numB = 0, 0

        #count length of A and B
        while headA:
            numA += 1
            headA = headA.next
        while headB:
            numB += 1
            headB = headB.next
        
        if numA > numB:
            while numA > numB:
                hA = hA.next
                numA -= 1
        elif numA < numB:
            while numA < numB:
                hB = hB.next
                numB -= 1
        
        #Now the rest of A and B is of same length
        n = numA
        while n != 0 and hA != hB:
            hA = hA.next
            hB = hB.next
        if hA == None:
            return None
        return hA
    
    # Two pointers Floyd's Linked List Cycle Finding Algorithm
    def getIntersectionNode3(self, headA, headB):
        p1 = headA
        p2 = headB

        #connect last node in A to the first node to form a cycle
        while p1.next:
            p1 = p1.next
        p1.next = headA
        p1 = p1.next

        while p2:
            while p1:
                if p1 == p2:
                    return p1
                p1 = p1.next
                if p1 == headA:
                    break 
            p2 = p2.next
        return None

    # Two pointers
    def getIntersectionNode4(self, headA, headB):
        p1 = headA
        p2 = headB

        # Go through nodes until intersection or until both nodes is None
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

            if p1 == p2:
                return p1
            
            #if p1 reaches end, connect to B head #by switching to B from A, it accounts for any length difference
            if not p1:
                p1 = headB
            
            #if p2 reaches end, connect to A head
            if not p2:
                p2 = headA
        
        return p1
        