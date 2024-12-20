#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def time_to_sec(time):
    """Convert a time object to a single integer representing the number of seconds from midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two time objects using the new helper functions."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Modify the time object by adding/subtracting the given seconds using the new helper functions."""
    total_seconds = time_to_sec(time) + seconds
    # Ensure total seconds are within the valid range (0 to 86399)
    total_seconds = total_seconds % 86400
    new_time = sec_to_time(total_seconds)

    # Update the original time object with new values
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

    return None

def valid_time(t):
    """Check for the validity of the time object attributes:
       0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60
    """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
