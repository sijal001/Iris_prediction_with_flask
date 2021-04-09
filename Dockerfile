FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP, https://unp.education
COPY ./main /usr/local/python/
EXPOSE 5000
WORKDIR /usr/local/python/
RUN pip install -r requirements.txt
CMD python predict_api.py