FROM python:3.11-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements and install psycopg2 dependencies
COPY ./requirements.txt /requirements.txt
RUN apk update
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt

# Creates a directory app in the container and copy the current directory to the container
WORKDIR /app
COPY ./src /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# File wsgi.py was not found. Please enter the Python path to wsgi file.
CMD ["gunicorn", "--bind", "0.0.0.0:5656", "app.wsgi"]
