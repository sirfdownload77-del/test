import streamlit as st
import datetime

# صفحے کی سیٹنگ
st.set_page_config(page_title="وکالت نامہ دیوانی - QLC", layout="wide")

# CSS برائے پروفیشنل پرنٹنگ اور نستعلیق فونٹ
st.markdown("""
    <style>
    @font-face {
        font-family: 'Jameel Noori Nastaleeq';
        src: url('https://fonts.cdnfonts.com/s/73173/JameelNooriNastaleeq.woff') format('woff');
    }
    @media print {
        @page { size: 8.5in 13in; margin: 0.3in; }
        .no-print { display: none !important; }
        header, footer, .stDeployButton { display: none !important; }
        body { margin: 0; padding: 0; }
        .v-container { border: 2px solid #000 !important; width: 100% !important; }
    }
    body { direction: rtl; font-family: 'Jameel Noori Nastaleeq', 'Arial', serif; }
    .v-container {
        border: 2px solid #000;
        padding: 40px;
        margin: auto;
        width: 100%;
        max-width: 800px;
        background-color: white;
    }
    .title { text-align: center; font-size: 30px; font-weight: bold; text-decoration: underline; margin-bottom: 20px; }
    .header-table { width: 100%; border-collapse: collapse; margin-bottom: 10px; }
    .header-table td { font-size: 20px; padding: 5px; vertical-align: middle; }
    .legal-text { text-align: justify; font-size: 19px; line-height: 2.1; margin: 15px 0; }
    .footer-section { margin-top: 30px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ وکالت نامہ دیوانی (QLC فارمیٹ)")

with st.form("vakalat_form"):
    st.write("### مقدمہ کی تفصیلات")
    c1, c2 = st.columns(2)
    with c1:
        court = st.text_input("بعدالت جناب", "سینئر سول جج صاحب ملتان")
        plaintiff = st.text_input("نام مدعی", "محمد عقیل")
    with c2:
        defendant = st.text_input("نام مدعا علیہم", "محمد سلیم")
        case_type = st.text_input("دعویٰ یا جرم", "تکمیل معاہدہ مختص بیع")
    
    st.divider()
    c3, c4 = st.columns(2)
    with c3:
        adv_names = st.text_area("وکیل صاحبان", "محمد حسن قریشی ایڈووکیٹ ہائی کورٹ")
        location = st.text_input("مقام پیروی", "ضلع کچہری ملتان")
    with c4:
        date_today = st.date_input("مورخہ", datetime.date.today())

    submit = st.form_submit_button("وکالت نامہ تیار کریں")

if submit:
    # آپ کی فراہم کردہ فائل سے اقتباس شدہ متن 
    legal_content = f"""
    مقدمہ مندرجہ بالا عنوان میں اپنی طرف سے واسطے پیروی و جوابدہی برائے پیشی یا / تصفیہ مقدمہ بمقام <b>{location}</b> کے لئے <b>{adv_names}</b> کو حسب ذیل شرائط پر وکیل مقرر کیا ہے کہ میں ہر پیشی پر خود یا بذریعہ مختار خاص روبرو عدالت حاضر ہوتا رہوں گا اور بروقت پکارے جانے مقدمہ وکیل صاحب موصوف کو اطلاع دے کر حاضر عدالت کروں گا۔ اگر پیشی پر مظہر حاضر نہ ہوا اور مقدمہ میری غیر حاضری کی وجہ سے کسی طور پر میرے خلاف ہو گیا تو صاحب موصوف اس کے کسی طور پر ذمہ دار نہ ہوں گے نیز وکیل صاحب موصوف صدر مقام کچہری کے علاوہ کسی جگہ یا کچہری کے اوقات سے پہلے یا بعد یا بروز تعطیل پیروی کرنے کے ذمہ دار نہ ہوں گے اور مقدمہ کچہری کے علاوہ کسی اور جگہ سماعت ہونے پر یا بروز تعطیل یا کچہری کے اوقات کے آگے پیچھے پیش ہونے پر مظہر کو کوئی نقصان پہنچے تو اس کے ذمہ دار یا اس کے واسطے کسی معاوضہ کے ادا کرنے یا مختانہ کے واپس کرنے کے بھی صاحب موصوف ذمہ دار ہوں گے۔ مجھ کو کل ساختہ برداختہ صاحب موصوف مثل کردہ ذات منظور و مقبول ہو گا اور صاحب موصوف کو عرضی دعویٰ یا جواب دعویٰ درخواست اجرائے ڈگری و نظر ثانی اپیل نگرانی و ہر قسم درخواست پر دستخط و تصدیق کرنے کا بھی اختیار ہو گا اور کسی حکم یا ڈگری کرانے اور ہر قسم کا روپیہ وصول کرنے اور رسید دینے اور داخل کرنے اور ہر قسم کے بیان دینے اور اس پر ثالثی و راضی نامہ و فیصلہ بر حلف کرنے اقبال دعویٰ دینے کا بھی اختیار ہو گا اور بصورت جانے بیر و نجات از کچہری صدر اپیل و برآمدگی مقدمہ یا منسوخی ڈگری یکطرفہ درخواست حکمِ امتناعی یا قرق یا گرفتاری قبل از گرفتاری و اجرائے ڈگری بھی صاحب موصوف کو بشرط ادائیگی علیحدہ مختانہ پیروی کا اختیار ہو گا اور بصورت ضرورت صاحب موصوف کو یہ بھی اختیار ہو گا کہ مقدمہ کو یا اسے کے کسی جزو کی کارروائی کے یا بصورت اپیل کسی دوسرے وکیل یا بیرسٹر کو اپنے بجائے یا اپنے ہمراہ مقرر کریں اور ایسے مشیر قانون کو بھی ہر امر میں وہی اور ویسے ہی اختیارات حاصل ہوں گے جیسے صاحب موصوف کو حاصل ہیں اور دورانِ مقدمہ میں جو کچھ ہرجانہ التواء پڑیگا وہ صاحب موصوف کا حق ہو گا۔ اگر وکیل صاحب موصوف کو پوری فیس تاریخ پیشی سے پہلے ادا نہ کروں گا تو صاحب موصوف کو پورا پورا اختیار ہوگا کہ وہ مقدمہ کی پیروی نہ کریں اور ایسی صورت میں میرا کوئی مطالبہ کسی قسم کا صاحب موصوف کے برخلاف نہیں ہو گا۔ لہذا وکالت نامہ لکھ دیا ہے تاکہ سند رہے اور بوقت ضرورت کام آوے۔
    """

    st.markdown(f"""
    <div class="v-container" style="direction: rtl;">
        <div class="title">وکالت نامہ دیوانی</div>
        
        <table class="header-table">
            <tr>
                <td colspan="3"><b>بعدالت جناب:</b> {court}</td>
            </tr>
            <tr>
                <td style="width: 45%;"><b>{plaintiff}</b> (مدعی)</td>
                <td style="text-align: center; width: 10%;"><b>بــــنـــام</b></td>
                <td style="width: 45%; text-align: left;"><b>{defendant}</b> (مدعا علیہم)</td>
            </tr>
        </table>
        
        <table class="header-table" style="border-top: 1px solid #eee;">
            <tr>
                <td><b>منجانب:</b> {plaintiff}</td>
                <td style="text-align: left;"><b>دعویٰ یا جرم:</b> {case_type}</td>
            </tr>
        </table>

        <div style="font-size: 20px; font-weight: bold; margin: 10px 0;">باعث تحریر آنکہ</div>

        <div style="display: flex; justify-content: space-between; font-size: 16px; color: #444;">
            <span>العبــــــــــــــــد</span>
            <span>الالعبــــــــــــــــد</span>
            <span>الالعبــــــــــــــــد</span>
        </div>

        <div class="legal-text">
            {legal_content}
        </div>

        <div style="display: flex; justify-content: space-between; font-size: 16px; color: #444; margin-bottom: 20px;">
            <span>العبــــــــــــــــد</span>
            <span>الالعبــــــــــــــــد</span>
            <span>الالعبــــــــــــــــد</span>
        </div>

        <p style="font-size: 18px;"><b>مورخہ:</b> {date_today.strftime('%d-%m-%Y')}</p>
        <p style="font-size: 18px; text-align: center;"><b>مضمون وکالت نامہ سُن لیا ہے اور اچھی طرح سمجھ لیا ہے اور منظور ہے۔</b></p>
        
        <div style="display: flex; justify-content: space-between; margin-top: 40px;">
            <span>العبــــــــــــــــد: ________________</span>
            <span>العبــــــــــــــــد: ________________</span>
            <span>العبــــــــــــــــد: ________________</span>
        </div>
        
        <div style="margin-top: 50px; border-top: 1px solid #000; padding-top: 10px; font-size: 12px; text-align: center; font-family: Arial;">
            <b>QLC Qureshi Law Chamber</b> | 02-Old Block, Near Judges Gate, Multan | {date_today.year}
        </div>
    </div>
    <script>setTimeout(function() {{ window.print(); }}, 500);</script>
    """, unsafe_allow_html=True)
