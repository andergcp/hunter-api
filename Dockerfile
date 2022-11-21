# pull official base image
FROM python:3.8.15-bullseye

# set work directory
WORKDIR /usr/src/app

# install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# start uvicorn server
CMD ["uvicorn", "main:app"]