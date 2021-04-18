FROM ubuntu

RUN apt-get update -y
RUN apt-get install -y \
    git \
    curl

#RUN apt-get update && apt-get install -y \
#    aufs-tools \
#    automake \
#    build-essential \
#    curl \
#    dpkg-sig \
#    libcap-dev \
#    libsqlite3-dev \
#    mercurial \
#    reprepro \
#    ruby1.9.1 \
#    ruby1.9.1-dev \
#    s3cmd=1.1.* \
#
#RUN rm -rf /var/lib/apt/lists/*

ADD /file.txt /home/root/
RUN cd ~
RUN mkdir slozka
CMD ["echo", "Oh, Hi mark"]
#ENTRYPOINT ["echo", "Oh, Hi mark"]
