import streamlit as st
import pandas as pd
import altair as alt
from numerize import numerize

st.set_page_config(
    layout='wide'
)

st.title("Analisa PDRB per Kapita 6 Provinsi di Pulau Jawa Tahun 2021")

#Latar Belakang
st.markdown("""<div style="text-align: justify">
 
Berdasarkan data Badan Pusat Statistik (BPS), PDRB per kapita di Jawa Tengah pada tahun 2021 merupakan yang terendah di Pulau Jawa. Angka tersebut sebesar Rp38,67 juta, jauh di bawah rata-rata nasional sebesar Rp62,24 juta per tahun. Empat provinsi lainnya, yaitu DI Yogyakarta, Jawa Barat, Banten, dan Jawa Timur, juga memiliki PDRB per kapita lebih rendah dari rata-rata nasional. DKI Jakarta memiliki PDRB per kapita yang tertinggi di Pulau Jawa, yaitu Rp274,71 juta per tahun (Katadata, 2022).

PDRB (Produk Domestik Regional Bruto) per kapita merupakan salah satu indikator penting dalam mengukur tingkat kemakmuran suatu daerah. PDRB per kapita menggambarkan nilai tambah yang dihasilkan oleh suatu daerah dalam satu tahun dibagi dengan jumlah penduduknya. Dalam konteks Indonesia, PDRB per kapita menjadi salah satu indikator penting dalam menentukan tingkat kemajuan suatu provinsi atau daerah.

Berdasarkan paparan sebelumnya. Dilakukan analisa apakah benar PDRB per kapita di pulau jawa cenderung rendah. Berikut adalah hasil analisanya :
</div>
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
st.markdown("""<div style="text-align: justify; margin-bottom: 5.5em;">
 
Diagram diatas menunjukkan bahwa provinsi-provinsi di pulau jawa cenderung memiliki <span style="color:steelblue">PDRB per kapita rendah dibawah PDRB per kapita Nasional</span>. Hanya DKI Jakarta yang memiliki <span style="color:green">PDRB per kapita diatas rata-rata Nasional.</span> PDRB per kapita suatu daerah dapat dipengaruhi oleh UMP (Upah Minimum Provinsi), tingkat pengangguran, sektor usaha, jumlah penduduk, dll. Sehingga dilakukan analisa berdasarkan hipotesis-hipotesis berikut:
1.	Apakah PDRB per kapita di Pulau Jawa cenderung rendah karena memiliki UMP rendah?
2.	Apakah PDRB per kapita di Pulau Jawa cenderung rendah karena tingkat pengangguran yang tinggi?
3.	Apakah PDRB per kapita di Pulau Jawa cenderung rendah karena kurangnya sektor dengan upah gaji tinggi?


</div>
""", unsafe_allow_html=True)

ump_col, umr_col = st.columns(2)

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
    title='UMP Tiap Provinsi di Indonesia',
    height=500
)

ump_line = alt.Chart(data_ump[data_ump['Provinsi'] == 'INDONESIA']).mark_rule(color='green', strokeDash=[5, 2]).encode(
    y='2020:Q'
)

ump_chart = (ump_bar + ump_line)
with ump_col:
    st.altair_chart(ump_chart, use_container_width=True)

#Import data umr tertinggi
umr_tinggi = pd.read_excel('dataset/10 UMR Tertinggi 2021.xlsx')

with umr_col:
    st.dataframe(umr_tinggi, use_container_width=True)
    st.markdown("""<div style="text-align: right">
    Tabel 10 Kabupaten/Kota dengan UMR Tertinggi di Indonesia tahun 2021
    </div>
    """, unsafe_allow_html=True)

#Kesimpulan UMP
st.markdown("""<div style="text-align: justify">
 
Diagram diatas menunjukkan bahwa provinsi-provinsi di pulau jawa cenderung memiliki UMP rendah dibandingkan dengan rata-rata UMP Nasional. Hal ini menunjukkan bahwa UMP mempengaruhi PDRB per kapita di pulau jawa.

Setelah dianalisa lebih lanjut, 10 kabupaten/kota di Indonesia dengan UMR tertinggi di tahun 2021 yang ditunjukkan pada tabel diatas (Kompas.com, 2021). 10 kabupaten/kota tersebut berlokasi di pulau jawa. Sehingga UMP cenderung rendah karena UMR di tiap kabupaten/kota yang kurang merata.


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
 
Diagram diatas menunjukkan bahwa 3 provinsi memiliki tingkat pengangguran dibawah rata-rata nasional dan 3 provinsi memiliki tingkat pengangguran diatas rata-rata nasional yang salah satunya adalah DKI Jakarta yang memiliki PDRB per kapita tertinggi. Hal ini menunjukkan bahwa tingkat pengangguran tidak mempengaruhi PDRB per kapita di pulau jawa.

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

#Bar Chart Sektor
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
 
Diagram diatas menunjukkan bahwa provinsi-provinsi di pulau jawa cenderung memiliki persentase rendah terhadap distribusi PDRB 6 sektor dengan upah gaji tinggi dibandingkan dengan rata-rata nasional. Hal ini menunjukkan distribusi PDRB 6 sektor dengan upah gaji tinggi mempengaruhi PDRB per kapita di pulau jawa. 

Dari analisa hipotesis-hipotesis diatas, penulis memberikan saran bahwa:
1.	Pemerintah perlu membuat strategi untuk meningkatkan UMR di daerah-daerah dengan UMR rendah.
2.	Pemerintah dan stakeholder sektor terkait  perlu mengelola dan meningkatkan usaha di sektor dengan upah gaji tinggi.

Dari saran-saran tersebut, diharapkan PDRB per kapita di pulau jawa dapat meningkat dengan lebih cepat.
 
</div>
""", unsafe_allow_html=True)

#hitung data hijau
#data_sektor[data_sektor['Provinsi'] == 'INDONESIA']['Persen']


