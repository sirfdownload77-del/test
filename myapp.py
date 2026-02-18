import streamlit as st

# صفحے کی سیٹنگ
st.set_page_config(page_title="QLC Summons Generator", layout="wide")

st.markdown("""
    <style>
    @media print {
        @page {
            size: 8.5in 13in; /* Legal Size */
            margin: 0.2in;
        }
        .no-print { display: none !important; }
        .stButton { display: none !important; }
    }
    body { direction: rtl; }
    </style>
    """, unsafe_allow_html=True)

st.title("QLC Qureshi Law Chamber")
st.subheader("سمن تنقیح طلب - لیگل سائز پرنٹ (13x8.5)")

# ان پٹ فارم
with st.form("summons_form"):
    st.write("### مشترکہ معلومات (Common Info)")
    c_col1, c_col2 = st.columns(2)
    with c_col1:
        court = st.text_input("بعدالت جناب", "سول جج صاحب، ملتان")
        case_no = st.text_input("مقدمہ نمبر")
    with c_col2:
        plaintiff = st.text_input("مدعی کا نام")
        subject = st.text_input("نالش بابت", "حصولِ ڈگری")
    
    st.divider()
    
    # دونوں سمن کے لیے الگ الگ ڈیٹا
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.write("### پہلا سمن (First Copy)")
        def1 = st.text_input("مدعا علیہ کا نام و پتہ (1)")
        date1 = st.text_input("تاریخِ پیشی (1)")
        issuance1 = st.text_input("تاریخِ اجراء (1)")
        note1 = st.text_input("تحریری بیان کی تاریخ (1)")

    with col_right:
        st.write("### دوسرا سمن (Second Copy)")
        def2 = st.text_input("مدعا علیہ کا نام و پتہ (2)")
        date2 = st.text_input("تاریخِ پیشی (2)")
        issuance2 = st.text_input("تاریخِ اجراء (2)")
        note2 = st.text_input("تحریری بیان کی تاریخ (2)")

    submit = st.form_submit_button("پرنٹ کے لیے تیار کریں")

# سمن کا مکمل ٹیمپلیٹ
def get_summons_layout(court, case_no, plaintiff, defendant, subject, hearing_date, issuance, note_date):
    return f"""
    <div style="border: 2px solid #000; padding: 20px; height: 5.8in; direction: rtl; font-family: 'Arial'; line-height: 1.6; position: relative; margin-bottom: 20px; box-sizing: border-box;">
        <h2 style="text-align: center; margin: 0; font-size: 20px;">سمن تنقیح طلب بنام مدعا علیہ</h2>
        <p style="text-align: center; font-size: 12px; margin-top: 2px;">(قاعدہ نمبر 5 مجموعہ ضابطہ دیوانی)</p>
        
        <p style="margin: 5px 0;"><b>بعدالت جناب:</b> {court}</p>
        <p style="margin: 5px 0;"><b>مقدمہ نمبر:</b> {case_no} &nbsp;&nbsp; <b>بنام</b> &nbsp;&nbsp; {plaintiff}</p>
        <p style="margin: 5px 0;"><b>بنام:</b> {defendant}</p>

        <p style="text-align: justify; font-size: 14px; margin: 10px 0;">
        ہر گاہ <b>{plaintiff}</b> نے آپ کے نام ایک نالش بابت <b>{subject}</b> کے دائر کی ہے لہذا آپ کو بذریعہ تحریر ہذا حکم ہوتا ہے کہ 
        <b>بتاریخ {hearing_date} بوقت 8 بجے</b> قبل از دوپہر اصالتاً معرفت وکیل جو مقدمہ کے حالات قرار واقعی واقف کیا گیا ہے 
        اور جو کل امور اہم متفقہ مقدمہ کا جواب دے سکے عدالت میں حاضر ہوں اور جوابدہی دعویٰ کریں۔
        </p>

        <p style="text-align: justify; font-size: 14px; margin: 10px 0;">
        اور ہر گاہ وہی تاریخ جو آپ کی حاضری کے لئے مقرر ہے انفصال قطعی مقدمہ کی تجویز ہوتی ہے پس آپ کو لازم ہے کہ اسی روز اپنے جملہ گواہوں کو پیش کریں 
        جن کی شہادت پر آپ استدلال کرنا چاہتے ہیں نیز آپ کو لازم ہے کہ جملہ دستاویزات بھی اسی روز پیش کریں۔
        </p>

        <p style="font-size: 14px;">واضح رہے کہ عدم حاضری کی صورت میں فیصلہ یکطرفہ ہوگا۔ آج <b>بتاریخ {issuance}</b> جاری کیا گیا۔</p>

        <table style="width: 100%; margin-top: 10px;">
            <tr>
                <td><b>دستخط جج صاحب</b> ________________</td>
                <td style="text-align: left;"><b>مہر عدالت</b> ________________</td>
            </tr>
        </table>

        <div style="margin-top: 10px; font-size: 11px; border-top: 1px solid #ccc; padding-top: 5px;">
            <b>اطلاع:</b> گواہان کو جبراً طلب کرنے کے لیے خرچہ عدالت جمع کروائیں۔ (2) اگر مطالبہ تسلیم کریں تو رقم عدالت میں جمع کرائیں۔
            <br><b>نوٹ:</b> تحریری بیان بتاریخ <b>{note_date}</b> تک داخل کریں۔
        </div>
    </div>
    """

if submit:
    # دونوں سمن کو ایک ساتھ جوڑنا
    combined_html = f"""
    <div style="width: 8.1in; margin: auto;">
        {get_summons_layout(court, case_no, plaintiff, def1, subject, date1, issuance1, note1)}
        <div class="no-print" style="text-align:center; color:gray; margin: 5px 0;">-------------------- کٹائی کی جگہ (Cut Here) --------------------</div>
        {get_summons_layout(court, case_no, plaintiff, def2, subject, date2, issuance2, note2)}
    </div>
    <script>window.print();</script>
    """
    st.components.v1.html(combined_html, height=1300, scrolling=True)
