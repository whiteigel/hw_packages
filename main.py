from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

def current_date():
    cur_date = datetime.date.today()
    print(cur_date)
    return

if __name__ == '__main__':
    current_date()
    calculate_salary()
    get_employees()
