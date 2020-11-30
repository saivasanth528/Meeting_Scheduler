from abc import ABC, abstractmethod


class Calendar(ABC):

    # time_slots = 31*[1440*[0]]  # initializing the calendar for 31 days

    @abstractmethod
    def is_time_slot_available(self, start_time, end_time):
        pass

    @abstractmethod
    def assign_time_slots(self, start_time, end_time):
        pass

    @abstractmethod
    def free_time_slots(self, start_time, end_time):
        pass
