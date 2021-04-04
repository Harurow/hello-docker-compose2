FROM python:alpine3.13
WORKDIR /app
COPY . .
RUN pip install requests
ENTRYPOINT ["python"]
CMD ["-u", "app.py"]
