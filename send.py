from project import Project
import schedule
import time

if __name__ == '__main__':
    p = Project()

    schedule.every().day.at("08:00",'Europe/Moscow').do(p.send)

    hour = 60 * 60

    for i in range(hour):
        schedule.run_pending()
        time.sleep(1)
