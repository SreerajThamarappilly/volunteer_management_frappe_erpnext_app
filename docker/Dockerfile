# Use official Frappe Docker image
FROM frappe/erpnext:version-14

# Switch to root user
USER root

# Set the working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    pkg-config \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Switch back to default user (non-root)
USER frappe

# Copy the requirements file
COPY requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose ports
EXPOSE 8000 6379

# Start the Frappe server
CMD ["bench", "start"]
