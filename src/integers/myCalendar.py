"""
My Calendar I
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.


Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
   Hide Hint #1
Store the events as a sorted list of intervals. If none of the events conflict, then the new event can be added.

"""
import bisect


class MyCalendar:
    # Solution 1 - 540 ms
    """
    def __init__(self):
        self.calendar = {'start': -1, 'end': -1, 'next': {'start': float('inf'), 'end': float('inf')}}

    def book(self, start: int, end: int) -> bool:
        curr = self.calendar
        while start >= curr['end']:
            last, curr = curr, curr['next']
        if curr['start'] < end:
            return False
        last['next'] = {'start': start, 'end': end, 'next': curr}
        return True
    """
    # Solution 2 - 180 ms
    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect(self.ends, start)
        if index == len(self.ends) or end <= self.starts[index]:
            self.starts.insert(index, start)
            self.ends.insert(index, end)
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))
