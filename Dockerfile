FROM httpd:alpine

ENV PYTHONUNBUFFERED=1
RUN apk update
RUN apk upgrade
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY index.html /usr/local/apache2/htdocs
COPY reviews.json /usr/local/apache2/htdocs
COPY review.py /usr/local/apache2/htdocs
COPY script.py /usr/local/apache2/htdocs
COPY utils.py /usr/local/apache2/htdocs
COPY filter.cgi /usr/local/apache2/htdocs
COPY httpd.conf /usr/local/apache2/conf


