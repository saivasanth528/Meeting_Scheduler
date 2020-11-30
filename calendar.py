from abc import ABC, abstractmethod


class Calendar(ABC):

    @abstractmethod
    def is_time_slot_available(self, start_time, end_time):
        pass

    @abstractmethod
    def assign_time_slots(self, start_time, end_time):
        pass

    @abstractmethod
    def free_time_slots(self, start_time, end_time):
        pass
