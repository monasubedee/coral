FROM python:3.6
COPY . /coral
WORKDIR /coral
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./bin/app.py
