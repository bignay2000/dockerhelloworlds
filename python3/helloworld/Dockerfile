#To Build:	    docker build --no-cache=true -t helloworld --build-arg VENDOR_TAG=latest .
#To Run:        docker run -d -t --name helloworld -h helloworld helloworld
#To Login:      docker exec -it helloworld bash
#Compose:       docker-compose up -d --build

ARG VENDOR_TAG
FROM alpine:${VENDOR_TAG}

RUN apk update

# include needed python 3
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add --update --no-cache bash

ENV PYTHON3_SLEEP="30"

# copy source files over
RUN mkdir -p /opt/helloworld
WORKDIR /opt/helloworld

COPY ./*.py /opt/helloworld/.
COPY ./*.sh /opt/helloworld/.

RUN chmod 0755 /opt/helloworld/entrypoint.sh
RUN chmod 0755 /opt/helloworld/*.py

ENTRYPOINT ["/opt/helloworld/entrypoint.sh"]