# build everything on top of this image
FROM python:3.10.1-slim-buster

WORKDIR /temp

COPY code .

RUN apt-get update && apt-get -y install make
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash"]