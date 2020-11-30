from calendar import Calendar
from operation import OperationEnum
from  time_slots import TimeSlot

class MeetingRoomCalendar(Calendar):

    def is_time_slot_available(self, start_time, end_time):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.CHECK_TIME_SLOTS)

    def assign_time_slots(self, start_time, end_time):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.ASSIGN_TIME_SLOTS)

    def free_time_slots(self, start_time, end_time):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.FREE_TIME_SLOTS)