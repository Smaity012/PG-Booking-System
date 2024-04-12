# PG Booking System

PG Booking System is a web-based application for managing bookings in a paying guest (PG) accommodation. It allows users to browse available rooms, book them, and view their booking history.
## Installation and Setup

1. **Clone the repository**:
    ```shell
    git clone https://github.com/Smaity012/PG-Booking-System.git
    ```

2. **Navigate to the project directory**:
    ```shell
    cd PG-Booking-System
    ```

3. **Create a virtual environment** (optional but recommended):
    ```shell
    python3 -m venv env
    source env/bin/activate
    ```

4. **Install the required dependencies**:
    ```shell
    pip install -r requirements.txt
    ```

5. **Set up the database**:
    ```shell
    python manage.py migrate
    ```

6. **Run the development server**:
    ```shell
    python manage.py runserver
    ```

7. Access the application at `http://localhost:8000`.


## Usage

1. **Register a new account** or log in with an existing account.
2. **Browse available rooms** on the homepage.
3. **Book a room** by selecting it and providing the necessary details.
4. **Manage your bookings** and view your booking history.


## Configuration

- Modify the database settings in `settings.py` to use your preferred database.
- Update other configurations such as `DEBUG`, `ALLOWED_HOSTS`, etc., in `settings.py` as needed.


## Contributing

Contributions are welcome! Please follow the guidelines in `CONTRIBUTING.md`.


## Contact

If you have any questions, feel free to reach out to [Sourav Maity](mailto:maitysourav012@gmail.com).


## Credits

- Built with [Django](https://www.djangoproject.com/) and [Bootstrap 4](https://getbootstrap.com/).
- Thanks to [Contributor Name] for their contributions.
