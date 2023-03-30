FROM python:3.11.2-alpine

EXPOSE 8000

WORKDIR /code

RUN pip install --upgrade pip
RUN apk add gcc musl-dev libffi-dev
RUN pip install pdm

COPY . /code

RUN pdm install --prod

CMD ["pdm", "run", "uvicorn", "src.core.main:app", "--host", "0.0.0.0", "--port", "8000"]