FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -m -u 1000 user
COPY . .
RUN mkdir -p static/tts_cache && chown -R user:user /app
USER user
ENV PORT=7860
EXPOSE 7860
CMD ["sh", "-c", "gunicorn -w 1 --threads 8 -b 0.0.0.0:${PORT} app:app"]
