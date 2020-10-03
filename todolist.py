# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker
import calendar

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
rows = session.query(Table).all()
today = datetime.today()
day_names = list(calendar.day_name)


def menu_choice():
    choice1 = int(input("1) Today's tasks\n2) Week's Tasks\n3) All Tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit \n>"))
    print()
    return choice1


while True:
    choice = menu_choice()
    if choice == 0:
        print("Bye!")
        break
    elif choice == 1:
        print("Today {} {}:".format(today.day, today.strftime('%b')))
        if not rows:
            print("Nothing to do!")
            print()
        else:
            rows_today = session.query(Table).filter(Table.deadline == today.date()).all()
            line = 0
            for r in rows_today:
                line += 1
                print("{}. {}".format(line, r.task))
            print()
    elif choice == 2:
        daynum = 7
        for n in range(daynum):
            rows_per_date = session.query(Table).filter(Table.deadline == today.date() + timedelta(days=n)).all()
            if not rows_per_date:
                curdate = today.date() + timedelta(days=n)
                print("{} {} {}:".format(day_names[curdate.weekday()], curdate.day, curdate.strftime('%b')))
                print("Nothing to do!")
                print()
            else:
                print("{} {} {}:".format(day_names[rows_per_date[0].deadline.weekday()], rows_per_date[0].deadline.day, rows_per_date[0].deadline.strftime('%b')))
                line1 = 0
                for r in rows_per_date:
                    line1 += 1
                    print("{}. {}".format(line1, r.task))
                print()
    elif choice == 3:
        all_rows = session.query(Table).all()
        sorted_all_rows = sorted(all_rows, key=lambda x: x.deadline)
        print("All tasks:")
        line2 = 0
        for r in sorted_all_rows:
            line2 += 1
            print("{}. {}. {} {}".format(line2, r.task, r.deadline.day, r.deadline.strftime('%b')))
        print()
    elif choice == 4:
        missed_tasks = session.query(Table).filter(Table.deadline < today.date())
        sorted_missed_tasks = sorted(missed_tasks, key=lambda x:x.deadline)
        if not missed_tasks:
            print("Missed tasks:")
            print("Nothing is missed\n")
        else:
            print("Missed tasks:")
            for r in sorted_missed_tasks:
                print("{}. {} {}".format(r.task, r.deadline.day, r.deadline.strftime('%b')))
            print()
    elif choice == 5:
        print("Enter task")
        new_task = input(">")
        print("Enter deadline")
        new_deadline = input(">")
        new_row = Table(task=new_task, deadline=datetime.strptime(new_deadline, '%Y-%m-%d'))
        session.add(new_row)
        session.commit()
        print("The task has been added!\n")
        rows = session.query(Table).all()
    elif choice == 6:
        all_rows = session.query(Table).all()
        sorted_all_rows = sorted(all_rows, key=lambda x: x.deadline)
        line2 = 0
        for r in sorted_all_rows:
            line2 += 1
            print("{}. {}. {} {}".format(line2, r.task, r.deadline.day, r.deadline.strftime('%b')))
        print()
        taskn = int(input("Choose the number of the task you want to delete: \n>"))
        session.delete(sorted_all_rows[taskn - 1])
        session.commit()
        print("The task has been deleted!\n")
    else:
        print("Invalid input")
