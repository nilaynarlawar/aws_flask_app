FROM python:3.9-alpine

RUN apk add --no-cache gcc
RUN apk add build-base
RUN apk add linux-headers
RUN apk add libc-dev
RUN pip install pipenv

ENV PROJECT_DIR .

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pipenv install --system --deploy

EXPOSE 5000

COPY . .

ENTRYPOINT ["python"]
 
CMD ["app.py"]
