#!/usr/bin/python2.7
#-*- encoding: utf-8 -*-
# @author: Florian Niefind
# @contact: nifflor@googlemail.com
# @date: 2016-03-21
 
from datetime import datetime, timedelta

class MeetingRoom():
    """
    Meeting room object
    """
    
    def __init__(self, room_uid, day = datetime.today()):
        """
        Initializes three corresponding lists, one with timestamps in 15 minute
        intervals, one with bools for availability and 1 with strings for 
        meeting names
        @param: day - datetime object of the day you want to schedule the 
                      meeting room for
        """
        
        self.name = 'Room %i'%(room_uid)
        #define possible start time for meetings as 9:00 and end time as 17:00
        start_time = day.replace(hour=9,minute=0,second=0,microsecond=0)
        end_time = day.replace(hour=17,minute=0,second=0,microsecond=0)
    
        self.times = [start_time]
        self.available = [True]
        self.event_name = ['']
        time_steps = (end_time - start_time).total_seconds()/(60*15) #/15
        for quarter in xrange(int(time_steps-1)):
            self.times.append(self.times[-1]+timedelta(minutes=15))
            if (self.times[-1] >= day.replace(hour=12,minute=0,second=0,microsecond=0) and 
                self.times[-1] < day.replace(hour=13,minute=0,second=0,microsecond=0)):
                self.available.append(False)
                self.event_name.append('Lunch')
            else:
                self.available.append(True)
                self.event_name.append('')

    def schedule_meeting(self, meeting_name, duration):
        """
        Schedules a meeting at the earliest available time
        @param: meeting_name - string with the name of the meeting which is 
                               filled into the event name list
        @param: duration - timedelta object of duration in minutes
        """
        #convert duration to time slots
        slots_needed = int(duration.total_seconds()/(60*15))
        #loop over slots
        for i in xrange(len(self.available)):
            #if enough time-slots are available
            if all(self.available[i:i+slots_needed]):
                self.available[i:i+slots_needed] = [False for x in xrange(slots_needed)]
                self.event_name[i:i+slots_needed] = [meeting_name for x in xrange(slots_needed)]
                break
                
    def show_schedule_by_slots(self):
        """
        Formatted printing of the meeting rooms schedule by time slots of 15 min
        """
        print '%s:'%(self.name)
        print 'Time, Available, Event Name'
        for time_slot in xrange(len(self.times)):
             print '%s, %s, %s'%(self.times[time_slot].time(),self.available[time_slot],self.event_name[time_slot])

    def show_schedule_by_events(self):
        """
        Printing similar to show_schedule_by_slots but prints events' starting
        times and durations.
        """
        print '%s:'%(self.name)
        current_event = 'DUMMY'
        for i in xrange(len(self.available)):
            if self.event_name[i] != current_event and not self.available[i]:
                print '%s %s %imin'%(self.times[i].strftime('%H:%M%p'), self.event_name[i],
                               sum([1 for x in self.event_name if x == self.event_name[i]])*15)
                current_event = self.event_name[i]

