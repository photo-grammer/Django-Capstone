# Django Application

This is a Django application that can be built and run using venv and Docker.

## Prerequisites

- Docker
- Python latest
- Django

## Building and Running with venv

1. Clone the repository:

   ```shell
   git clone https://github.com/photo-grammer/Django-Capstone
   ```

2. Create and activate a virtual environment:

   ```shell
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

5. Start the Django development server:

   ```shell
   python manage.py runserver
   ```

6. Access the application in your web browser:

   ```
   http://localhost:8000/
   ```

## Building and Running with Docker

1. Clone the repository:

   ```shell
   git clone https://github.com/photo-grammer/Django-Capstone
   ```

2. Build the Docker image:

   ```shell
   docker build -t django-app .
   ```

3. Run the Docker container:

   ```shell
   docker run -p 8000:8000 django-app
   ```

4. Access the application in your web browser:

   ```
   http://localhost:8000/
   ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

