from calendar import Calendar
from operation import OperationEnum
import datetime
from time_slots import TimeSlot


class EmployeeCalendar(Calendar):
    time_slots = 31 * [1440 * [0]]  # initializing the calendar for 31 days

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
