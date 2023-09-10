import click
#request input from user

# Define data structures to store information
lecturers = []
units = []
students = []

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('department')
def add_lecturer(name, department):
    """Add a new lecturer."""
    lecturers.append({'name': name, 'department': department})
    click.echo(f"Lecturer '{name}' in '{department}' added.")

@cli.command()
@click.argument('code')
@click.argument('name')
def add_unit(code, name):
    """Add a new unit."""
    units.append({'code': code, 'name': name})
    click.echo(f"Unit '{code}' - '{name}' added.")

@cli.command()
@click.argument('student_id', type=int)
@click.argument('name')
@click.argument('unit_codes', nargs=-1)
def add_student(student_id, name, unit_codes):
    """Add a new student."""
    student_units = []
    for code in unit_codes:
        unit = next((u for u in units if u['code'] == code), None)
        if unit:
            student_units.append(unit)
        else:
            click.echo(f"Warning: Unit '{code}' not found.")

    students.append({'student_id': student_id, 'name': name, 'units': student_units})
    click.echo(f"Student '{name}' with ID '{student_id}' added to units: {unit_codes}.")

@cli.command()
@click.option('--lecturers', is_flag=True, help="List lecturers")
@click.option('--units', is_flag=True, help="List units")
@click.option('--students', is_flag=True, help="List students")
def list(lecturers, units, students):
    """List lecturers, units, or students."""
    if lecturers:
        for lecturer in lecturers:
            click.echo(f"Name: {lecturer['name']}, Department: {lecturer['department']}")
    if units:
        for unit in units:
            click.echo(f"Code: {unit['code']}, Name: {unit['name']}")
    if students:
        for student in students:
            unit_names = [unit['name'] for unit in student['units']]
            click.echo(f"Student ID: {student['student_id']}, Name: {student['name']}, Units: {', '.join(unit_names)}")

if __name__ == '__main__':
    cli()
