FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

# Instal netcat-openbsd
RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install -r requirements.txt

COPY . .

# Salin wait-for-it.sh ke dalam container
COPY wait-for-it.sh /wait-for-it.sh

# Berikan izin eksekusi pada wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Set izin pada direktori kerja
RUN chmod -R 755 /app

# Gunakan wait-for-it.sh untuk menunggu MySQL siap sebelum menjalankan server Django
CMD ["/wait-for-it.sh", "db:3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
