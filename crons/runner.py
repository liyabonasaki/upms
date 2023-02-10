import schedule
import time
import schedules


class Runner:
    def start_runner() -> None:
        schedules.schedules()
        schedule.run_pending()
        time.sleep(1)


if __name__ =='__main__':
    while True:
        Runner.start_runner()