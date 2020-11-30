from calendar import Calendar
from operation import OperationEnum
import datetime
from time_slots import TimeSlot



class EmployeeCalendar(Calendar):

    # def time_slot_helper(self, day,  start_time_slot, end_time_slot, operation):
    #
    #     for time_slot in range(start_time_slot, end_time_slot + 1):
    #         if operation == OperationEnum.CHECK_TIME_SLOTS:
    #             # checking the available time slots
    #             if self.time_slots[day][time_slot] == 2:
    #                 # indicates he already had the two meetings in the slot
    #                 return False
    #         elif operation == OperationEnum.ASSIGN_TIME_SLOTS:
    #             # Assigning the time slots
    #             self.time_slots[day][time_slot] += 1
    #         else:
    #             # Freeing the time slots
    #             self.time_slots[day][time_slot] -= 1
    #     return True
    #
    # def handle_given_time_slots(self, start_time: datetime.datetime, end_time: datetime.datetime, operation):
    #
    #     start_time_slot = start_time.hour * 60 + start_time.minute
    #     end_time_slot = end_time.hour * 60 + end_time.minute
    #
    #     if start_time.day == end_time.day:
    #         # if the meeting occurs at same day
    #         return self.time_slot_helper(start_time.day, start_time_slot, end_time_slot, operation)
    #     else:
    #         return self.time_slot_helper(start_time.day, start_time_slot, 1441, operation) and \
    #                self.time_slot_helper(end_time.day, 0, end_time_slot, operation)

    def is_time_slot_available(self, start_time: datetime.datetime, end_time: datetime.datetime):

        available_result = TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.CHECK_TIME_SLOTS)

        if not available_result:
            print('you have exceeded the max limit of bookings at a time')
            return False
        return True

    def assign_time_slots(self, start_time: datetime.datetime, end_time: datetime.datetime):
        # self.handle_given_time_slots(start_time, end_time, OperationEnum.ASSIGN_TIME_SLOTS)
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.ASSIGN_TIME_SLOTS)

    def free_time_slots(self, start_time: datetime.datetime, end_time: datetime.datetime):
        return TimeSlot.handle_given_time_slots(self, start_time, end_time, OperationEnum.FREE_TIME_SLOTS)
