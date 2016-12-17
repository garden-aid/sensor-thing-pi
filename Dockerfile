FROM resin/rpi-raspbian

RUN apt-get update

## Look at this https://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/
## and this https://github.com/shaunmulligan/grovePi/blob/master/Dockerfile
RUN apt-get install -y sudo make gcc python python-dev python-pip git libi2c-dev python-serial i2c-tools python-smbus 
RUN python -V

RUN git clone https://github.com/WiringPi/WiringPi.git && cd WiringPi && ./build && echo "wiringPi Installed"

RUN git clone https://github.com/garden-aid/GrovePi.git && cd GrovePi/Software/Python && sudo python setup.py install

# pip install python deps from requirements.txt
# For caching until requirements.txt changes
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["bash","start.sh"]