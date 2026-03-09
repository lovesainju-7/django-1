FROM python:3.12.3-slim AS builder

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final Stage 
FROM python:3.12.3-slim

WORKDIR /app

# Copy installed dependencies
COPY --from=builder /usr/local /usr/local

# Copy Django project
COPY . .

# Set environment variables to optimize Python performance.
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]