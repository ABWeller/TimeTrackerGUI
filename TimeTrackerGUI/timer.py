import datetime as dt

def report_time():
    """
    This is just here for readability and future changes
    :return: datetime object: the current recorded time when this function is called
    """
    return dt.datetime.now()


def calculate_total_time(start_time, end_time):
    """

    :param start_time: First datetime object recorded
    :param end_time: last datetime object recorded
    :return: string: calculated total time between start_time and end_time
    """

    total_time = end_time - dt.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
    return total_time.strftime("%H:%M:%S")

def calculate_date(start_time, end_time):
    """

    :param start_time: First datetime object recorded
    :param end_time: last datetime object recorded
    :return: string: 1 date if there is no rollover, 2 dates if there is rollover
    """

    if start_time.date() != end_time.date():
        return start_time.strftime("%m/%d/%y") + " - " + end_time.strftime("%m/%d/%y")
    else:
        return end_time.strftime("%m/%d/%y")

def save_to_file(date, startTime, endTime, totalTime, note):
    """
    saves time values separated by commas
    :param date: str
    :param startTime: datetime object
    :param endTime: datetime object
    :param totalTime:
    :param note: note string should include its own comma at the beginning
    :return:
    """
    filler = ","
    with open("timeArchives.txt", "a+", encoding="utf8") as f:
        f.write(str(date + filler + startTime.strftime("%H:%M:%S") + filler + endTime.strftime("%H:%M:%S") + filler + totalTime + note + "\n"))
