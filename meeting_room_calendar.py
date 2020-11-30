from calendar import Calendar
from operation import OperationEnum
from  time_slots import TimeSlot

class MeetingRoomCalendar(Calendar):
    time_slots = 31 * [1440 * [0]]  # initializing the calendar for 31 days
    def is_time_slot_available(self, start_time, end_time):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.CHECK_TIME_SLOTS, 1)

    def assign_time_slots(self, start_time, end_time):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.ASSIGN_TIME_SLOTS, 1)

    def free_time_slots(self, start_time, end_time):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.FREE_TIME_SLOTS, 1)