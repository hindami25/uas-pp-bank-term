import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from st_pages import Page, show_pages, add_page_title
import time
from streamlit_extras.stylable_container import stylable_container 
from annotated_text import annotated_text, annotation
from streamlit_extras.grid import grid 

# Mengatur tata letak halaman
st.set_page_config(layout="wide")

show_pages(
    [
        Page("pages/Informasi.py", "Informasi", "💡"),
        Page("Dashboard.py", "Dataset Dashboard", "🏠"),
        Page("pages/Prediksi.py", "Model Prediksi", "🎲"),
        Page("pages/Clustering.py", "Model Clustering", "🫧"),
    ]
)


# Membaca data
df = pd.read_csv("used_train.csv")
numeric_df = pd.read_csv("numeric_train.csv")

# Muat model
model = joblib.load("prediksi_compression.joblib")



# Judul dan deskripsi awal
colA, colB, colC = st.columns([0.2, 0.8, 0.2], gap="small")
with colA:
      my_grid = grid(1, vertical_align="bottom")
      my_grid.image("dice.gif")

with colB:
   with stylable_container(
            key="title",
            css_styles="""
               {
                  text-align : center;
                  background-color: #F0F2F6; /* Warna background */
                  padding: 0px 20px 20px 0; /* Jarak antara isi dan border */
                  height: 1000px;
               }
               """
   ):
      st.title('🎲 Model Prediksi 🎲')

with colC:
      my_grid = grid(1, vertical_align="bottom")
      my_grid.image("dice.gif")

with st.sidebar:
   selected_menu = option_menu("Pilih Menu", ["Tentang", "PREDIKSI", "Feature Importance"], 
    icons=['house', 'cloud-upload', "list-task"], 
    menu_icon="cast", default_index=0)

#selected_menu = option_menu(None, ["Tentang", "PREDIKSI", "Feature Importance"], 
   # icons=['house', 'cloud-upload', "list-task"], 
    #menu_icon="cast", default_index=0, orientation="horizontal")

if selected_menu == "Tentang":
   st.header("Tentang Model ❓")
   st.write("Model Prediksi menggunakan algoritma Random Forest Classifier yang dilatih dengan Bank Term Deposit Dataset dan diperoleh akurasi hingga 99% ")
   st.write("Model bertujuan untuk memprediksi apakah seorang nasabah dengan atribut/fitur tertentu akan setuju untuk menggunakan produk Deposito berjangka yang dipromosikan")
   st.divider()

   col1, col2, col3 = st.columns([0.3, 0.3, 0.4])
   with col1:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #ffffff; /* Warna background */
               padding: 20px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):   
         st.metric("Algoritma", "RF Classifier ⚙️")
   
   with col2:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #ffffff; /* Warna background */
               padding: 20px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.metric("Akurasi", "0.99 🎯")

   with col3:
      st.subheader("Panduan Penggunaan")
      with st.expander("Panduan",expanded=False):
         st.write("1. Masukkan atribut/fitur dari nasabah yang menjadi target")
         st.write("2. Atribut/fitur menggambarkan kondisi dan rekam jejak nasabah")
         st.write("3. Tekan tombol PREDIKSI untuk memulai proses prediksi setelah semua atribut/fitur dimasukkan")
         st.write("4. Hasil prediksi akan ditampilkan")

