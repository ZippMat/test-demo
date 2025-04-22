FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG INCLUDE_ENV=false

# Conditional copy of .env
RUN if [ "$INCLUDE_ENV" = "true" ]; then echo "Copying .env..." && cp .env /app/.env; else echo "Skipping .env"; fi

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
