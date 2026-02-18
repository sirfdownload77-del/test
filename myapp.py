import streamlit as st
import datetime

st.set_page_config(page_title="QLC Vertical Summons", layout="wide")

# CSS برائے عمودی پرنٹنگ اور فونٹ
st.markdown("""
    <style>
    @font-face {
        font-family: 'Jameel Noori Nastaleeq';
        src: url('https://fonts.cdnfonts.com/s/73173/JameelNooriNastaleeq.woff') format('woff');
    }
    @media print {
        @page { size: 8.5in 13in; margin: 0; }
        html, body { height: 13in; margin: 0 !important; padding: 0 !important; overflow: hidden; }
        .main-container {
            display: flex;
            width: 8.5in;
            height: 13in;
            flex-direction: row;
            justify-content: space-between;
        }
        .summons-box {
            width: 49%;
            height: 100%;
            border-left: 1px dashed #000;
            padding: 15px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }
        .no-print { display: none !important; }
        header, footer, .stDeployButton { display: none !important; }
    }
    body { direction: rtl; font-family: 'Jameel Noori Nastaleeq', 'Arial', serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("QLC - عمودی سمن جنریٹر (Date Picker کے ساتھ)")

with st.form("vertical_form"):
    st.write("### بنیادی معلومات")
    c1, c2 = st.columns(2)
    with c1:
        court = st.text_input("بعدالت جناب", "سول جج صاحب، ملتان")
        case_no = st.text_input("مقدمہ نمبر")
        plaintiff = st.text_input("مدعی کا نام")
    with c2:
        subject = st.text_input("نالش بابت", "حصولِ ڈگری / تعمیلِ مختص")
        issuance_date = st.date_input("تاریخِ اجراء (Issuance Date)", datetime.date.today())
        statement_date = st.date_input("تحریری بیان کی تاریخ (Note Date)")

    st.divider()
    col_l, col_r = st.columns(2)
    with col_l:
        st.write("### سمن 1")
        def1 = st.text_area("مدعا علیہ 1 (نام و پتہ)")
        hearing1 = st.date_input("تاریخِ پیشی 1")
    with col_r:
        st.write("### سمن 2")
        def2 = st.text_area("مدعا علیہ 2 (نام و پتہ)", help="خالی چھوڑنے پر پہلے کی نقل بنے گی")
        hearing2 = st.date_input("تاریخِ پیشی 2")

    submit = st.form_submit_button("پرنٹ تیار کریں")

def render_summons(court, case_no, plaintiff, defendant, subject, hearing, issuance, note):
    # تاریخوں کو خوبصورت اردو فارمیٹ میں تبدیل کرنا
    h_str = hearing.strftime('%d-%m-%Y')
    i_str = issuance.strftime('%d-%m-%Y')
    n_str = note.strftime('%d-%m-%Y')
    
    return f"""
    <div class="summons-box" style="direction: rtl; line-height: 1.6;">
        <h3 style="text-align: center; font-size: 20px; margin-bottom: 0;">سمن تنقیح طلب بنام مدعا علیہ</h3>
        <p style="text-align: center; font-size: 11px; margin-top: 0;">(قاعدہ نمبر 5 مجموعہ ضابطہ دیوانی)</p>
        
        <p style="font-size: 14px; margin: 5px 0;"><b>بعدالت جناب:</b> {court}</p>
        <p style="font-size: 14px; margin: 5px 0;"><b>مقدمہ نمبر:</b> {case_no} &nbsp;&nbsp; <b>بنام</b> &nbsp;&nbsp; {plaintiff}</p>
        <p style="font-size: 14px; margin: 5px 0;"><b>بنام مدعا علیہ:</b> {defendant}</p>

        <p style="text-align: justify; font-size: 13.5px;">
        ہر گاہ <b>{plaintiff}</b> نے آپ کے نام ایک نالش بابت <b>{subject}</b> کے دائر کی ہے لہذا آپ کو بذریعہ تحریر ہذا حکم ہوتا ہے کہ 
        <b>بتاریخ {h_str} بوقت 8 بجے</b> قبل از دوپہر اصالتاً یا معرفت وکیل جو مقدمہ کے حالات سے واقف ہو عدالت میں حاضر ہوں اور جوابدہی دعویٰ کریں۔
        </p>

        <p style="text-align: justify; font-size: 13.5px;">
        اور ہر گاہ وہی تاریخ جو آپ کی حاضری کے لئے مقرر ہے انفصال قطعی مقدمہ کی تجویز ہوتی ہے پس آپ کو لازم ہے کہ اسی روز اپنے جملہ گواہوں کو پیش کریں جن کی شہادت پر آپ استدلال کرنا چاہتے ہیں نیز آپ کو لازم ہے کہ جملہ دستاویزات بھی اسی روز پیش کریں۔
        </p>

        <p style="font-size: 13.5px;">واضح رہے کہ اگر بروز مذکور آپ حاضر نہ ہوں گے تو مقدمہ بغیر حاضری مسموع ہوگا اور فصیل ہوگا۔ آج <b>بتاریخ {i_str}</b> جاری کیا گیا۔</p>

        <div style="margin-top: 20px; display: flex; justify-content: space-between;">
            <span><b>دستخط جج صاحب</b> ________</span>
            <span><b>مہر عدالت</b> ________</span>
        </div>

        <div style="font-size: 11px; border-top: 1px solid #000; padding-top: 10px; margin-top: 30px;">
            <b>اطلاع:</b> (1) اگر آپ کو اندیشہ ہو کہ گواہ مرضی سے حاضر نہ ہوں گے تو خرچہ ضروری داخل کر کے سمن جاری کروائیں تاکہ وہ جبراً حاضر کرائے جائیں۔ 
            (2) اگر مطالبہ تسلیم کرتے ہوں تو روپیہ اور خرچہ عدالت میں داخل کریں تاکہ کارروائی باجراء ڈگری سے بچ سکیں۔
            <br><br>
            <b>نوٹ:</b> تحریری بیان بتاریخ <b>{n_str}</b> تک داخل کریں۔
        </div>
    </div>
    """

if submit:
    # فائنل ڈیٹا کی تیاری
    d2 = def2 if def2 else def1
    h2 = hearing2 if def2 else hearing1
    
    html_content = f"""
    <div class="main-container">
        {render_summons(court, case_no, plaintiff, def1, subject, hearing1, issuance_date, statement_date)}
        {render_summons(court, case_no, plaintiff, d2, subject, h2, issuance_date, statement_date)}
    </div>
    <script>setTimeout(function() {{ window.print(); }}, 500);</script>
    """
    st.components.v1.html(html_content, height=1300)
