import EventPlannerClass

def main():

    calendar = EventPlannerClass.EventScheduler()
    while True:
        print("____________________________________________________________________________________________________")
        print("What would you like to do? (1- Add Event, 2- Display Events, 3- Delete Event, C - Close Application)")
        option = input()
        if option == "1":
            calendar.addEvent()
        elif option == "2":
            calendar.displayEvents()
        elif option == "3":
            calendar.deleteEvent()
        elif option == "C":
            exit()

if __name__ == "__main__":
    main()