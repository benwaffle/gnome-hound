FROM ubuntu
WORKDIR /root
RUN apt-get -y update \
    && apt-get -y install git make autoconf autotools-dev gettext pkg-config yelp-tools
RUN git clone git://git.gnome.org/jhbuild \
    && cd jhbuild \
    && ./autogen.sh \
    && make \
    && make install
ADD gen-conf.py /gen-conf.py
RUN /gen-conf.py

FROM etsy/hound
COPY --from=0 /root/config.json /data/config.json
VOLUME /db
EXPOSE 6080
