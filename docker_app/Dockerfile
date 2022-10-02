FROM python:3.7

WORKDIR /app

RUN pip install pandas scikit-learn flask gunicorn xgboost

ADD ./model ./model
ADD server.py server.py

EXPOSE 3000

CMD [ "gunicorn", "--bind", "0.0.0.0:3000", "server:app" ]