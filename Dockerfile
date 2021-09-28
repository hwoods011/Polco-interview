from python:3.9.7-slim

workdir /app

expose 5000

add songs /app/songs
add requirements.txt /app/requirements.txt

run pip install -r requirements.txt


cmd ['python', '-m', 'flask', 'run']