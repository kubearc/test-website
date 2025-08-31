FROM registry.access.redhat.com/ubi9/python-39

# Build-time args
ARG APP_VERSION=1.0.0
ARG API_URL=https://default.api.local

# Runtime envs
ENV APP_VERSION=${APP_VERSION} \
    API_URL=${API_URL} \
    APP_NAME="MyApp" \
    APP_PORT=8080

WORKDIR /opt/app
COPY . .

# Install Flask directly (no requirements.txt needed)
RUN pip install --no-cache-dir flask

EXPOSE 8080

CMD ["python", "app.py"]
