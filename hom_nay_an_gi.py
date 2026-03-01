import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Hôm Nay Ăn Gì?",
    page_icon="🍜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful design
st.markdown("""
<style>
    /* Import beautiful fonts */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@400;500;700&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global styles */
    .main {
        background: linear-gradient(135deg, #fdfbfb 0%, #fff8f0 100%);
    }
    
    /* Navigation Bar Title */
    .navbar-title {
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 1rem 0 2rem 0;
    }
    
    /* Hero Section */
    .hero {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, #fff5f0 0%, #ffe8d8 100%);
        border-radius: 30px;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(255, 107, 107, 0.1);
    }
    
    .hero-title {
        text-align: center;
        font-family: 'Montserrat';
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }

    .hero-title2 {
        font-family: 'Montserrat';
        font-size: 2.5rem;
        font-weight: 750;
        text-align: center;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }

    .hero-title3 {
        font-family: 'Montserrat';
        font-size: 1.8rem;
        font-weight: 730;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-family: 'Montserrat';
        font-size: 4rem;
        color: #666;
        margin-bottom: 1.5rem;
        font-weight: 600;
        animation: fadeInDown 1s ease;
    }

    .hero-subtitle2 {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        color: #666;
        margin-bottom: 1.5rem;
        font-weight: 700;
        animation: fadeInDown 1s ease;
    }
    
    .hero-description {
        font-family: 'Montserrat';
        font-size: 1.1rem;
        color: #777;
        max-width: 1000px;
        margin: 0 auto 2rem !important;
        line-height: 1.8;
        animation: fadeInDown 1s ease;
    }
    
    /* Buttons */
    .cta-button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-family: 'DM Sans', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 6px 25px rgba(255, 107, 107, 0.3);
        display: inline-block;
        margin: 0.5rem;
        text-decoration: none;
    }
    
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 35px rgba(255, 107, 107, 0.4);
    }
    
    .cta-button-secondary {
        background: white;
        color: #ff6b6b;
        border: 2px solid #ff6b6b;
    }
    
    /* Feature Cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .feature-card {
        background: white;
        padding: 12px 14px;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 2px solid transparent;
        margin-bottom: 24px;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15);
        border-color: #ff6b6b;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 6px;
        text-align: center;
    }
    
    .feature-title {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        font-weight: 650;
        color: #333;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .feature-description {
        font-family: 'Montserrat';
        color: #666;
        line-height: 1.6;
        text-align: center;
    }
    
    /* Restaurant Cards */
    .restaurant-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 2px solid transparent;
    }
    
    .restaurant-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.15);
        border-color: #ff6b6b;
    }
    
    .restaurant-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .restaurant-address {
        font-family: 'DM Sans', sans-serif;
        color: #666;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    .restaurant-info {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }
    
    .info-badge {
        background: linear-gradient(135deg, #fff5f0 0%, #ffe8d8 100%);
        color: #ff6b6b;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-family: 'DM Sans', sans-serif;
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    /* Section Titles */
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 900;
        color: #333;
        margin: 3rem 0 2rem 0;
        text-align: center;
    }
    
    /* Filter Section */
    .filter-section {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        margin-bottom: 2rem;
    }
    
    /* Stats Cards */
    .stats-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 6px 25px rgba(255, 107, 107, 0.3);
    }
    
    .stats-number {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
    }
    
    .stats-label {
        font-family: 'DM Sans', sans-serif;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Team Cards */
    .team-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .team-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15);
    }
    
    .team-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .team-role {
        font-family: 'DM Sans', sans-serif;
        color: #ff6b6b;
        font-weight: 500;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Form Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #ffe8d8;
        font-family: 'DM Sans', sans-serif;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #ff6b6b;
        box-shadow: 0 0 0 3px rgba(255, 107, 107, 0.1);
    }
    
    /* Streamlit Button Override */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-family: 'DM Sans', sans-serif;
        font-weight: 700;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Dữ liệu về quán ăn
restaurants_data = [
    {
        "name": "Quán Đức Quân",
        "address": "Số 2 Ngõ 84 Chùa Láng",
        "distance": "<500m",
        "price": "30-40k",
        "type": ["Bún/Phở/Miến/Bánh canh/Súp"],
        "time": ["Sáng", "Trưa", "Tối"],
        "hours": "5:00 - 0:00",
        "menu": [
            {"dish": "Bún chả nướng chấm-chan", "price": "35k"},
            {"dish": "Bún, miến, bánh đa trộn", "price": "35k"},
            {"dish": "Bún, miến, bánh đa riêu cua, cá, bò, mọc, chả lá lốt, thập cẩm", "price": "35k"}
        ],
        "reviews": [
            {"name": "Minh Anh", "rating": 5, "content": "Rất ngon!"},
            {"name": "Hoàng Long", "rating": 4, "content": "Phục vụ tốt."},
            {"name": "Thu Hà", "rating": 5, "content": "Sẽ quay lại!"}
        ]
    },
    {
        "name": "Phở Bò Hà Nội",
        "address": "45 Nguyễn Chí Thanh, Đống Đa",
        "distance": "500m-1km",
        "price": "30-40k",
        "type": ["Phở"],
        "time": ["Sáng", "Trưa"],
        "rating": 4.7,
        "hours": "6:00 - 14:00",
        "menu": [
            {"dish": "Phở tái", "price": "35k"},
            {"dish": "Phở bò viên", "price": "35k"},
            {"dish": "Phở đặc biệt", "price": "40k"}
        ],
        "reviews": [
            "Nước dùng ngọt thanh, thịt bò tươi",
            "Phở ngon nhất khu vực",
            "Đi sớm để có chỗ ngồi"
        ]
    },
    {
        "name": "Bún Chả Hà Nội",
        "address": "67 Láng Hạ, Đống Đa",
        "distance": "<500m",
        "price": "25-40k",
        "type": ["Bún"],
        "time": ["Trưa", "Tối"],
        "rating": 4.3,
        "hours": "10:00 - 21:00",
        "menu": [
            {"dish": "Bún chả", "price": "35k"},
            {"dish": "Bún chả giò", "price": "40k"},
            {"dish": "Nem rán", "price": "25k"}
        ],
        "reviews": [
            "Chả nướng thơm, nước mắm vừa miệng",
            "Giá hợp lý, bún tươi",
            "Đông khách vào giờ cao điểm"
        ]
    },
    {
        "name": "Trà Sữa Gong Cha",
        "address": "89 Chùa Láng, Đống Đa",
        "distance": "<500m",
        "price": "30-50k",
        "type": ["Trà sữa"],
        "time": ["Sáng", "Trưa", "Tối", "Khuya"],
        "rating": 4.6,
        "hours": "8:00 - 23:00",
        "menu": [
            {"dish": "Trà sữa trân châu", "price": "35k"},
            {"dish": "Trà sữa phô mai", "price": "40k"},
            {"dish": "Trà đào", "price": "35k"}
        ],
        "reviews": [
            "Trà ngon, topping nhiều",
            "Không gian thoáng, WiFi nhanh",
            "Giá hơi cao nhưng chất lượng tốt"
        ]
    },
    {
        "name": "Mì Cay Seoul",
        "address": "12 Nguyễn Phúc Lai, Đống Đa",
        "distance": "500m-1km",
        "price": "30-50k",
        "type": ["Mì", "Đồ ăn vặt"],
        "time": ["Trưa", "Tối", "Khuya"],
        "rating": 4.4,
        "hours": "11:00 - 23:30",
        "menu": [
            {"dish": "Mì cay 3 cấp độ", "price": "35k"},
            {"dish": "Tokbokki", "price": "30k"},
            {"dish": "Gà rán phô mai", "price": "45k"}
        ],
        "reviews": [
            "Mì cay vừa miệng, có nhiều level",
            "Đồ ăn Hàn Quốc authentic",
            "Không gian nhỏ nhưng đồ ăn ổn"
        ]
    },
    {
        "name": "Bánh Mì Que",
        "address": "34 Chùa Láng, Đống Đa",
        "distance": "<500m",
        "price": "<30k",
        "type": ["Đồ ăn vặt"],
        "time": ["Trưa", "Tối", "Khuya"],
        "rating": 4.2,
        "hours": "14:00 - 1:00",
        "menu": [
            {"dish": "Bánh mì que xúc xích", "price": "15k"},
            {"dish": "Bánh mì que bò", "price": "18k"},
            {"dish": "Combo 3 que", "price": "40k"}
        ],
        "reviews": [
            "Rẻ, ngon, hợp túi tiền sinh viên",
            "Ăn vặt tối tuyệt vời",
            "Đông khách vào tối muộn"
        ]
    },
    {
        "name": "Lẩu Thái Tomyum",
        "address": "56 Nguyễn Chí Thanh, Đống Đa",
        "distance": "500m-1km",
        "price": ">50k",
        "type": ["Lẩu"],
        "time": ["Trưa", "Tối"],
        "rating": 4.8,
        "hours": "11:00 - 22:00",
        "menu": [
            {"dish": "Lẩu Thái hải sản", "price": "120k/người"},
            {"dish": "Lẩu Thái bò", "price": "100k/người"},
            {"dish": "Lẩu Thái gà", "price": "90k/người"}
        ],
        "reviews": [
            "Nước lẩu chuẩn vị, hải sản tươi",
            "Giá cao nhưng xứng đáng",
            "Thích hợp đi nhóm"
        ]
    },
    {
        "name": "Xôi Yến Thịt Kho",
        "address": "78 Láng Hạ, Đống Đa",
        "distance": "<500m",
        "price": "<30k",
        "type": ["Xôi"],
        "time": ["Sáng"],
        "rating": 4.5,
        "hours": "6:00 - 10:00",
        "menu": [
            {"dish": "Xôi thịt kho", "price": "20k"},
            {"dish": "Xôi xíu mại", "price": "20k"},
            {"dish": "Xôi gà", "price": "25k"}
        ],
        "reviews": [
            "Xôi dẻo, thịt kho đậm đà",
            "Ăn sáng nhanh gọn",
            "Giá rẻ, no lâu"
        ]
    },
    {
        "name": "Bún cá bà Tuyết",
        "address": "Ngõ 84 Chùa Láng",
        "distance": "<500m",
        "price": "40-50k",
        "type": ["Xôi"],
        "time": ["Sáng"],
        "rating": 4.5,
        "hours": "6:00 - 10:00",
        "menu": [
            {"dish": "Xôi thịt kho", "price": "20k"},
            {"dish": "Xôi xíu mại", "price": "20k"},
            {"dish": "Xôi gà", "price": "25k"}
        ],
        "reviews": [
            "Xôi dẻo, thịt kho đậm đà",
            "Ăn sáng nhanh gọn",
            "Giá rẻ, no lâu"
        ]
    },
    {
        "name": "Cơm Thố Anh Nguyễn",
        "address": "Số 17 Chùa Láng",
        "phone": "0972489933",
        "distance": "220m",
        "price": ["40-50k", ">50k"],
        "type": ["Cơm"],
        "time": ["Trưa", "Tối"],
        "hours": "9:45 - 21:45",
        "menu": [
          {"dish": "Cơm Thố Dương Châu", "price": "35k" },
          {"dish": "Cơm Thố Ốp La", "price": "35k" },
          {"dish": "Cơm Thố Gà", "price": "45k" },
          {"dish": "Cơm Thố Gà Quay", "price": "45k" },
          {"dish": "Cơm Thố Gà Nướng", "price": "45k", "tag": "Best seller top2" },
          {"dish": "Cơm Thố Bò", "price": "50k", "tag": "Best seller top3" },
          {"dish": "Cơm Thố Sườn Sụn", "price": "50k" },
          {"dish": "Cơm Thố Xá Xíu", "price": "50k", "tag": "Best seller top1" },
          {"dish": "Cơm Thố Gà + Xá Xíu", "price": "55k" },
          {"dish": "Cơm Thố Bò + Xá Xíu", "price": "60k" },
          {"dish": "Cơm Thố Bò + Gà", "price": "60k" },
          {"dish": "Cơm Thố Đặc Biệt (Bò + Gà + Xá Xíu + Trứng)", "price": "70k"}
        ],
        "reviews": [
            {"name": "Nguyễn Khánh Linh", "rating": 5, "content": "Ăn ổn, giá cả phù hợp, mới nhìn tưởng khẩu phần ít nhưng đến lúc ăn xong no ná thở, phải cố để không bỏ dở"},
            {"name": "Ngọc Tùng", "rating": 5, "content": "Đồ ăn ngon nha mọi người, mình đặt ship về đồ ăn vẫn nóng hổi"},
            {"name": "Nguyễn Đức Tài", "rating": 1, "content": "Khách đến chờ 15 phút đi ra mua đồ ăn bánh mì, nước uống quay lại vẫn chưa xong"}
        ]
    },
    {
        "name": "KOMTO",
        "address": "127 Ngõ 121/2 Chùa Láng",
        "phone": "0901020089",
        "distance": "150m",
        "price": "40-50k",
        "type": ["Cơm/Xôi/Cháo", "Gà/Thịt chiên"],
        "time": ["Trưa", "Tối"],
        "hours": "Mở đến 22:00",
        "menu": [
          { "dish": "Gà giòn sốt Thái (M)", "price": "40k" },
          { "dish": "Gà giòn sốt Thái (L)", "price": "50k" },
          { "dish": "Cơm đùi gà quế Lâm", "price": "50k" },
          { "dish": "Gà giòn sốt me (M)", "price": "40k" },
          { "dish": "Gà giòn sốt me (L)", "price": "50k" },
          { "dish": "Cơm đùi gà sốt me", "price": "50k" },
          { "dish": "Cơm gà giòn sốt mật ong (M)", "price": "40k" },
          { "dish": "Cơm gà giòn sốt mật ong (L)", "price": "50k" },
          { "dish": "Cơm heo Tứ Xuyên", "price": "50k" },
          { "dish": "Cơm gà sốt đặc biệt", "price": "40k" },
          { "dish": "Cơm gà nướng đặc biệt", "price": "45k" }
        ],
        "reviews": [
          {
            "name": "Thục Nghi",
            "rating": 4,
            "content": "Mình đi tầm 12h trưa quán siêu đông khách nên phục vụ hơi lâu nhưng đổi lại cơm ăn ngon, so với giá tầm 40-55k thì khẩu phần rất ổn. Canh ăn kèm free hơi nhạt, sốt Thái ổn, sốt me hợp chấm gà hơn."
          },
          {
            "name": "Công nhân pháp lý",
            "rating": 4,
            "content": "Tôi thề với ae, gọi phần gà không sốt thì giòn thật sự luôn. Phần cơm đặc biệt sốt làm gà không còn giòn nữa. KFC, Jollibee no door."
          }
        ]
     },
     {
        "name": "Kofuku - Tiệm cơm mì",
        "address": "2 Ngõ 106 Phố Chùa Láng",
        "distance": "220m",
        "price": "35k-55k",
        "type": ["Cơm/Xôi/Cháo"],
        "time": ["Trưa", "Tối"],
        "hours": "10:00 - 14:00, 15:00 - 21:00",
        "menu": [
              { "dish": "Cơm Katsudon", "price": "55k" },
              { "dish": "Cơm gà Oyakodon", "price": "45k" },
              { "dish": "Cơm cari", "price": "35k" },
              { "dish": "Cơm cari Tonkatsu", "price": "55k" },
              { "dish": "Cơm gà Karaage", "price": "50k" },
              { "dish": "Cơm thịt heo Ontama", "price": "55k" },
              { "dish": "Cơm xá xíu", "price": "55k" },
              { "dish": "Cơm thịt heo Kimchi", "price": "55k" },
              { "dish": "Cơm thịt heo", "price": "50k" },
              { "dish": "Cơm cari tôm chiên", "price": "45k" },
              { "dish": "Cơm cari trứng ngâm tương", "price": "40k" },
              { "dish": "Trứng ngâm tương", "price": "8k/quả" },
              { "dish": "Trứng Ontama", "price": "8k/quả" },
              { "dish": "Kim chi", "price": "10k" },
              { "dish": "Tôm chiên", "price": "10k/3 con" },
              { "dish": "Tonkatsu", "price": "30k/cái" },
              { "dish": "Gà Karaage", "price": "30k/5 cái" }
              { "dish": "Trà tắc", "price": "10k" },
              { "dish": "Trà chanh", "price": "10k" },
              { "dish": "Trà bát bảo", "price": "10k" },
              { "dish": "Trà Olong", "price": "10k" },
              { "dish": "Coca", "price": "15k/lon" }
         ],
         "reviews": [
            {
              "name": "Linh Nhi",
              "rating": 4,
              "content": "Đông khách ở quán rất nhiều, cá nhân mình thấy cơm cà ri đáng thử nhất. Điểm trừ là quán bám mùi quần áo khá nặng, nhưng đồ ăn ngon nên chấp nhận."
            },
            {
              "name": "Nguyet Anh Le",
              "rating": 4,
              "content": "Quán nhỏ, buổi trưa rất đông, mình phải đợi khoảng 10 phút mới có chỗ. Cơm cà ri khá ngon, thịt không bị dai, khẩu phần vừa đủ. Nhân viên tận tình và giá rẻ hơn nhiều chỗ khác."
            },
            {
              "name": "Kim Ngân Trần",
              "rating": 5,
              "content": "Cơm cà ri tonkatsu ngon lắm, thịt chiên xù giòn, cơm dẻo. Giá sinh viên tầm 50–65k/món. Không gian hơi nhỏ."
            }
            ]
    }, 

]

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_restaurant' not in st.session_state:
    st.session_state.selected_restaurant = None
if 'filters' not in st.session_state:
    st.session_state.filters = {
        'distance': 'Tất cả',
        'price': 'Tất cả',
        'type': 'Tất cả',
        'time': 'Tất cả'
    }

st.markdown("""
<style>
/* Style cho button trong navbar */
div[data-testid="column"] button {
    font-family: 'Montserrat', sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: #ffffff;
    background-color: #ff7a00;
    border-radius: 12px;
    padding: 12px 0;
    border: none;
}

/* Hover effect */
div[data-testid="column"] button:hover {
    background-color: #e86c00;
    color: #ffffff;
}

/* Button đang được click */
div[data-testid="column"] button:focus {
    box-shadow: 0 0 0 0.2rem rgba(255, 122, 0, 0.4);
}
</style>
""", unsafe_allow_html=True)

# Navigation function
def navigate_to(page):
    st.session_state.page = page
    # Only keep selected_restaurant if going to detail page
    if page != 'detail':
        st.session_state.selected_restaurant = None
    st.rerun()

# Navigation Bar
def render_navbar():
    # Title
    st.markdown('<div class="navbar-title">🍜 HÔM NAY ĂN GÌ?</div>', unsafe_allow_html=True)
    
    # Navigation buttons
    pages = {
        'home': 'Trang chủ',
        'search': 'Tìm quán',
        'about': 'Về dự án',
        'contribute': 'Đóng góp'
    }
    
    cols = st.columns(len(pages))
    for i, (page_key, page_name) in enumerate(pages.items()):
        with cols[i]:
            if st.button(page_name, key=f"nav_{page_key}", use_container_width=True):
                navigate_to(page_key)

# Page 1: Home
def render_home():
    # Hero Section
    st.markdown("""
    <div class="hero">
        <div class="hero-title2">Giới thiệu nhanh</div>
        <div class="hero-subtitle2">Website hỗ trợ sinh viên lựa chọn quán ăn quanh khu vực Chùa Láng</div>
        <p class="hero-description">
            "Hôm Nay Ăn Gì?" là nền tảng giúp sinh viên, đặc biệt là sinh viên Ngoại Thương, nhanh chóng tìm được quán ăn phù hợp trong bán kính 0–2km quanh Chùa Láng dựa trên giá cả, thời gian, khoảng cách và trải nghiệm thực tế từ sinh viên.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # About Preview
    st.markdown('<div class="hero-title2">Đặc điểm nổi bật</div>', unsafe_allow_html=True)
    
    preview_cols = st.columns(4)
    previews = [
        ("⚡", "Tìm quán ăn nhanh chóng"),
        ("🎓", "Dữ liệu do sinh viên thu thập"),
        ("💰", "Phù hợp ngân sách sinh viên"),
        ("✨", "Giao diện đơn giản, dễ sử dụng")
    ]
    
    for col, (icon, text) in zip(preview_cols, previews):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <p class="feature-description">{text}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown('<div class="hero-title2">Các tính năng chính</div>', unsafe_allow_html=True)
    
    features = [
        {
            "icon": "🔍",
            "title": "Tìm kiếm thông minh",
            "description": "Lọc quán ăn theo nhiều tiêu chí."
        },
        {
            "icon": "📍",
            "title": "Bản đồ vị trí",
            "description": "Xem vị trí quán ăn và khoảng cách từ Chùa Láng."
        },
        {
            "icon": "⭐",
            "title": "Review thực tế",
            "description": "Đánh giá trực tiếp từ sinh viên, không quảng cáo."
        },
        {
            "icon": "⏱",
            "title": "Gợi ý theo thời gian",
            "description": "Gợi ý quán cho bữa sáng, trưa, tối, ăn vặt."
        }
    ]
    
    feature_cols = st.columns(2)
    for idx, feature in enumerate(features):
        with feature_cols[idx % 2]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature['icon']}</div>
                <div class="feature-title">{feature['title']}</div>
                <p class="feature-description">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# Page 2: Search/Explore
