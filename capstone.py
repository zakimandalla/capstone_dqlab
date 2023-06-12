import streamlit as st
import pandas as pd
import altair as alt
from numerize import numerize

st.set_page_config(
    layout='wide'
)

st.title("Analisa PDRB per Kapita 6 Provinsi di Pulau Jawa dan Nasional Tahun 2021")
st.markdown("""<div style="text-align: justify">
 
PDRB (Produk Domestik Regional Bruto) per kapita merupakan salah satu indikator penting dalam mengukur tingkat kemakmuran suatu daerah. PDRB per kapita menggambarkan nilai tambah yang dihasilkan oleh suatu daerah dalam satu tahun dibagi dengan jumlah penduduknya. Dalam konteks Indonesia, PDRB per kapita menjadi salah satu indikator penting dalam menentukan tingkat kemajuan suatu provinsi atau daerah.

Pulau Jawa merupakan salah satu pulau terbesar di Indonesia dan memiliki peran penting dalam perekonomian nasional. Terdapat enam provinsi di Pulau Jawa, yaitu Jawa Barat, Jawa Tengah, Jawa Timur, Banten, DKI Jakarta, dan Yogyakarta. Keenam provinsi ini memiliki perbedaan karakteristik dan potensi ekonomi yang berbeda-beda.

Berdasarkan data Badan Pusat Statistik (BPS), PDRB per kapita di Jawa Tengah pada tahun 2021 merupakan yang terendah di Pulau Jawa. Angka tersebut sebesar Rp38,67 juta, jauh di bawah rata-rata nasional sebesar Rp62,24 juta per tahun. Empat provinsi lainnya, yaitu DI Yogyakarta, Jawa Barat, Banten, dan Jawa Timur, juga memiliki PDRB per kapita lebih rendah dari rata-rata nasional. DKI Jakarta memiliki PDRB per kapita yang tertinggi di Pulau Jawa, yaitu Rp274,71 juta per tahun. PDRB per kapita atau PDB per kapita adalah indikator penting dalam mengukur tingkat kemakmuran suatu wilayah, menunjukkan tingkat pembangunan dan pendapatan penduduk (Katadata, 2022).</div>
""", unsafe_allow_html=True)

pdrbperkapita = pd.read_excel('dataset/PDRB Per Kapita-Rapi.xlsx')

freq = st.selectbox("Freq", ['Pulau Jawa','Seluruh Indonesia'])

data = {
    'Pulau Jawa' : pdrbperkapita[pdrbperkapita['Provinsi'].isin(['INDONESIA', 'DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH', 'JAWA TIMUR', 'BANTEN', 'DI YOGYAKARTA'])],
    'Seluruh Indonesia' : pdrbperkapita
}

pdrbperkapita_bar = alt.Chart(data[freq]).mark_bar().encode(
    alt.X('Provinsi', title='Provinsi'),
    alt.Y('HB2021', title='PDRB Per Kapita')
).properties(
    title='PDRB Per Kapita Tiap Provinsi di Indonesia'
)

st.altair_chart(pdrbperkapita_bar,use_container_width=True)

st.markdown("""<div style="text-align: justify">
 
Selanjutnya dicari mengapa demikian. Ada beberapa faktor yang mempengaruhi: UMP, Tingkat pengangguran, Sektor Usaha, dll.</div>
""", unsafe_allow_html=True)

data_ump = pd.read_excel('dataset/UMP 2018-2020.xlsx')

ump_bar = alt.Chart(data_ump).mark_bar().encode(
    alt.X('Provinsi', title='Provinsi'),
    alt.Y('2020', title='UMP 2020'),
    color=alt.condition(
        alt.FieldOneOfPredicate(field='Provinsi', oneOf=['DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH', 'JAWA TIMUR', 'BANTEN', 'DI YOGYAKARTA']),
        alt.value('green'),  # Warna merah untuk provinsi di pulau jawa
        alt.value('steelblue')  # Warna default untuk provinsi lainnya
    )
).properties(
    title='UMP Tiap Provinsi di Indonesia'
)

ump_line = alt.Chart(data_ump[data_ump['Provinsi'] == 'INDONESIA']).mark_rule(color='green', strokeDash=[5, 2]).encode(
    y='2020:Q'
)

chart = (ump_bar + ump_line)

st.altair_chart(chart, use_container_width=True)



st.markdown("""<div style="text-align: justify">
 
Kesimpulan dari bar chart UMP.

Lanjut analisa berikutnya</div>
""", unsafe_allow_html=True)

data_pengangguran = pd.read_excel('dataset/Tingkat Pengangguran.xlsx')

pengangguran_bar = alt.Chart(data_pengangguran).mark_bar().encode(
    alt.X('Provinsi', title='Provinsi'),
    alt.Y('Agustus 2021', title='Pengangguran 2021'),
    color=alt.condition(
        alt.FieldOneOfPredicate(field='Provinsi', oneOf=['DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH', 'JAWA TIMUR', 'BANTEN', 'DI YOGYAKARTA']),
        alt.value('green'),  # Warna merah untuk provinsi di pulau jawa
        alt.value('steelblue')  # Warna default untuk provinsi lainnya
    )
).properties(
    title='Tingkat Pengangguran Terbuka Tiap Provinsi di Indonesia'
)

st.altair_chart(pengangguran_bar,use_container_width=True)

st.dataframe(data_ump, use_container_width=True)