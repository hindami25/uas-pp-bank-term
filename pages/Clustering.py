import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from st_pages import Page, show_pages
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.grid import grid 

# Mengatur tata letak halaman
st.set_page_config(layout="wide")

with st.sidebar:
   selected_menu = option_menu("Pilih Menu", ["Tentang", "OUTPUT", "Experimental"], 
    icons=['house', 'cloud-upload', "list-task"], 
    menu_icon="cast", default_index=0)
   
   
show_pages(
    [
        Page("pages/Informasi.py", "Informasi", "💡"),
        Page("Dashboard.py", "Dataset Dashboard", "🏠"),
        Page("pages/Prediksi.py", "Model Prediksi", "🎲"),
        Page("pages/Clustering.py", "Model Clustering", "🫧"),
    ]
)




# Mengatur notifikasi
st.set_option('deprecation.showPyplotGlobalUse', False)

# Membaca data
df = pd.read_csv("used_train.csv")
numeric_train_df = pd.read_csv("numeric_train.csv")


# Memuat model dari file joblib
kmeans_model = joblib.load('kmeans_model.joblib')

# Judul dan deskripsi awal
colA, colB, colC = st.columns([0.2, 0.8, 0.2], gap="small")
with colA:
      my_grid = grid(1, vertical_align="bottom")
      my_grid.image("group.gif")

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
      st.title('Model Clustering')

with colC:
      my_grid = grid(1, vertical_align="bottom")
      my_grid.image("group.gif")
    

if selected_menu == "Tentang":
   st.header("Tentang Model")
   st.write("Model Clustering menggunakan algoritma K-Means yang bertujuan untuk mengelompokkan data Bank Term Deposit Dataset dan diperoleh Silhouette Score: 0.59 dengan 3 Cluster")
   st.write("Model ini bertujuan untuk mengelompokkan nasabah menjadi 3 kategori")
   st.divider()

   col1, col2, col3 = st.columns(3)
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
        st.metric("Algoritma", "K-Means ⚙️")

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
        st.metric("Silhouette Score", "0.59 🎯")
   
   with col3:
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
        st.metric("Clusters", "3 🫧")



if selected_menu == "OUTPUT":
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
        st.header("'OUTPUT'")
    with st.expander("Penjelasan",expanded=False):
         st.write("Rekomendasi Hasil Clustering nasabah menggunakan fitur 'age' dan 'balance' disertai dengan label kategori")
         st.write("Rekomendasi ini merupakan Hasil Clustering yang paling baik menurut developer")
    st.divider()      
   # Melakukan prediksi klaster untuk data
    labels = kmeans_model.fit_predict(numeric_train_df)

    # Mengatur ukuran figur
    plt.figure(figsize=(10, 6))

    # Membuat grafik hasil klastering
    plt.scatter(df["age"][labels == 0], df["balance"][labels == 0], c='seagreen', label='Perintis Keuangan')
    plt.scatter(df["age"][labels == 1], df["balance"][labels == 1], c='royalblue', label='Pencari Stabilitas Keuangan')
    plt.scatter(df["age"][labels == 2], df["balance"][labels == 2], c='gold', label='Investor Keuangan')
    plt.title('Hasil Clustering Age - Balance')
    plt.xlabel("age")
    plt.ylabel("balance")

    plt.legend()

    # Menampilkan plot di Streamlit
    st.pyplot()
    st.divider()
    col4, col5, col6 = st.columns(3)
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
            my_grid=grid(1, vertical_align="bottom")
            my_grid.subheader("Kategori Perintis Keuangan")
            my_grid.write("Nasabah yang memiliki saldo rendah dengan usia bervariasi")
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
         my_grid=grid(1, vertical_align="bottom")
         my_grid.subheader("Kategori Pencari Stabilitas Keuangan")
         my_grid.write("Nasabah yang memiliki saldo rata-rata dengan usia bervariasi")

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
         my_grid=grid(1, vertical_align="bottom")
         my_grid.subheader("Kategori Investor Keuangan")
         my_grid.write("Nasabah yang memiliki saldo tinggi dengan usia bervariasi")



if selected_menu == "Experimental":
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
      st.header("'Experimental'")
    
    col7, col8 = st.columns(2)
    with col7:
        with st.expander("Penjelasan",expanded=False):
            st.write("Proses Clustering yang dapat disesuaikan dengan fitur yang diinginkan oleh pengguna untuk dicoba")
            st.write("Jumlah cluster yang digunakan tetap sama yaitu 3 cluster namun fiturnya dapat diubah sesuai keinginan ")
    with col8:
        with st.expander("Petunjuk Penggunaan",expanded=False):
            st.write("1. Pilih 2 fitur yang ingin digunakan untuk proses Clustering")
            st.write("2. Hasil Clustering akan muncul tanpa label")
       
    
    st.divider()

    # memilih fitur1
    feature_list = list(df.columns)
    selected_feature1 = st.selectbox('Pilih Fitur1', feature_list, index=0)

    # memilih fitur2
    selected_feature2 = st.selectbox('Pilih Fitur2', feature_list, index=0)

    # Melakukan prediksi klaster untuk data
    labels = kmeans_model.fit_predict(numeric_train_df)

    # Mengatur ukuran figur
    plt.figure(figsize=(10, 6))

    # Membuat grafik hasil klastering
    plt.scatter(df[selected_feature1][labels == 1], df[selected_feature2][labels == 1], c='seagreen')
    plt.scatter(df[selected_feature1][labels == 0], df[selected_feature2][labels == 0], c='royalblue')
    plt.scatter(df[selected_feature1][labels == 2], df[selected_feature2][labels == 2], c='gold')
    plt.title('Hasil Clustering')
    plt.xlabel(selected_feature1)
    plt.ylabel(selected_feature2)

    plt.legend()

    # Menampilkan plot di Streamlit
    st.pyplot()
