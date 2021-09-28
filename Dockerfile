from python:3.9.7-slim

run apt-get update
run apt-get install -y curl

workdir /app

expose 5000
add requirements.txt /app/requirements.txt

run pip install -r requirements.txt

add songs /app/songs
add schema.sql /app/
add seed.sql /app/




ENV FLASK_APP='songs.webapp'
ENV FLASK_ENV='development'

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]