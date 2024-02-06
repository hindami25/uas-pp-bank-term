import streamlit as st
from st_pages import Page, show_pages
from streamlit_extras.stylable_container import stylable_container 
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

# Judul dan deskripsi awal
colA, colB, colC = st.columns([0.2, 0.8, 0.2], gap="small")
with colA:
      my_grid = grid(1, vertical_align="bottom")
      my_grid.image("bulb.gif")

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
      st.title('💡 Informasi Umum 💡')
   
   with stylable_container(
            key="title2",
            css_styles="""
               {
                  text-align : center;
                  padding: 0px 20px 20px 0; /* Jarak antara isi dan border */
                  height: 1000px;
               }
               """
   ):
     st.write("*Informasi umum mengenai Deposit Berjangka beserta kelebihan dan bentuk promosinya*")

with colC:
      my_grid = grid(1, vertical_align="bottom")
      my_grid.image("bulb.gif")

st.divider()

# Info Deposit
with stylable_container(
            key="head1",
            css_styles="""
               {
                text-align : center;
                
                align-items: center;
               }
               """
):
    st.header("Apa itu Deposit Berjangka??")
    left, mid, right = st.columns([0.1, 0.8, 0.1])
    with mid:
        st.image("wallet.gif")
    st.subheader("***Deposito berjangka adalah produk perbankan yang memberikan kesempatan kepada nasabah untuk menyimpan sejumlah dana dalam jangka waktu tertentu dengan tingkat bunga tetap***")

st.divider()

#Keuntungan Deposit
with stylable_container(
            key="head1",
            css_styles="""
               {
                text-align : center;
                
                align-items: center;
               }
               """
):
    st.header("Apa Karakteristiknya??")
    left, mid, right = st.columns([0.1, 0.9, 0.1])
    with mid:
        st.image("traffic.gif")
        
    st.subheader("***Berikut merupakan 3 karakteristik utama dari Deposit Berjangka***")

    col1, col2, col3 = st.columns([0.3, 0.3, 0.3])
    
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
            my_grid = grid(1, vertical_align="bottom")
            my_grid.subheader("Jangka Waktu Tetap")
            my_grid.write("Nasabah menyetorkan dana mereka untuk jangka waktu tertentu, yang dapat berkisar dari beberapa bulan hingga beberapa tahun. Jangka waktu ini telah ditentukan sejak awal dan tidak dapat diubah selama periode deposito")
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
            my_grid = grid(1, vertical_align="bottom")
            my_grid.subheader("Penalti untuk Penarikan Awal")
            
            my_grid.write("Sebagian besar deposito berjangka memiliki ketentuan bahwa penarikan dana sebelum jatuh tempo akan dikenai penalti. Oleh karena itu, nasabah diharapkan untuk mempertimbangkan kebutuhan keuangan mereka dengan hati-hati sebelum menempatkan dana dalam deposito berjangka")
            
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
            my_grid = grid(1, vertical_align="bottom")
            my_grid.subheader("Tingkat Bunga Tetap")
            my_grid.write("Deposito berjangka menawarkan tingkat bunga tetap yang lebih tinggi dibandingkan dengan rekening tabungan biasa. Tingkat bunga ini ditetapkan pada awal periode deposito dan tetap konstan hingga jatuh tempo")
st.divider()


#Penawaran Deposit
with stylable_container(
            key="head1",
            css_styles="""
               {
                text-align : center;
                align-items: center;
               }
               """
):
    st.header("Bagaimana Bentuk Promosinya??")
    left, mid, right = st.columns([0.1, 0.9, 0.1])
    with mid:
        st.image("promote.gif")
        
    st.subheader("***Berikut merupakan 4 bentuk promosi produk Deposit Berjangka yang biasa dilakukan***")

    col4, col5 = st.columns([0.3, 0.3])
    
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
            my_grid = grid(1, vertical_align="bottom")
            my_grid.subheader("Tingkat Bunga Kompetitif")
            my_grid.write("Bank dapat menawarkan tingkat bunga yang lebih tinggi dibandingkan dengan produk simpanan lainnya sebagai daya tarik bagi nasabah untuk memilih deposito berjangka")
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
            my_grid = grid(1, vertical_align="bottom")
            my_grid.subheader("Promosi Bonus Awal")
            
            my_grid.write("Bank mungkin memberikan bonus awal atau insentif tambahan untuk nasabah yang membuka deposito berjangka dengan jumlah tertentu")
            
    col6, col7 = st.columns([0.3, 0.3])
    
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
            my_grid = grid(1, vertical_align="bottom")
            my_grid.subheader("Promosi Melalui Platform Digital")
            my_grid.write("Bank dapat mempromosikan deposito berjangka melalui situs web, aplikasi seluler, atau platform digital lainnya dengan memberikan informasi yang jelas tentang manfaat dan syaratnya")

    with col7:
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
            my_grid = grid(1, vertical_align="bottom")
            my_grid.subheader("Program Investasi Jangka Panjang")
            my_grid.write("Bank dapat menawarkan program investasi jangka panjang yang terkait dengan deposito berjangka, seperti pembelian reksa dana atau produk investasi lainnya dengan tingkat risiko yang sesuai")

st.divider()

with stylable_container(
            key="head1",
            css_styles="""
               {
                text-align : center;
                
                align-items: center;
               }
               """
):
    st.header("Kesimpulan")
    st.write("*Beberapa keuntungan dari deposito berjangka melibatkan kestabilan investasi, penghasilan bunga yang tetap, dan perlindungan terhadap fluktuasi suku bunga. Namun, perlu diingat bahwa tingkat bunga tetap juga berarti kurangnya potensi pertumbuhan jika dibandingkan dengan investasi yang mungkin menghasilkan hasil yang lebih tinggi tetapi dengan tingkat risiko yang lebih tinggi pula. Sebagai hasilnya, keputusan untuk membuka deposito berjangka sebaiknya didasarkan pada tujuan keuangan dan toleransi risiko pribadi.*")










