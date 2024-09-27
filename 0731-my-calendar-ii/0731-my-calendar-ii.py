class MyCalendarTwo:

    def __init__(self):
        self.bookings=[]
        self.overlap_bookings=[]

    def book(self, start: int, end: int) -> bool:
        for booking in self.overlap_bookings:
            if self.does_overlap(booking[0],booking[1],start,end):
                return False

        for booking in self.bookings:
            if self.does_overlap(booking[0],booking[1],start,end):
                self.overlap_bookings.append(self.get_overlapped(booking[0],booking[1],start,end))


        self.bookings.append((start,end))
        return True

    def does_overlap(self,start1,end1,start2,end2):
        return max(start1,start2)<min(end1,end2)

    def get_overlapped(self,start1,end1,start2,end2):
        return max(start1,start2),min(end1,end2)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)