FROM python:3.11

# Set the working directory
WORKDIR /app

# Set environmental variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy over the requirements file and install the dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r ./requirements.txt

# Copy over the source code
COPY . .

# Expose the port
EXPOSE 80

CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "80"]