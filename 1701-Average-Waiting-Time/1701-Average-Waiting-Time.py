class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle_time = 0
        net_wait_time = 0

        for customer in customers:
            next_idle_time = max(customer[0], next_idle_time) + customer[1]
            net_wait_time += next_idle_time - customer[0]

        # Divide by total customers to get average.
        average_wait_time = net_wait_time / len(customers)
        return average_wait_time