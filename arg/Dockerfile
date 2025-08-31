FROM registry.access.redhat.com/ubi9/python-39

# Build-time args
ARG APP_VERSION=1.0.0
ARG API_URL=https://default.api.local

# Runtime envs
ENV APP_NAME="MyApp" APP_PORT=8080

# Working directory
WORKDIR /app
COPY . /app

# Write build info into app directory (writable)
RUN echo "Building MyApp version ${APP_VERSION} with API URL ${API_URL}" > /app/build-info.txt

# Install requirements if present
RUN pip install --no-cache-dir -r requirements.txt || true

EXPOSE 8080
CMD ["python", "app.py"]
