FROM python:3.9
RUN mkdir /src
WORKDIR ./src
COPY . .
RUN pip install --upgrade setuptools pip wheel
RUN pip install -r requirements.txt