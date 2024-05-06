import pandas as pd
import numpy as np
from random import choice
from sqlalchemy import create_engine

user      = 'postgres'
password  = 'root'
hostname  = '127.0.0.1'
database  = 'etl'
port      = '5434'
conn_string = f'postgresql://{user}:{password}@{hostname}:{port}/{database}'
engine      = create_engine(conn_string)
conn        = engine.connect()


# ---------- Buat Ambil dan jadiin Table di database------
rows = 100
nama = ['Agus', 'Supri', 'Rendi', 'Ujang', 'Asep', 'Tatang']
pekerjaan = ['Insinyur', 'Pengusaha', 'Guru', 'Sales', 'Koki', 'Satpam']
asalkota = ['Jakarta','Bogor','Depok','Tangerang','Semarang','Surabaya']

df = pd.DataFrame({
    'nama' : [choice(nama) for x in range(rows)],
    'usia' : np.random.randint(20, 60, size = rows),
    'pekerjaan' : [choice(pekerjaan) for x in range(rows)],
    'asal_kota' : [choice(asalkota) for x in range(rows)],
})

# Menyimpan DataFrame ke dalam tabel di database
df.to_sql("data_karyawan", conn, if_exists='replace', index=False)

