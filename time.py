def add_time(start, duration):
    # start = '3:00 PM'
    start_hours = start.split(':')[0]
    minutes = start.split(':')[1]
    start_minute = minutes.split(' ')[0]
    start_text = minutes.split(' ')[1]
    # print(start_hours,start_minute, start_text)
    duration_hours = duration.split(':')[0]
    duration_minute = duration.split(':')[1]
    hours = 12
    total_hours = int(start_hours) + int(duration_hours) 
    total_min = int(start_minute) + int(duration_minute)
    # print('hours:', total_hours, 'min:',total_min)
    number_of_days = total_hours//24 
    days = round(number_of_days)
    if total_min > 60:
        total_hours+= 1
        remaining_min = total_min % 60
        # print(total_hours)
        if total_hours > 24 :
            days+=1
        if start_text == 'PM' :
            new_hour = total_hours % hours
            # print(new_hour)
            start_text = 'PM'
        elif start_text == 'AM' and total_hours > hours:
            new_hour = total_hours % hours
            # print(new_hour)
        elif start_text == 'AM':
            start_text = 'PM'
        else:
            new_hour = total_hours
        formatted_hour = f'{new_hour}' if new_hour != 0 else 12
        formatted_min = f"0{remaining_min}" if remaining_min < 10 else str(remaining_min)
        if days == 0:
            new_time = f'{formatted_hour}:{formatted_min} {start_text} '
        
        elif days == 1:
            new_time = f'{formatted_hour}:{formatted_min} {start_text} (next day)'
        else:
            new_time = f'{formatted_hour}:{formatted_min} {start_text} ({days} days later)'
        print(new_time)
            
    else:
        if total_hours > 24 :
            days+=1
        if start_text == 'PM' :
            new_hour = total_hours % hours
            print(new_hour)
            start_text = 'AM'
        elif start_text == 'AM' and total_hours > hours:
            new_hour = total_hours % hours
            print(new_hour)
        elif start_text == 'AM':
            start_text = 'PM'
        else:
            new_hour = total_hours
        
        if days == 0:
            new_time = f'{new_hour}:{total_min} {start_text} '
        
        elif days == 1:
            new_time = f'{new_hour}:{total_min} {start_text} (next day)'
        else:
            new_time = f'{new_hour}:{total_min} {start_text} ({days} days later)'
        print(new_time)








    return new_time
# def add_time(start, duration, start_day=None):
#     from datetime import datetime, timedelta

#     # Days of the week for reference
#     days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#     # Extract hours, minutes, and AM/PM from the start time
#     start_hours = int(start.split(':')[0])
#     minutes = start.split(':')[1]
#     start_minute = int(minutes.split(' ')[0])
#     start_text = minutes.split(' ')[1]  # AM or PM

#     # Convert start time to 24-hour format for calculations
#     if start_text == 'PM' and start_hours != 12:
#         start_hours += 12
#     elif start_text == 'AM' and start_hours == 12:
#         start_hours = 0

#     # Extract hours and minutes from the duration
#     duration_hours = int(duration.split(':')[0])
#     duration_minutes = int(duration.split(':')[1])

#     # Calculate the new total time in minutes
#     total_minutes = start_hours * 60 + start_minute + duration_hours * 60 + duration_minutes

#     # Calculate the new time
#     new_hours = (total_minutes // 60) % 24
#     new_minutes = total_minutes % 60

#     # Determine how many days later
#     days = total_minutes // (24 * 60)

#     # Convert new hours back to 12-hour format
#     new_text = 'AM' if new_hours < 12 else 'PM'
#     new_hours = new_hours % 12
#     new_hours = new_hours if new_hours != 0 else 12  # Adjust for 12-hour clock format

#     # Format minutes with leading zero
#     formatted_minutes = f"0{new_minutes}" if new_minutes < 10 else str(new_minutes)

#     # Determine the new day of the week if a starting day is provided
#     if start_day:
#         start_day = start_day.capitalize()
#         start_index = days_of_week.index(start_day)
#         new_day = days_of_week[(start_index + days) % 7]
#         day_part = f", {new_day}"
#     else:
#         day_part = ""

#     # Add information about days later
#     if days == 0:
#         days_later = ""
#     elif days == 1:
#         days_later = " (next day)"
#     else:
#         days_later = f" ({days} days later)"

#     # Construct the final new time
#     new_time = f"{new_hours}:{formatted_minutes} {new_text}{day_part}{days_later}"
#     return new_time


# Test Cases
print(add_time('11:59 PM', '24:05'))                     # '12:04 AM (2 days later)'
print(add_time('3:30 PM', '2:12', 'Monday'))             # '5:42 PM, Monday'
print(add_time('2:59 AM', '24:00', 'saturDay'))          # '2:59 AM, Sunday (next day)'
print(add_time('11:59 PM', '24:05', 'Wednesday'))        # '12:04 AM, Friday (2 days later)'
print(add_time('8:16 PM', '466:02', 'tuesday'))          # '6:18 AM, Monday (20 days later)'
