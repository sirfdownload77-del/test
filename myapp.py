import streamlit as st
import datetime

st.set_page_config(page_title="QLC Vertical Summons", layout="wide")

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
            padding: 20px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }
        .no-print { display: none !important; }
        header, footer, .stDeployButton { display: none !important; }
    }
    body { direction: rtl; font-family: 'Jameel Noori Nastaleeq', 'Arial', serif; }
    .case-header-table {
        width: 100%;
        margin: 10px 0;
        border-collapse: collapse;
    }
    .case-header-table td {
        vertical-align: middle;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("QLC - عمودی سمن جنریٹر")

# ڈیفالٹ تاریخ
default_date = datetime.date(2026, 2, 18)

with st.form("vertical_form"):
    st.write("### کیس کی تفصیلات")
    c1, c2 = st.columns(2)
    with c1:
        court = st.text_input("بعدالت جناب", "سول جج صاحب، ملتان")
        case_no = st.text_input("مقدمہ نمبر", "123/2026")
        plaintiff = st.text_input("مدعی کا نام", "محمد عقیل")
    with c2:
        defendant_name = st.text_input("مدعا علیہ کا نام", "محمد سلیم")
        subject = st.text_input("نالش بابت", "تکمیل معاہدہ مختص بیع")
        issuance_date = st.date_input("تاریخِ اجراء", default_date)
        statement_date = st.date_input("تحریری بیان کی تاریخ", default_date)

    st.divider()
    col_l, col_r = st.columns(2)
    with col_l:
        st.write("### سمن 1")
        def1_full = st.text_area("مدعا علیہ 1 کا مکمل پتہ", "محمد سلیم ولد نامعلوم سکنہ ملتان")
        hearing1 = st.date_input("تاریخِ پیشی 1", default_date)
    with col_r:
        st.write("### سمن 2")
        def2_full = st.text_area("مدعا علیہ 2 کا مکمل پتہ")
        hearing2 = st.date_input("تاریخِ پیشی 2", default_date)

    submit = st.form_submit_button("پرنٹ کے لیے تیار کریں")

def render_summons(court, case_no, plaintiff, versus, defendant_address, subject, hearing, issuance, note):
    h_str = hearing.strftime('%d.%m.%Y')
    i_str = issuance.strftime('%d.%m.%Y')
    n_str = note.strftime('%d.%m.%Y')
    
    return f"""
    <div class="summons-box" style="direction: rtl; line-height: 1.7;">
        <h3 style="text-align: center; font-size: 22px; margin-bottom: 0;">سمن تنقیح طلب بنام مدعا علیہ</h3>
        <p style="text-align: center; font-size: 11px; margin-top: 0;">(قاعدہ نمبر 5 مجموعہ ضابطہ دیوانی)</p>
        
        <p style="font-size: 15px; margin: 10px 0 5px 0;"><b>بعدالت جناب:</b> {court}</p>
        
        <p style="font-size: 15px; margin: 0;"><b>مقدمہ نمبر:</b> {case_no}</p>
        
        <table class="case-header-table">
            <tr>
                <td style="text-align: right; width: 40%;"><b>{plaintiff}</b> (مدعی)</td>
                <td style="text-align: center; width: 20%;"><b>بنام</b></td>
                <td style="text-align: left; width: 40%;"><b>{versus}</b> (مدعا علیہ)</td>
            </tr>
        </table>

        <p style="font-size: 15px; margin: 10px 0;"><b>بنام:</b> {defendant_address}</p>

        <p style="text-align: justify; font-size: 14px;">
        ہر گاہ <b>{plaintiff}</b> نے آپ کے نام ایک نالش بابت <b>{subject}</b> کے دائر کی ہے لہذا آپ کو بذریعہ تحریر ہذا حکم ہوتا ہے کہ 
        <b>بتاریخ {h_str} بوقت 8 بجے</b> قبل از دوپہر اصالتاً یا معرفت وکیل جو مقدمہ کے حالات سے قرار واقعی واقف کیا گیا ہے اور جو کل امور اہم متفقہ مقدمہ کا جواب دے سکے عدالت میں حاضر ہوں اور جوابدہی دعویٰ کریں۔
        
        اور ہر گاہ وہی تاریخ جو آپ کی حاضری کے لئے مقرر ہے انفصال قطعی مقدمہ کی تجویز ہوتی ہے پس آپ کو لازم ہے کہ اسی روز اپنے جملہ گواہوں کو پیش کریں جن کی شہادت پر آپ استدلال کرنا چاہتے ہیں نیز آپ کو لازم ہے کہ جملہ دستاویزات بھی اسی روز پیش کریں۔
        </p>

        <p style="font-size: 14px;">واضح رہے کہ اگر بروز مذکور آپ حاضر نہ ہوں گے تو مقدمہ بغیر حاضری مسموع ہوگا اور فصیل ہوگا۔ آج <b>بتاریخ {i_str}</b> جاری کیا گیا۔</p>

        <div style="margin-top: 25px; display: flex; justify-content: space-between; font-size: 15px;">
            <span><b>دستخط جج صاحب</b> ________</span>
            <span><b>مہر عدالت</b> ________</span>
        </div>

        <div style="font-size: 11px; border-top: 1px solid #000; padding-top: 10px; margin-top: auto; padding-bottom: 20px;">
            <b>اطلاع:</b> (1) اگر آپ کو اندیشہ ہو کہ گواہ مرضی سے حاضر نہ ہوں گے تو خرچہ ضروری داخل کر کے سمن جاری کروائیں (2) اگر مطالبہ تسلیم کریں تو رقم عدالت میں داخل کریں۔
            <br><br>
            <b>نوٹ:</b> تحریری بیان بتاریخ <b>{n_str}</b> تک داخل کریں۔
        </div>
    </div>
    """

if submit:
    d2 = def2_full if def2_full else def1_full
    h2 = hearing2 if def2_full else hearing1
    
    html_content = f"""
    <div class="main-container">
        {render_summons(court, case_no, plaintiff, defendant_name, def1_full, subject, hearing1, issuance_date, statement_date)}
        {render_summons(court, case_no, plaintiff, defendant_name, d2, subject, h2, issuance_date, statement_date)}
    </div>
    <script>setTimeout(function() {{ window.print(); }}, 500);</script>
    """
    st.components.v1.html(html_content, height=1300)
