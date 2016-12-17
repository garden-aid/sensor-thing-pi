FROM resin/rpi-raspbian

RUN apt-get update
RUN apt-get install git wget make

## Look at this https://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/
RUN git clone https://github.com/DexterInd/GrovePi.git
RUN cd ./GrovePi/Script/ && head -n -191 ./install.sh > ./docker-i.sh && chmod +x ./docker-i.sh && ./docker-i.sh && echo "GrovePi installed"
 
# pip install python deps from requirements.txt
# For caching until requirements.txt changes
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["bash","start.sh"]