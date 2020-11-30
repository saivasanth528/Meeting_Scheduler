# Meeting_Scheduler
Python Console Application for meeting scheduling

Functionality that should be exposed -
● init_meeting_system(M, N)
● Take 2 arguments -
■ M - Number of meeting rooms
■ N - Number of employees
● prints "success" on success
● book(employee_id, start_time, end_time)
● if success, prints the id of the room and id of the meeting itself
● If given time is beyond 1 month, print 'Cannot book beyond 1 month from
today'
● If meeting duration is more than 3 hrs, print 'Cannot book a meeting of more
than 3 hrs duration'
● if this employee has already 2 meetings scheduled at the same time, print 'you
have exceeded the max limit of bookings at a time'
● if room not found, prints 'All rooms busy for the given time interval'
● Handle any others errors if necessary
● Assume a format for start times and end times (example iso 8601 format)
● cancel(employee_id, meeting_id)
● if success, prints 'success'
● if this employee id is not the organiser of this meeting id, print 'you are not the
organizer of this meeting'
