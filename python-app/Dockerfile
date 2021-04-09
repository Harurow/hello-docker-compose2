FROM python:alpine3.13
WORKDIR /app
COPY . .
RUN pip install requests
CMD ["python", "-u", "./src/app.py"]
