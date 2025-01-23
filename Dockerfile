FROM python:3.12.7

ENV PYTHONUNBBUFFERED=1

WORKDIR /recipesite

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY recipesite .

CMD ["gunicorn", "recipesite.wsgi:application", "--bind", "0.0.0.0:8000"]