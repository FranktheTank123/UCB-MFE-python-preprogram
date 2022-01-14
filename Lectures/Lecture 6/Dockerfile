# build everything on top of this image
FROM python:3.10.1-slim-buster

WORKDIR /code

COPY code .

RUN apt-get update && apt-get -y install make
RUN pip install -r requiremenets.txt

CMD ["bash"]