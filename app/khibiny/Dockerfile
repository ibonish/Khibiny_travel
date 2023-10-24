FROM python:3.7-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "khibiny.wsgi:application"]

# FROM python:3.9

# WORKDIR /app

# RUN pip install gunicorn==20.1.0

# COPY requirements.txt .

# RUN pip install -r requirements.txt --no-cache-dir

# COPY . .

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "khibiny.wsgi"] 
