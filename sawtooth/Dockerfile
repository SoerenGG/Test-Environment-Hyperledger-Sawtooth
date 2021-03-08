FROM ubuntu:bionic

RUN apt-get update \
 && apt-get upgrade -y

RUN apt-get install -y gnupg
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN apt-get install -y sudo
RUN apt-get install -y software-properties-common
RUN apt-get install -y git
RUN apt-get install -y python3-pip

# install sawtooth, sdk, and other
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8AA7AF1F1091A5FD
RUN add-apt-repository 'deb [arch=amd64] http://repo.sawtooth.me/ubuntu/chime/stable bionic universe'
RUN apt-get update

RUN apt-get install -y sawtooth
RUN apt-get install -y sawtooth-devmode-engine-rust

RUN dpkg -l '*sawtooth*'

RUN pip3 install grpcio grpcio-tools protobuf
RUN pip3 install --upgrade protobuf

# COPY FILES AND SCRIPTS
COPY cleanup.sh /tmp/
COPY my_wrapper_script.sh /tmp/

WORKDIR /tmp

# system setup
RUN sawtooth keygen my_key \
	&& sawadm keygen \
	&& sawset genesis --key $HOME/.sawtooth/keys/my_key.priv \
	&& sawset proposal create \
	--key $HOME/.sawtooth/keys/my_key.priv \
	sawtooth.consensus.algorithm.name=Devmode \
	sawtooth.consensus.algorithm.version=0.1 -o config.batch \
	&& sawadm genesis config-genesis.batch config.batch \
