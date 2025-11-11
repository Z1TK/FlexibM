ARG PYTHON_VERISON=3.12
FROM python:${PYTHON_VERISON}-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

# COPY . .

CMD alembic upgrade head && uvicorn backend.src.main:app --reload --host 0.0.0.0 --port 8000