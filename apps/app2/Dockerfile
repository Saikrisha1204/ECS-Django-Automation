FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files for production
RUN python manage.py collectstatic --noinput

# Expose application port
EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "project.wsgi:application","--bind", "0.0.0.0:8000","--workers", "3","--access-logfile", "-","--error-logfile", "-","--forwarded-allow-ips", "*"]
