# smart-schedule-notifier-
Smart Scheduler

Smart Scheduler is a Python-based personal task scheduler and reminder system. It allows users to create, view, and delete tasks, with automated email reminders and notifications for upcoming deadlines. Designed for personal productivity, this program runs in the background and keeps users informed about their tasks in real-time.

🛠 Features
Add Tasks: Schedule tasks with date, time, and optional deadline descriptions.
View Tasks: Display all scheduled tasks in a readable format.
Delete Tasks: Remove tasks by selecting their index from the list.
Automated Email Reminders: Get email notifications 10 minutes before a task starts.
Deadline Notifications: Receive email alerts when a task deadline is reached.
Persistent Storage: Tasks are saved in a JSON file (schedules.json) to keep data between sessions.
Background Checking: Continuously runs a background thread to monitor tasks and send reminders automatically.
💻 Technologies Used
Python 3.x
smtplib for sending emails
threading for background task monitoring
json for persistent task storage
datetime for scheduling logic
uuid for unique task IDs
os for file handling
⚡ Usage
Clone the repository:
git clone https://github.com/yourusername/smart-scheduler.git
cd smart-scheduler
Run the program:
python scheduler.py
Enter your email credentials when prompted:
Your email address
App password (for Gmail or compatible SMTP servers)
Use the main menu to:
Add new tasks
View existing tasks
Delete tasks
Exit the program

The scheduler runs a background thread that checks for reminders and deadlines every 5 seconds.

📧 Email Setup
The program uses Gmail SMTP (smtp.gmail.com) by default.
For Gmail users, generate an App Password if using 2FA:
Google App Passwords
Make sure your email allows SMTP access.
📝 Notes
Task times are based on your local system time.
The program uses schedules.json to store tasks; do not delete this file unless you want to reset all tasks.
Email functionality requires a stable internet connection.
🔧 Future Improvements
GUI interface for easier task management
Support for recurring tasks
Integration with calendar apps (Google Calendar, Outlook)
Customizable reminder intervals
👤 Author

Hasan – 11-year-old Python enthusiast and robotics/AI programmer