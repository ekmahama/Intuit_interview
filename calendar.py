class myCalendar:
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        if not self.calendar:
            self.calendar.append((start, end))
            return True
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True
