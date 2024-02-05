import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt
import streamlit as st
import plotly.graph_objects as go
import seaborn as sns
from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.grid import grid 
from st_pages import Page, show_pages, add_page_title
from streamlit_extras.metric_cards import style_metric_cards 



# Mengatur tata letak halaman
st.set_page_config(layout="wide", page_icon='🏠')

show_pages(
    [
        Page("pages/Informasi.py", "Informasi", "💡"),
        Page("Dashboard.py", "Dataset Dashboard", "🏠"),
        Page("pages/Prediksi.py", "Model Prediksi", "🎲"),
        Page("pages/Clustering.py", "Model Clustering", "🫧"),
    ]
)


alt.themes.enable("dark")


# Membaca data
df = pd.read_csv("used_train.csv")
numeric_df = pd.read_csv("numeric_train.csv")


# Judul dan deskripsi awal
colA, colB, colC = st.columns([0.2, 0.8, 0.2], gap="small")
with colA:
      my_grid = grid(1, vertical_align="bottom")
      my_grid.image("bank.gif")

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
      st.title('🏦 Bank Term Deposit Dataset 🏦')

with colC:
      my_grid = grid(1, vertical_align="bottom")
      with stylable_container(
            key="gif",
            css_styles="""
               {
                  text-align : center;
                  background-color: #F0F2F6; /* Warna background */
                  padding: 0px 0px 0px 20px; /* Jarak antara isi dan border */
                  height: 1000px;
               }
               """
   ):
         my_grid.image("bank.gif")




   
   
   

with st.expander("Tentang Dataset", expanded=False):
   st.write("Dataset dari lembaga perbankan Portugal yang berisi berbagai fitur atribut nasabah dan bertujuan untuk melatih model yang memprediksi apakah nasabah akan setuju untuk berlangganan deposito berjangka atau tidak.")
   st.write("Dataset dapat dimanfaatkan untuk memahami target nasabah dan meningkatkan efektivitas kampanye pemasaran")
st.divider()

with st.sidebar:
   selected_main = option_menu("Pilih Mode", ["Semua Data", "Kolom"], 
        icons=['house', 'list-task'], menu_icon="cast", default_index=1)

