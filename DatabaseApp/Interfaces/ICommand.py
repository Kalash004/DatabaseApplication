import abc


class ICommand(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def execute(self):
        raise NotImplemented
