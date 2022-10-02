FROM python:3.7

#COPY requirements.txt /opt/app/requirements.txt
#WORKDIR /opt/app
#RUN pip install -r requirements.txt
#RUN mkdir /app
#COPY . /app

WORKDIR /app
#RUN pip3 install -r requirements.txt
RUN pip3 install flask sklearn pandas gunicorn tensorflow tensorflow_io

ADD ./model ./model
ADD server.py server.py

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "server:app" ]