# 14 input
if selected_menu == "PREDIKSI":
   with stylable_container(
         key="subtitle",
         css_styles="""
            {
               text-align : center;
               padding: 0px 20px 20px 0; /* Jarak antara isi dan border */
               height: 1000px;
            }
            """
   ):
      st.header("Ayo Memprediksi!")
   st.divider()
   
   col4, col5, col6 = st.columns(3, gap="medium")
   with col4:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #ffffff; /* Warna background */
               padding: 20px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         # age number
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Berapa umur target?")
         my_grid = grid(1, vertical_align="bottom")
         age = my_grid.number_input("Masukkan umur", min_value=17, max_value=100, value="min", label_visibility="collapsed")
         my_grid.divider()

         # job pilih
         job_options = ['Management','Technician', 'Entrepreneur', 'Blue-collar', 'Unknown',
                        'Retired', 'Admin', 'Services','Self-employed',
                        'Unemployed', 'Housemaid','Student']
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Apa pekerjaan target?")
         
         my_grid = grid(1, vertical_align="bottom")
         job = my_grid.selectbox("Masukkan pekerjaan", job_options, index=0, placeholder="Pilih pekerjaan", label_visibility="collapsed")
         my_grid.divider()

         # marital pilih
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Apa status perkawinan target?")
         marital_options = ['Married', 'Single', 'Divorced']
         my_grid = grid(1, vertical_align="bottom")
         marital = my_grid.selectbox("Masukkan status", marital_options, index=0, placeholder="Pilih status", label_visibility="collapsed")
         my_grid.divider()
         
         # education pilih
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Apa pendidikan terakhir target?")
         edu_options = ['Primary (Sekolah Dasar)', 'Secondary (Sekolah Menengah)', 'Tertiary (Sekolah Tinggi)', 'Unknown']
         my_grid = grid(1, vertical_align="bottom")
         edu = my_grid.selectbox("Masukkan status", edu_options, index=0, placeholder="Pilih status", label_visibility="collapsed")
         my_grid.divider()
         
         # campaign num
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Sudah berapa kali target dihubungi?")
         my_grid = grid(1, vertical_align="bottom")
         campaign = my_grid.number_input("Masukkan campaign", min_value=1, max_value=100, value="min", label_visibility="collapsed")
        

   with col5:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #ffffff; /* Warna background */
               padding: 20px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         # default y/n
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Apakah target memiliki kredit dalam keadaan gagal bayar?")
         default_options = ['Ya', 'Tidak']
         
         my_grid = grid(1, vertical_align="bottom")
         default = my_grid.radio("label", default_options, index=0, label_visibility="collapsed")
         my_grid.divider()


         # balance number
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Berapa saldo tahunan target?")
         my_grid = grid(1, vertical_align="bottom")
         balance = my_grid.number_input("Dalam Euro", min_value=-200000, max_value=None, value=0, label_visibility="visible")
         my_grid.divider()

         # housing y/n
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Apakah target memiliki rumah?")
         default_options = ['Ya', 'Tidak']
         my_grid = grid(1, vertical_align="bottom")
         house = my_grid.radio("label1", default_options, index=0, label_visibility="collapsed")
         my_grid.divider()


         # loan y/n
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Apakah target memiliki hutang?")
         default_options = ['Ya', 'Tidak']
         my_grid = grid(1, vertical_align="bottom")
         loan = my_grid.radio("label2", default_options, index=0, label_visibility="collapsed")
         my_grid.divider()

         # pdays num
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Berapa hari sejak terakhir kali promosi kepada target?")
         my_grid = grid(1, vertical_align="bottom")
         pdays = my_grid.number_input("Jika tidak pernah dihubungi masukkan -1", min_value=-1, value=0, label_visibility="visible")

   with col6:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #ffffff; /* Warna background */
               padding: 20px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         # contact pilih
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Apa tipe komunikasi yang digunakan?")
         contact_options = ['Telephone', 'Cellular', 'Unknown']
         my_grid = grid(1, vertical_align="bottom")
         contact = my_grid.selectbox("Masukkan contact", contact_options, index=0, placeholder="Pilih metode", label_visibility="collapsed")
         my_grid.divider()

         # day num
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Kapan terakhir kali target dihubungi dalam bulan ini?")
         my_grid = grid(1, vertical_align="bottom")
         day = my_grid.number_input("Masukkan tanggal", min_value=1, max_value=31, value=1, label_visibility="visible")
         my_grid.divider()

         # month pilih
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Kapan terakhir kali target dihubungi dalam satu tahun ini?")
         my_grid = grid(1, vertical_align="bottom")
         month_options = ['Januari', 'Februari', 'Maret', 'April', 'Mei','Juni','Juli','Agustus',
                           'September', 'Oktober', 'November', 'Desember']
         month = my_grid.selectbox("Masukkan month", month_options, index=0, placeholder="Pilih bulan", label_visibility="collapsed")
         my_grid.divider()

         # duration num
         my_grid = grid(1, vertical_align="bottom")
         my_grid.subheader("Berapa durasi kontak terakhir dengan target?")
         my_grid = grid(1, vertical_align="bottom")
         duration = my_grid.number_input("Dalam satuan detik", min_value=0, max_value=None, value=0, label_visibility="visible")

   st.divider()
   # Inisialisasi variabel untuk menyimpan hasil input
   input_data = {}

   # Widget untuk tombol Submit
   if st.button("SUBMIT", type="primary", use_container_width=True):
      submit_pressed = True

      # Simpan hasil input ke dalam variabel
      input_data = {
         "age": age,
         "job": job,
         "marital": marital,
         "education": edu,
         "default": default,
         "balance": balance,
         "housing": house,
         "loan": loan,
         "contact": contact,
         "day": day,
         "month": month,
         "duration": duration,
         "campaign": campaign,
         "pdays": pdays,
      }
      # Konversi dictionary ke DataFrame
      df_input = pd.DataFrame([input_data])
      st.table(df_input)
      numeric_df_input = df_input

      # Membuat peta nilai (mapping) untuk encoding
      mapping_job = {'Management':1, 'Technician':2, 'Entrepreneur':3, 'Blue-collar':4, 'unknown':5,
      'Retired':6, 'Admin':7, 'services':8, 'Self-employed':9, 'Unemployed':10, 'Housemaid':11,
      'Student':12}
      mapping_marital = {'Married': 3, 'Single': 1, 'Divorced': 0}
      mapping_education = {'Tertiary (Sekolah Tinggi)': 3, 'Secondary (Sekolah Menengah)': 2, 'Unknown': 0, 'Primary (Sekolah Dasar)': 1}
      mapping_default = {'Tidak': 0, 'Ya': 1}
      mapping_housing = {'Tidak': 0, 'Ya': 1}
      mapping_loan = {'Tidak': 0, 'Ya': 1}
      mapping_contact = {'Unknown': 0, 'Cellular': 1, 'Telephone': 2}
      mapping_month = {'Januari':1, 'Februari':2, 'Maret':3,
                     'April':4, 'Mei':5, 'Juni':6,
                     'Juli':7, 'Agustus':8, 'September':9,
                     'Oktober':10, 'November':11, 'Desember':12}
      #mapping_y = {'Tidak': 0, 'Ya': 1}

      # Melakukan encoding manual
      numeric_df_input['job'] = df_input['job'].map(mapping_job)
      numeric_df_input['marital'] = df_input['marital'].map(mapping_marital)
      numeric_df_input['education'] = df_input['education'].map(mapping_education)
      numeric_df_input['default'] = df_input['default'].map(mapping_default)
      numeric_df_input['housing'] = df_input['housing'].map(mapping_housing)
      numeric_df_input['loan'] = df_input['loan'].map(mapping_loan)
      numeric_df_input['contact'] = df_input['contact'].map(mapping_contact)
      numeric_df_input['month'] = df_input['month'].map(mapping_month)
      #numeric_df_input['y'] = train_df['y'].map(mapping_y)

      # Lakukan Prediksi
      predictions = model.predict(numeric_df_input)

      # Tampilkan hasil prediksi
      if predictions == 1:
         with stylable_container(
         key="false",
         css_styles="""
            {
               color: #000000;
               text-align : center;
               font-size: 72px;
               padding: 10px; /* Jarak antara isi dan border */
               background-color: #F0F2F6; /* Warna background */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
            }
            """
         ):
           
           st.subheader("Target ini **:green[SETUJU]** untuk menggunakan produk Deposito Berjangka")
      else:
         with stylable_container(
         key="false",
         css_styles="""
            {
               color: #000000;
               text-align : center;
               font-size: 72px;
               padding: 10px; /* Jarak antara isi dan border */
               background-color: #F0F2F6; /* Warna background */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
            }
            """
         ):
           
           st.subheader("Target ini **:red[TIDAK SETUJU]** untuk menggunakan produk Deposito Berjangka")


if selected_menu == "Feature Importance": 
   st.header("Tentang Feature Importance")
   st.write("'Feature Importance' (kepentingan fitur) adalah konsep yang digunakan dalam machine learning untuk menentukan sejauh mana setiap fitur atau variabel independen berkontribusi terhadap prediksi model. Dengan kata lain, feature importance membantu kita memahami peran dan dampak relatif dari setiap fitur terhadap output atau hasil prediksi dari model.")
   st.divider()
   st.image("feature-importance.png", use_column_width=True)
   
