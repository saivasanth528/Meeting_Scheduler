from operation import OperationEnum
import datetime


class TimeSlot:

    @staticmethod
    def manage_time_slots(calendar_object, day, start_time_slot, end_time_slot, operation, slot_limit):

        for time_slot in range(start_time_slot, end_time_slot):
            if operation == OperationEnum.CHECK_TIME_SLOTS:
                # checking the available time slots
                if calendar_object.time_slots[day][time_slot] == slot_limit:
                    # indicates he already had the two meetings in the slot
                    return False
            elif operation == OperationEnum.ASSIGN_TIME_SLOTS:
                # Assigning the time slots
                calendar_object.time_slots[day][time_slot] += 1
            else:
                # Freeing the time slots
                calendar_object.time_slots[day][time_slot] -= 1
        return True

    @staticmethod
    def handle_given_time_slots(calendar_object, start_time: datetime.datetime, end_time: datetime.datetime, operation,
                                slot_limit):

        no_of_minutes_in_a_hour = 60
        start_time_slot = start_time.hour * no_of_minutes_in_a_hour + start_time.minute
        end_time_slot = end_time.hour * no_of_minutes_in_a_hour + end_time.minute

        if start_time.day == end_time.day:
            # if the meeting occurs at same day
            return TimeSlot.manage_time_slots(calendar_object, start_time.day - 1, start_time_slot, end_time_slot,
                                              operation, slot_limit)
        else:
            return TimeSlot.manage_time_slots(calendar_object, start_time.day - 1, start_time_slot, 1440, operation, slot_limit) and \
                   TimeSlot.manage_time_slots(calendar_object, end_time.day - 1, 0, end_time_slot, operation, slot_limit)
