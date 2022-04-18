# FROM ubuntu:18.04
FROM python:3.6-alpine
# RUN apt-get update
# RUN apt-get install -y \
#     python3 \
#     python3-pip \
#     libcurl3-dev
    
# RUN apt-get install -y  gunicorn
RUN mkdir -p /application
COPY . /application
WORKDIR /application
RUN pip3 install -r requirements.txt
ENV PYTHONPATH="$PYTHONPATH:src/main/python/"
EXPOSE 8086
#ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf", "app:flask_jenkins_app", "--access-logfile", "-", "--error-logfile", "-" ,"--log-level", "debug"]
ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf", "app:flask_jenkins_app"]
# ENTRYPOINT ["python3"]
# CMD ["src/main/python/app.py"]
