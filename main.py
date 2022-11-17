import Event_class

def main():
    print("Bugger")
    test = Event_class.Event_Schedule('Meeting', 2022, 11, 17, 17, 0, 'Discussing the project')
    print(f"Today you have a {test.event_name}")

if __name__ == '__main__':
    main()