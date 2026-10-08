# UQ Hair

UQ Hair is a software system for the UQ Hair Salon. It allows the user to create, read, update and delete clients, staff, appointments, products and purchases.

## Installation

To use the software, unzip the folder and place it on the main salon computer. Make sure Python 3.10 or later is installed on the machine.

Install Jinja2:

    pip install Jinja2

Fill out the `database.py` file with the data for your salon.

## Usage

To use the software, run `main.py`:

    python -m main.py

The first time the software runs, it will prompt you to set a password. This can be reset by deleting the `login.txt` file.

Interaction with the software is through the terminal. Type in numbers to interact with the menus, then input data as necessary.

## Features

- Client management
- Staff management
- Appointment management
- Product management
- Purchase management
- Email receipts
- Appointment reminder emails
- Advertising emails
- Password-protected login

## Future Updates

If I had more time and skill, I would add:

- Text messaging for appointment reminders
- Automatic repeat bookings every 6 or 8 weeks
- An option to duplicate existing bookings

## Author

Sophie-Lea Riley

UQ College IT Project

## Acknowledgments

- Thea Koutsoukis (UQ Collage IT teacher) for guidance and support throughout the project.
- UQ College IT for the project brief and learning resources.
- Python documentation and standard library resources.
- Jinja2 documentation and examples.