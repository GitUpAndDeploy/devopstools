# Start with a skinny Python base – like a light foundation for our house
FROM python:3.13-slim-bookworm
# Set directory inside the container. All commands after this happen here.
WORKDIR /app
# Copy important files into the container.
COPY requirements.txt .
COPY app.py .
# Install necessary Python libraries (our building materials)
RUN pip install --no-cache-dir -r requirements.txt
# Tell Docker that our app inside will listen on port 8888.
EXPOSE 8888
# Our fixed mission: Always run Python
ENTRYPOINT ["python"]
# When the container starts, run our Python app!
CMD ["app.py"]
