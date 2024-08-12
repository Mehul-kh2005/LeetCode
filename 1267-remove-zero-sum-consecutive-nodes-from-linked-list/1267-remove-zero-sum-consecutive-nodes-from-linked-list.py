class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        current = front
        prefix_sum = 0
        prefix_sum_to_node = {}
        while current is not None:
            # Add current's value to the prefix sum
            prefix_sum += current.val

            # If prefix_sum is already in the hashmap,
            # we have found a zero-sum sequence:
            if prefix_sum in prefix_sum_to_node:
                prev = prefix_sum_to_node[prefix_sum]
                current = prev.next

                # Delete zero sum nodes from hashmap
                # to prevent incorrect deletions from linked list
                p = prefix_sum + current.val
                while p != prefix_sum:
                    del prefix_sum_to_node[p]
                    current = current.next
                    p += current.val

                # Make connection from the node before 
                # the zero sum sequence to the node after
                prev.next = current.next
            else:
                # Add new prefix_sum to hashmap
                prefix_sum_to_node[prefix_sum] = current

            # Progress to next element in list
            current = current.next

        return front.next