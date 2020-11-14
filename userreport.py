class WorkItem(object):
    """Representation of one unit of work done.

    A WorkItem contains a name, an Assignment, a TimeUnit
    """
    def __init__(self, assignment, timeunit):
        self.assignment = assignment
        self.timeunit = timeunit


class UserReport(object):
    """Report of work incoming from the user.

    Contains one or more WorkItems.
    """
    def __init__(self, items):
        self.items = items

