#!/usr/bin/python2.7
#-*- encoding: utf-8 -*-
# @author: Florian Niefind
# @contact: nifflor@googlemail.com
# @date: 2016-03-21
from datetime import datetime, timedelta
from MeetingRoom import MeetingRoom
from Read_Input import parse_input

if __name__ == '__main__':
    
    #create meeting rooms
    M1 = MeetingRoom(1)
    M2 = MeetingRoom(2)

    #read all meetings
    all_meetings = parse_input('Test_Input.txt')

    #sort all meetings
    from operator import itemgetter
    all_meetings_sorted = sorted(all_meetings, key=itemgetter(1),reverse=True) 

    #odd-even split the sorted meetings across the two rooms    
    events_M1 = []
    events_M2 = []
    for meeting_ix in xrange(len(all_meetings_sorted)):
        if meeting_ix % 2 == 0:
            events_M2.append(all_meetings_sorted[meeting_ix])
        else:
            events_M1.append(all_meetings_sorted[meeting_ix])

    #assert that event fit into timeslots
    assert((sum([x[1] for x in events_M1])/15) < sum(M1.available))
    assert((sum([x[1] for x in events_M2])/15) < sum(M2.available))

    #fill the events
    for event in events_M1:
        M1.schedule_meeting(event[0],timedelta(minutes=event[1]))
    for event in events_M2:
        M2.schedule_meeting(event[0],timedelta(minutes=event[1]))

    #plot the results
    M1.show_schedule_by_events()
    print
    M2.show_schedule_by_events()

