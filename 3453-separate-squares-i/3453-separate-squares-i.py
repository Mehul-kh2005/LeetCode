class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        events = []

        for sq in squares:
            y, l = sq[1], sq[2]
            total_area += l * l
            events.append((y, l, 1))
            events.append((y + l, l, -1))

        # sort by y-coordinate
        events.sort(key=lambda x: x[0])

        covered_width = (
            0.0  # sum of all bottom edges under the current scanning line
        )
        curr_area = 0.0  # current cumulative area
        prev_height = 0.0  # height of the previous scanning line

        for y, l, delta in events:
            diff = y - prev_height
            # additional area between two scanning lines
            area = covered_width * diff
            # if this part of the area exceeds more than half of the total area
            if 2 * (curr_area + area) >= total_area:
                return prev_height + (total_area - 2 * curr_area) / (
                    2 * covered_width
                )
            # update width: add width at the start event, subtract width at the end event
            covered_width += delta * l
            curr_area += area
            prev_height = y

        return 0.0