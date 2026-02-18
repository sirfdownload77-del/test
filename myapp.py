import streamlit as st

st.set_page_config(page_title="QLC Summons Generator", layout="wide")

# CSS برائے لیگل سائز پرنٹنگ
st.markdown("""
    <style>
    @media print {
        html, body {
            height: 12.8in; /* کاغذ سے تھوڑا کم تاکہ مارجن برقرار رہے */
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden;
        }
        .main-container {
            width: 8.5in;
            height: 12.8in;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            margin: auto;
        }
        .summons-box {
            height: 48% !important; /* صفحے کا آدھے سے تھوڑا کم حصہ */
            page-break-inside: avoid;
            border: 2px solid #000 !important;
            padding: 15px !important;
            box-sizing: border-box;
        }
        .no-print { display: none !important; }
        /* ہائیڈ کریں اسٹریم لٹ کے ڈیفالٹ ایلیمنٹس */
        header, footer, .stDeployButton { display: none !important; }
    }
    body { direction: rtl; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

st.title("QLC Qureshi Law Chamber")
st.subheader("سمن تنقیح طلب - فکسڈ لیگل سائز (13x8.5)")

with st.form("summons_form"):
    st.write("### مشترکہ معلومات")
    c1, c2 = st.columns(2)
    with c1:
        court = st.text_input("بعدالت جناب", "سول جج صاحب، ملتان")
        case_no = st.text_input("مقدمہ نمبر")
    with c2:
        plaintiff = st.text_input("مدعی کا نام")
        subject = st.text_input("نالش بابت", "حصولِ ڈگری")
    
    st.divider()
    col_l, col_r = st.columns(2)
    with col_l:
        st.write("### سمن 1")
        def1 = st.text_area("نام و پتہ مدعا علیہ (1)", height=100)
        date1 = st.text_input("تاریخِ پیشی (1)")
        issuance1 = st.text_input("تاریخِ اجراء (1)")
        note1 = st.text_input("تحریری بیان کی تاریخ (1)")
    with col_r:
        st.write("### سمن 2")
        def2 = st.text_area("نام و پتہ مدعا علیہ (2)", height=100)
        date2 = st.text_input("تاریخِ پیشی (2)")
        issuance2 = st.text_input("تاریخِ اجراء (2)")
        note2 = st.text_input("تحریری بیان کی تاریخ (2)")

    submit = st.form_submit_button("پرنٹ کے لیے تیار کریں")

def render_summons(court, case_no, plaintiff, defendant, subject, hearing_date, issuance, note_date):
    return f"""
    <div class="summons-box" style="direction: rtl; line-height: 1.5;">
        <h2 style="text-align: center; margin: 0; font-size: 18px;">سمن تنقیح طلب بنام مدعا علیہ</h2>
        <p style="text-align: center; font-size: 11px; margin: 0;">(قاعدہ نمبر 5 مجموعہ ضابطہ دیوانی)</p>
        
        <p style="margin: 5px 0; font-size: 14px;"><b>بعدالت جناب:</b> {court}</p>
        <p style="margin: 5px 0; font-size: 14px;"><b>مقدمہ نمبر:</b> {case_no} &nbsp;&nbsp; <b>بنام</b> &nbsp;&nbsp; {plaintiff}</p>
        <p style="margin: 5px 0; font-size: 14px;"><b>بنام:</b> {defendant}</p>

        <p style="text-align: justify; font-size: 13px; margin: 5px 0;">
        ہر گاہ <b>{plaintiff}</b> نے آپ کے نام ایک نالش بابت <b>{subject}</b> کے دائر کی ہے لہذا آپ کو بذریعہ تحریر ہذا حکم ہوتا ہے کہ 
        <b>بتاریخ {hearing_date} بوقت 8 بجے</b> قبل از دوپہر اصالتاً معرفت وکیل حاضر ہوں اور جوابدہی دعویٰ کریں۔
        اور ہر گاہ وہی تاریخ انفصال قطعی مقدمہ کی تجویز ہوتی ہے پس آپ کو لازم ہے کہ اسی روز اپنے جملہ گواہوں اور دستاویزات کو پیش کریں۔
        </p>

        <p style="font-size: 13px; margin: 5px 0;">عدم حاضری کی صورت میں فیصلہ یکطرفہ ہوگا۔ آج <b>بتاریخ {issuance}</b> جاری کیا گیا۔</p>

        <table style="width: 100%; margin-top: 5px;">
            <tr style="font-size: 13px;">
                <td><b>دستخط جج صاحب</b> ________</td>
                <td style="text-align: left;"><b>مہر عدالت</b> ________</td>
            </tr>
        </table>

        <div style="margin-top: 5px; font-size: 10px; border-top: 1px solid #ccc; padding-top: 5px;">
            <b>اطلاع:</b> گواہان کو جبراً طلب کرنے کے لیے خرچہ عدالت جمع کروائیں۔ (2) اگر مطالبہ تسلیم کریں تو رقم جمع کرائیں۔
            <br><b>نوٹ:</b> تحریری بیان بتاریخ <b>{note_date}</b> تک داخل کریں۔
        </div>
    </div>
    """

if submit:
    html_content = f"""
    <div class="main-container">
        {render_summons(court, case_no, plaintiff, def1, subject, date1, issuance1, note1)}
        {render_summons(court, case_no, plaintiff, def2, subject, date2, issuance2, note2)}
    </div>
    <script>
        setTimeout(function() {{
            window.print();
        }}, 500);
    </script>
    """
    st.components.v1.html(html_content, height=1200)
