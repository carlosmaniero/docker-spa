FROM ubuntu:14.04
MAINTAINER Carlos Maniero


# install python3.5
ADD https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz /opt/
WORKDIR /opt/
RUN tar xzvf Python-3.5.0.tgz
WORKDIR /opt/Python-3.5.0
RUN apt-get update --fix-missing
RUN apt-get install -y libssl-dev openssl build-essential
RUN ./configure
RUN make
RUN make install
RUN rm /usr/bin/python3
RUN ln -s /opt/Python-3.5.0/Python /usr/bin/python3

# Install Node.js and other dependencies
RUN apt-get install -y supervisor
RUN apt-get install -y libpq-dev
ADD https://bootstrap.pypa.io/get-pip.py .
RUN python3 get-pip.py
RUN mkdir -p /opt/app
WORKDIR /opt/app
ADD . .

RUN pip3 install -r requirements.txt

# Run the application
CMD ["sh", "start_django.sh"]
