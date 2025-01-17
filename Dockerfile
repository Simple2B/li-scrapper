FROM python:3.9

# set working directory
WORKDIR /app

# set environment varibles
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONHASHSEED random
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on

# install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
ENV PATH="${PATH}:/root/.poetry/bin"
COPY poetry.lock .
COPY pyproject.toml .

COPY . /app

RUN poetry install

# CMD ["bash", "./start_server.sh"]
