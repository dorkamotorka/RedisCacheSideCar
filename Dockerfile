FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy everything from local to docker image
COPY . .

# Install the dependencies in the docker image
# Install pipenv and project dependencies
RUN pip install pipenv && \
    pipenv install --deploy --ignore-pipfile

EXPOSE 5000

CMD ["pipenv", "run", "python", "src/app.py"]
