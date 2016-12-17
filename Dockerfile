FROM resin/raspberrypi3-python

#switch on systemd init system in container
ENV INITSYSTEM on

RUN apt-get update
RUN apt-get install -y libi2c-dev python-serial python3-smbus arduino minicom python-dev
RUN apt-get install -y python3-rpi.gpio

# pip install python deps from requirements.txt
# For caching until requirements.txt changes
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


RUN git clone https://github.com/WiringPi/WiringPi.git && cd WiringPi && ./build && echo "wiringPi Installed"

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["bash","start.sh"]