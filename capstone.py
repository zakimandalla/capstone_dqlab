import streamlit as st
import pandas as pd
import altair as alt
from numerize import numerize

st.set_page_config(
    layout='wide'
)

st.title("Analisa PDRB per Kapita 6 Provinsi di Pulau Jawa dan Nasional Tahun 2021")

#Latar Belakang
st.markdown("""<div style="text-align: justify">
 
PDRB (Produk Domestik Regional Bruto) per kapita merupakan salah satu indikator penting dalam mengukur tingkat kemakmuran suatu daerah. PDRB per kapita menggambarkan nilai tambah yang dihasilkan oleh suatu daerah dalam satu tahun dibagi dengan jumlah penduduknya. Dalam konteks Indonesia, PDRB per kapita menjadi salah satu indikator penting dalam menentukan tingkat kemajuan suatu provinsi atau daerah.

Pulau Jawa merupakan salah satu pulau terbesar di Indonesia dan memiliki peran penting dalam perekonomian nasional. Terdapat enam provinsi di Pulau Jawa, yaitu Jawa Barat, Jawa Tengah, Jawa Timur, Banten, DKI Jakarta, dan Yogyakarta. Keenam provinsi ini memiliki perbedaan karakteristik dan potensi ekonomi yang berbeda-beda.

Berdasarkan data Badan Pusat Statistik (BPS), PDRB per kapita di Jawa Tengah pada tahun 2021 merupakan yang terendah di Pulau Jawa. Angka tersebut sebesar Rp38,67 juta, jauh di bawah rata-rata nasional sebesar Rp62,24 juta per tahun. Empat provinsi lainnya, yaitu DI Yogyakarta, Jawa Barat, Banten, dan Jawa Timur, juga memiliki PDRB per kapita lebih rendah dari rata-rata nasional. DKI Jakarta memiliki PDRB per kapita yang tertinggi di Pulau Jawa, yaitu Rp274,71 juta per tahun. PDRB per kapita atau PDB per kapita adalah indikator penting dalam mengukur tingkat kemakmuran suatu wilayah, menunjukkan tingkat pembangunan dan pendapatan penduduk (Katadata, 2022).</div>
""", unsafe_allow_html=True)

pulau_jawa = ['INDONESIA', 'DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH', 'JAWA TIMUR', 'BANTEN', 'DI YOGYAKARTA']

freq = st.selectbox("Pilih Data", ['Pulau Jawa','Seluruh Indonesia'])

#Function Pilih Data
def select_data(data, select_list):
    data = {
        'Pulau Jawa' : data[data['Provinsi'].isin(select_list)],
        'Seluruh Indonesia' : data
    }
    return data

#Import data pdrb per kapita
pdrbperkapita = pd.read_excel('dataset/PDRB Per Kapita-Rapi.xlsx')

#Bar Chart PDRB Per Kapita 2021
data_1 = select_data(pdrbperkapita, pulau_jawa)

pdrbperkapita_bar = alt.Chart(data_1[freq]).mark_bar().encode(
    alt.X('Provinsi', title='Provinsi'),
    alt.Y('HB2021', title='PDRB Per Kapita'),
    color=alt.condition(
        alt.datum['HB2021'] >= 62258.08,
        alt.value('green'),  
        alt.value('steelblue')  
    )
).properties(
    title='PDRB Per Kapita Tiap Provinsi di Indonesia',
    height=400
)

pdrbperkapita_line = alt.Chart(pdrbperkapita[pdrbperkapita['Provinsi'] == 'INDONESIA']).mark_rule(color='green', strokeDash=[5, 2]).encode(
    y='HB2021:Q'
)

pdrbperkapita_chart = (pdrbperkapita_bar + pdrbperkapita_line)
st.altair_chart(pdrbperkapita_chart,use_container_width=True)

#Kesimpulan PDRB Per Kapita
st.markdown("""<div style="text-align: justify">
 
PDRB per Kapita 6 Provinsi di Pulau Jawa, 5 diantaranya berada dibawah rata-rata pdrb nasional.
Selanjutnya dicari apakah faktor-faktor seperti UMP, Tingkat pengangguran, dan Sektor lapangan usaha tertentu mempengaruhi PDRB per Kapita suatu daerah.</div>
""", unsafe_allow_html=True)

#Import data ump
data_ump = pd.read_excel('dataset/UMP 2018-2020.xlsx')

#Bar Chart UMP
data_2 = select_data(data_ump, pulau_jawa)

ump_bar = alt.Chart(data_2[freq]).mark_bar().encode(
    alt.X('Provinsi', title='Provinsi'),
    alt.Y('2020', title='UMP 2020'),
    color=alt.condition(
        alt.datum['2020'] >= 2672371,
        alt.value('green'),  # Warna merah untuk provinsi di pulau jawa
        alt.value('steelblue')  # Warna default untuk provinsi lainnya
    )
).properties(
    title='UMP Tiap Provinsi di Indonesia'
)

