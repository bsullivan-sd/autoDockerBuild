FROM docker
RUN apk -U add python3
COPY main.py /main.py
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements
CMD python3 --version