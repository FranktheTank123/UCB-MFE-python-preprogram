# build everything on top of this image
FROM python:3.10.1-slim-buster

WORKDIR /docker_code

COPY code .
#COPY code /docker_code
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y make

CMD ["bash"]