import pandas as pd
import numpy as np
from random import choice
import psycopg2

# Koneksi ke database PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="etl",
    user="postgres",
    password="root"
)

# Membuat kursor untuk eksekusi query
cur = conn.cursor()

#Extract
rows = 12
nama = ['Agus', 'Supri', 'Rendi', 'Ujang', 'Asep', 'Tatang']
pekerjaan = ['Insinyur', 'Pengusaha', 'Guru', 'Sales', 'Koki', 'Satpam']
asalkota = ['Jakarta','Bogor','Depok','Tangerang','Semarang','Surabaya']

df = pd.DataFrame({
    'nama' : [choice(nama) for x in range(rows)],
    'usia' : np.random.randint(20, 60, size = rows),
    'pekerjaan' : [choice(pekerjaan) for x in range(rows)],
    'asal_kota' : [choice(asalkota) for x in range(rows)],
})

#Transform
#menambahkan column provinsi
provinsi = {'Jakarta' : 'DKI JAKARTA', 'Bogor':'JAWA BARAT', 'Depok':'JAWA BARAT', 'Tangerang':'BANTEN', 'Semarang': 'JAWA TENGAH', 'Surabaya':'JAWA TIMUR'}
df['provinsi'] = df['asal_kota'].map(provinsi)
#menambahkan gaji
gaji = {'Insinyur': 5000000, 'Pengusaha': 9500000, 'Guru': 2500000, 'Sales': 3000000, 'Koki': 4000000, 'Satpam': 4500000}
df.insert(loc=3, column='gaji', value=df['pekerjaan'].map(gaji))
df

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

#load
for index, row in df.iterrows():
    cur.execute("""
        INSERT INTO etl_transform (nama, usia, pekerjaan, asal_kota, provinsi, gaji)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['nama'], row['usia'], row['pekerjaan'], row['asal_kota'], row['provinsi'], row['gaji']))

# Commit perubahan dan tutup koneksi
conn.commit()
cur.close()
conn.close()

print('SELESAI!!!')