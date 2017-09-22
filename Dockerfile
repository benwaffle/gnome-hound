FROM ubuntu:latest
ADD gen-conf.py /gen-conf.py
WORKDIR /root
RUN apt-get -y update && apt-get -y install git make autoconf autotools-dev gettext pkg-config yelp-tools
RUN git clone git://git.gnome.org/jhbuild \
    && cd jhbuild \
    && ./autogen.sh \
    && make \
    && make install \
    && /gen-conf.py
