FROM python:3.7-alpine
LABEL maintainer="nguyen.ensma@gmail.com"
RUN pip install Flask &&\
    pip install Dash &&\
    pip install requests
#COPY src des
#ADD src des/
#EXPOSE 80
#ENV PATH /opt/anaconda3/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
WORKDIR /app
ADD app.py /app
ADD core.py /app
EXPOSE 8050
CMD ["python","app.py"]
