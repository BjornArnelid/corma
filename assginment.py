class Task(object):
    def __init__(self, task_name):
        self.task_name = task_name


class Assignment(object):
    """The work assignment

    Contains an identifier, a description and a set of ExportActions.
    """
    def __init__(self, identifier, description="", export_actions=None):
        if ' ' in identifier:
            raise ValueError

        if export_actions is None:
            export_actions = []

        self.identifier = identifier
        self.description = description
        self.export_actions = export_actions
