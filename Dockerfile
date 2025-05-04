# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your server script into the container
COPY server.py .

# (Optional) Install dependencies if needed
# If you use any external libraries, create requirements.txt and uncomment the lines below
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# By default, run the MCP server using standard input/output
CMD ["python", "server.py"]
