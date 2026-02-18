import streamlit as st

st.set_page_config(page_title="QLC Vertical Summons", layout="wide")

# CSS برائے عمودی تقسیم (Vertical Split)
st.markdown("""
    <style>
    @media print {
        @page {
            size: 8.5in 13in;
            margin: 0;
        }
        html, body {
            height: 13in;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden;
        }
        .main-container {
            display: flex; /* عمودی تقسیم کے لیے فلیکس باکس */
            width: 8.5in;
            height: 13in;
            flex-direction: row; /* سائیڈ بائی سائیڈ */
            justify-content: space-between;
        }
        .summons-box {
            width: 48%; /* چوڑائی آدھے سے کم تاکہ درمیان میں جگہ رہے */
            height: 100%;
            border-left: 1px dashed #000; /* کٹائی کا نشان */
            padding: 10px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }
        .no-print { display: none !important; }
        header, footer, .stDeployButton { display: none !important; }
    }
    body { direction: rtl; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

st.title("QLC - عمودی سمن جنریٹر")

with st.form("vertical_form"):
    st.write("### کیس کی معلومات")
    c1, c2 = st.columns(2)
    with c1:
        court = st.text_input("بعدالت جناب", "سول جج صاحب، ملتان")
        case_no = st.text_input("مقدمہ نمبر")
        plaintiff = st.text_input("مدعی کا نام")
    with c2:
        subject = st.text_input("نالش بابت", "حصولِ ڈگری")
        issuance = st.text_input("تاریخِ اجراء")
        note_date = st.text_input("تحریری بیان کی تاریخ")

    st.divider()
    col_l, col_r = st.columns(2)
    with col_l:
        st.write("### سمن 1 (بائیں طرف)")
        def1 = st.text_area("مدعا علیہ 1", height=80)
        date1 = st.text_input("تاریخِ پیشی 1")
    with col_r:
        st.write("### سمن 2 (دائیں طرف)")
        def2 = st.text_area("مدعا علیہ 2", height=80)
        date2 = st.text_input("تاریخِ پیشی 2")

    submit = st.form_submit_button("پرنٹ تیار کریں")

def render_vertical_summons(court, case_no, plaintiff, defendant, subject, hearing_date, issuance, note_date):
    return f"""
    <div class="summons-box" style="direction: rtl; line-height: 1.4; padding: 15px;">
        <h3 style="text-align: center; font-size: 16px; margin-bottom: 5px;">سمن تنقیح طلب بنام مدعا علیہ</h3>
        <p style="text-align: center; font-size: 10px; margin: 0;">(قاعدہ نمبر 5 مجموعہ ضابطہ دیوانی)</p>
        
        <p style="font-size: 13px; margin: 5px 0;"><b>بعدالت جناب:</b><br>{court}</p>
        <p style="font-size: 13px; margin: 5px 0;"><b>مقدمہ نمبر:</b> {case_no}</p>
        <p style="font-size: 13px; margin: 5px 0;"><b>بنام:</b> {plaintiff}</p>
        <p style="font-size: 13px; margin: 5px 0;"><b>بنام مدعا علیہ:</b><br>{defendant}</p>

        <p style="text-align: justify; font-size: 12px; margin: 10px 0;">
        ہر گاہ <b>{plaintiff}</b> نے آپ کے نام ایک نالش بابت <b>{subject}</b> کے دائر کی ہے لہذا آپ کو حکم ہوتا ہے کہ 
        <b>بتاریخ {hearing_date} بوقت 8 بجے</b> قبل از دوپہر اصالتاً یا معرفت وکیل حاضر عدالت ہوں اور جوابدہی دعویٰ کریں۔
        <br><br>
        اسی روز اپنے جملہ گواہوں اور دستاویزات کو پیش کریں۔ عدم حاضری کی صورت میں فیصلہ یکطرفہ ہوگا۔ 
        <br><br>
        آج <b>بتاریخ {issuance}</b> جاری کیا گیا۔
        </p>

        <div style="margin-top: auto; font-size: 12px;">
            <p><b>دستخط جج صاحب</b> ________</p>
            <p style="text-align: left;"><b>مہر عدالت</b> ________</p>
        </div>

        <div style="font-size: 9px; border-top: 1px solid #ccc; padding-top: 5px; margin-top: 10px;">
            <b>اطلاع:</b> گواہان کو جبراً طلب کرنے کے لیے خرچہ عدالت جمع کروائیں۔ 
            <br><b>نوٹ:</b> تحریری بیان بتاریخ <b>{note_date}</b> تک داخل کریں۔
        </div>
    </div>
    """

if submit:
    html_content = f"""
    <div class="main-container">
        {render_vertical_summons(court, case_no, plaintiff, def1, subject, date1, issuance, note_date)}
        {render_vertical_summons(court, case_no, plaintiff, def2 if def2 else def1, subject, date2 if def2 else date1, issuance, note_date)}
    </div>
    <script>setTimeout(function() {{ window.print(); }}, 500);</script>
    """
    st.components.v1.html(html_content, height=1300)
