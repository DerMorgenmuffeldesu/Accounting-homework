import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from rich.console import Console 

def main():
    # Print current date
    console = Console()
    console.print(f"[bold blue]Current date:[/] {datetime.date.today()}")

    # Get employees and calculate their salaries
    employees = get_employees()
    for employee in employees:
        salary = calculate_salary(employee)
        console.print(f"[bold green]Employee {employee['name']} has a salary of[/] {salary}")

if __name__ == '__main__':
    main()