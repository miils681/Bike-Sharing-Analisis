import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='whitegrid')

# Load dataset
@st.cache_data
def load_data():
    hour_df = pd.read_csv('data/hour.csv') 
    day_df = pd.read_csv('data/day.csv')    
    return hour_df, day_df

hour_df, day_df = load_data()

# Dashboard title
st.title(':bike: Bike Sharing Dashboard :bike:')

# Sidebar filtering data
st.sidebar.header("Filter Data")
selected_hour = st.sidebar.selectbox("Pilih Jam:", options=["All"] + sorted(hour_df['hr'].unique().tolist()), key='hour_filter')
selected_date = st.sidebar.selectbox("Pilih Tanggal:", options=["All"] + sorted(hour_df['dteday'].unique().tolist()), key='date_filter')

# Filter data
filtered_data = hour_df.copy()
if selected_hour != "All":
    filtered_data = filtered_data[filtered_data['hr'] == selected_hour]
if selected_date != "All":
    filtered_data = filtered_data[filtered_data['dteday'] == selected_date]

# 1. Waktu paling populer dalam penyewaan sepeda
st.header("Grafik penyewaan sepeda berdasarkan jam")

# Mengelompokkan dan menghitung total penyewaan per jam
popular_hour = hour_df.groupby('hr')['cnt'].sum().reset_index()

# Mengubah kolom jam menjadi format waktu (misalnya '00:00', '01:00', dll.)
popular_hour['hr_formatted'] = popular_hour['hr'].astype(str).str.zfill(2) + ':00'

# Plot line chart dengan format jam yang diubah
fig1, ax1 = plt.subplots()
sns.lineplot(data=popular_hour, x='hr_formatted', y='cnt', ax=ax1, marker='o', color=sns.color_palette("Blues", n_colors=3)[2])  # Menggunakan warna biru yang lebih gelap
ax1.set_title('Jumlah Penyewaan Sepeda Berdasarkan Jam')
ax1.set_xlabel('Jam')
ax1.set_ylabel('Jumlah Penyewaan')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')  # Mengatur rotasi agar label tidak tumpang tindih
st.pyplot(fig1)


# Menampilkan data yang difilter
st.subheader(f"Data Penyewaan untuk Jam: {selected_hour} dan Tanggal: {selected_date}")
st.write(filtered_data)

# 2. Pengaruh cuaca terhadap jumlah penyewaan
# Mengganti nilai cuaca dengan label deskriptif
hour_df['weather_desc'] = hour_df['weathersit'].replace({
    1: 'Clear, Few clouds, Partly cloudy',
    2: 'Mist + Cloudy, Mist + Broken clouds',
    3: 'Light Snow, Light Rain + Thunderstorm',
    4: 'Heavy Rain + Thunderstorm + Mist'
})

st.header("Jumlah penyewaan sepeda berdasarkan kondisi cuaca")

# Filter data untuk visualisasi
weather_effect = filtered_data.groupby('weathersit')['cnt'].sum().reset_index()

# Map nilai 'weathersit' ke deskripsi cuaca
weather_effect['weather_desc'] = weather_effect['weathersit'].replace({
    1: 'Clear, Few clouds, Partly cloudy',
    2: 'Mist + Cloudy, Mist + Broken clouds',
    3: 'Light Snow, Light Rain + Thunderstorm',
    4: 'Heavy Rain + Thunderstorm + Mist'
})

# Plot bar chart dengan deskripsi cuaca
fig2, ax2 = plt.subplots()
sns.barplot(data=weather_effect, x='weather_desc', y='cnt', ax=ax2, palette="Blues")  # Menggunakan palet biru
ax2.set_title('Pengaruh Cuaca Terhadap Penyewaan Sepeda')
ax2.set_xlabel('Situasi Cuaca')
ax2.set_ylabel('Jumlah Penyewaan')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=30, ha='right')
st.pyplot(fig2)


# 3. Tren penyewaan sepeda berdasarkan hari kerja dan libur
day_df['day_name'] = day_df['weekday'].replace({
    0: 'Minggu',
    1: 'Senin',
    2: 'Selasa',
    3: 'Rabu',
    4: 'Kamis',
    5: 'Jumat',
    6: 'Sabtu'
})

day_order = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu']
day_df['day_name'] = pd.Categorical(day_df['day_name'], categories=day_order, ordered=True)

st.header("Tren Penyewaan Sepeda Berdasarkan Hari Kerja dan Hari Libur")
weekday_trend = day_df.groupby('day_name')['cnt'].sum().reset_index()

# Plot bar chart for rentals per weekday
fig3, ax3 = plt.subplots()
sns.barplot(data=weekday_trend, x='day_name', y='cnt', ax=ax3, order=day_order, palette="Blues")  # Menggunakan palet biru
ax3.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari Kerja dan Hari Libur')
ax3.set_xlabel('Hari')
ax3.set_ylabel('Jumlah Penyewaan')
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=30, ha='right')
st.pyplot(fig3)

# 4. Perbandingan penyewaan oleh pengguna casual dan registered
st.header("Perbandingan Penyewaan oleh Pengguna Casual dan Registered")

# Mengelompokkan dan menghitung jumlah pengguna casual dan registered per jam
casual_registered_comparison = filtered_data.groupby('hr')[['casual', 'registered']].sum().reset_index()

# Mengubah kolom jam menjadi format waktu (misalnya '00:00', '01:00', dll.)
casual_registered_comparison['hr_formatted'] = casual_registered_comparison['hr'].astype(str).str.zfill(2) + ':00'

# Plot line chart dengan format jam yang diubah
fig4, ax4 = plt.subplots()
sns.lineplot(data=casual_registered_comparison, x='hr_formatted', y='casual', ax=ax4, label='Casual', marker='o', color=sns.color_palette("Blues", n_colors=3)[1])  # Menggunakan warna biru medium
sns.lineplot(data=casual_registered_comparison, x='hr_formatted', y='registered', ax=ax4, label='Registered', marker='o', color=sns.color_palette("Blues", n_colors=3)[2])  # Menggunakan warna biru yang lebih gelap
ax4.set_title('Perbandingan Penyewaan Sepeda oleh Casual dan Registered')
ax4.set_xlabel('Jam')
ax4.set_ylabel('Jumlah Penyewaan')
ax4.legend(title='Tipe Pengguna')
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45, ha='right')  # Mengatur rotasi agar label tidak tumpang tindih
st.pyplot(fig4)

# 5. Penyewaan berdasarkan waktu
st.header("Penyewaan Berdasarkan Waktu")
hour_df['time_of_day'] = pd.cut(hour_df['hr'], bins=[0, 6, 12, 18, 24], labels=['Malam', 'Pagi', 'Siang', 'Sore'])
time_trend = hour_df.groupby('time_of_day')['cnt'].sum().reset_index()

# Plot bar chart for rentals based on time of day
fig5, ax5 = plt.subplots()
sns.barplot(data=time_trend, x='time_of_day', y='cnt', ax=ax5, palette="Blues")  # Menggunakan palet biru
ax5.set_title('Jumlah Penyewaan Sepeda Berdasarkan Waktu')
ax5.set_xlabel('Waktu')
ax5.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig5)

st.write("Keterangan jam : Malam (00.01-6.00), Pagi (06.01-12.00), Siang (12.01-18.00), dan Sore (18.01-24.00)")
