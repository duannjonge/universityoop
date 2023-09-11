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
    """Add a new student to the database with associated units"""
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

if __name__ == '__main__':
    cli()