if selected_main == "Kolom":
   # NAMA FEATURE / ROW1
   #my_grid = grid([0.2, 0.8], [0.2, 0.5, 0.3], [0.1, 0.5], vertical_align="bottom")
   col1, col2 = st.columns([0.2, 0.8], gap="large")

   # Judul dan deskripsi awal
   with col1:
       # Mendapatkan daftar fitur dari DataFrame
      feature_list = list(df.columns)
      st.subheader("Pilih Kolom")
      selected_feature = st.selectbox('Pilih Kolom', feature_list, index=0, label_visibility="collapsed")

   with col2:
      # Deskripsi untuk setiap fitur
      feature_descriptions = {
         'age': 'data tentang umur nasabah',
         'job': 'data tentang pekerjaan nasabah',
         'marital': 'data tentang stasus perkawinan nasabah',
         'education': 'data tentang pendidikan terakhir nasabah',
         'default': 'data tentang kepemilikan kredit dalam kondisi gagal bayar milik nasabah',
         'balance': 'data tentang saldo tahunan nasabah dalam mata uang Euro',
         'housing': 'data tentang kepemilikan rumah nasabah',
         'loan': 'data tentang kepemilikan hutang nasabah',
         'contact':'data tentang saluran untuk menghubungi nasabah',
         'day':'data tentang tanggal kapan terakhir kali nasabah dihubungi dalam satu bulan',
         'month':'data tentang bulan apa terakhir kali nasabah dihubungi dalam satu tahun',
         'duration': 'data tentang berapa durasi kontak terakhir dengan nasabah (dalam satuan detik)',
         'campaign': 'data tentang berapa kali nasabah sudah dihubungi',
         'pdays': 'data tentang berapa hari sejak terakhir kali promosi kepada nasabah',
         'y': 'data tentang persetujuan target untuk menggunakan produk Deposito Berjangka'
      }
      
      st.header(f"{selected_feature}")
      st.write(f"***{selected_feature} adalah kolom yang berisi {feature_descriptions[selected_feature]}***")
   st.divider()
   
   # ROW 3
   col3, col4 = st.columns([0.3, 0.7], gap="small")

   with col3:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               background-color: #ffffff; /* Warna background */
               padding: 0px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.header("Deskripsi 💡 ")
         tab1, tab2, tab3 = st.tabs(["Describe", "Unique", "Missing"])

         with tab1:
            st.write(f"Tipe data: {df[selected_feature].dtype}")
            st.table(df[selected_feature].describe())

         with tab2:
            st.metric("Jumlah Data Unik", df[selected_feature].nunique())
            if df[selected_feature].dtype == 'object':
                  st.data_editor(
                     df[selected_feature].unique(),
                     column_config={
                        "widgets": st.column_config.TextColumn(
                              "Widgets",
                              help="Streamlit **widget** commands 🎈",
                              default="st.",
                              max_chars=50,
                              validate="^st\.[a-z_]+$",
                        )
                     },
                     hide_index=True,
                  )

         with tab3:
            st.metric("Jumlah Data Kosong", df[selected_feature].isnull().sum())
            
         
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
         st.header("Grafik Frekuensi Data 📊")
         tab4, tab5 = st.tabs(["Vertikal", "Horizontal"])
         with tab4:
            value_counts = df[selected_feature].value_counts()
            df_counts = pd.DataFrame({'Value': value_counts.index, 'Count': value_counts.values})

            # Buat grafik batang menggunakan Plotly Express
            fig = px.bar(df_counts, x='Value', y='Count', title=f'Frekuensi Data {selected_feature}')

            # Tampilkan chart menggunakan st.plotly_chart
            st.plotly_chart(fig, use_container_width=True)
            
         with tab5:
            # Hitung frekuensi dan persentase
            value_counts = df[selected_feature].value_counts()
            total_data = len(df)
            percentages = (value_counts / total_data) * 100

            # Gabungkan data
            fig = pd.DataFrame({
               'Value': value_counts.index,
               'Count': value_counts.values,
               'Percentage': percentages.values,
            })

            # Buat diagram batang horizontal dengan plotly.express
            fig = px.bar(fig, x='Percentage', y='Value', text='Count', orientation='h',
                        labels={'Percentage': 'Persentase (%)'},
                        title=f'Frekuensi dan Persentase Data di Kolom {selected_feature}')

            # Tampilkan diagram menggunakan st.plotly_chart
            st.plotly_chart(fig, use_container_width=True)
      

   #with col5:
      
   # ROW 4
   col6, col7 = st.columns([0.1, 0.5], gap="small")

   with col6:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 20px; /* Jarak antara isi dan border */
               background-color: #ffffff; /* Warna background */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         my_grid = grid(1, vertical_align="bottom")
         my_grid.header("Sample Data 🔬")
         tab3, tab4 = st.tabs(["Head", "Tail"])

         with tab3:
            st.dataframe(df[selected_feature].head(10))

         with tab4:
            st.dataframe(df[selected_feature].tail(10))

   with col7:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 20px 20px 20px 20px;
               background-color: #ffffff; /* Warna background */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
            st.header("Grafik Perbandingan 📊")

            # Buat chart Altair
            chart = alt.Chart(df).mark_bar().encode(
               x=selected_feature,
               y='count()',
               color='y:N'
            ).properties(
               title=f'Grafik perbandingan antara "{selected_feature}" dan kolom "y" (Persetujuan Nasabah)'
            )

            #Tampilkan chart menggunakan st.altair_chart
            my_grid = grid(1, vertical_align="bottom")
            my_grid.altair_chart(chart, use_container_width=True)

   with stylable_container(
         key="corr",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 22px 0 22px 22px; /* Jarak antara isi dan border */
               background-color: #ffffff; /* Warna background */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
            

            st.header("Korelasi 🧮")
            corr_matrix_selected = numeric_df.corrwith(numeric_df[selected_feature])
            corr_df = pd.DataFrame({'Korelasi': corr_matrix_selected})

            # Buat heatmap menggunakan plotly.graph_objects
            fig = go.Figure(data=go.Heatmap(z=[corr_df['Korelasi']],
                                          x=corr_df.index,
                                          y=[selected_feature],
                                          colorscale='blues'))

            fig.update_layout(title_text=f"Heatmap Korelasi antara {selected_feature} dan kolom lainnya",
                              xaxis=dict(title='Kolom'),
                              yaxis=dict(title='Kolom Terpilih'))

            # Tampilkan heatmap menggunakan st.plotly_chart
            my_grid = grid(1, vertical_align="bottom")
            my_grid.plotly_chart(fig)

      
else:
   # NAMA FEATURE / ROW1
   col1, col2, col3, col4  = st.columns(4)
   with col1:
      with stylable_container(
         key="metric",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               
               padding: 30px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.metric("Jumlah Kolom 🚥", df.shape[1])

   with col2:
      with stylable_container(
         key="metric",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               
               padding: 20px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.metric("Jumlah Baris 🚥", df.shape[0])

   with col3:
      with stylable_container(
         key="metric",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 20px; /* Jarak antara isi dan border */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.metric("Jumlah Data Kosong/NaN 🚥", 0)

   with col4:
      with stylable_container(
         key="metric",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 20px; /* Jarak antara isi dan border */
               
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.metric("Jumlah Data Duplikat 🚥", df.duplicated().sum())
   

   st.divider()

   # ROW 3
   col5, col6 = st.columns([0.4, 0.6], gap="small")

   with col5:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 20px; /* Jarak antara isi dan border */
               background-color: #ffffff; /* Warna background */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.header("Deskripsi 💡")
         tab1, tab2, tab3 = st.tabs(["Describe (Numeric)", "Describe (Categorical)", "Unique"])

         with tab1:
            # Iterasi melalui kolom-kolom DataFrame
            for column in df.columns:
               if df[column].dtype != 'object':
                  table = (df.describe())  # Menampilkan deskripsi untuk kolom berjenis objek

            # Menampilkan deskripsi DataFrame hanya sekali di luar loop
            st.table(table)

         with tab2:
            # Iterasi melalui kolom-kolom DataFrame
            for column in df.columns:
               if df[column].dtype == 'object':
                  table = (df.describe(include=['object']))  # Menampilkan deskripsi untuk kolom berjenis objek

            # Menampilkan deskripsi DataFrame hanya sekali di luar loop
            st.table(table)

         with tab3:
            st.write("Jumlah Data Unik")
            st.table(df.nunique())

   with col6:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 20px; /* Jarak antara isi dan border */
               background-color: #ffffff; /* Warna background */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.header("Grafik Jumlah Data Unik 📊")
         # Menampilkan jumlah data unik per kolom dalam bentuk grafik horizontal
         my_grid = grid(1, vertical_align="bottom")
         fig = px.bar(y=df.columns, x=[df[col].nunique() for col in df.columns], labels={'y': 'Kolom', 'x': 'Jumlah Data Unik'}, orientation='h')
         my_grid.plotly_chart(fig, use_container_width=True)

   # ROW 4
   col7, col8 = st.columns([0.5, 0.5], gap="small")

   with col7:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 20px; /* Jarak antara isi dan border */
               background-color: #ffffff; /* Warna background */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         st.header("Dataframe 🔬")
         tab4, tab5, tab6 = st.tabs(["Full", "Head", "Tail"])
         
         with tab4:
            st.dataframe(df)

         with tab5:
            st.write(df.head(10))

         with tab6:
            st.write(df.tail(10))

   with col8:
      with stylable_container(
         key="container_with_border",
         css_styles="""
            {
               border: 2px solid #ccc; /* Warna dan ketebalan border */
               border-radius: 10px; /* Jari-jari sudut (rounded corners) */
               padding: 20px; /* Jarak antara isi dan border */
               background-color: #ffffff; /* Warna background */
               box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Efek bayangan (shadow) */
            }
            """
      ):
         # Menampilkan korelasi antara semua kolom
         st.header("Korelasi Seluruh Kolom 🧮")
         corr_matrix_all = numeric_df.corr()

         # Buat heatmap menggunakan plotly.graph_objects
         fig = go.Figure(data=go.Heatmap(z=corr_matrix_all.values,
                                       x=corr_matrix_all.columns,
                                       y=corr_matrix_all.columns,
                                       colorscale='blues'))
         fig.update_layout(title_text="Heatmap Korelasi antara Semua Kolom")

         # Tampilkan heatmap menggunakan st.plotly_chart
         my_grid = grid(0.7, vertical_align="bottom")
         my_grid.plotly_chart(fig, use_container_width=True)
         



   