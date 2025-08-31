FROM registry.access.redhat.com/ubi9/python-39

# Build-time args
ARG APP_VERSION=1.0.0
ARG API_URL=https://default.api.local

# Runtime envs (copy from ARG)
ENV APP_VERSION=${APP_VERSION} \
    API_URL=${API_URL} \
    APP_NAME="MyApp" \
    APP_PORT=8080

# Workdir
WORKDIR /opt/app

# Copy source
COPY . .

# Write build info into a safe path
RUN echo "Building MyApp version ${APP_VERSION} with API URL ${API_URL}" > /tmp/build-info.txt

# Install dependencies if any
RUN pip install --no-cache-dir -r requirements.txt || true

EXPOSE 8080
CMD ["python", "app.py"]
