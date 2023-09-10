import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Base, Student, Lecturer, Unit

engine = create_engine('sqlite:///university.db')
Base.metadata.create_all(engine)  # Create the database schema if it doesn't exist
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Student Name', help='Name of the student')
@click.option('--unit', prompt='Student Unit', help='Unit of the student')
def create_studentname(name, unit):
    """Add a new student to the database"""
    # Create a new Student instance using the ORM mechanism
    student = Student(name=name)
    
    # If you have a unit_id that corresponds to a unit in the 'units' table, set it here
    # student.unit_id = <unit_id>

    session.add(student)
    session.commit()
    click.echo(f'Student "{name}" created successfully.')



# @cli.command()
# @click.option('--name', prompt='Shipment Name', help='Name of the shipment')
# @click.option('--status', prompt='Shipment Status', help='Status of the shipment')
# @click.option('--recipient', prompt='Recipient Name', help='Name of the recipient')
# @click.option('--recipient-address', prompt='Recipient Address', help='Address of the recipient')
# @click.option('--carrier', prompt='Carrier Name', help='Name of the carrier')
# def create_shipment(name, status, recipient, recipient_address, carrier):
#     """Add a new shipment to the database with recipient, address, and carrier details"""

#     existing_recipient = session.query(
#         Recipient).filter_by(name=recipient).first()
#     if existing_recipient:
#         recipient_id = existing_recipient.id
#     else:

#         new_recipient = Recipient(name=recipient, address=recipient_address)
#         session.add(new_recipient)
#         session.commit()
#         recipient_id = new_recipient.id

#     existing_carrier = session.query(Carrier).filter_by(name=carrier).first()
#     if existing_carrier:
#         carrier_id = existing_carrier.id
#     else:

#         new_carrier = Carrier(name=carrier)
#         session.add(new_carrier)
#         session.commit()
#         carrier_id = new_carrier.id

#     shipment = Shipment(name=name, status=status,
#                         recipient_id=recipient_id, carrier_id=carrier_id)
#     session.add(shipment)
#     session.commit()
#     click.echo(
#         f'Shipment "{name}" has been created successfully with recipient "{recipient}" and carrier "{carrier}".')


# @cli.command()
# def list_shipments():
#     """Show all shipments"""
#     shipments = session.query(Shipment).all()
#     if not shipments:
#         click.echo('No shipments found.')
#     else:
#         click.echo(
#             '************************************************************Shipment History*******************************************')
#         for shipment in shipments:
#             click.echo(
#                 f'Recipient: {shipment.recipient.name}| Package:{shipment.name}| Carrier: {shipment.carrier.name}| Delivery Address: {shipment.recipient.address}| Status: {shipment.status}')


# @cli.command()
# @click.option('--name', prompt='Shipment Name', help='Name of the shipment to update')
# @click.option('--status', prompt='New Shipment Status', help='New status for the shipment')
# def update_status(name, status):
#     """Update shipment status"""
#     shipment = session.query(Shipment).filter_by(name=name).first()
#     if not shipment:
#         click.echo(f'Shipment "{name}" not found.')
#     else:
#         shipment.status = status
#         session.commit()
#         click.echo(f'Shipment "{name}" updated successfully.')


# @cli.command()
# @click.option('--name', prompt='Shipment Name', help='Name of the shipment to delete')
# def delete_shipment(name):
#     """Delete a shipment from the database"""

#     shipment = session.query(Shipment).filter_by(name=name).first()
#     if not shipment:
#         click.echo(f'Shipment "{name}" not found.')
#     else:

#         session.delete(shipment)
#         session.commit()
#         click.echo(
#             f'Shipment "{name}" has been deleted successfully.')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    cli()