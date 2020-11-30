# Meeting_Scheduler
Python Console Application for meeting scheduling

Functionality that exposed  as-
● init_meeting_system(M, N)\
● Take 2 arguments -\
■ M - Number of meeting rooms\
■ N - Number of employees\

● book(employee_id, start_time, end_time)\
● if success, prints the id of the room and id of the meeting itself\
● If given time is beyond 1 month,is prints 'Cannot book beyond 1 month from
today'\
● If meeting duration is more than 3 hrs, it prints 'Cannot book a meeting of more
than 3 hrs duration'\
● if this employee has already 2 meetings scheduled at the same time, it prints 'you
have exceeded the max limit of bookings at a time'\
● if room not found,it prints 'All rooms busy for the given time interval'\
● THe format for start and end time is YYYY/MM/DD/HH/MM


● cancel(employee_id, meeting_id)\
● if success, it prints 'success'\
● if this employee id is not the organiser of this meeting id, it prints 'you are not the\
organizer of this meeting'\



NOTE: The system will work eventhough we tried to schedule the meeting in the timespan which fell between two days.
