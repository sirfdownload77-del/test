import streamlit as st
import datetime

# صفحے کی سیٹنگ
st.set_page_config(page_title="وکالت نامہ دیوانی - QLC", layout="wide")

# نستعلیق فونٹ اور پیج ڈیزائن کی مکمل CSS
st.markdown("""
    <style>
    @font-face {
        font-family: 'Jameel Noori Nastaleeq';
        src: url('https://fonts.cdnfonts.com/s/73173/JameelNooriNastaleeq.woff') format('woff');
    }
    @media print {
        @page { size: 8.5in 13in; margin: 0.5in; }
        .no-print { display: none !important; }
        header, footer, .stDeployButton { display: none !important; }
        .v-container { border: 2px solid #000 !important; width: 100% !important; box-shadow: none !important; }
    }
    body { direction: rtl; font-family: 'Jameel Noori Nastaleeq', serif; }
    .v-container {
        border: 2px solid #000;
        padding: 40px;
        margin: auto;
        width: 100%;
        max-width: 850px;
        background-color: white;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        color: black;
    }
    .header-table { width: 100%; border-collapse: collapse; margin-bottom: 10px; }
    .header-table td { font-size: 22px; padding: 5px; vertical-align: middle; color: black; }
    .legal-text { text-align: justify; font-size: 20px; line-height: 2.2; margin: 15px 0; color: black; }
    .abd-row { display: flex; justify-content: space-between; font-size: 18px; font-weight: bold; margin: 10px 0; color: black; }
    .footer-info { margin-top: 50px; border-top: 1px solid #000; padding-top: 10px; text-align: center; font-size: 14px; font-family: Arial; color: black; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ وکالت نامہ دیوانی جنریٹر")

# ڈیٹا انٹری فارم
with st.form("input_form"):
    st.write("### مقدمہ کی تفصیلات درج کریں")
    col1, col2 = st.columns(2)
    with col1:
        court_name = st.text_input("بعدالت جناب", "سینئر سول جج صاحب ملتان")
        p_name = st.text_input("مدعی / سائل کا نام", "محمد عقیل")
        adv_name = st.text_input("وکیل / وکلاء صاحبان", "محمد حسن قریشی ایڈووکیٹ ہائی کورٹ")
    with col2:
        d_name = st.text_input("مدعا علیہ / مسئول علیہ کا نام", "محمد سلیم")
        case_subject = st.text_input("دعویٰ یا جرم", "تکمیل معاہدہ مختص بیع")
        current_date = st.date_input("مورخہ", datetime.date.today())
    
    submit_btn = st.form_submit_button("وکالت نامہ تیار کریں")

if submit_btn:
    # آپ کے فراہم کردہ ڈیزائن کے مطابق آؤٹ پٹ
    st.markdown(f"""
    <div class="v-container" style="direction: rtl;">
        <h2 style="text-align: center; text-decoration: underline; margin-bottom: 20px; color: black;">وکالت نامہ دیوانی</h2>
        
        <table class="header-table">
            <tr>
                <td colspan="3"><b>بعدالت جناب:</b> {court_name}</td>
            </tr>
            <tr>
                <td style="width: 45%;"><b>{p_name}</b> (مدعی)</td>
                <td style="text-align: center; width: 10%;"><b>بــــنـــام</b></td>
                <td style="width: 45%; text-align: left;"><b>{d_name}</b> (مدعا علیہم)</td>
            </tr>
            <tr>
                <td style="border-top: 1px solid #000;"><b>منجانب:</b> {p_name}</td>
                <td style="border-top: 1px solid #000;"></td>
                <td style="border-top: 1px solid #000; text-align: left;"><b>دعویٰ یا جرم:</b> {case_subject}</td>
            </tr>
        </table>

        <div style="font-size: 22px; font-weight: bold; margin-top: 20px; color: black;">باعث تحریر آنکہ</div>

        <div class="abd-row">
            <span>العبــــــــــــــــد</span>
            <span>العبــــــــــــــــد</span>
            <span>العبــــــــــــــــد</span>
        </div>

        <div class="legal-text">
            مقدمہ مندرجہ بالا عنوان میں اپنی طرف سے واسطے پیروی و جوابدہی برائے پیشی یا / تصفیہ مقدمہ بمقام <b>ضلع کچہری ملتان</b> کے لئے <b>{adv_name}</b> کو حسب ذیل شرائط پر وکیل مقرر کیا ہے کہ میں ہر پیشی پر خود یا بذریعہ مختار خاص روبرو عدالت حاضر ہوتا رہوں گا اور بروقت پکارے جانے مقدمہ وکیل صاحب موصوف کو اطلاع دے کر حاضر عدالت کروں گا۔ اگر پیشی پر مظہر حاضر نہ ہوا اور مقدمہ میری غیر حاضری کی وجہ سے کسی طور پر میرے خلاف ہو گیا تو صاحب موصوف اس کے کسی طور پر ذمہ دار نہ ہوں گے نیز وکیل صاحب موصوف صدر مقام کچہری کے علاوہ کسی جگہ یا کچہری کے اوقات سے پہلے یا بعد یا بروز تعطیل پیروی کرنے کے ذمہ دار نہ ہوں گے اور مقدمہ کچہری کے علاوہ کسی اور جگہ سماعت ہونے پر یا بروز تعطیل یا کچہری کے اوقات کے آگے پیچھے پیش ہونے پر مظہر کو کوئی نقصان پہنچے تو اس کے ذمہ دار یا اس کے واسطے کسی معاوضہ کے ادا کرنے یا مختانہ کے واپس کرنے کے بھی صاحب موصوف ذمہ دار ہوں گے۔ مجھ کو کل ساختہ برداختہ صاحب موصوف مثل کردہ ذات منظور و مقبول ہو گا اور صاحب موصوف کو عرضی دعویٰ یا جواب دعویٰ درخواست اجرائے ڈگری و نظر ثانی اپیل نگرانی و ہر قسم درخواست پر دستخط و تصدیق کرنے کا بھی اختیار ہو گا اور کسی حکم یا ڈگری کرانے اور ہر قسم کا روپیہ وصول کرنے اور رسید دینے اور داخل کرنے اور ہر قسم کے بیان دینے اور اس پر ثالثی و راضی نامہ و فیصلہ بر حلف کرنے اقبال دعویٰ دینے کا بھی اختیار ہو گا اور بصورت جانے بیر و نجات از کچہری صدر اپیل و برآمدگی مقدمہ یا منسوخی ڈگری یکطرفہ درخواست حکمِ امتناعی یا قرق یا گرفتاری قبل از گرفتاری و اجرائے ڈگری بھی صاحب موصوف کو بشرط ادائیگی علیحدہ مختانہ پیروی کا اختیار ہو گا اور بصورت ضرورت صاحب موصوف کو یہ بھی اختیار ہو گا کہ مقدمہ کو یا اسے کے کسی جزو کی کارروائی کے یا بصورت اپیل کسی دوسرے وکیل یا بیرسٹر کو اپنے بجائے یا اپنے ہمراہ مقرر کریں اور ایسے مشیر قانون کو بھی ہر امر میں وہی اور ویسے ہی اختیارات حاصل ہوں گے جیسے صاحب موصوف کو حاصل ہیں اور دورانِ مقدمہ میں جو کچھ ہرجانہ التواء پڑیگا وہ صاحب موصوف کا حق ہو گا۔ اگر وکیل صاحب موصوف کو پوری فیس تاریخ پیشی سے پہلے ادا نہ کروں گا تو صاحب موصوف کو پورا پورا اختیار ہوگا کہ وہ مقدمہ کی پیروی نہ کریں اور ایسی صورت میں میرا کوئی مطالبہ کسی قسم کا صاحب موصوف کے برخلاف نہیں ہو گا۔ لہذا وکالت نامہ لکھ دیا ہے تاکہ سند رہے اور بوقت ضرورت کام آوے۔
        </div>

        <div class="abd-row">
            <span>العبــــــــــــــــد</span>
            <span>العبــــــــــــــــد</span>
            <span>العبــــــــــــــــد</span>
        </div>

        <p style="font-size: 20px; margin-top: 20px; color: black;"><b>مورخہ:</b> {current_date.strftime('%d-%m-%Y')}</p>
        <p style="font-size: 20px; text-align: center; font-weight: bold; margin: 20px 0; color: black;">مضمون وکالت نامہ سُن لیا ہے اور اچھی طرح سمجھ لیا ہے اور منظور ہے۔</p>

        <div class="abd-row" style="margin-top: 40px;">
            <span>العبــــــــــــــــد: ________________</span>
            <span>العبــــــــــــــــد: ________________</span>
            <span>العبــــــــــــــــد: ________________</span>
        </div>

        <div class="footer-info">
            <b>QLC Qureshi Law Chamber</b> | 02-Old Block, Near Judges Gate, Multan | {current_date.year}
        </div>
    </div>
    <script>setTimeout(function() {{ window.print(); }}, 500);</script>
    """, unsafe_allow_html=True)
