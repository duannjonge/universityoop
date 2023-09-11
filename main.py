import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Base, Student, Lecturer, Unit

engine = create_engine('sqlite:///university.db')
Base.metadata.create_all(engine)  # Create the database schema if it doesn't exist
Session = sessionmaker(bind=engine)

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Session()  # Create a session and pass it to the Click context

@cli.command(name="add-student")
@click.option('--name', prompt='Student Name', help='Name of the student')
@click.option('--units', prompt='Student Units', help='Comma-separated list of units for the student')
def create_student(name, units):
    """ create student """
    session = click.get_current_context().obj  # Retrieve the session from the Click context

    # Split the units string into a list
    units_list = [unit.strip() for unit in units.split(',')]

    # Create a new Student instance
    student = Student(name=name)
    
    # Query and associate units with the student
    for unit_name in units_list:
        unit = session.query(Unit).filter_by(name=unit_name).first()
        if unit:
            student.units.append(unit)
        else:
            click.echo(f'Unit "{unit_name}" does not exist. Skipping.')

    session.add(student)
    session.commit()
    click.echo(f'Student "{name}" created successfully with units: {", ".join(units_list)}')




@cli.command(name="list-students")
def list_students():
    """ list students """
    session = click.get_current_context().obj  # Retrieve the session from the Click context

    students = session.query(Student).all()

    if not students:
        click.echo("No students found in the database.")
    else:
        click.echo("Student Names:")
        for student in students:
            click.echo(student.name)

@cli.command(name="delete-student")
@click.option('--name', prompt='Student Name', help='Name of the student to delete')
def delete_student(name):
    """Delete a student by name from the database."""
    session = click.get_current_context().obj  # Retrieve the session from the Click context

    # Query the student by name
    student = session.query(Student).filter_by(name=name).first()

    if not student:
        click.echo(f'Student "{name}" not found in the database.')
    else:
        # Delete the student
        session.delete(student)
        session.commit()
        click.echo(f'Student "{name}" has been deleted from the database.')

@cli.command(name="add-lecturer")
@click.option('--name', prompt='Lecturer Name', help='Name of the lecturer')
@click.option('--department', prompt='Lecturer Department', help='Department of the lecturer')
def create_lecturer(name, department):
    """Add Lecturer"""
    session = click.get_current_context().obj  # Retrieve the session from the Click context

    # Create a new Lecturer instance
    lecturer = Lecturer(name=name, department=department)

    session.add(lecturer)
    session.commit()
    click.echo(f'Lecturer "{name}" created successfully in the {department} department.')



#delete Lecturer
@cli.command(name="delete-lecturer")
@click.option('--lecturer-id', prompt='Lecturer ID', type=int, help='ID of the lecturer to delete')
def delete_lecturer(lecturer_id):
    """Delete a lecturer """
    session = click.get_current_context().obj  # Retrieve the session from the Click context

    # Query the lecturer by ID
    lecturer = session.query(Lecturer).filter_by(id=lecturer_id).first()

    if lecturer:
        department_name = lecturer.department  # Get the department name before deleting
        session.delete(lecturer)
        session.commit()
        click.echo(f'Lecturer ID {lecturer_id} and associated department "{department_name}" deleted successfully.')
    else:
        click.echo(f'Lecturer with ID {lecturer_id} not found in the database.')

#add units
@cli.command(name="add-unit")
@click.option('--name', prompt='Unit Name', help='Name of the unit to add')
def add_unit(name):
    """Add a new unit"""
    session = click.get_current_context().obj  # Retrieve the session from the Click context

    # Check if a unit with the same name already exists
    existing_unit = session.query(Unit).filter_by(name=name).first()

    if existing_unit:
        click.echo(f'Unit "{name}" already exists in the database. Skipping.')
    else:
        # Create a new Unit instance and add it to the session
        unit = Unit(name=name)
        session.add(unit)
        session.commit()
        click.echo(f'Unit "{name}" added successfully.')


@cli.command(name="delete-unit")
@click.option('--name', prompt='Unit Name', help='Name of the unit to delete')
def delete_unit(name):
    """Delete a unit """
    session = click.get_current_context().obj
    unit = session.query(Unit).filter_by(name=name).first()

    if unit:
        session.delete(unit)
        session.commit()
        click.echo(f'Unit "{name}" deleted successfully.')
    else:
        click.echo(f'Unit "{name}" not found.')
if __name__ == '__main__':
    cli()
