#To Build:	    docker build --no-cache=true -t helloworld --build-arg VENDOR_TAG=latest .
#To Run:        docker run -d -t --name helloworld -h helloworld helloworld
#To Login:      docker exec -it helloworld bash
#Compose:       docker-compose up -d --build

ARG VENDOR_TAG
FROM mcr.microsoft.com/powershell:${VENDOR_TAG}

ENV POWERSHELL_SLEEP="30"

# copy source files over
RUN mkdir -p /opt/helloworld
WORKDIR /opt/helloworld

COPY ./*.ps1 /opt/helloworld/.
COPY ./*.sh /opt/helloworld/.
RUN chmod 0755 /opt/helloworld/*.ps1
RUN chmod 0755 /opt/helloworld/*.sh

ENTRYPOINT ["/opt/helloworld/entrypoint.sh"]