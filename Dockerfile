FROM python:3.8-buster
# can not use slim, some apt-get force 3.7 otherwise

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y --fix-missing\
  && apt-get install -y --no-install-recommends \
    apt-utils \
    locales \
    wget \
    ca-certificates \
  && apt-get clean

# UTF-8
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# Avoid installing python3- pacakge, might force 3.7 packages
RUN apt-get install -y --no-install-recommends \
    libfreetype6 \
    libfreetype6-dev \
    && apt-get clean

# Setup pip
RUN wget -q -O /tmp/get-pip.py --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
  && python3 /tmp/get-pip.py \
  && pip3 install -U pip \
  && rm /tmp/get-pip.py

RUN pip3 install \
    matplotlib \
    numpy \
    seaborn \
  && rm -rf /root/.cache/pip

RUN mkdir /dmc
WORKDIR /dmc
COPY *.py /dmc

ENV LC_ALL=C
CMD /bin/bash
