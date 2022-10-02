FROM python:3.7
#COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ADD ./models ./models
ADD app.py app.py 
EXPOSE 5000
CMD ["gunicorn", "--bind","0.0.0.0:5000", "server:app"]

