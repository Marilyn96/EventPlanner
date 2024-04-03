# This class encapuslates the functions required for the event scheduler application
# Author: Marilyn Mosala

from datetime import datetime

class EventScheduler:
    def __init__(self):
        self.eventCalendar = {}

    # This method adds an event to the calendar, given the event title, description, date and time
    def addEvent(self):
        print("____________________________________________________________________________________________________")
        print("You are about to enter an event")

        print("Event Title:")
        title = input()

        print("Event Description:")
        description = input()

        # validate date format
        dateFormat = "%Y-%m-%d"
        resultDate = False
        print("Event Date: *Please use the following format (YYYY-MM-DD)*")
        while not resultDate:
            date = input()
            try:
                resultDate = bool(datetime.strptime(date, dateFormat))
            except ValueError:
                resultDate = False
                print("Invalid date format. Please enter date using format YYYY-MM-DD")

        # validate time format
        dateFormat = "%H:%M"
        resultTime = False
        print("Event Time: *Please use the following format (HH:MM)*")
        while not resultTime:
            time = input()
            try:
                resultTime = bool(datetime.strptime(time, dateFormat))
            except ValueError:
                resultTime = False
                print("Invalid time format. Please enter time using format HH:MM:")

        # add the event to the calendar
        num = len(self.eventCalendar)        # The number of events currently in the calendar
        event = {"title": title,
                 "description": description,
                 "date": date,
                 "time": time}
        self.eventCalendar[title] = event
        print("____________________________________________________________________________________________________")
        print("The following event has been added: " + "\n")
        printFormat(title,description,date,time)

    # This method displays events that are currently in the calendar, prints an error if calendar is empty
    def displayEvents(self):
        if len(self.eventCalendar) == 0:
            print("____________________________________________________________________________________________________")
            print("There are currently no events in the calendar")
        else:
            sortedDict = {i: j for i, j in sorted(self.eventCalendar.items(),key=lambda  x: (x[1]["date"], x[1]["time"]))}
            print("____________________________________________________________________________________________________")
            print("Here is the list of events sorted by date and time:\n")
            for i in sortedDict:
                printFormat(sortedDict[i]["title"],sortedDict[i]["description"],sortedDict[i]["date"],
                            sortedDict[i]["time"])

    # This method deletes an event in the calendar given the event title, throws exception if it does not exist
    def deleteEvent(self):
        print("____________________________________________________________________________________________________")
        print("What is the title of the event you wish to delete?")
        title = input()
        try:
            del(self.eventCalendar[title])
            print("Event Successfully Deleted")
        except KeyError:
            print("No event with that title exists")


def printFormat(title,description, date, time):
    print("Title: " + title + "\n" +
          "Description : " + description + "\n" +
          "Date: " + date + "\n" +
          "Time: " + time + "\n")




