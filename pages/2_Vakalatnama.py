import streamlit as st

# CSS فارمیٹنگ برائے نستعلیق اور پرنٹنگ
st.markdown("""
    <style>
    @import url('https://fonts.cdnfonts.com/css/jameel-noori-nastaleeq');
    
    .v-container {
        direction: rtl;
        font-family: 'Jameel Noori Nastaleeq', serif;
        border: 2px solid #000;
        padding: 40px;
        background-color: white;
        color: black;
        width: 100%;
        max-width: 800px;
        margin: auto;
    }
    .header-table { width: 100%; border-collapse: collapse; }
    .header-table td { font-size: 22px; padding: 10px; color: black; }
    .legal-text { text-align: justify; font-size: 20px; line-height: 2.2; margin-top: 20px; color: black; }
    .abd-row { display: flex; justify-content: space-between; font-size: 18px; margin: 20px 0; font-weight: bold; color: black; }
    .footer-info { border-top: 1px solid #000; margin-top: 40px; padding-top: 10px; text-align: center; font-family: Arial; font-size: 12px; color: black; }
    
    @media print {
        .v-container { border: none; padding: 0; }
        header, footer, .stDeployButton { display: none !important; }
    }
    </style>
""", unsafe_allow_html=True)

# وکالت نامہ کا ڈسپلے
st.markdown(f"""
<div class="v-container">
    <h1 style="text-align: center; text-decoration: underline;">وکالت نامہ دیوانی</h1>
    
    <table class="header-table">
        <tr>
            <td colspan="3"><b>بعدالت جناب:</b> سینئر سول جج صاحب ملتان</td>
        </tr>
        <tr>
            <td style="width: 45%;"><b>محمد عقیل</b> (مدعی)</td>
            <td style="text-align: center; width: 10%;"><b>بــــنـــام</b></td>
            <td style="width: 45%; text-align: left;"><b>محمد سلیم</b> (مدعا علیہم)</td>
        </tr>
        <tr>
            <td style="border-top: 1px solid #000;"><b>منجانب:</b> محمد عقیل</td>
            <td style="border-top: 1px solid #000;"></td>
            <td style="border-top: 1px solid #000; text-align: left;"><b>دعویٰ یا جرم:</b> تکمیل معاہدہ مختص بیع</td>
        </tr>
    </table>

    <div style="font-size: 24px; font-weight: bold; margin-top: 25px;">باعث تحریر آنکہ</div>

    <div class="abd-row">
        <span>العبــــــــــــــــد</span>
        <span>العبــــــــــــــــد</span>
        <span>العبــــــــــــــــد</span>
    </div>

    <div class="legal-text">
        مقدمہ مندرجہ بالا عنوان میں اپنی طرف سے واسطے پیروی و جوابدہی برائے پیشی یا / تصفیہ مقدمہ بمقام <b>ضلع کچہری ملتان</b> کے لئے <b>محمد حسن قریشی ایڈووکیٹ ہائی کورٹ</b> کو حسب ذیل شرائط پر وکیل مقرر کیا ہے کہ میں ہر پیشی پر خود یا بذریعہ مختار خاص روبرو عدالت حاضر ہوتا رہوں گا اور بروقت پکارے جانے مقدمہ وکیل صاحب موصوف کو اطلاع دے کر حاضر عدالت کروں گا۔ اگر پیشی پر مظہر حاضر نہ ہوا اور مقدمہ میری غیر حاضری کی وجہ سے کسی طور پر میرے خلاف ہو گیا تو صاحب موصوف اس کے کسی طور پر ذمہ دار نہ ہوں گے نیز وکیل صاحب موصوف صدر مقام کچہری کے علاوہ کسی جگہ یا کچہری کے اوقات سے پہلے یا بعد یا بروز تعطیل پیروی کرنے کے ذمہ دار نہ ہوں گے اور مقدمہ کچہری کے علاوہ کسی اور جگہ سماعت ہونے پر یا بروز تعطیل یا کچہری کے اوقات کے آگے پیچھے پیش ہونے پر مظہر کو کوئی نقصان پہنچے تو اس کے ذمہ دار یا اس کے واسطے کسی معاوضہ کے ادا کرنے یا مختانہ کے واپس کرنے کے بھی صاحب موصوف ذمہ دار ہوں گے۔ مجھ کو کل ساختہ برداختہ صاحب موصوف مثل کردہ ذات منظور و مقبول ہو گا اور صاحب موصوف کو عرضی دعویٰ یا جواب دعویٰ درخواست اجرائے ڈگری و نظر ثانی اپیل نگرانی و ہر قسم درخواست پر دستخط و تصدیق کرنے کا بھی اختیار ہو گا اور کسی حکم یا ڈگری کرانے اور ہر قسم کا روپیہ وصول کرنے اور رسید دینے اور داخل کرنے اور ہر قسم کے بیان دینے اور اس پر ثالثی و راضی نامہ و فیصلہ بر حلف کرنے اقبال دعویٰ دینے کا بھی اختیار ہو گا اور بصورت جانے بیر و نجات از کچہری صدر اپیل و برآمدگی مقدمہ یا منسوخی ڈگری یکطرفہ درخواست حکمِ امتناعی یا قرق یا گرفتاری قبل از گرفتاری و اجرائے ڈگری بھی صاحب موصوف کو بشرط ادائیگی علیحدہ مختانہ پیروی کا اختیار ہو گا اور بصورت ضرورت صاحب موصوف کو یہ بھی اختیار ہو گا کہ مقدمہ کو یا اسے کے کسی جزو کی کارروائی کے یا بصورت اپیل کسی دوسرے وکیل یا بیرسٹر کو اپنے بجائے یا اپنے ہمراہ مقرر کریں اور ایسے مشیر قانون کو بھی ہر امر میں وہی اور ویسے ہی اختیارات حاصل ہوں گے جیسے صاحب موصوف کو حاصل ہیں اور دورانِ مقدمہ میں جو کچھ ہرجانہ التواء پڑیگا وہ صاحب موصوف کا حق ہو گا۔ اگر وکیل صاحب موصوف کو پوری فیس تاریخ پیشی سے پہلے ادا نہ کروں گا تو صاحب موصوف کو پورا پورا اختیار ہوگا کہ وہ مقدمہ کی پیروی نہ کریں اور ایسی صورت میں میرا کوئی مطالبہ کسی قسم کا صاحب موصوف کے برخلاف نہیں ہو گا۔ لہذا وکالت نامہ لکھ دیا ہے تاکہ سند رہے اور بوقت ضرورت کام آوے۔
    </div>

    <div class="abd-row">
        <span>العبــــــــــــــــد</span>
        <span>العبــــــــــــــــد</span>
        <span>العبــــــــــــــــد</span>
    </div>

    <p style="font-size: 20px;"><b>مورخہ:</b> 19-02-2026</p>
    <p style="font-size: 20px; text-align: center; font-weight: bold; margin: 20px 0;">مضمون وکالت نامہ سُن لیا ہے اور اچھی طرح سمجھ لیا ہے اور منظور ہے۔</p>

    <div class="abd-row" style="margin-top: 50px;">
        <span>العبــــــــــــــــد: ________________</span>
        <span>العبــــــــــــــــد: ________________</span>
        <span>العبــــــــــــــــد: ________________</span>
    </div>

    <div class="footer-info">
        <b>QLC Qureshi Law Chamber</b> | 02-Old Block, Near Judges Gate, Multan | 2026
        <br>
        Email: qureshilaw1977@gmail.com | WhatsApp: +92 330 5477770 | Cell: +92 303 0244382
    </div>
</div>
""", unsafe_allow_html=True)
