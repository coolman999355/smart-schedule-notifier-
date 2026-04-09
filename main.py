from datetime import datetime, timedelta
import time
import smtplib
import json
import os
import threading
import uuid

json_file = "schedules.json"

app_password = input("Enter app password: ")
my_email = input("Enter your email: ")


def load_schedules():
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            try:
                return json.load(file)
            except:
                return []
    return []

def save_all_schedules(schedules):
    with open(json_file, "w") as file:
        json.dump(schedules, file, indent=4)


def add_schedule(name, year, month, day, hour, minute, deadline):
    schedules = load_schedules()

    schedule = {
        "id": str(uuid.uuid4()),  
        "name": name,
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "deadline": deadline,
        "reminder_sent": False,
        "deadline_sent": False
    }

    schedules.append(schedule)
    save_all_schedules(schedules)
    print(" Schedule added!")

def view_schedules():
    schedules = load_schedules()

    if not schedules:
        print(" No schedules.")
        return

    print("\n Your schedules:\n")
    for i, s in enumerate(schedules):
        print(
            f"{i+1}. {s['name']} | "
            f"{s['year']}/{s['month']}/{s['day']} "
            f"{s['hour']}:{s['minute']:02d} | "
            f"Deadline: {s['deadline']} | "
            f"Reminder: {s['reminder_sent']} | "
            f"Done: {s['deadline_sent']}"
        )

def delete_schedule(index):
    schedules = load_schedules()

    if 0 <= index < len(schedules):
        removed = schedules.pop(index)
        save_all_schedules(schedules)
        print(f" Deleted: {removed['name']}")
    else:
        print(" Invalid index")


def send_email(subject, body):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)

            message = f"Subject:{subject}\n\n{body}"

            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=message
            )

        print(f" Sent: {subject}")

    except Exception as e:
        print(" Email error:", e)


def mark_sent(schedule_id, key):
    schedules = load_schedules()

    for s in schedules:
        if s["id"] == schedule_id:
            s[key] = True

    save_all_schedules(schedules)


def check_schedules():
    print(" Reminder system running...")

    while True:
        schedules = load_schedules()
        now = datetime.now()

        for s in schedules:
            task_dt = datetime(
                s["year"], s["month"], s["day"],
                s["hour"], s["minute"]
            )

            reminder_time = task_dt - timedelta(minutes=10)

            if s["reminder_sent"] and s["deadline_sent"]:
                continue

            if reminder_time <= now < task_dt and not s["reminder_sent"]:
                send_email(
                    "Reminder",
                    f"Task '{s['name']}' is in 10 minutes!"
                )
                mark_sent(s["id"], "reminder_sent")
                continue

            if now >= task_dt and not s["deadline_sent"]:
                send_email(
                    "Deadline Reached",
                    f"Time for '{s['name']}'!"
                )
                mark_sent(s["id"], "deadline_sent")

        time.sleep(5)


def main_menu():
    while True:
        print("\n====== SMART SCHEDULER ======")
        print("1. Add")
        print("2. View")
        print("3. Delete")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            try:
                name = input("Task: ")
                year = int(input("Year: "))
                month = int(input("Month: "))
                day = int(input("Day: "))
                hour = int(input("Hour: "))
                minute = int(input("Minute: "))
                deadline = input("Deadline description: ")

                add_schedule(name, year, month, day, hour, minute, deadline)

            except:
                print(" Invalid input")

        elif choice == "2":
            view_schedules()

        elif choice == "3":
            view_schedules()
            try:
                i = int(input("Delete number: ")) - 1
                delete_schedule(i)
            except:
                print(" Invalid")

        elif choice == "4":
            print(" Bye!")
            break

        else:
            print(" Invalid")


if __name__ == "__main__":
    threading.Thread(target=check_schedules, daemon=True).start()

    main_menu()