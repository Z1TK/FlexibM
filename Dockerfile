ARG PYTHON_VERISON=3.12
FROM python:${PYTHON_VERISON}-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONNUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY . .

CMD ["python", "-m", "uvicorn", "backend.src.main:app", "--host=0.0.0.0", "--port=8000"]