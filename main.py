import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px




st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)



tab1, tab2 = st.tabs(["My Paper Publication", "Activities"])


with tab1:
   col1, col2, col3 = st.columns(3)
   with col1:
     st.image("https://statkomat.com/gambar/ugi.png", caption='', width = 350)
   with col1:
     st.markdown("<a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>STATKOMAT</b></font></a> | <a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>YOUTUBE</b></font></a> | <a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>LITERATURE REVIEW</b></font></a> | <a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>LIST OF PAPERS</b></font></a> | <a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>PUBLICATION</b></font></a> | <a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>PLS-SEM</b></font></a> | <a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>MY SOFTWARE</b></font></a> | <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>MY BOOK</b></font></a> | <a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>UGI</b></font></a> | <a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>SHINY</b></font></a> | <a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>INDCOMP</b></font></a> | <a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>FIGSHARE</b></font></a> | <a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>GITHUB</b></font></a>", unsafe_allow_html=True)



with tab1:
   st.write('''<font color = "#ff00ff" size = 5><b>Publication Year for 2024</b></font>
            
[1] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Evaluation of foot analysis in the presence of dental malocclusion: A systematic review</font><br>Author: Ervina Sofyanti, Ananto Ali Alhasyimi, Cendrawasih Andusyana Farmasyanti, Maria Purbiati, Endah Mardiati, Ida Bagus Narmada, Haryono Utomo, <font color = "red" size = 5>Prana Ugiana Gio</font>, Anand Marya<br>Journal: <font color = "#ff00ff">Dental Journal</font><br>Journal Link: <a href = "https://e-journal.unair.ac.id/MKG/article/view/50044" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21101083128&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>

[2] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">INDCOMP: A Shiny App for Open Data Repository of the Performance of an Indonesian Company Listed at the Indonesia Stock Exchange</font><br>Author: <font color = "red" size = 5>Prana Ugiana Gio</font>, Herman Mawengkang, Muhammad Zarlis, Saib Suwilo<br>Journal: <font color = "#ff00ff">Engineering, Technology & Applied Science Research (ETASR)</font><br>Journal Link: <a href = "https://etasr.com/index.php/ETASR/article/view/8131" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21101144516&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>                    
         

            
[3] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Unlocking insights from Ministry of Marine Affairs and Fisheries annual reports using LDA: a deep dive into SDG 14</font><br>Author: Ahmad Marzuqi, Rezzy Eko Caraka, <font color = "red" size = 5>Prana Ugiana Gio</font>, Rung Ching Chen, Maengseok Noh, Bens Pardamean<br>Journal: <font color = "#ff00ff">Engineering, Technology & Applied Science Research (ETASR)</font><br>Journal Link: <a href = "https://telkomnika.uad.ac.id/index.php/TELKOMNIKA/article/view/26063" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21100256101&tip=sid" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>                    
         

[4] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">The ecological footprint of industrial value added and energy consumption in Indonesia</font><br>Author: Robert Kurniawan, Novan Adi Adi Nugroho, Ahmad Fudholi, Agung Purwanto, Bagus Sumargo, <font color = "red" size = 5>Prana Ugiana Gio</font>, Sri Kuswantono Wongsonadi<br>Journal: <font color = "#ff00ff">International Journal of Energy Sector Management</font><br>Journal Link: <a href = "https://www.emerald.com/insight/content/doi/10.1108/IJESM-05-2023-0006/full/html" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=6400153116&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>                    
         


[5] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Green Infrastructure Vulnerability and Regional Poverty Reduction: New Sustainable Development Recommendations Based on a Spatial Clustering Approach</font><br>Author: Bagus Sumargo, Robert Kurniawan, Bahrul Ilmi Nasution, Aldi Firmansyah, Bagaskoro Cahyo Laksono, <font color = "red" size = 5>Prana Ugiana Gio</font>, Mohamad Andrian Isnaeni, Mukhtar Yusuf & Vita Cita Emia Tarigan<br>Journal: <font color = "#ff00ff">Journal of Poverty</font><br>Journal Link: <a href = "https://www.tandfonline.com/doi/full/10.1080/10875549.2024.2379769" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=4700152755&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>                    
         

[6] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">The role of renewable energy and foreign direct investment toward environmental degradation convergence to achieve sustainability: evidence from ASEAN countries</font><br>Author: Robert Kurniawan, Arya Candra Kusuma, Bagus Sumargo, <font color = "red" size = 5>Prana Ugiana Gio</font>, Sri Kuswantono Wongsonadi, Karta Sasmita <br>Journal: <font color = "#ff00ff">International Journal of Energy Sector Management</font><br>Journal Link: <a href = "https://www.emerald.com/insight/content/doi/10.1108/IJESM-02-2024-0012/full/html" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=6400153116&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>                    
         


            





[7] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Understanding Pediatric Health Trends in Papua: Insights From SUSENAS, RISKESDAS, Remote Sensing, and Its Relevance to Prabowo and Gibran's Free Lunch and Milk Program</font><br>Author: Rezzy Eko Caraka, Khairunnisa Supardi, Puspita Anggraini Kaban, Robert Kurniawan, <font color = "red" size = 5>Prana Ugiana Gio</font>, Yunho Kim, Syihabuddin Ahmad Mufti, Rung-Ching Chen, Muhammad Khahfi Zuhanda, Avia Enggar Tyasti, Noor Ell Goldameir, Bens Pardamean<br>Journal: <font color = "#ff00ff">IEEE Access</font><br>Journal Link: <a href = "https://ieeexplore.ieee.org/document/10477418/authors#authors" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21100374601&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br> 



[8] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Empowering deaf communication: a novel LSTM model for recognizing Indonesian sign language</font><br>Author: Rezzy Eko Caraka, Khairunnisa Supardi, Robert Kurniawan, Yunho Kim, <font color = "red" size = 5>Prana Ugiana Gio</font>, Budi Yuniarto, Faiq Zakki Mubarok & Bens Pardamean<br>Journal: <font color = "#ff00ff">Universal Access in the Information Society</font><br>Journal Link: <a href = "https://link.springer.com/article/10.1007/s10209-024-01095-1" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=2600147401&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br> 




[9] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Business Predictive Analytics of Smallholder Indonesian Maize using Vector Error Correction</font><br>Author: Anita Rizky Lubis, Nelva Meyriani Br Ginting, Sri Fajar Ayu, Rezzy Eko Caraka, Yunho Kim, <font color = "red" size = 5>Prana Ugiana Gio</font>, Bens Pardamean<br>Journal: <font color = "#ff00ff">Engineering Letters</font><br>Journal Link: <a href = "https://www.engineeringletters.com/issues_v32/issue_2/EL_32_2_21.pdf" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=17800156701&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br> 


            


[10] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Fine-Tuning of Predictive Models CNN-LSTM and CONV-LSTM for Nowcasting PM2.5 Level</font><br>Author: Tafia Hasna Putri, Rezzy Eko Caraka, Toni Toharudin, Yunho Kim, Rung-Ching Chen, <font color = "red" size = 5>Prana Ugiana Gio</font>, Anjar Dimara Sakti, Resa Septiani Pontoh, Indah Reski Pratiwi, Farid Azhar Lutfi Nugraha, Thalita Safa Azzahra, Jessica Jesslyn Cerelia, Gumgum Darmawan, Defi Yusti Faidah, Bens Pardamean<br>Journal: <font color = "#ff00ff">IEEE Access</font><br>Journal Link: <a href = "https://ieeexplore.ieee.org/document/10443012" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21100374601&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br> 


[11] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Decoding the Narrative: Patterns and Dynamics in Monkeypox Scholarly Publications</font><br>Author: Muhammad Khahfi Zuhanda, Desniarti, Anil Hakim Syofra, Andre Hasudungan Lubis, <font color = "red" size = 5>Prana Ugiana Gio</font>, Habib Satria, Rahmad Syah<br>Journal: <font color = "#ff00ff">International Journal of Advanced Computer Science and Applications</font><br>Journal Link: <a href = "https://thesai.org/Publications/ViewPaper?Volume=15&Issue=1&Code=IJACSA&SerialNo=65" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21100867241&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br> 




[12] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Investigating Adolescent Vulnerability in Indonesia: A Socio-Remote Sensing Big Data Analytics Study Using Night Light Data</font><br>Author: Toni Toharudin, Rezzy Eko Caraka, Puspita Anggraini Kaban, Khairunnisa Supardi, Robert Kurniawan, Yunho Kim, Syihabuddin Ahmad Mufti, <font color = "red" size = 5>Prana Ugiana Gio</font>, Anjar Dimara Sakti, Rung-Ching Chen, Maengseok Noh, and Bens Pardamean<br>Journal: <font color = "#ff00ff">IEEE Access</font><br>Journal Link: <a href = "https://ieeexplore.ieee.org/document/10409177" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21100374601&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br> 



<br><br>
            




<font color = "#ff00ff" size = 5><b>Publication Year for 2023</b></font>
            
[1] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Strategic insights for MSMEs: navigating the new normal with big data and business analytics</font><br>Author: Rezzy Eko Caraka, Robert Kurniawan, Rung Ching Chen, <font color = "red" size = 5>Prana Ugiana Gio</font>, Jamilatuzzahro, Bahrul Ilmi Nasution, Anjar Dimara Sakti, Muhammad Yunus Hendrawan, Bens Pardamean<br>Journal: <font color = "#ff00ff">Journal of Asia Business Studies</font><br>Journal Link: <a href = "https://www.emerald.com/insight/content/doi/10.1108/JABS-10-2022-0354/full/html" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21100385808&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>


[2] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Hybrid Local Search Algorithm for Optimization Route of Travelling Salesman Problem</font><br>Author: Muhammad Khahfi Zuhanda, Noriszura Ismail, Rezzy Eko Caraka, Rahmad Syah, <font color = "red" size = 5>Prana Ugiana Gio</font><br>Journal: <font color = "#ff00ff">International Journal of Advanced Computer Science and Applications</font><br>Journal Link: <a href = "https://thesai.org/Downloads/Volume14No9/Paper_35-Hybrid_Local_Search_Algorithm_for_Optimization_Route.pdf" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=21100867241&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>


[3] <font color = "#0000ff">Title: <font color = "blue" style="background-color: #d0ff14">Measuring the physical infrastructure development as poverty reduction program in Kalimantan, Indonesia</font><br>Author: Budhi Fatanza Wiratama, Robert Kurniawan, Mulyanto, Mohamad Andrian Isnaeni, Bagus Sumargo, <font color = "red" size = 5>Prana Ugiana Gio</font><br>Journal: <font color = "#ff00ff">Cities</font><br>Journal Link: <a href = "https://www.sciencedirect.com/science/article/pii/S026427512300327X" target = "_blank" style = "text-decoration:none">Link</a><br>Scopus Indexed & Scimago Link: <a href = "https://www.scimagojr.com/journalsearch.php?q=16956&tip=sid&clean=0" target = "_blank" style = "text-decoration:none">Yes</a></font><br><br>







             ''', unsafe_allow_html = True)





























with tab2:
   col1, col2, col3 = st.columns(3)
   with col1:
     st.image("https://statkomat.com/gambar/ugi.png", caption='', width = 350)
   with col1:
     st.markdown("<a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>STATKOMAT</b></font></a> | <a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'><font color = 'orange'><b>YOUTUBE</b></font></a>", unsafe_allow_html=True)

