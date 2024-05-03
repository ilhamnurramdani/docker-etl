# docker-etl
# ETL dengan PostgreSQL, Pandas, dan Python

Proyek ETL (Extract, Transform, Load) menggunakan Python, Pandas, dan PostgreSQL. Ini mengekstrak data acak, mentransformasikannya, dan memuatnya ke dalam database PostgreSQL.

## Persyaratan

- Python 3.12
- PostgreSQL 15
- Pandas 2.2.2
- NumPy 1.26.4

## Instalasi

1. Klon repository ini:

    ```bash
    git clone https://github.com/username_anda/nama_repository_anda.git
    cd nama_repository_anda
    ```

2. Siapkan PostgreSQL:
    - Pastikan Anda telah menginstal Docker.
    - Atur variabel lingkungan PostgreSQL Anda di dalam `.env`.

3. Bangun dan jalankan kontainer Docker:

    ```bash
    docker-compose up -d
    ```

4. Instal dependensi Python:

    ```bash
    pip install -r requirements.txt
    ```

## Penggunaan

1. Jalankan skrip Python:

    ```bash
    python app.py
    ```

## Deskripsi

- **Ekstrak**: Data acak dibuat menggunakan library `random` dan `numpy` Python dan disimpan dalam DataFrame Pandas.
- **Transformasi**: Data dalam DataFrame ditransformasi dengan menambahkan kolom untuk provinsi (`provinsi`) dan gaji (`gaji`).
- **Muat**: Data yang telah ditransformasi dimuat ke dalam tabel database PostgreSQL yang bernama `etl_transform`.

## Struktur Berkas

- `app.py`: Berisi skrip Python untuk pipeline ETL.
- `requirements.txt`: Daftar dependensi Python.
- `docker-compose.yml`: Berkas Docker Compose untuk menyiapkan PostgreSQL.
- `README.md`: Berkas ini.
