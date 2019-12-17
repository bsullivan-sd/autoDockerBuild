FROM docker
RUN apk -U add python3
COPY main.py /main.py
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD python3 --version