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
        font-family: 'Montserrat';
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
    }

    .hero-title2 {
        font-family: 'Playfair Display';
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: fadeInDown 1s ease;
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
        font-weight: 600;
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
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15);
        border-color: #ff6b6b;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .feature-title {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 0.5rem;
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

# Sample data - Dữ liệu mẫu về quán ăn
restaurants_data = [
    {
        "name": "Cơm Tấm Sườn Bì Chả",
        "address": "123 Chùa Láng, Đống Đa",
        "distance": "<500m",
        "price": "25-35k",
        "type": ["Cơm"],
        "time": ["Sáng", "Trưa", "Tối"],
        "rating": 4.5,
        "hours": "6:00 - 22:00",
        "menu": [
            {"dish": "Cơm tấm sườn", "price": "30k"},
            {"dish": "Cơm tấm bì", "price": "25k"},
            {"dish": "Cơm tấm trứng", "price": "20k"}
        ],
        "reviews": [
            "Giá rẻ, phục vụ nhanh, hợp ăn trưa",
            "Sườn mềm, chả ngon, cơm dẻo",
            "Quán gần trường, đông sinh viên"
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
    }
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
            "Hôm Nay Ăn Gì?" là nền tảng giúp sinh viên, đặc biệt là sinh viên Ngoại Thương, nhanh chóng tìm được quán ăn phù hợp trong bán kính 1–2km quanh Chùa Láng dựa trên giá cả, thời gian, khoảng cách và trải nghiệm thực tế từ sinh viên.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # # CTA Buttons
    # col1, col2, col3 = st.columns([1, 1, 1])
    # with col1:
    #     st.write("")
    # with col2:
    #     if st.button("🔍 Bắt đầu tìm quán", key="cta_search", use_container_width=True):
    #         navigate_to('search')
    #     if st.button("📋 Xem danh sách quán", key="cta_list", use_container_width=True):
    #         navigate_to('search')
    # with col3:
    #     st.write("")
    
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
    
    # col1, col2, col3 = st.columns([1, 1, 1])
    # with col2:
    #     if st.button("📖 Tìm hiểu thêm", key="learn_more", use_container_width=True):
    #         navigate_to('about')
    
    # Features Section
    st.markdown('<h2 class="section-title">Các tính năng chính</h2>', unsafe_allow_html=True)
    
    features = [
        {
            "icon": "🔍",
            "title": "Tìm kiếm thông minh",
            "description": "Lọc quán theo giá, khoảng cách, loại món và thời gian ăn."
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
                <h3 class="feature-title">{feature['title']}</h3>
                <p class="feature-description">{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# Page 2: Search/Explore
def render_search():
    st.markdown('<h2 class="section-title">🔍 Tìm quán ăn</h2>', unsafe_allow_html=True)
    
    # Filters
    st.markdown('<div class="filter-section">', unsafe_allow_html=True)
    st.markdown("### 🎯 Bộ lọc")
    
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
            ["Tất cả", "<30k", "30-50k", ">50k"],
            key="price_filter"
        )
    
    with col3:
        type_filter = st.selectbox(
            "Loại món",
            ["Tất cả", "Cơm", "Bún", "Phở", "Mì", "Đồ ăn vặt", "Trà sữa", "Xôi", "Lẩu"],
            key="type_filter"
        )
    
    with col4:
        time_filter = st.selectbox(
            "Thời gian",
            ["Tất cả", "Sáng", "Trưa", "Tối", "Khuya"],
            key="time_filter"
        )
    
    if st.button("✅ Áp dụng bộ lọc", use_container_width=True):
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
    st.markdown(f"### 📋 Kết quả ({len(filtered_restaurants)} quán)")
    
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
                if st.button("👁️ Xem chi tiết", key=f"view_{restaurant['name']}", use_container_width=True):
                    st.session_state.selected_restaurant = restaurant
                    st.session_state.page = 'detail'
                    st.rerun()

# Page 3: Restaurant Detail
def render_detail():
    if st.session_state.selected_restaurant is None:
        st.markdown('<h2 class="section-title">⚠️ Chưa chọn quán</h2>', unsafe_allow_html=True)
        st.info("Vui lòng chọn một quán từ trang Tìm quán để xem chi tiết!")
        st.markdown('<div style="height: 1rem;"></div>', unsafe_allow_html=True)
        if st.button("🔍 Đi đến trang Tìm quán", use_container_width=True):
            navigate_to('search')
        return
    
    restaurant = st.session_state.selected_restaurant
    
    # Back button
    if st.button("⬅️ Quay lại danh sách"):
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
    
    # Sample reviewer names
    reviewers = ["Nguyễn Văn A", "Trần Thị B", "Lê Văn C"]
    ratings = [5, 4, 5]
    
    for idx, review in enumerate(restaurant['reviews']):
        stars = "⭐" * ratings[idx % len(ratings)]
        st.markdown(f"""
        <div style="margin-bottom: 1.5rem;">
            <div style="margin-bottom: 0.5rem;">
                <span style="font-family: 'DM Sans', sans-serif; color: #ffa500; font-size: 1.2rem;">{stars}</span>
                <span style="font-family: 'DM Sans', sans-serif; color: #333; font-weight: 700; margin-left: 0.5rem;">- {reviewers[idx % len(reviewers)]}</span>
            </div>
            <p style="font-family: 'DM Sans', sans-serif; color: #666; font-style: italic; margin-left: 0;">"{review}"</p>
        </div>
        """, unsafe_allow_html=True)

# Page 4: About Project
def render_about():
    st.markdown('<h2 class="section-title">💡 Về dự án</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">📖 Giới thiệu dự án</h3>
        <p class="feature-description">
            "Hôm Nay Ăn Gì?" được xây dựng nhằm hỗ trợ sinh viên lựa chọn quán ăn phù hợp 
            quanh khu vực Chùa Láng. Dự án xuất phát từ nhu cầu thực tế của sinh viên khi 
            mới nhập học, gặp khó khăn trong việc tìm địa điểm ăn uống phù hợp với ngân sách 
            và thời gian.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Mục tiêu")
    
    goals = [
        "Xây dựng web hỗ trợ sinh viên tìm quán trong bán kính 1–2km",
        "Cho phép lọc theo giá, loại món, thời gian",
        "Cung cấp thông tin ngắn gọn, tập trung trải nghiệm thật",
        "Áp dụng kiến thức Python vào sản phẩm thực tế"
    ]
    
    for goal in goals:
        st.markdown(f"""
        <div class="restaurant-card">
            <p>✅ {goal}</p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3 class="feature-title">👥 Đối tượng</h3>
            <p class="feature-description">
                Sinh viên Ngoại Thương và sinh viên khu vực Chùa Láng.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3 class="feature-title">💻 Công nghệ sử dụng</h3>
            <ul style="font-family: 'DM Sans', sans-serif; color: #666;">
                <li>Python (Streamlit)</li>
                <li>Google Sheet lưu dữ liệu</li>
                <li>Google Maps API</li>
                <li>Pandas cho xử lý dữ liệu</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Page 5: Contribute
def render_contribute():
    st.markdown('<h2 class="section-title">📩 Đóng góp dữ liệu</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <p class="feature-description">
            Bạn biết quán ăn ngon quanh Chùa Láng? Hãy chia sẻ với cộng đồng sinh viên! 
            Thông tin của bạn sẽ giúp ích cho rất nhiều bạn sinh viên khác.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("contribute_form"):
        st.markdown("### 📝 Thông tin quán ăn")
        
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
        
        submit = st.form_submit_button("🚀 Gửi đánh giá", use_container_width=True)
        
        if submit:
            if name and address and food_type and time_slots and review:
                st.success("✅ Cảm ơn bạn đã đóng góp! Thông tin của bạn đã được ghi nhận.")
                st.balloons()
            else:
                st.error("⚠️ Vui lòng điền đầy đủ các thông tin bắt buộc (*)")

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
