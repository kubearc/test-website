FROM registry.access.redhat.com/ubi9/python-39

ARG APP_VERSION=1.0.0
ARG API_URL=https://default.api.local
ENV APP_VERSION=${APP_VERSION} \
    API_URL=${API_URL} \
    APP_NAME="MyApp" \
    APP_PORT=8080

WORKDIR /opt/app
COPY . .

# Optional: check what files got copied
RUN ls -l /opt/app

RUN pip install --no-cache-dir -r requirements.txt || true

EXPOSE 8080

# Adjust to your real entry point
CMD ["python", "app.py"]
