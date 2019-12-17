FROM docker
RUN apk add --no-cache --update python3 python3-dev  gcc build-base
COPY main.py /main.py
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
CMD python3 /main.py