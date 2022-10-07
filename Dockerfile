# set base image (host OS)
FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./src /app

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]

COPY . .
# set the working directory in the container
WORKDIR /python-docker

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "export","/python-docker/FLASK_APP=server.py"]
CMD [ "python3", "-m" , "flask", "run"]