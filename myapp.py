import streamlit as st

# Set page to wide mode to better view the forms
st.set_page_config(page_title="QLC Summons Generator", layout="wide")

st.title("QLC Qureshi Law Chamber - Summons Generator")
st.subheader("تیاری سمن تنقیح طلب (ایک صفحہ پر دو)")

# --- Input Section ---
with st.expander("کیس کی تفصیلات درج کریں (Enter Case Details)", expanded=True):
    col_common1, col_common2 = st.columns(2)
    with col_common1:
        court = st.text_input("بعدالت جناب (Court Name)", "سول جج صاحب، ملتان")
        case_no = st.text_input("مقدمہ نمبر (Case No.)")
    with col_common2:
        plaintiff = st.text_input("مدعی کا نام (Plaintiff)")
        subject = st.text_input("نالش بابت (Subject of Suit)", "حصولِ ڈگری")

    st.divider()

    col_def1, col_def2 = st.columns(2)
    with col_def1:
        st.write("### مدعا علیہ نمبر 1")
        def1 = st.text_input("نام و پتہ (Defendant 1)")
        date1 = st.date_input("تاریخ پیشی (Hearing Date)", key="d1")
    with col_def2:
        st.write("### مدعا علیہ نمبر 2")
        def2 = st.text_input("نام و پتہ (Defendant 2)", help="خالی چھوڑنے پر پہلے کاپی ہی بنے گی")
        date2 = st.date_input("تاریخ پیشی (Hearing Date)", key="d2")

# Use data from Def 1 if Def 2 is empty
final_def2 = def2 if def2 else def1
final_date2 = date2 if def2 else date1

# --- Template Function ---
def get_summons_html(court, case_no, plaintiff, defendant, subject, date):
    return f"""
    <div style="border: 2px solid #000; padding: 20px; margin-bottom: 20px; direction: rtl; font-family: 'Arial';">
        <h2 style="text-align: center; margin: 0;">سمن تنقیح طلب بنام مدعا علیہ</h2>
        <p style="text-align: center; font-size: 14px;">(قاعدہ نمبر 5 مجموعہ ضابطہ دیوانی)</p>
        <p><b>بعدالت جناب:</b> {court}</p>
        <p><b>مقدمہ نمبر:</b> {case_no} <b>بنام</b> {plaintiff} وغیرہ</p>
        <p><b>بنام:</b> {defendant}</p>
        <p style="text-align: justify; line-height: 1.6;">
            ہر گاہ {plaintiff} نے آپ کے نام ایک نالش بابت {subject} کے دائر کی ہے لہذا آپ کو بذریعہ تحریر ہذا حکم ہوتا ہے کہ 
            <b>بتاریخ {date} بوقت 8 بجے</b> قبل از دوپہر اصالتاً یا معرفت وکیل حاضر عدالت ہوں اور جوابدہی دعویٰ کریں۔ 
            اسی روز اپنے جملہ گواہوں اور دستاویزات کو ہمراہ لائیں جن پر آپ استدلال کرنا چاہتے ہیں۔ 
            واضح رہے کہ عدم حاضری کی صورت میں کارروائی یکطرفہ عمل میں لائی جائے گی۔
        </p>
        <p style="font-size: 12px; border-top: 1px solid #ccc; padding-top: 10px;">
            <b>اطلاع:</b> اگر آپ گواہان کو جبراً طلب کرنا چاہتے ہیں تو خرچہ عدالت میں جمع کروا کر سمن جاری کروائیں۔
        </p>
        <table style="width: 100%; margin-top: 20px;">
            <tr>
                <td>دستخط جج صاحب ____________</td>
                <td style="text-align: left;">مہر عدالت ____________</td>
            </tr>
        </table>
    </div>
    """

# --- Preview & Print ---
if st.button("Generate & Print"):
    # Combine two templates
    full_html = f"""
    <div id="print-area">
        {get_summons_html(court, case_no, plaintiff, def1, subject, date1)}
        <div style="text-align:center; color: gray;">----------------------------------------------------------------------</div>
        {get_summons_html(court, case_no, plaintiff, final_def2, subject, final_date2)}
    </div>
    <script>window.print();</script>
    """
    st.components.v1.html(full_html, height=1200, scrolling=True)
