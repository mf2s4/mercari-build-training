# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        listA = []
        listB = []

        while headA:
            listA.append(headA)
            headA = headA.next
        while headB:
            listB.append(headB)
            headB = headB.next
        
        previousNode = None

        while listA and listB != 0:
            nodeA = listA.pop()
            nodeB = listB.pop()

            if nodeA != nodeB:
                return previousNode
            
            previousNode = nodeA

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

        