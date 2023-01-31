ARG APP_IMAGE=python:3.11-alpine
FROM $APP_IMAGE AS base

# apk is here for numpy and pandas to compile correctly
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --prefix=/install -r /requirements.txt

FROM base
ARG DDF_SERVICE_PROJ_KEY_ARG
ENV DDF_SERVICE_PROJ_KEY=$DDF_SERVICE_PROJ_KEY_ARG
WORKDIR /project
COPY --from=builder /install /usr/local
ADD . /project

ENTRYPOINT ["python", "-m", "uvicorn", "main:app",  "--host", "0.0.0.0", "--port", "80"]