# build everything on top of this image
FROM python:3.10.1-slim-buster

# install vim just for fim
RUN apt-get update && apt-get install vim -y

# create a folder at /code, and cd into that folder
WORKDIR /code

# copy every from the current working directoy that into `/code`
# note: the directory is the one where this dockerfile is located
# this is equivalent to:
# COPY . .
COPY . /code

# this is the entrypoint
CMD ["bash"]