import time
import schedule
import tasks


def schedules() -> [None]:

    """ 1 min """
    schedule.every(1).minutes.do(tasks.tasks())

    # """ 1 hour """
    # schedule.every().hour.do(tasks.tasks())
    #
    # """ bedtime jobs """
    # schedule.every().day.at("00:00").do(tasks.tasks())
    #
    # """ in between jobs """
    # schedule.every(5).to(10).minutes.do(tasks.tasks())
    #
    # """ every mondays run this job"""
    # schedule.every().monday.do(tasks.tasks())

    """ Every tuesday at 18:00 """
    schedule.every().tuesday.at("18:00").do(tasks.tasks())
