# Dockerfile for Debian/Ubuntu

FROM python:3.11

# Install system dependencies for GDAL and GEOS
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file first for better caching
COPY requirements.txt /code/

# Install the GDAL Python bindings
RUN pip install --no-cache-dir gdal==$(gdal-config --version)

# Install other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /code/

# Default command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
