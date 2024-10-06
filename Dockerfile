# Use the official Python 3 image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN pip3 install agentql asyncio playwright python-dotenv pymongo flask

# Install Playwright browsers
RUN playwright install

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libdbus-1-3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libatspi2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Command to run when the container starts
# CMD ["python3", "query.py"]
CMD ["python3", "start.py"]
