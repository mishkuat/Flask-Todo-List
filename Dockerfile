# 1. Use an official, stable, and lightweight Python base image
FROM python:3.11-slim

# 2. Set the directory inside the container where our application files will sit
WORKDIR /app

# 3. Copy just the requirements file first. 
# (This is a trick! If you don't change your requirements, Docker skips downloading 
# your packages again next time you build, making it lightning fast.)
COPY requirements.txt .

# 4. Install the Python dependencies listed in requirements.txt
RUN apt-get update && apt-get install -y gcc libpq-dev build-essential --no-install-recommends \
 && pip install --no-cache-dir --break-system-packages -r requirements.txt \
 && apt-get purge -y --auto-remove gcc build-essential \
 && rm -rf /var/lib/apt/lists/*

# 5. Copy the rest of your app's files (app.py, templates/, static/) into the container
COPY . .

# 6. Inform Docker that the application inside the container listens on port 5000
EXPOSE 5000

# 7. Start the Flask application
CMD ["python", "main.py"]