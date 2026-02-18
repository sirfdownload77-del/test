import streamlit as st

# صفحے کی بنیادی سیٹنگ
st.set_page_config(
    page_title="QLC Qureshi Law Chamber",
    page_icon="⚖️",
    layout="wide"
)

# نستعلیق فونٹ اور سٹائلنگ
st.markdown("""
    <style>
    @font-face {
        font-family: 'Jameel Noori Nastaleeq';
        src: url('https://fonts.cdnfonts.com/s/73173/JameelNooriNastaleeq.woff') format('woff');
    }
    .main-title {
        font-family: 'Jameel Noori Nastaleeq', serif;
        font-size: 50px;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        font-family: 'Arial';
        font-size: 20px;
        text-align: center;
        color: #555;
        margin-top: 0px;
    }
    .chamber-info {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-right: 5px solid #1E3A8A;
        direction: rtl;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

# ہیڈر سیکشن
st.markdown('<div class="main-title">QLC قریشی لاء چیمبر</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Qureshi Law Chamber - Multan</div>', unsafe_allow_html=True)

st.divider()

# چیمبر کی تفصیلات کا کالم
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="chamber-info">
        <h3>محمد حسن قریشی</h3>
        <p>ایڈووکیٹ ہائی کورٹ</p>
        <p><b>پتہ:</b> 02-اولڈ بلاک، نزد ججز گیٹ، ملتان</p>
        <p><b>ای میل:</b> qureshilaw1977@gmail.com</p>
        <p><b>واٹس ایپ:</b> +92 330 5477770 | <b>سیل:</b> +92 303 0244382</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.info("### فارم کا انتخاب کریں")
    st.write("بائیں طرف موجود مینو سے مطلوبہ فارم پر کلک کریں:")
    st.success("1️⃣ سمن (Summons)\n\n2️⃣ وکالت نامہ (آنے والا ہے)\n\n3️⃣ فردِ پتہ (آنے والا ہے)")

st.divider()

# ہدایات
st.markdown("### 📋 ہدایات برائے استعمال")
st.markdown("""
* **مینو کا استعمال:** تمام قانونی فارمز بائیں جانب (Sidebar) میں ترتیب سے موجود ہیں۔
* **ڈیٹا انٹری:** فارم منتخب کرنے کے بعد تمام ضروری معلومات اردو یا انگریزی میں درج کریں۔
* **پرنٹنگ:** 'پرنٹ' بٹن دبانے پر نیا ڈائیلاگ کھلے گا۔ وہاں کاغذ کا سائز **Legal (8.5x13)** منتخب کرنا نہ بھولیں۔
* **فونٹ:** بہترین رزلٹ کے لیے اپنے کمپیوٹر میں 'Jameel Noori Nastaleeq' فونٹ انسٹال کریں۔
""")

# فوٹر
st.sidebar.markdown("---")
st.sidebar.write("Developed for **QLC Qureshi Law Chamber**")
st.sidebar.write("📍 Multan, Pakistan")
