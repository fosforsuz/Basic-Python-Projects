from sqlalchemy import create_engine, Column, Integer, String, Date, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import date, datetime, time, timedelta
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    task = Column(String, default='Nothing to do!')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


def menu():
    return """1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit"""


def add_item(task, deadline):
    new_row = Task(task=task)
    session.add(new_row)
    try:
        new_row.deadline = datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("\nWrong date format. Must be: YYYY-MM-DD. The current date is set.")

    session.add(new_row)
    session.commit()
    print("\nThe task has been added!\n")


def query_all_tasks():
    print("All tasks:")
    rows = session.query(Task).order_by(Task.deadline).all()
    if len(rows) == 0:
        print('Nothing to do!\n')
    else:
        for i in range(0, len(rows)):
            row = rows[i]
            print(f"{i + 1}. {row.task}. {datetime.strftime(row.deadline, '%d %b')}")
        print('\n')


def query_today_tasks():
    rows = session.query(Task).filter(Task.deadline == datetime.today().date()).all()
    print(f"\nToday {datetime.strftime(datetime.today(), '%d %b')}:")
    if rows:
        for row in rows:
            print(f"{row.id}. {row.task}")
    else:
        print("Nothing to do!\n")


def query_week_tasks():
    today = datetime.today().date()
    for i in range(7):
        rows = session.query(Task).filter(Task.deadline == today).all()
        print(f"\n{datetime.strftime(today, '%A %d %b')}")
        if rows:
            for row in rows:
                print(f"{row.id}. {row.task}\n")
        else:
            print('Nothing to do!\n')
        today += timedelta(days=1)


def query_missed_tasks():
    rows = session.query(Task).filter(Task.deadline < datetime.today().date()).all()
    print("Missed tasks:")
    if rows:
        for row in rows:
            print(f"{row.id}. {row.task}. {datetime.strftime(row.deadline, '%d %b')}")
    else:
        print("Nothing is missed!")
    print()


def delete_task():
    rows = session.query(Task).order_by(Task.deadline).all()
    print("Choose the number of the task you want to delete:")
    if rows:
        for row in rows:
            print(f"{row.id}. {row.task}. {datetime.strftime(row.deadline, '%d %b')}")
        num = input()
        session.query(Task).filter(Task.id == num).delete()
        session.commit()
        print("The task has been deleted!")
    else:
        print("No tasks to delete")
    print()


def main():
    while True:
        print(menu())
        choice = int(input())
        if choice == 1:
            query_today_tasks()
        elif choice == 2:
            query_week_tasks()
        elif choice == 3:
            query_all_tasks()
        elif choice == 4:
            query_missed_tasks()
        elif choice == 5:
            task = input('\nEnter task\n')
            deadline = input("Enter deadline\n")
            add_item(task, deadline)
        elif choice == 6:
            delete_task()
        elif choice == 0:
            print('Bye!')
            session.close()
            exit()


if __name__ == '__main__':
    main()