def render_search():
    st.markdown('<div class="hero-title3">Bộ lọc</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        distance_filter = st.selectbox(
            "Khoảng cách",
            ["Tất cả", "<500m", "500m-1km", "1-2km"],
            key="distance_filter"
        )
    
    with col2:
        price_filter = st.selectbox(
            "Mức giá",
            ["Tất cả", "<30k", "30-40k", "40-50k", ">50k"],
            key="price_filter"
        )
    
    with col3:
        type_filter = st.selectbox(
            "Loại món",
            ["Tất cả", "Cơm/Xôi/Cháo", "Bún/Phở/Miến/Bánh canh/Súp", "Gà/Thịt chiên", "Đồ Hàn", "Nem nướng", "Bánh mì pate/chảo/muối ớt", "Bánh tráng", "Tacos", "Bánh cuốn"],
            key="type_filter"
        )
    
    with col4:
        time_filter = st.selectbox(
            "Thời gian",
            ["Tất cả", "Sáng", "Trưa", "Tối", "Khuya"],
            key="time_filter"
        )
    
    if st.button("Áp dụng bộ lọc", use_container_width=True):
        st.session_state.filters = {
            'distance': distance_filter,
            'price': price_filter,
            'type': type_filter,
            'time': time_filter
        }
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Filter restaurants
    filtered_restaurants = restaurants_data.copy()
    
    if st.session_state.filters['distance'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if r['distance'] == st.session_state.filters['distance']]
    
    if st.session_state.filters['price'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if r['price'] == st.session_state.filters['price']]
    
    if st.session_state.filters['type'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if st.session_state.filters['type'] in r['type']]
    
    if st.session_state.filters['time'] != 'Tất cả':
        filtered_restaurants = [r for r in filtered_restaurants if st.session_state.filters['time'] in r['time']]
    
    # Display results
    st.markdown(
        f'''
        <div class="hero-title3">
            Kết quả ({len(filtered_restaurants)} quán)
        </div>
        ''',
        unsafe_allow_html=True
    )
        
    if len(filtered_restaurants) == 0:
        st.info("Không tìm thấy quán nào phù hợp với bộ lọc của bạn. Hãy thử thay đổi tiêu chí tìm kiếm!")
    else:
        for restaurant in filtered_restaurants:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"""
                <div class="restaurant-card">
                    <h3 class="restaurant-name">{restaurant['name']}</h3>
                    <p class="restaurant-address">📍 {restaurant['address']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Use unique key for each button and store restaurant data before navigating
                if st.button("Xem chi tiết", key=f"view_{restaurant['name']}", use_container_width=True):
                    st.session_state.selected_restaurant = restaurant
                    st.session_state.page = 'detail'
                    st.rerun()

# Page 3: Restaurant Detail
def render_detail():
    if st.session_state.selected_restaurant is None:
        st.markdown('<h2 class="section-title">Chưa chọn quán</h2>', unsafe_allow_html=True)
        st.info("Vui lòng chọn một quán từ trang Tìm quán để xem chi tiết!")
        st.markdown('<div style="height: 1rem;"></div>', unsafe_allow_html=True)
        if st.button("Đi đến trang Tìm quán", use_container_width=True):
            navigate_to('search')
        return
    
    restaurant = st.session_state.selected_restaurant
    
    # Back button
    if st.button("<-  Quay lại danh sách"):
        navigate_to('search')
    
    st.markdown(f'<h2 class="section-title">{restaurant["name"]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; color: #666; font-size: 1.1rem; margin-top: -1rem;">📍 {restaurant["address"]}</p>', unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Thông tin chi tiết
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Thông tin chi tiết</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Khoảng cách:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['distance']} từ Chùa Láng</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Mức giá:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['price']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Giờ mở cửa:</p>
            <p style="font-family: 'DM Sans', sans-serif; color: #666;">{restaurant['hours']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="margin-bottom: 1rem;">
        <p style="font-family: 'DM Sans', sans-serif; font-weight: 700; color: #333; margin-bottom: 0.3rem;">Loại món:</p>
        <p style="font-family: 'DM Sans', sans-serif; color: #666;">{', '.join(restaurant['type'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Menu tiêu biểu
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Menu tiêu biểu</h3>', unsafe_allow_html=True)
    
    for item in restaurant['menu']:
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.8rem 0; border-bottom: 1px solid #f0f0f0;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.2rem;">🍽️</span>
                <span style="font-family: 'DM Sans', sans-serif; color: #333; font-size: 1rem;">{item['dish']}</span>
            </div>
            <span style="font-family: 'DM Sans', sans-serif; color: #ff6b6b; font-weight: 700; font-size: 1.1rem;">{item['price']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="height: 2rem;"></div>', unsafe_allow_html=True)
    
    # Đánh giá từ sinh viên
    st.markdown('<h3 style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; margin-bottom: 1rem;">Đánh giá từ sinh viên</h3>', unsafe_allow_html=True)

    for review in restaurant["reviews"]:
        stars = "⭐" * review["rating"]

        st.markdown(f"""
        <div style="margin-bottom: 1.5rem;">
            <div style="margin-bottom: 0.5rem;">
                <span style="color:#ffa500; font-size:1.2rem;">
                    {stars}
                </span>
                <span style="font-weight:700; margin-left:0.5rem;">
                    - {review["name"]}
                </span>
            </div>
            <p style="color:#666; font-style:italic;">
                "{review["content"]}"
            </p>
        </div>
        """, unsafe_allow_html=True)

# Page 4: About Project
def render_about():
    st.markdown('<div class="hero-title3">Giới thiệu dự án</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-card">
        <p class="feature-description">
            "Hôm Nay Ăn Gì?" là dự án được nhóm sinh viên Trường Đại học Ngoại thương xây dựng nhằm hỗ trợ sinh viên lựa chọn quán ăn phù hợp 
            quanh khu vực Chùa Láng. Dự án xuất phát từ nhu cầu thực tế của sinh viên. đặc biệt là tân sinh viên khi 
            mới nhập học gặp khó khăn trong việc tìm địa điểm ăn uống phù hợp với ngân sách 
            và thời gian rảnh của mình.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="hero-title3">Mục tiêu</div>', unsafe_allow_html=True)
    
    goals = [
        "Hỗ trợ sinh viên tìm quán trong bán kính 0–2km",
        "Cho phép lọc theo giá, loại món, thời gian",
        "Cung cấp thông tin ngắn gọn, tập trung trải nghiệm thật",
        "Áp dụng kiến thức Python vào sản phẩm thực tế"
    ]
    
    for goal in goals:
        st.markdown(f"""
        <div class="restaurant-card">
            <p class="feature-description">{goal}</p>
        </div>
        """, unsafe_allow_html=True)
    
# Page 5: Contribute
def render_contribute():   
    with st.form("contribute_form"):
        st.markdown('<div class="hero-title3">Thông tin quán ăn</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Tên quán *", placeholder="VD: Cơm Tấm Sài Gòn")
            address = st.text_input("Địa chỉ *", placeholder="VD: 123 Chùa Láng, Đống Đa")
            price = st.selectbox("Giá trung bình *", ["<30k", "30-50k", ">50k"])
        
        with col2:
            food_type = st.multiselect(
                "Loại món *",
                ["Cơm", "Bún", "Phở", "Mì", "Đồ ăn vặt", "Trà sữa", "Xôi", "Lẩu"]
            )
            time_slots = st.multiselect(
                "Thời gian phục vụ *",
                ["Sáng", "Trưa", "Tối", "Khuya"]
            )
            rating = st.slider("Đánh giá của bạn", 1.0, 5.0, 4.0, 0.5)
        
        review = st.text_area(
            "Đánh giá ngắn *",
            placeholder="Chia sẻ trải nghiệm của bạn về quán này...",
            height=150
        )
        
        submit = st.form_submit_button("Gửi đánh giá", use_container_width=True)
        
        if submit:
            if name and address and food_type and time_slots and review:
                st.success("Cảm ơn bạn đã đóng góp! Thông tin của bạn đã được ghi nhận.")
                st.balloons()
            else:
                st.error("Vui lòng điền đầy đủ các thông tin bắt buộc (*)")

# Main App Logic
def main():
    render_navbar()
    
    # Route to appropriate page
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'search':
        render_search()
    elif st.session_state.page == 'detail':
        render_detail()
    elif st.session_state.page == 'about':
        render_about()
    elif st.session_state.page == 'contribute':
        render_contribute()

if __name__ == "__main__":
    main()
