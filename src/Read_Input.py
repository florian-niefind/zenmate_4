#!/usr/bin/python2.7
#-*- encoding: utf-8 -*-
# @author: Florian Niefind
# @contact: nifflor@googlemail.com
# @date: 2016-03-21


def parse_input(input_file):
    meetings = []
    with open(input_file, 'rb') as infile:
        for line in infile:
            line = line.strip()
            line = line.split(' ')
            meeting_name = ' '.join(line[0:-1])
            duration = int(line[-1].strip('min'))
            meetings.append((meeting_name,duration))
    return meetings

