FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# sanity check (IMPORTANT)
RUN python inference.py

CMD ["python", "inference.py"]
