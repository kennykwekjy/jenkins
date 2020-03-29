FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
EXPOSE 8000
# ENTRYPOINT ["python"]
CMD ["python", "app.py"]
