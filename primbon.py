import streamlit as st
from datetime import datetime

st.title("Insert Judul Here")

name = st.text_input("masukkan nama kamu:")

ttl = st.date_input(
    "masukkan tanggal lahir"
    ,min_value=datetime.strptime('1945-01-01','%Y-%m-%d'))

hari_lahir_num = ttl.isoweekday()

hari = {
    1:"senin",
    2:"selasa",
    3:"rabu",
    4:"kamis",
    5:"jumat",
    6:"sabtu",
    7:"minggu"
}

watak = {
    1:
    """Apabila seseorang lahir di hari Senin, mereka biasanya adalah sosok yang sangat ceria, murah senyum, dan menyenangkan.""",
    2:
    """Orang yang lahir di hari Selasa juga terkenal rupawan dan berkharisma sama menariknya seperti yang lahir di hari Senin.""",
    3:
    """Orang yang lahir di hari Rabu dikenal sebagai sosok yang dermawan dan penuh kasih sayang.""",
    4:
    """Orang yang lahir di hari Kamis terkenal sebagai pekerja keras yang pantang menyerah. Baginya, bekerja sudah bagaikan nafas untuknya.""",
    5:
    """Orang yang lahir di hari jumat biasanya sangat suka jalan-jalan, serta mencari pengalaman baru setiap harinya.""",
    6:
    """Mereka yang lahir pada hari Sabtu juga juga suka petualangan dan hal-hal baru.""",
    7:
    """Pada dasarnya, orang-orang yang terlahir di hari Minggu dikenal sebagai pribadi menyenangkan, bijaksana, sabar dan selalu tampak ceria meski sedang dirundung masalah berat."""
}

st.subheader(f'Hello, {name}!')
st.subheader(f'Kamu lahir dihari {hari[hari_lahir_num]}')
st.write({watak[hari_lahir_num]})


