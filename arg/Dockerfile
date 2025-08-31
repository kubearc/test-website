# Use a lightweight base image
FROM registry.access.redhat.com/ubi9/python-39

# --- Build-time ARGs ---
# These are only available during build
ARG APP_VERSION=1.0.0
ARG API_URL=https://default.api.local

# Example: use them inside build
RUN echo "Building MyApp version ${APP_VERSION} with API URL ${API_URL}" > /build-info.txt

# --- Runtime ENVs ---
# These are baked into the image, but can be overridden at runtime
ENV APP_NAME="MyApp" \
    APP_PORT=8080

# Working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install dependencies if present
RUN pip install --no-cache-dir -r requirements.txt || true

# Expose port
EXPOSE 8080

# Startup command
CMD ["python", "app.py"]
