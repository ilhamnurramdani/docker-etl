import pandas as pd
import numpy as np
from sqlalchemy import create_engine

user      = 'postgres'
password  = 'root'
hostname  = '127.0.0.1'
database  = 'etl'
port      = '5434'
conn_string = f'postgresql://{user}:{password}@{hostname}:{port}/{database}'
engine      = create_engine(conn_string)
conn        = engine.connect()

#Extract
query = "SELECT * FROM data_karyawan"
df = pd.read_sql(query, engine)

#Transform
#menambahkan column provinsi
provinsi = {'Jakarta' : 'DKI JAKARTA', 'Bogor':'JAWA BARAT', 'Depok':'JAWA BARAT', 'Tangerang':'BANTEN', 'Semarang': 'JAWA TENGAH', 'Surabaya':'JAWA TIMUR'}
df['provinsi'] = df['asal_kota'].map(provinsi)
#menambahkan gaji
gaji = {'Insinyur': 5000000, 'Pengusaha': 9500000, 'Guru': 2500000, 'Sales': 3000000, 'Koki': 4000000, 'Satpam': 4500000}
df.insert(loc=3, column='gaji', value=df['pekerjaan'].map(gaji))

#Perhitungan statistik sederhana
#Rata-rata Usia dan gaji Berdasarkan Pekerjaan
rata_usia_gaji_by_perkerjaan = df.groupby('pekerjaan').agg({'usia' : 'mean', 'gaji':'mean'}).reset_index()

# Jumlah Orang dari Setiap Kota
jumlah_orang_setiap_kota = df['asal_kota'].value_counts()

#Pekerjaan Paling Umum di Setiap Provinsi
pekerjaan_paling_umum_provinsi = df.groupby('provinsi')['pekerjaan'].agg(lambda x : x.mode().iloc[0])

print('Rata-rata Usia dan gaji Berdasarkan Pekerjaan : ')
print(rata_usia_gaji_by_perkerjaan)
print()
print('Jumlah Orang dari Setiap Kota :')
print(jumlah_orang_setiap_kota)
print()
print('Pekerjaan Paling Umum di Setiap Provinsi : ')
print(pekerjaan_paling_umum_provinsi)

# Simpan DataFrame ke dalam tabel di database menggunakan engine SQLAlchemy
df.to_sql("data_karyawan_transform", engine, if_exists='replace', index=False)

print('SELESAI!!!')