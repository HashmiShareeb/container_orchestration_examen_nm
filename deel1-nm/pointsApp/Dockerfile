FROM python:3.12.0-alpine as builder

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

FROM python:3.12.0-alpine

WORKDIR /app

# Copy only necessary files from the build stage
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY app.py . 
# Add other necessary files here
RUN pip install uvicorn
# Set environment variables if required
ENV FLASK_ENV=production

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]


