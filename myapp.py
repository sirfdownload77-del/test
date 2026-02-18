import streamlit as st

# صفحے کی سیٹنگ
st.set_page_config(page_title="QLC Summons Generator", layout="wide")

st.title("QLC Qureshi Law Chamber")
st.subheader("سمن تنقیح طلب - مکمل قانونی تحریر کے ساتھ")

# ڈیٹا ان پٹ
with st.form("summons_form"):
    col1, col2 = st.columns(2)
    with col1:
        court = st.text_input("بعدالت جناب", "سول جج صاحب، ملتان")
        case_no = st.text_input("مقدمہ نمبر")
        plaintiff = st.text_input("مدعی کا نام")
    with col2:
        subject = st.text_input("نالش بابت", "حصولِ ڈگری")
        issuance_date = st.text_input("تاریخِ اجراء (آج کی تاریخ)")
        statement_date = st.text_input("تحریری بیان کی آخری تاریخ (نوٹ کے لیے)")

    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        st.write("### سمن 1 (مدعا علیہ اول)")
        def1 = st.text_input("نام و پتہ مدعا علیہ 1")
        date1 = st.text_input("تاریخِ پیشی 1")
    with c2:
        st.write("### سمن 2 (مدعا علیہ دوم / کاپی)")
        def2 = st.text_input("نام و پتہ مدعا علیہ 2 (خالی چھوڑنے پر پہلے کاپی بنے گی)")
        date2 = st.text_input("تاریخِ پیشی 2")

    submit = st.form_submit_button("سمن تیار کریں")

# مدعا علیہ 2 کے لیے ڈیٹا کی جانچ
final_def2 = def2 if def2 else def1
final_date2 = date2 if date2 else date1

# مکمل قانونی تحریر کا فنکشن
def get_full_tehrir(court, case_no, plaintiff, defendant, subject, hearing_date, issuance, statement_date):
    return f"""
    <div style="border: 1px solid #000; padding: 25px; margin-bottom: 30px; direction: rtl; font-family: 'Arial'; line-height: 1.8;">
        <h2 style="text-align: center; margin: 0;">سمن تنقیح طلب بنام مدعا علیہ</h2>
        <p style="text-align: center; font-size: 14px;">(قاعدہ نمبر 5 مجموعہ ضابطہ دیوانی)</p>
        
        <p><b>بعدالت جناب:</b> {court}</p>
        <p><b>مقدمہ نمبر:</b> {case_no} &nbsp;&nbsp; <b>بنام</b> &nbsp;&nbsp; {plaintiff}</p>
        <p><b>بنام:</b> {defendant}</p>

        <p style="text-align: justify;">
        ہر گاہ <b>{plaintiff}</b> نے آپ کے نام ایک نالش بابت <b>{subject}</b> کے دائر کی ہے لہذا آپ کو بذریعہ تحریر ہذا حکم ہوتا ہے کہ 
        <b>بتاریخ {hearing_date} بوقت 8 بجے</b> قبل از دوپہر اصالتاً معرفت وکیل جو مقدمہ کے حالات قرار واقعی واقف کیا گیا ہے 
        اور جو کل امور اہم متفقہ مقدمہ کا جواب دے سکے یا جس کے ساتھ کوئی اور شخص ہو جو جوابات ایسے سوالات کا دے سکے عدالت میں حاضر ہوں اور جوابدہی دعویٰ کریں۔
        </p>

        <p style="text-align: justify;">
        اور ہر گاہ وہی تاریخ جو آپ کی حاضری کے لئے مقرر ہے انفصال قطعی مقدمہ کی تجویز ہوتی ہے پس آپ کو لازم ہے کہ اسی روز اپنے جملہ گواہوں کو پیش کریں 
        جن کی شہادت پر آپ استدلال کرنا چاہتے ہیں نیز آپ کو لازم ہے کہ جملہ دستاویزات جن پر آپ بتائید اپنی جواب دہی کے استدلال کرنا چاہتے ہیں اسی روز پیش کریں۔
        </p>

        <p>واضح رہے کہ اگر بروز مذکور آپ حاضر نہ ہوں گے تو مقدمہ بغیر حاضری مسموع ہوگا اور فصیل ہوگا۔ بہ ثبت میرے دستخط اور مہر عدالت آج <b>بتاریخ {issuance}</b> جاری کیا گیا۔</p>

        <table style="width: 100%; margin-top: 15px;">
            <tr>
                <td><b>دستخط جج صاحب</b> ________________</td>
                <td style="text-align: left;"><b>مہر عدالت</b> ________________</td>
            </tr>
        </table>

        <div style="margin-top: 15px; font-size: 13px; border-top: 1px solid #eee; padding-top: 10px;">
            <b>اطلاع:</b> (1) اگر آپ کو یہ اندیشہ ہو کہ آپ کے گواہ اپنی مرضی سے حاضر نہ ہوں گے تو آپ عدالت سے سمن بایں مراد جاری کرا سکتے ہیں کہ جو گواہ حاضر نہ ہو وہ جبراً حاضر کرایا جائے... بشرطیکہ آپ خرچہ ضروری عدالت میں داخل کریں۔ <br>
            (2) اگر مطالبہ مدعی تسلیم کرتے ہوں تو آپ کو لازم ہے کہ روپیہ اور خرچہ ثالثی عدالت میں داخل کریں۔
        </div>

        <div style="margin-top: 10px; font-size: 13px;">
            <b>نوٹ:</b> اگر تحریری بیان کی ضرورت ہو تو آپ کو چاہیے کہ بتاریخ <b>{statement_date}</b> تک تحریری بیان داخل کریں۔
        </div>
    </div>
    """

# ڈسپلے اور پرنٹ
if submit:
    full_html = f"""
    <div id="print-area">
        {get_full_tehrir(court, case_no, plaintiff, def1, subject, date1, issuance_date, statement_date)}
        <div style="text-align:center; color: #ccc; margin: 10px 0;">--------------------------------------------------------------------------------</div>
        {get_full_tehrir(court, case_no, plaintiff, final_def2, subject, final_date2, issuance_date, statement_date)}
    </div>
    <script>window.print();</script>
    """
    st.components.v1.html(full_html, height=1500, scrolling=True)
