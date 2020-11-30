from calendar import Calendar
from operation import OperationEnum
import datetime
from time_slots import TimeSlot


class EmployeeCalendar(Calendar):
    NO_OF_DAYS = 31
    NO_OF_MINUTES_IN_A_DAY = 1440

    def __init__(self):

        self.time_slots = self.NO_OF_DAYS * [self.NO_OF_MINUTES_IN_A_DAY * [0]]

    def is_time_slot_available(self, start_time: datetime.datetime, end_time: datetime.datetime):

        available_result = TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.CHECK_TIME_SLOTS, 2)

        if not available_result:
            print('you have exceeded the max limit of bookings at a time')
            return False
        return True

    def assign_time_slots(self, start_time: datetime.datetime, end_time: datetime.datetime):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.ASSIGN_TIME_SLOTS, 2)

    def free_time_slots(self, start_time: datetime.datetime, end_time: datetime.datetime):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.FREE_TIME_SLOTS, 2)
