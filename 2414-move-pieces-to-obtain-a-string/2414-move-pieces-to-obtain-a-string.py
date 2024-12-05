class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_queue = []
        target_queue = []

        for i in range(len(start)):
            if start[i] != "_":
                start_queue.append((start[i], i))
            if target[i] != "_":
                target_queue.append((target[i], i))

        if len(start_queue) != len(target_queue):
            return False

        while not len(start_queue) == 0:
            start_char, start_index = start_queue.pop(0)
            target_char, target_index = target_queue.pop(0)

            if (
                start_char != target_char
                or (start_char == "L" and start_index < target_index)
                or (start_char == "R" and start_index > target_index)
            ):
                return False

        return True