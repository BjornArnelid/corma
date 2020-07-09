class WorkItem(object):
    """Representation of the type of work done.

    A WorkItem generally contains a name, a type and one or several actions that should be done when reporting time
    """
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions
