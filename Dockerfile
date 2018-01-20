FROM python:3.6-alpine

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/
ADD . /usr/src/app/
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;
EXPOSE 9090
CMD ["python", "app.py"]