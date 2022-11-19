import timer

user_input = ""
is_started = False
print("'start'- start time, 'stop'- stop time and save total, 'close'- close program \n")

while user_input != "close":
    user_input = input("-")

    if user_input == "start":
        start = timer.report_time()
        print("start time: " + start.strftime("%H:%M:%S"))
        is_started = True
    elif user_input == "stop" and is_started:
        end = timer.report_time()
        total = timer.calculate_total_time(start, end)
        print("end time: " + end.strftime("%H:%M:%S"))
        print("Total: " + total)
        timer.save_to_file(timer.calculate_date(start,end), start, end, total)
        is_started = False
    elif user_input == "stop" and not is_started:
        print("Must start timer before stopping")
    else:
        print("try recognized command: \n'start'- start time, 'stop'- stop time and save total, 'close'- close program \n")