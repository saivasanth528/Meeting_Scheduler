from employee_calendar import EmployeeCalendar
from meeting_room_calendar import MeetingRoomCalendar
from meeting import Meeting


class MeetingScheduler:

    no_of_meetings = 0
    employee_calendar_objects: EmployeeCalendar = []
    meeting_room_calendar_objects: MeetingRoomCalendar = []
    scheduled_meetings = {}

    def __init__(self, number_of_meeting_rooms, number_of_employees):
        self.number_of_meeting_rooms = number_of_meeting_rooms
        self.number_of_employees = number_of_employees

        for i in range(self.number_of_employees):
            self.employee_calendar_objects.append(EmployeeCalendar())

        for i in range(self.number_of_meeting_rooms):
            self.meeting_room_calendar_objects.append(MeetingRoomCalendar())

    def book(self, employee_id, start_time, end_time):

        if employee_id <= 0 or employee_id > self.number_of_employees:

            print("Invalid Employee Id, Note: Employee Id ranges from 1 to ", self.number_of_employees)
            return

        current_employee: EmployeeCalendar = self.employee_calendar_objects[employee_id-1]

        if current_employee.is_time_slot_available(start_time, end_time):

            for room in range(0, len(self.meeting_room_calendar_objects)):

                room_calendar_object = self.meeting_room_calendar_objects[room]

                if room_calendar_object.is_time_slot_available(start_time, end_time):

                    room_calendar_object.assign_time_slots(start_time, end_time)
                    current_employee.assign_time_slots(start_time, end_time)
                    self.no_of_meetings += 1

                    meeting_obj = Meeting(employee_id, start_time, end_time, room, self.no_of_meetings)
                    self.scheduled_meetings[self.no_of_meetings] = meeting_obj
                    print("Success Room Id: ", room, " Meeting Id: ", self.no_of_meetings)
                    return True

            print('All rooms busy for the given time interval')

    def cancel(self, employee_id, meeting_id):

        if meeting_id not in self.scheduled_meetings:
            print("Enter valid meeting id")
            return False
        current_meeting: Meeting = self.scheduled_meetings[meeting_id]

        if current_meeting.organizer == employee_id:
            current_employee: EmployeeCalendar = self.employee_calendar_objects[employee_id - 1]
            current_employee.free_time_slots(current_meeting.start_time, current_meeting.end_time)
            room_object: MeetingRoomCalendar = self.meeting_room_calendar_objects[ current_meeting.meeting_room_id]
            room_object.free_time_slots(current_meeting.start_time, current_meeting.end_time)
            self.scheduled_meetings.pop(meeting_id)
            print("Meeting cancelled successfully")
        else:
            print('you are not the organizer of this meeting')


















