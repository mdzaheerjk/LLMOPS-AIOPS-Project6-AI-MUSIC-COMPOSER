FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -e .

# Set environment variables
ENV PYTHONPATH=.

EXPOSE 8501
# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]