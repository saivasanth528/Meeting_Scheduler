from meeting_scheduler import MeetingScheduler

import sys
import datetime


def get_time_stamp(year, month, day, hour, minute):

    return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))


def is_start_time_of_meeting_exceeds_one_month(current_given_time_stamp, current_time_stamp):

    if (current_given_time_stamp.year - current_time_stamp.year) * 12 + current_given_time_stamp.month \
            - current_time_stamp.month > 1:
        print("Cannot Book Meeting beyond one month from today")
        return True
    return False


def validate_given_date(given_date):

    try:
        year, month, day, hours, minutes = given_date.split('/')
        current_given_time_stamp = get_time_stamp(year, month, day, hours, minutes)
        current_time_stamp = datetime.datetime.now()
        if current_given_time_stamp < current_time_stamp:
            raise ValueError("Meeting can't be scheduled on the past date")

        return current_given_time_stamp
    except ValueError as e:

        print("Invalid Date", e)
        return False


def compare_meeting_duration(start_time_of_meeting, end_time_of_meeting):

    time_difference = end_time_of_meeting - start_time_of_meeting

    time_difference = time_difference.total_seconds() / 60

    if time_difference > 180:

        print("Cannot book a meeting of more than 3 hours duration")
        return False

    return True


def take_meeting_schedule_from_user():

    start_time_of_meeting = input(
        "Enter the starting time of the meeting in this format 'YYYY/MM/DD/HH/MM', " "time(24 hour format): ")

    start_time_of_meeting = validate_given_date(start_time_of_meeting)

    if not start_time_of_meeting or is_start_time_of_meeting_exceeds_one_month(start_time_of_meeting, datetime.datetime.now()):
        return [None, None, False]

    end_time_of_meeting = input(
        "Enter the ending time of the meeting in this format 'YYYY/MM/DD/HH/MM', " "time(24 hour format): ")

    end_time_of_meeting = validate_given_date(end_time_of_meeting)

    if not end_time_of_meeting:
        return [None, None, False]

    if not compare_meeting_duration(start_time_of_meeting, end_time_of_meeting):
        return [None, None, False]
    return [start_time_of_meeting, end_time_of_meeting, True]


if __name__ == '__main__':

    number_of_meeting_rooms = int(input("Enter the number of meeting rooms: "))
    number_of_employees = int(input("Enter the number of employees: "))

    if number_of_employees <= 0 or number_of_meeting_rooms <= 0:
        print("System cannot schedule any meetings due to invalid inputs")
        sys.exit()

    meeting_scheduler = MeetingScheduler(number_of_meeting_rooms, number_of_employees)
    print("**************MEETING SCHEDULER ****************")

    while True:

        print("1. Book\t  2. Cancel\t   3.Exit")
        user_choice = int(input())

        if user_choice == 1:
            meeting_times = take_meeting_schedule_from_user()
            if meeting_times[2]:
                employee_id = int(input("Enter the employee Id: "))
                meeting_scheduler.book(employee_id, meeting_times[0], meeting_times[1])
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            sys.exit()
