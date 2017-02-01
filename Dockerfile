FROM python:3.4-onbuild
RUN [ "python", "./manage.py", "makemigrations"]
RUN [ "python", "./manage.py", "migrate"]
#RUN [ "python", "./manage.py", "test", "system"]
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
