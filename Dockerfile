FROM rws2154/auto_docker_build
COPY main.py /main.py
COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
CMD python3 /main.py