ump_line = alt.Chart(data_ump[data_ump['Provinsi'] == 'INDONESIA']).mark_rule(color='green', strokeDash=[5, 2]).encode(
    y='2020:Q'
)

ump_chart = (ump_bar + ump_line)
st.altair_chart(ump_chart, use_container_width=True)

#Kesimpulan UMP
st.markdown("""<div style="text-align: justify">
 
Dari bar chart diatas kita tahu bahwa UMP 5 dari 6 provinsi di pulau jawa berada dibawah rata-rata nasional. Sehingga dapat dikatakan bahwa UMP mempengaruhi PDRB per Kapita suatu daerah.

</div>
""", unsafe_allow_html=True)

#Import Data Pengangguran
data_pengangguran = pd.read_excel('dataset/Tingkat Pengangguran.xlsx')

#Bar Chart Pengangguran
data_3 = select_data(data_pengangguran, pulau_jawa)

pengangguran_bar = alt.Chart(data_3[freq]).mark_bar().encode(
    alt.X('Provinsi', title='Provinsi'),
    alt.Y('Agustus 2021', title='Tingkat Pengangguran'),
    color=alt.condition(
        alt.datum['Agustus 2021'] <= 6.49,
        alt.value('green'),  # Warna merah untuk provinsi di pulau jawa
        alt.value('steelblue')  # Warna default untuk provinsi lainnya
    )
).properties(
    title='Tingkat Pengangguran Terbuka Agustus 2021 Tiap Provinsi di Indonesia'
)

pengangguran_line = alt.Chart(data_pengangguran[data_pengangguran['Provinsi'] == 'INDONESIA']).mark_rule(color='green', strokeDash=[5, 2]).encode(
    y='Agustus 2021:Q'
)

pengangguran_chart = (pengangguran_bar + pengangguran_line)
st.altair_chart(pengangguran_chart,use_container_width=True)

#Kesimpulan Pengangguran
st.markdown("""<div style="text-align: justify">
 
Dari bar chart diatas kita tahu bahwa Tingkat Pengangguran 3 Provinsi bernilai diatas rata-rata dan 3 lainnya dibawah rata-rata nasional. Sehingga Tingkat pengangguran mungkin tidak mempengaruhi PDRB per Kapita suatu daerah.

</div>
""", unsafe_allow_html=True)

#Import Data Rata2 upah gaji
gaji_rata2 = pd.read_excel('dataset/Rata-Rata Upah_Gaji.xlsx')

gaji_sort = gaji_rata2[['Sektor','Agustus 2021']].sort_values(by='Agustus 2021', ascending=False).reset_index()
gaji_sort.drop(columns='index',inplace=True)

#Show Table
st.markdown("##### Tabel Rata-Rata Upah Gaji per Sektor")
st.dataframe(gaji_sort, use_container_width=True)

#Pendekatan sektor
st.markdown("""<div style="text-align: justify">
 
Tabel diatas menampilkan rata-rata upah gaji per sektor usaha. Dari situ dilakukan perhitungan persentase distribusi PDRB daerah terhadap 6 sektor dengan upah gaji teratas.

</div>
""", unsafe_allow_html=True)

#Import Data Sektor
data_sektor = pd.read_excel('dataset/Persentase 6 Top Sektor di Jawa.xlsx')

#Bar Chart Pengangguran
sektor_bar = alt.Chart(data_sektor).mark_bar().encode(
    alt.X('Provinsi', title='Provinsi'),
    alt.Y('Persen', title='Persentase'),
    color=alt.condition(
        alt.datum['Persen'] >= 25.06,
        alt.value('green'),  # Warna merah untuk provinsi di pulau jawa
        alt.value('steelblue')  # Warna default untuk provinsi lainnya
    )
).properties(
    title='Persentase 6 Sektor dengan Rata-Rata Upah Gaji Teratas 2021'
)

sektor_line = alt.Chart(data_sektor[data_sektor['Provinsi'] == 'INDONESIA']).mark_rule(color='green', strokeDash=[5, 2]).encode(
    y='Persen:Q'
)

sektor_chart = (sektor_bar + sektor_line)
st.altair_chart(sektor_chart,use_container_width=True)

#Kesimpulan Sektor
st.markdown("""<div style="text-align: justify">
 
Dari bar chart diatas kita tahu bahwa 4 dari 6 Provinsi di pulau jawa bernilai dibawah rata-rata persentase nasional. Sehingga persentase DPRB 6 sektor teratas mempengaruhi PDRB per Kapita suatu daerah.

Sehingga penulis merekomendasikan untuk pemerintas dan pemilik usaha sektor terkait bekerja sama berinvestasi untuk meningkatkan segala aspek di sektor tersebut.
</div>
""", unsafe_allow_html=True)

#hitung data hijau
#data_sektor[data_sektor['Provinsi'] == 'INDONESIA']['Persen']