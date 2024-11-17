FROM python:3.9-slim
WORKDIR /app
# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy application code
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
