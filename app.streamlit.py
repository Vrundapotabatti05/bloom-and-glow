import streamlit as st
import uuid
from datetime import datetime

st.set_page_config(
    page_title="Bloom & Glow - Premium Gift Shop",
    page_icon="gifts",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #FFF0F5 0%, #FFE4E1 25%, #FFF0F5 50%, #F8F0FF 75%, #FFF0F5 100%);
        font-family: 'Poppins', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #FFE4E1 0%, #FFF0F5 50%, #F8F0FF 100%);
        padding: 20px 40px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(255, 20, 147, 0.2);
        text-align: center;
        border: 2px solid #FFB6C1;
    }

    .main-header h1 {
        font-family: 'Playfair Display', serif;
        background: linear-gradient(135deg, #FF69B4 0%, #FF1493 50%, #9370DB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        margin: 0;
    }

    .main-header p {
        color: #D63384;
        font-size: 1.1rem;
        margin: 5px 0 0 0;
        font-weight: 500;
    }

    .search-wrapper {
        background: linear-gradient(135deg, #FFE4E1 0%, #FFF0F5 50%, #F8F0FF 100%);
        padding: 25px 30px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 30px rgba(255, 20, 147, 0.15);
        border: 2px solid #FFB6C1;
    }

    .search-inner {
        display: flex;
        align-items: center;
        background: white;
        border-radius: 50px;
        padding: 5px 10px 5px 25px;
        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.2);
    }

    .search-icon {
        font-size: 1.3rem;
        margin-right: 10px;
        color: #FF69B4;
    }

    .search-tags {
        display: flex;
        gap: 8px;
        margin-top: 12px;
        justify-content: center;
        flex-wrap: wrap;
    }

    .search-tag {
        background: white;
        color: #D63384;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.8rem;
        border: 1px solid #FFB6C1;
        font-weight: 500;
    }

    .stTextInput > div > div > input {
        border-radius: 25px !important;
        border: 2px solid #FF69B4 !important;
        padding: 14px 25px !important;
        font-size: 1.05rem !important;
        background: white !important;
        color: #1a1a1a !important;
        transition: all 0.3s ease !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #FF1493 !important;
        box-shadow: 0 0 25px rgba(255, 20, 147, 0.4) !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #888 !important;
    }

    .stTextArea > div > div > textarea::placeholder {
        color: #888 !important;
    }

    .category-btn {
        background: linear-gradient(145deg, #FFFFFF 0%, #FFF5F8 100%);
        border-radius: 20px;
        padding: 20px 15px;
        text-align: center;
        box-shadow: 0 6px 20px rgba(255, 105, 180, 0.12);
        border: 2px solid transparent;
        cursor: pointer;
        transition: all 0.3s ease;
        height: 130px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .category-btn:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(255, 20, 147, 0.25);
        border-color: #FF69B4;
    }

    .category-btn.active {
        background: linear-gradient(135deg, #FF69B4 0%, #FF1493 100%);
        border-color: #FF1493;
        box-shadow: 0 8px 25px rgba(255, 20, 147, 0.4);
    }

    .category-btn.active .cat-name {
        color: white;
    }

    .cat-icon {
        font-size: 2.8rem;
        margin-bottom: 8px;
    }

    .cat-name {
        font-family: 'Playfair Display', serif;
        font-size: 0.95rem;
        font-weight: 600;
        color: #D63384;
    }

    .product-card {
        background: white;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 6px 20px rgba(255, 105, 180, 0.1);
        transition: all 0.3s ease;
        border: 1px solid #FFE4E1;
        height: 100%;
    }

    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(255, 20, 147, 0.2);
    }

    .product-img {
        width: 100%;
        height: 200px;
        background: linear-gradient(135deg, #FFE4E1 0%, #F8F0FF 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4.5rem;
        position: relative;
    }

    .product-badge {
        position: absolute;
        top: 12px;
        right: 12px;
        background: linear-gradient(135deg, #FF69B4 0%, #FF1493 100%);
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
    }

    .product-wishlist {
        position: absolute;
        top: 12px;
        left: 12px;
        background: rgba(255,255,255,0.9);
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .product-body {
        padding: 18px;
    }

    .product-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.05rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 6px;
    }

    .product-desc {
        color: #888;
        font-size: 0.85rem;
        margin-bottom: 10px;
        line-height: 1.4;
    }

    .product-rating {
        display: flex;
        align-items: center;
        gap: 5px;
        margin-bottom: 8px;
        font-size: 0.85rem;
    }

    .stars {
        color: #FFD700;
        letter-spacing: 1px;
    }

    .rating-count {
        color: #999;
        font-size: 0.8rem;
    }

    .product-tags {
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
        margin-bottom: 10px;
    }

    .ptag {
        background: #FFF0F5;
        color: #D63384;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: 500;
    }

    .product-price-row {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 12px;
    }

    .price-now {
        font-size: 1.3rem;
        font-weight: 700;
        color: #D63384;
    }

    .price-was {
        font-size: 0.9rem;
        color: #aaa;
        text-decoration: line-through;
    }

    .price-save {
        background: #E8F5E9;
        color: #2E7D32;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 0.7rem;
        font-weight: 600;
    }

    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 50%, #9370DB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 35px 0 20px 0;
        padding-bottom: 12px;
        border-bottom: 3px solid #FF69B4;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .cart-badge {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 50%, #9370DB 100%);
        color: white;
        padding: 10px 25px;
        border-radius: 25px;
        font-weight: 700;
        font-size: 0.95rem;
        position: fixed;
        top: 20px;
        right: 30px;
        z-index: 1000;
        box-shadow: 0 5px 20px rgba(255, 20, 147, 0.4);
        font-size: 0.9rem;
    }

    .feature-box {
        background: linear-gradient(145deg, #FFFFFF 0%, #FFF0F5 100%);
        padding: 25px 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.15);
        border: 2px solid #FFB6C1;
        transition: all 0.3s ease;
    }

    .feature-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(255, 20, 147, 0.25);
        border-color: #FF69B4;
    }

    .feature-icon { font-size: 2.5rem; margin-bottom: 12px; }

    .feature-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.15rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FF1493 0%, #9370DB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 8px;
    }

    .feature-desc { color: #555; font-size: 0.95rem; line-height: 1.6; }

    .stButton[key="my_orders_btn"] > button {
        background: linear-gradient(135deg, #9370DB 0%, #FF69B4 100%) !important;
        border: 2px solid #FF69B4 !important;
        margin-top: 10px;
    }

    .footer {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 30%, #9370DB 70%, #DDA0DD 100%);
        padding: 45px;
        border-radius: 25px;
        margin-top: 50px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 40px rgba(255, 20, 147, 0.3);
    }

    .footer h3 {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }

    .stButton > button {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 50%, #9370DB 100%);
        color: white;
        border: none;
        padding: 14px 35px;
        border-radius: 25px;
        font-weight: 700;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 20, 147, 0.3);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #FF1493 0%, #9370DB 50%, #FF69B4 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 20, 147, 0.5);
    }

    .offer-banner {
        background: linear-gradient(135deg, #FFD700 0%, #FF1493 50%, #9370DB 100%);
        padding: 18px 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 6px 25px rgba(255, 20, 147, 0.4);
        animation: pulse 2s infinite;
        letter-spacing: 0.5px;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.015); }
    }

    .divider {
        height: 3px;
        background: linear-gradient(90deg, transparent, #FFB6C1, #DDA0DD, #FFB6C1, transparent);
        margin: 30px 0;
        border-radius: 2px;
    }

    .stTextArea > div > div > textarea {
        border-radius: 15px;
        border: 2px solid #FF69B4;
        padding: 14px 20px;
        transition: all 0.3s ease;
        color: #1a1a1a !important;
    }

    .stTextArea > div > div > textarea:focus {
        border-color: #FF1493;
        box-shadow: 0 0 20px rgba(255, 20, 147, 0.3);
    }

    .stSelectbox > div > div {
        border-radius: 15px;
        border: 2px solid #FF69B4;
    }

    .stSelectbox > div > div:focus-within {
        border-color: #FF1493;
        box-shadow: 0 0 20px rgba(255, 20, 147, 0.3);
    }

    .stSelectbox > div > div > div[role="combobox"] {
        color: #1a1a1a !important;
    }

    .stRadio > div {
        gap: 15px;
    }

    .stRadio > div > label {
        background: linear-gradient(145deg, #FFF0F5 0%, #FFE4E1 100%);
        padding: 12px 20px;
        border-radius: 15px;
        border: 2px solid #FFB6C1;
        transition: all 0.3s ease;
    }

    .stRadio > div > label:hover {
        border-color: #FF69B4;
        box-shadow: 0 4px 15px rgba(255, 20, 147, 0.2);
    }

    .stTextInput label, .stTextArea label, .stSelectbox label {
        color: #FF1493 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    .bank-details {
        background: linear-gradient(145deg, #FFF0F5 0%, #FFE4E1 50%, #F8F0FF 100%);
        border-radius: 20px;
        padding: 30px;
        border: 2px solid #FF69B4;
        margin: 20px 0;
        box-shadow: 0 5px 20px rgba(255, 20, 147, 0.15);
    }

    .bank-details h4 {
        font-family: 'Playfair Display', serif;
        background: linear-gradient(135deg, #FF1493 0%, #9370DB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 15px;
        font-size: 1.3rem;
    }

    .bank-details p { margin: 10px 0; font-size: 0.95rem; }
    .bank-details .label { color: #888; font-weight: 500; }
    .bank-details .value { color: #FF1493; font-weight: 700; }

    .upi-id-display {
        background: linear-gradient(145deg, #FFF0F5 0%, #FFE4E1 50%, #F8F0FF 100%);
        border-radius: 20px;
        padding: 30px;
        border: 2px solid #FF69B4;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 5px 20px rgba(255, 20, 147, 0.15);
    }

    .upi-id-display .upi-label { font-size: 0.95rem; color: #888; margin-bottom: 10px; }
    .upi-id-display .upi-id { font-size: 1.6rem; font-weight: 700; background: linear-gradient(135deg, #FF1493 0%, #9370DB 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: 1px; }

    .order-success {
        background: linear-gradient(145deg, #FFF0F5 0%, #FFE4E1 50%, #F8F0FF 100%);
        border-radius: 25px;
        padding: 45px;
        text-align: center;
        box-shadow: 0 12px 50px rgba(255, 20, 147, 0.3);
        border: 3px solid #FF69B4;
    }

    .order-success h2 {
        font-family: 'Playfair Display', serif;
        background: linear-gradient(135deg, #FF1493 0%, #9370DB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.2rem;
        margin-bottom: 20px;
    }

    .order-success .order-id {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 50%, #9370DB 100%);
        color: white;
        padding: 10px 30px;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: 600;
        display: inline-block;
        margin: 15px 0;
    }

    .step-indicator { display: flex; justify-content: center; gap: 20px; margin-bottom: 30px; }
    .step { display: flex; align-items: center; gap: 10px; }
    .step-circle { width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.1rem; }
    .step-circle.active { background: linear-gradient(135deg, #FF1493 0%, #FF69B4 50%, #9370DB 100%); color: white; box-shadow: 0 4px 15px rgba(255, 20, 147, 0.4); }
    .step-circle.inactive { background: #F0F0F0; color: #bbb; }
    .step-label { font-weight: 500; color: #999; }
    .step-label.active { background: linear-gradient(135deg, #FF1493 0%, #9370DB 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 700; }

    .product-detail-card {
        background: white;
        border-radius: 25px;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(255, 20, 147, 0.15);
        border: 1px solid #FFE4E1;
    }

    .detail-img {
        width: 100%;
        height: 350px;
        background: linear-gradient(135deg, #FFE4E1 0%, #F8F0FF 50%, #FFF0F5 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 8rem;
    }

    .detail-body { padding: 35px; }

    .detail-name {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 10px;
    }

    .detail-rating { display: flex; align-items: center; gap: 8px; margin-bottom: 15px; }

    .detail-price-row { display: flex; align-items: center; gap: 15px; margin-bottom: 20px; }

    .detail-now { font-size: 2rem; font-weight: 700; color: #D63384; }
    .detail-was { font-size: 1.1rem; color: #aaa; text-decoration: line-through; }
    .detail-save { background: #E8F5E9; color: #2E7D32; padding: 5px 15px; border-radius: 15px; font-size: 0.85rem; font-weight: 600; }

    .detail-specs { margin: 20px 0; }
    .spec-row { display: flex; gap: 15px; margin-bottom: 12px; flex-wrap: wrap; }
    .spec-item { background: #FFF0F5; padding: 8px 16px; border-radius: 12px; font-size: 0.85rem; color: #D63384; font-weight: 500; }

    .detail-features { margin: 20px 0; }
    .feat-item { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; font-size: 0.9rem; color: #555; }
    .feat-check { color: #FF69B4; font-size: 1.1rem; }
</style>
""", unsafe_allow_html=True)

if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'cart_total' not in st.session_state:
    st.session_state.cart_total = 0
if 'checkout_step' not in st.session_state:
    st.session_state.checkout_step = 0
if 'customer_info' not in st.session_state:
    st.session_state.customer_info = {}
if 'selected_payment' not in st.session_state:
    st.session_state.selected_payment = None
if 'order_id' not in st.session_state:
    st.session_state.order_id = None
if 'active_category' not in st.session_state:
    st.session_state.active_category = None
if 'view_product' not in st.session_state:
    st.session_state.view_product = None
if 'order_history' not in st.session_state:
    st.session_state.order_history = []
if 'show_orders' not in st.session_state:
    st.session_state.show_orders = False

products = {
    "Candles": [
        {"name": "Lavender Dream Candle", "price": 599, "original_price": 899, "discount": 33, "emoji": "🕯️", "desc": "Hand-poured soy candle with real lavender buds for a calming aromatherapy experience.", "rating": 4.8, "reviews": 324, "material": "100% Natural Soy Wax", "weight": "250g", "burn_time": "40 hours", "occasion": "Relaxation, Meditation", "features": ["Hand-poured", "Eco-friendly", "Cotton wick", "Non-toxic", "Reusable jar"]},
        {"name": "Rose Petal Candle Set", "price": 899, "original_price": 1299, "discount": 31, "emoji": "🌹", "desc": "Set of 3 romantic rose-scented candles in elegant glass holders.", "rating": 4.7, "reviews": 256, "material": "Soy & Beeswax Blend", "weight": "3 x 150g", "burn_time": "30 hours each", "occasion": "Anniversary, Date Night", "features": ["Set of 3", "Glass holders included", "Romantic fragrance", "Long lasting", "Gift ready"]},
        {"name": "Vanilla Bliss Candle", "price": 449, "original_price": 699, "discount": 36, "emoji": "✨", "desc": "Creamy vanilla bean scented candle that fills your room with warmth.", "rating": 4.9, "reviews": 512, "material": "Pure Soy Wax", "weight": "200g", "burn_time": "35 hours", "occasion": "Everyday, Gifting", "features": ["Bestseller", "Premium vanilla extract", "Smokeless", "Even burn", "Ceramic jar"]},
        {"name": "Berry Bonanza Candle", "price": 699, "original_price": 999, "discount": 30, "emoji": "🫐", "desc": "Mixed berry fragrance with sparkling glitter finish for a festive vibe.", "rating": 4.6, "reviews": 189, "material": "Soy Wax with Glitter", "weight": "280g", "burn_time": "42 hours", "occasion": "Parties, Celebrations", "features": ["Glitter finish", "Berry blend scent", "Handcrafted", "Lead-free wick", "Luxury packaging"]},
        {"name": "Cherry Blossom Candle", "price": 799, "original_price": 1199, "discount": 33, "emoji": "🌸", "desc": "Delicate Japanese cherry blossom scent in a beautiful pink jar.", "rating": 4.8, "reviews": 298, "material": "Coconut & Soy Blend", "weight": "300g", "burn_time": "45 hours", "occasion": "Self-care, Gifting", "features": ["Japanese inspired", "Premium fragrance", "Pink ceramic jar", "45hr burn", "Vegan friendly"]},
        {"name": "Cotton Candy Candle", "price": 549, "original_price": 799, "discount": 31, "emoji": "🍭", "desc": "Sweet cotton candy fragrance that brings back childhood memories.", "rating": 4.5, "reviews": 203, "material": "Soy Wax", "weight": "220g", "burn_time": "38 hours", "occasion": "Kids room, Fun gifting", "features": ["Sweet scent", "Fun design", "Safe for kids", "Cotton wick", "Glass container"]},
    ],
    "Corset Flowers": [
        {"name": "Pink Satin Corset Bouquet", "price": 1499, "original_price": 2199, "discount": 32, "emoji": "💐", "desc": "Silk flowers elegantly arranged in a luxury satin corset wrap.", "rating": 4.9, "reviews": 445, "material": "Premium Silk Flowers", "size": "Medium (12 inches)", "color": "Baby Pink", "occasion": "Valentine's, Anniversary", "features": ["Lasts forever", "Satin ribbon wrap", "12 silk flowers", "Gift box included", "Customizable"]},
        {"name": "Purple Velvet Corset", "price": 1799, "original_price": 2599, "discount": 31, "emoji": "🌺", "desc": "Luxury velvet corset arrangement with deep purple artificial flowers.", "rating": 4.8, "reviews": 334, "material": "Velvet & Silk", "size": "Large (15 inches)", "color": "Royal Purple", "occasion": "Birthday, Mother's Day", "features": ["Velvet texture", "Premium flowers", "Elegant packaging", "Photo-ready", "Preserved blooms"]},
        {"name": "Baby Pink Dream", "price": 1299, "original_price": 1899, "discount": 32, "emoji": "🎀", "desc": "Delicate pink roses wrapped in a corset-style arrangement with bow.", "rating": 4.7, "reviews": 287, "material": "Silk & Satin", "size": "Small (10 inches)", "color": "Baby Pink", "occasion": "Propose, Valentine's", "features": ["Bow detail", "Silk roses", "Compact size", "Gift tag included", "Eco-friendly"]},
        {"name": "Lavender Fields Corset", "price": 1599, "original_price": 2299, "discount": 30, "emoji": "💜", "desc": "Lavender arrangement with corset detail and dried flower accents.", "rating": 4.6, "reviews": 198, "material": "Dried & Artificial Flowers", "size": "Medium (13 inches)", "color": "Lavender", "occasion": "Wedding, Housewarming", "features": ["Dried flowers", "Long lasting", "Corset design", "Natural scent", "Handmade"]},
        {"name": "Sunset Blush Corset", "price": 1699, "original_price": 2499, "discount": 32, "emoji": "🌺", "desc": "Orange and pink gradient corset bouquet for a warm, vibrant look.", "rating": 4.8, "reviews": 256, "material": "Premium Silk", "size": "Large (14 inches)", "color": "Orange-Pink Gradient", "occasion": "Birthday, Congrats", "features": ["Gradient design", "Vibrant colors", "Premium wrap", "Photo-perfect", "Luxury feel"]},
        {"name": "Royal Purple Corset", "price": 1999, "original_price": 2899, "discount": 31, "emoji": "👑", "desc": "Premium purple flowers in a regal corset arrangement with golden accents.", "rating": 4.9, "reviews": 412, "material": "Silk & Gold Foil", "size": "X-Large (16 inches)", "color": "Royal Purple", "occasion": "VIP Gifting, Weddings", "features": ["Gold accents", "Premium flowers", "Royal design", "Velvet box", "Personalized tag"]},
    ],
    "Bouquets": [
        {"name": "Romantic Red Roses", "price": 999, "original_price": 1499, "discount": 33, "emoji": "🌹", "desc": "12 long-stem red roses with baby's breath, wrapped in luxury paper.", "rating": 4.9, "reviews": 856, "material": "Fresh Red Roses", "size": "Standard Bouquet", "color": "Red", "occasion": "Valentine's, Proposal", "features": ["12 long-stem roses", "Baby's breath included", "Luxury wrapping", "Free card", "Same day delivery"]},
        {"name": "Pastel Paradise Bouquet", "price": 1299, "original_price": 1899, "discount": 32, "emoji": "🌸", "desc": "Mixed pastel flowers including pink, peach, and lilac blooms.", "rating": 4.7, "reviews": 334, "material": "Mixed Fresh Flowers", "size": "Large Bouquet", "color": "Pastel Mix", "occasion": "Birthday, Thank You", "features": ["20+ stems", "Mixed pastels", "Seasonal flowers", "Eco wrapping", "Care guide"]},
        {"name": "Wildflower Bliss", "price": 899, "original_price": 1299, "discount": 31, "emoji": "🌻", "desc": "Rustic wildflower bouquet with a hand-tied burlap wrap.", "rating": 4.6, "reviews": 223, "material": "Fresh Wildflowers", "size": "Medium Bouquet", "color": "Multi-color", "occasion": "Housewarming, Get Well", "features": ["Rustic design", "Burlap wrap", "Wild assortment", "Fragrant", "Natural look"]},
        {"name": "Peony Dream Bouquet", "price": 1599, "original_price": 2299, "discount": 30, "emoji": "🌷", "desc": "Fresh pink peonies in luxury gold-foil wrapping.", "rating": 4.9, "reviews": 567, "material": "Fresh Peonies", "size": "Premium Bouquet", "color": "Blush Pink", "occasion": "Wedding, Anniversary", "features": ["Premium peonies", "Gold foil wrap", "Fragrant blooms", "Gift bag included", "Nationwide delivery"]},
        {"name": "Sunflower Sunshine", "price": 799, "original_price": 1199, "discount": 33, "emoji": "🌻", "desc": "Bright sunflower arrangement to bring joy and warmth.", "rating": 4.8, "reviews": 445, "material": "Fresh Sunflowers", "size": "Standard Bouquet", "color": "Yellow", "occasion": "Birthday, Get Well Soon", "features": ["Cheerful blooms", "Long stems", "Bright yellow", "Eco-friendly wrap", "Photo-ready"]},
        {"name": "Mixed Tulip Bouquet", "price": 1199, "original_price": 1799, "discount": 33, "emoji": "🌷", "desc": "Colorful tulips for any occasion, arranged in a cone wrap.", "rating": 4.7, "reviews": 312, "material": "Fresh Tulips", "size": "Standard Bouquet", "color": "Multi-color", "occasion": "Spring, Any Celebration", "features": ["15 fresh tulips", "Cone wrap design", "Vibrant colors", "Fragile-safe packing", "Same day dispatch"]},
    ],
    "Jewelries": [
        {"name": "Rose Gold Necklace Set", "price": 1999, "original_price": 2999, "discount": 33, "emoji": "💍", "desc": "Elegant rose gold plated necklace with matching drop earrings.", "rating": 4.8, "reviews": 389, "material": "Rose Gold Plated Brass", "type": "Necklace & Earrings Set", "chain_length": "18 inches", "occasion": "Party, Anniversary", "features": ["Tarnish free", "Nickel free", "Adjustable chain", "Gift box included", "Hypoallergenic"]},
        {"name": "Pearl Drop Earrings", "price": 899, "original_price": 1299, "discount": 31, "emoji": "💎", "desc": "Classic freshwater pearl earrings with gold plating.", "rating": 4.9, "reviews": 567, "material": "Freshwater Pearl & Gold", "type": "Drop Earrings", "size": "2 cm drop", "occasion": "Office, Formal Events", "features": ["Genuine pearl", "Gold plated", "Lightweight", "Elegant design", "Satin pouch"]},
        {"name": "Heart Pendant Chain", "price": 1299, "original_price": 1899, "discount": 32, "emoji": "❤️", "desc": "Delicate heart pendant on a rose gold chain, perfect for gifting.", "rating": 4.7, "reviews": 423, "material": "Rose Gold Plated Silver", "type": "Pendant Necklace", "chain_length": "16-18 inches", "occasion": "Valentine's, Birthday", "features": ["Heart design", "Adjustable chain", "Sparkling stone", "Gift ready", "Anti-tarnish"]},
        {"name": "Crystal Bracelet Set", "price": 1599, "original_price": 2299, "discount": 30, "emoji": "✨", "desc": "Set of 3 sparkling crystal bead bracelets in rose gold.", "rating": 4.6, "reviews": 278, "material": "Crystal & Rose Gold", "type": "Bracelet Set (3 pcs)", "size": "Adjustable", "occasion": "Party, Casual Wear", "features": ["Set of 3", "Crystal beads", "Stretchy band", "Stackable", "Gift pouch"]},
        {"name": "Butterfly Ring", "price": 699, "original_price": 999, "discount": 30, "emoji": "🦋", "desc": "Adjustable butterfly ring in rose gold with crystal wings.", "rating": 4.8, "reviews": 445, "material": "Rose Gold & Crystal", "type": "Adjustable Ring", "size": "Free Size", "occasion": "Daily Wear, Gift", "features": ["Butterfly design", "Crystal wings", "Adjustable", "Comfortable fit", "Gift box"]},
        {"name": "Diamond Stud Earrings", "price": 2499, "original_price": 3499, "discount": 29, "emoji": "💍", "desc": "Premium cubic zirconia stud earrings in white gold plating.", "rating": 4.9, "reviews": 678, "material": "CZ & White Gold", "type": "Stud Earrings", "size": "6mm stones", "occasion": "Wedding, Formal", "features": ["Sparkling CZ", "White gold", "Secure clasp", "Premium box", "Lifetime warranty"]},
    ],
    "Beauty Products": [
        {"name": "Rose Quartz Face Roller", "price": 799, "original_price": 1199, "discount": 33, "emoji": "💫", "desc": "Natural rose quartz facial roller for skin massage and relaxation.", "rating": 4.8, "reviews": 456, "material": "100% Natural Rose Quartz", "type": "Face Roller", "size": "Dual-ended", "occasion": "Skincare, Self-care", "features": ["Dual-ended", "Cooling effect", "Reduces puffiness", "Silk pouch included", "Gift worthy"]},
        {"name": "Pink Clay Face Mask", "price": 499, "original_price": 749, "discount": 33, "emoji": "🧖", "desc": "Gentle pink clay face mask set with 5 single-use packets.", "rating": 4.7, "reviews": 334, "material": "Pink Clay & Botanicals", "type": "Face Mask Set", "size": "5 x 15ml packets", "occasion": "Spa Day, Self-care", "features": ["5 packets", "Gentle formula", "Brightening", "Pore minimizing", "All skin types"]},
        {"name": "Floral Lip Gloss Set", "price": 699, "original_price": 999, "discount": 30, "emoji": "💋", "desc": "Set of 4 floral scented lip glosses in pink shades.", "rating": 4.6, "reviews": 267, "material": "Natural Oils & Pigments", "type": "Lip Gloss Set", "size": "4 x 5ml", "occasion": "Daily Wear, Party", "features": ["4 shades", "Floral scented", "Moisturizing", "Non-sticky", "Cruelty free"]},
        {"name": "Lavender Body Butter", "price": 599, "original_price": 899, "discount": 33, "emoji": "🧴", "desc": "Ultra-moisturizing lavender body butter for silky smooth skin.", "rating": 4.9, "reviews": 589, "material": "Shea Butter & Lavender Oil", "type": "Body Butter", "size": "250ml", "occasion": "Daily Skincare", "features": ["Deep moisturizing", "Natural lavender", "24hr hydration", "Paraben free", "Glass jar"]},
        {"name": "Rose Water Toner", "price": 449, "original_price": 649, "discount": 31, "emoji": "🌹", "desc": "Pure rose water facial toner for refreshed, glowing skin.", "rating": 4.7, "reviews": 398, "material": "100% Pure Rose Water", "type": "Face Toner", "size": "200ml", "occasion": "Daily Skincare", "features": ["100% pure", "pH balanced", "Refreshing", "All skin types", "Spray bottle"]},
        {"name": "Himalayan Bath Salts", "price": 399, "original_price": 599, "discount": 33, "emoji": "🛁", "desc": "Pink Himalayan bath salts with rose and jasmine essential oils.", "rating": 4.8, "reviews": 312, "material": "Himalayan Salt & Essential Oils", "type": "Bath Salt", "size": "500g", "occasion": "Bath Time, Relaxation", "features": ["500g jar", "Rose & jasmine", "Detoxifying", "Muscle relaxation", "Mason jar"]},
    ],
    "Soft Toys": [
        {"name": "Giant Pink Teddy Bear", "price": 1999, "original_price": 2999, "discount": 33, "emoji": "🧸", "desc": "3ft tall ultra-soft teddy bear in baby pink with satin bow.", "rating": 4.9, "reviews": 789, "material": "Premium Plush Fabric", "size": "3 feet (90 cm)", "color": "Baby Pink", "occasion": "Birthday, Valentine's", "features": ["3ft tall", "Ultra soft", "Satin bow", "Surface washable", "Gift wrapped"]},
        {"name": "Unicorn Plush Set", "price": 1299, "original_price": 1899, "discount": 32, "emoji": "🦄", "desc": "Set of 3 colorful unicorn plushies in pastel shades.", "rating": 4.8, "reviews": 456, "material": "Soft Plush & Polyester", "size": "3 x 20 cm", "color": "Pastel Rainbow", "occasion": "Kids, Collectors", "features": ["Set of 3", "Pastel colors", "Soft filling", "Machine washable", "Collectible"]},
        {"name": "Bunny with Heart", "price": 799, "original_price": 1199, "discount": 33, "emoji": "🐰", "desc": "Soft bunny holding a red heart pillow, perfect for gifting.", "rating": 4.7, "reviews": 334, "material": "Plush & Velvet", "size": "35 cm", "color": "White & Pink", "occasion": "Valentine's, Love", "features": ["Heart pillow", "Velvet texture", "Super soft", "Safe for all ages", "Gift tag"]},
        {"name": "Panda Couple Set", "price": 1499, "original_price": 2199, "discount": 32, "emoji": "🐼", "desc": "Matching panda plush couple that holds hands when placed together.", "rating": 4.9, "reviews": 567, "material": "Premium Plush", "size": "2 x 30 cm", "color": "Black & White", "occasion": "Couples, Anniversary", "features": ["Magnetic hands", "Couple set", "Super soft", "Premium quality", "Gift box"]},
        {"name": "Dinosaur Plush Collection", "price": 999, "original_price": 1499, "discount": 33, "emoji": "🦕", "desc": "Set of 2 adorable dinosaur plushies in pastel green and pink.", "rating": 4.6, "reviews": 223, "material": "Soft Plush", "size": "2 x 25 cm", "color": "Pastel Green & Pink", "occasion": "Kids, Decor", "features": ["Set of 2", "Cute design", "Soft filling", "Non-toxic", "Kid safe"]},
        {"name": "Rainbow Unicorn", "price": 1199, "original_price": 1799, "discount": 33, "emoji": "🌈", "desc": "Magical rainbow colored unicorn with a golden horn and wings.", "rating": 4.8, "reviews": 389, "material": "Plush & Satin", "size": "40 cm", "color": "Rainbow", "occasion": "Birthday, Fantasy", "features": ["Rainbow body", "Golden horn", "Winged design", "Light up option", "Premium quality"]},
    ],
}

UPI_ID = "bloomglow@upi"
BANK_DETAILS = {
    "bank_name": "HDFC Bank",
    "account_name": "Bloom & Glow Pvt. Ltd.",
    "account_number": "50100234567890",
    "ifsc": "HDFC0001234",
    "branch": "MG Road, Bangalore",
    "account_type": "Current Account"
}

def add_to_cart(product, quantity=1):
    cart_item = {"name": product["name"], "price": product["price"], "emoji": product["emoji"], "quantity": quantity}
    st.session_state.cart.append(cart_item)
    st.session_state.cart_total += product["price"] * quantity

def render_stars(rating):
    full = int(rating)
    half = 1 if rating - full >= 0.5 else 0
    return "★" * full + ("½" if half else "") + "☆" * (5 - full - half)

def display_search_bar():
    st.markdown("""
    <div class="search-wrapper">
        <div style="text-align:center; margin-bottom:15px;">
            <h1 style="font-family:'Playfair Display',serif; background:linear-gradient(135deg, #FF69B4 0%, #FF1493 50%, #9370DB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; font-size:2.8rem; margin:0;">Bloom & Glow</h1>
            <p style="color:#D63384; font-size:1rem; margin:5px 0 0 0; font-weight:500;">Premium Gifts for Every Special Occasion</p>
        </div>
    """, unsafe_allow_html=True)

    col1, search_col, col2 = st.columns([1, 3, 1])
    with search_col:
        search_query = st.text_input(
            "",
            placeholder="🔍  Search for candles, flowers, jewelry, beauty products...",
            label_visibility="collapsed",
            key="search_main"
        )

    if st.session_state.order_history:
        if st.button("My Orders", key="my_orders_btn"):
            st.session_state.show_orders = not st.session_state.show_orders
            st.rerun()

    st.markdown("""
        <div class="search-tags">
            <span class="search-tag">🕯️ Candles</span>
            <span class="search-tag">💐 Corset Flowers</span>
            <span class="search-tag">🌸 Bouquets</span>
            <span class="search-tag">💍 Jewelry</span>
            <span class="search-tag">💄 Beauty</span>
            <span class="search-tag">🧸 Soft Toys</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    return search_query

def display_offer_banner():
    st.markdown("""
    <div class="offer-banner">
        SPECIAL OFFER: Use code BLOOM30 for extra 30% off on your first order! | Free delivery on orders above Rs.999
    </div>
    """, unsafe_allow_html=True)

def display_categories():
    st.markdown('<h2 class="section-header">Shop by Category</h2>', unsafe_allow_html=True)
    categories = list(products.keys())
    icons = ["🕯️", "💐", "🌸", "💍", "💄", "🧸"]
    cols = st.columns(6)

    for idx, (col, category, icon) in enumerate(zip(cols, categories, icons)):
        with col:
            is_active = st.session_state.active_category == category
            if st.button(f"{icon}\n{category}", key=f"cat_{category}", use_container_width=True):
                if st.session_state.active_category == category:
                    st.session_state.active_category = None
                else:
                    st.session_state.active_category = category
                st.rerun()

def display_product_card(product):
    saved = product["original_price"] - product["price"]
    rating_str = render_stars(product.get("rating", 4.5))

    st.markdown(f"""
    <div class="product-card">
        <div class="product-img">
            {product['emoji']}
            <div class="product-badge">{product['discount']}% OFF</div>
            <div class="product-wishlist">♡</div>
        </div>
        <div class="product-body">
            <div class="product-name">{product['name']}</div>
            <div class="product-desc">{product['desc'][:80]}...</div>
            <div class="product-rating">
                <span class="stars">{rating_str}</span>
                <span style="color:#D63384; font-weight:600;">{product.get('rating', 4.5)}</span>
                <span class="rating-count">({product.get('reviews', 100)})</span>
            </div>
            <div class="product-tags">
                <span class="ptag">{product.get('material', 'Premium')[:20]}</span>
                <span class="ptag">{product.get('occasion', 'Gifting')[:20]}</span>
            </div>
            <div class="product-price-row">
                <span class="price-now">Rs.{product['price']}</span>
                <span class="price-was">Rs.{product['original_price']}</span>
                <span class="price-save">Save Rs.{saved}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_product_detail(product):
    saved = product["original_price"] - product["price"]
    rating_str = render_stars(product.get("rating", 4.5))

    st.markdown(f"""
    <div class="product-detail-card">
        <div class="detail-img">{product['emoji']}</div>
        <div class="detail-body">
            <div class="detail-name">{product['name']}</div>
            <div class="detail-rating">
                <span class="stars" style="font-size:1.3rem;">{rating_str}</span>
                <span style="color:#D63384; font-weight:700; font-size:1.1rem;">{product.get('rating', 4.5)}</span>
                <span style="color:#999;">({product.get('reviews', 100)} reviews)</span>
            </div>
            <p style="color:#555; font-size:1rem; line-height:1.7; margin-bottom:15px;">{product['desc']}</p>
            <div class="detail-price-row">
                <span class="detail-now">Rs.{product['price']}</span>
                <span class="detail-was">Rs.{product['original_price']}</span>
                <span class="detail-save">You Save Rs.{saved} ({product['discount']}% OFF)</span>
            </div>
            <div class="detail-specs">
                <h4 style="font-family:'Playfair Display',serif; color:#D63384; margin-bottom:10px;">Product Details</h4>
                <div class="spec-row">
    """ + "".join([f'<span class="spec-item">{k.title()}: {v}</span>' for k, v in product.items() if k not in ["name","price","original_price","discount","emoji","desc","rating","reviews"]]) + f"""
                </div>
            </div>
            <div class="detail-features">
                <h4 style="font-family:'Playfair Display',serif; color:#D63384; margin-bottom:10px;">Highlights</h4>
                {"".join([f'<div class="feat-item"><span class="feat-check">✔</span> {f}</div>' for f in product.get("features", ["Premium Quality", "Gift Ready", "Fast Delivery"])])}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def display_products(category_products, section_title):
    st.markdown(f'<h2 class="section-header">{section_title}</h2>', unsafe_allow_html=True)
    cols_per_row = 3
    for i in range(0, len(category_products), cols_per_row):
        cols = st.columns(cols_per_row)
        for idx, col in enumerate(cols):
            if i + idx < len(category_products):
                product = category_products[i + idx]
                with col:
                    display_product_card(product)
                    btn_col1, btn_col2 = st.columns(2)
                    with btn_col1:
                        if st.button("View Details", key=f"view_{product['name']}", use_container_width=True):
                            st.session_state.view_product = product
                            st.rerun()
                    with btn_col2:
                        if st.button("Add to Cart", key=f"add_{product['name']}", use_container_width=True):
                            add_to_cart(product)
                            st.success(f"Added!")
                            st.rerun()

def display_features():
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Why Choose Us</h2>', unsafe_allow_html=True)
    cols = st.columns(4)
    features = [
        ("🚚", "Free Delivery", "Free shipping on orders above Rs.999"),
        ("🎁", "Gift Wrapping", "Beautiful premium gift wrapping included"),
        ("🔒", "Secure Payment", "100% secure payment options"),
        ("💝", "Special Offers", "Exclusive discounts every week"),
    ]
    for col, (icon, title, desc) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="feature-box">
                <div class="feature-icon">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

def display_order_history():
    st.markdown('<h2 class="section-header">My Orders</h2>', unsafe_allow_html=True)

    if not st.session_state.order_history:
        st.info("You haven't placed any orders yet. Start shopping!")
        return

    for order in st.session_state.order_history:
        status_colors = {
            "Confirmed": "#4CAF50",
            "Processing": "#FF9800",
            "Shipped": "#2196F3",
            "Delivered": "#9C27B0"
        }
        status_color = status_colors.get(order["status"], "#4CAF50")

        st.markdown(f"""
        <div style="background:white; border-radius:20px; padding:25px; margin-bottom:20px; box-shadow:0 5px 20px rgba(255,20,147,0.1); border:2px solid #FFB6C1;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:15px;">
                <div>
                    <span style="font-family:'Playfair Display',serif; font-size:1.2rem; font-weight:700; color:#FF1493;">Order #{order['order_id']}</span>
                    <span style="color:#888; margin-left:15px; font-size:0.9rem;">📅 {order['date']}</span>
                </div>
                <span style="background:{status_color}; color:white; padding:6px 18px; border-radius:20px; font-weight:600; font-size:0.85rem;">✓ {order['status']}</span>
            </div>
        """, unsafe_allow_html=True)

        items_html = ""
        for item in order["items"]:
            items_html += f"""
            <div style="display:flex; align-items:center; gap:12px; padding:10px 0; border-bottom:1px solid #FFE4E1;">
                <span style="font-size:1.8rem;">{item['emoji']}</span>
                <div style="flex:1;">
                    <div style="font-weight:600; color:#333;">{item['name']}</div>
                    <div style="color:#888; font-size:0.85rem;">Qty: {item['quantity']}</div>
                </div>
                <div style="font-weight:700; color:#FF1493;">Rs.{item['price'] * item['quantity']}</div>
            </div>
            """

        st.markdown(f"""
            <div style="background:#FFF0F5; border-radius:12px; padding:15px; margin-bottom:15px;">
                {items_html}
            </div>
            <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:15px;">
                <div style="color:#555; font-size:0.9rem;">
                    <strong>📍 Delivery:</strong> {order['address'].get('address', 'N/A')}, {order['address'].get('state', 'N/A')} - {order['address'].get('pincode', 'N/A')}
                </div>
                <div style="text-align:right;">
                    <span style="color:#888; font-size:0.9rem;">Payment: {order['payment']['method']}</span><br>
                    <span style="font-family:'Playfair Display',serif; font-size:1.4rem; font-weight:700; background:linear-gradient(135deg, #FF1493 0%, #9370DB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">Total: Rs.{order['total']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Continue Shopping", use_container_width=True, type="primary"):
        st.session_state.show_orders = False
        st.rerun()

def display_footer():
    st.markdown("""
    <div class="footer">
        <h3>Bloom & Glow</h3>
        <p>Making every moment special with our curated collection of premium gifts.</p>
        <p style="margin-top: 20px; font-size: 0.9rem;">Contact: support@bloomandglow.com | +91 98765 43210</p>
        <p style="font-size: 0.85rem; margin-top: 10px;">© 2026 Bloom & Glow. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

def display_step_indicator(step):
    steps = [("Cart", 1), ("Details", 2), ("Payment", 3), ("Confirm", 4)]
    cols = st.columns(4)
    for idx, (label, num) in enumerate(steps):
        with cols[idx]:
            cls = "active" if num <= step else "inactive"
            lbl_cls = "active" if num <= step else ""
            st.markdown(f"""
            <div class="step">
                <div class="step-circle {cls}">{num}</div>
                <span class="step-label {lbl_cls}">{label}</span>
            </div>
            """, unsafe_allow_html=True)

def display_cart_section():
    if not st.session_state.cart:
        st.info("Your cart is empty. Start shopping to add items!")
        return

    st.markdown(f'<h2 class="section-header">Your Cart ({len(st.session_state.cart)} items)</h2>', unsafe_allow_html=True)

    for idx, item in enumerate(st.session_state.cart):
        col1, col2, col3, col4 = st.columns([3, 2, 1, 1])
        with col1:
            st.write(f"{item['emoji']} **{item['name']}**")
        with col2:
            st.write(f"Rs.{item['price']} x {item['quantity']}")
        with col3:
            st.write(f"**Rs.{item['price'] * item['quantity']}**")
        with col4:
            if st.button("Remove", key=f"remove_{idx}"):
                st.session_state.cart_total -= item['price'] * item['quantity']
                st.session_state.cart.pop(idx)
                st.rerun()

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    delivery = 0 if st.session_state.cart_total >= 999 else 49
    total = st.session_state.cart_total + delivery

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### Subtotal: Rs.{st.session_state.cart_total}")
        if st.session_state.cart_total >= 999:
            st.success("You qualify for FREE delivery!")
        else:
            st.info(f"Add Rs.{999 - st.session_state.cart_total} more for free delivery")
    with col2:
        st.markdown(f"### Delivery: {'FREE' if delivery == 0 else 'Rs.49'}")

    st.markdown(f"### Total Amount: **Rs.{total}**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Proceed to Checkout", use_container_width=True, type="primary"):
            st.session_state.checkout_step = 2
            st.rerun()
    with col2:
        if st.button("Clear Cart", use_container_width=True):
            st.session_state.cart = []
            st.session_state.cart_total = 0
            st.rerun()

def display_customer_details():
    st.markdown('<h2 class="section-header">Delivery Details</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background:linear-gradient(145deg, #FFF0F5 0%, #FFE4E1 50%, #F8F0FF 100%); border-radius:20px; padding:30px; border:2px solid #FF69B4; margin-bottom:25px; box-shadow:0 5px 20px rgba(255,20,147,0.15);">
        <div style="text-align:center; margin-bottom:20px;">
            <span style="font-size:2.5rem;">📦</span>
            <h3 style="font-family:'Playfair Display',serif; background:linear-gradient(135deg, #FF1493 0%, #9370DB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; margin:10px 0 5px 0; font-size:1.4rem;">Where should we deliver your gifts?</h3>
            <p style="color:#D63384; font-size:0.9rem;">All fields with * are required</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("👤 First Name *", value=st.session_state.customer_info.get("first_name", ""))
        phone = st.text_input("📱 Phone Number *", value=st.session_state.customer_info.get("phone", ""), max_chars=10)
        states = ["Select State", "Andhra Pradesh", "Bihar", "Delhi", "Goa", "Gujarat", "Haryana", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Punjab", "Rajasthan", "Tamil Nadu", "Telangana", "Uttar Pradesh", "West Bengal"]
        state = st.selectbox("📍 State *", states, index=states.index(st.session_state.customer_info.get("state", "Select State")) if "state" in st.session_state.customer_info else 0)
    with col2:
        last_name = st.text_input("👤 Last Name *", value=st.session_state.customer_info.get("last_name", ""))
        email = st.text_input("✉️ Email Address", value=st.session_state.customer_info.get("email", ""))
        pincode = st.text_input("📮 Pincode *", value=st.session_state.customer_info.get("pincode", ""), max_chars=6)

    address = st.text_area("🏠 Full Delivery Address *", value=st.session_state.customer_info.get("address", ""), height=100)
    landmark = st.text_input("🗺️ Landmark (Optional)", value=st.session_state.customer_info.get("landmark", ""))

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Cart", use_container_width=True):
            st.session_state.checkout_step = 1
            st.rerun()
    with col2:
        if st.button("Continue to Payment", use_container_width=True, type="primary"):
            if first_name and last_name and phone and pincode and address and state != "Select State":
                st.session_state.customer_info = {"first_name": first_name, "last_name": last_name, "phone": phone, "email": email, "pincode": pincode, "address": address, "landmark": landmark, "state": state}
                st.session_state.checkout_step = 3
                st.rerun()
            else:
                st.error("Please fill all required fields (*)")

def display_payment_options():
    st.markdown('<h2 class="section-header">Select Payment Method</h2>', unsafe_allow_html=True)
    total = st.session_state.cart_total + (0 if st.session_state.cart_total >= 999 else 49)
    st.markdown(f"**Order Total: Rs.{total}**")
    st.markdown("---")

    payment_method = st.radio("Choose Payment Method", ["UPI Payment", "Bank Transfer", "Cash on Delivery"], label_visibility="collapsed")

    if payment_method == "UPI Payment":
        st.markdown(f"""
        <div style="background:linear-gradient(145deg,#FFF5F8,#F8F0FF); border-radius:20px; padding:30px; border:2px solid #FF69B4; margin-bottom:20px;">
            <div style="text-align:center;">
                <div style="font-size:3rem; margin-bottom:10px;">📱</div>
                <div style="font-family:'Playfair Display',serif; font-size:1.3rem; font-weight:600; color:#D63384;">UPI Payment</div>
                <div style="color:#666; font-size:0.95rem;">Pay instantly using any UPI app</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="upi-id-display">
            <div class="upi-label">Send payment to UPI ID</div>
            <div class="upi-id">{UPI_ID}</div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        for col, (name, icon) in zip([c1, c2, c3, c4], [("Google Pay", "💳"), ("PhonePe", "📱"), ("Paytm", "💰"), ("BHIM", "🏦")]):
            with col:
                st.markdown(f"""
                <div style="text-align:center; padding:15px; background:white; border-radius:15px; box-shadow:0 3px 10px rgba(0,0,0,0.08);">
                    <div style="font-size:2.5rem;">{icon}</div>
                    <div style="font-weight:600; color:#333; font-size:0.85rem;">{name}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("**How to pay:**")
        st.markdown(f"1. Open your UPI app\n2. Send **Rs.{total}** to **{UPI_ID}**\n3. Enter transaction ID below")

        upi_ref = st.text_input("UPI Reference / Transaction ID *", placeholder="e.g., 123456789012")
        if upi_ref:
            st.session_state.selected_payment = {"method": "UPI", "upi_id": UPI_ID, "reference": upi_ref, "amount": total}

    elif payment_method == "Bank Transfer":
        st.markdown(f"""
        <div style="background:linear-gradient(145deg,#FFF5F8,#F8F0FF); border-radius:20px; padding:30px; border:2px solid #FF69B4; margin-bottom:20px;">
            <div style="text-align:center;">
                <div style="font-size:3rem; margin-bottom:10px;">🏦</div>
                <div style="font-family:'Playfair Display',serif; font-size:1.3rem; font-weight:600; color:#D63384;">Bank Transfer / NEFT / IMPS</div>
                <div style="color:#666; font-size:0.95rem;">Transfer directly to our bank account</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="bank-details">
            <h4>Bank Account Details</h4>
            <p><span class="label">Bank Name:</span> <span class="value">{BANK_DETAILS['bank_name']}</span></p>
            <p><span class="label">Account Holder:</span> <span class="value">{BANK_DETAILS['account_name']}</span></p>
            <p><span class="label">Account Number:</span> <span class="value">{BANK_DETAILS['account_number']}</span></p>
            <p><span class="label">IFSC Code:</span> <span class="value">{BANK_DETAILS['ifsc']}</span></p>
            <p><span class="label">Branch:</span> <span class="value">{BANK_DETAILS['branch']}</span></p>
            <p><span class="label">Account Type:</span> <span class="value">{BANK_DETAILS['account_type']}</span></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"**Transfer Amount: Rs.{total}**")
        bank_ref = st.text_input("Transaction Reference Number *", placeholder="e.g., NEFT/IMPS/UPI reference")
        if bank_ref:
            st.session_state.selected_payment = {"method": "Bank Transfer", "bank": BANK_DETAILS['bank_name'], "reference": bank_ref, "amount": total}

    elif payment_method == "Cash on Delivery":
        st.markdown(f"""
        <div style="background:linear-gradient(145deg,#FFF5F8,#F8F0FF); border-radius:20px; padding:30px; border:2px solid #FF69B4; margin-bottom:20px;">
            <div style="text-align:center;">
                <div style="font-size:3rem; margin-bottom:10px;">💵</div>
                <div style="font-family:'Playfair Display',serif; font-size:1.3rem; font-weight:600; color:#D63384;">Cash on Delivery</div>
                <div style="color:#666; font-size:0.95rem;">Pay when your order arrives</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if total > 5000:
            st.warning("COD not available for orders above Rs.5000. Please choose UPI or Bank Transfer.")
        else:
            st.info(f"Please keep **Rs.{total}** ready in cash at delivery.")
            st.session_state.selected_payment = {"method": "COD", "amount": total}

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Details", use_container_width=True):
            st.session_state.checkout_step = 2
            st.rerun()
    with col2:
        if st.button("Place Order", use_container_width=True, type="primary"):
            if st.session_state.selected_payment:
                if st.session_state.selected_payment.get("method") in ["UPI", "Bank Transfer"] and not st.session_state.selected_payment.get("reference"):
                    st.error("Please enter the transaction reference number!")
                else:
                    st.session_state.order_id = f"BG{datetime.now().strftime('%Y%m%d')}{str(uuid.uuid4())[:6].upper()}"
                    total = st.session_state.cart_total + (0 if st.session_state.cart_total >= 999 else 49)
                    order = {
                        "order_id": st.session_state.order_id,
                        "date": datetime.now().strftime("%d %b %Y, %I:%M %p"),
                        "items": list(st.session_state.cart),
                        "total": total,
                        "payment": st.session_state.selected_payment.copy(),
                        "address": st.session_state.customer_info.copy(),
                        "status": "Confirmed"
                    }
                    st.session_state.order_history.insert(0, order)
                    st.session_state.checkout_step = 4
                    st.rerun()
            else:
                st.error("Please select a payment method!")

def display_order_confirmation():
    st.markdown(f"""
    <div class="order-success">
        <h2>Order Placed Successfully!</h2>
        <p>Thank you for shopping with Bloom & Glow!</p>
        <div class="order-id">Order ID: {st.session_state.order_id}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    total = st.session_state.cart_total + (0 if st.session_state.cart_total >= 999 else 49)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Delivery Details")
        info = st.session_state.customer_info
        st.markdown(f"**Name:** {info['first_name']} {info['last_name']}")
        st.markdown(f"**Phone:** {info['phone']}")
        if info.get('email'): st.markdown(f"**Email:** {info['email']}")
        st.markdown(f"**Address:** {info['address']}")
        if info.get('landmark'): st.markdown(f"**Landmark:** {info['landmark']}")
        st.markdown(f"**Pincode:** {info['pincode']} | **State:** {info['state']}")
    with col2:
        st.markdown("### Payment Details")
        payment = st.session_state.selected_payment
        st.markdown(f"**Method:** {payment['method']} | **Amount:** Rs.{payment['amount']}")
        if payment.get('reference'): st.markdown(f"**Reference:** {payment['reference']}")
        st.markdown("### Order Items")
        for item in st.session_state.cart:
            st.markdown(f"{item['emoji']} {item['name']} x {item['quantity']} — Rs.{item['price'] * item['quantity']}")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.info("**What happens next?**")
    st.markdown("1. Order confirmation on phone/email\n2. Processing within 24 hours\n3. Delivery in 3-5 business days\n4. Queries: support@bloomandglow.com | +91 98765 43210")

    if st.button("Continue Shopping", use_container_width=True, type="primary"):
        st.session_state.cart = []
        st.session_state.cart_total = 0
        st.session_state.checkout_step = 0
        st.session_state.customer_info = {}
        st.session_state.selected_payment = None
        st.session_state.order_id = None
        st.rerun()

def main():
    if st.session_state.view_product:
        product = st.session_state.view_product
        if st.button("← Back to Shop"):
            st.session_state.view_product = None
            st.rerun()
        display_product_detail(product)
        st.markdown("")
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            if st.button("Add to Cart", key="add_detail", use_container_width=True, type="primary"):
                add_to_cart(product)
                st.success(f"Added {product['name']} to cart!")
                st.session_state.view_product = None
                st.rerun()
        return

    cart_count = len(st.session_state.cart)
    if cart_count > 0 and st.session_state.checkout_step == 0:
        st.markdown(f'<div class="cart-badge">Cart ({cart_count}) — Rs.{st.session_state.cart_total}</div>', unsafe_allow_html=True)

    if st.session_state.checkout_step > 0:
        st.markdown("""<div class="main-header" style="padding:15px 40px; margin-bottom:20px;"><h1 style="font-size:2rem;">Bloom & Glow — Checkout</h1></div>""", unsafe_allow_html=True)
        display_step_indicator(st.session_state.checkout_step)

    if st.session_state.checkout_step == 0:
        if st.session_state.show_orders:
            display_order_history()
            display_footer()
            return

        search_query = display_search_bar()
        display_offer_banner()
        display_categories()

        if search_query:
            st.markdown(f'<h2 class="section-header">Search Results for "{search_query}"</h2>', unsafe_allow_html=True)
            results = []
            for cat_items in products.values():
                for item in cat_items:
                    if search_query.lower() in item["name"].lower() or search_query.lower() in item["desc"].lower() or search_query.lower() in item.get("material", "").lower() or search_query.lower() in item.get("occasion", "").lower():
                        results.append(item)
            if results:
                display_products(results, f"Found {len(results)} products")
            else:
                st.warning("No products found. Try a different search term.")
        elif st.session_state.active_category:
            display_products(products[st.session_state.active_category], f"{st.session_state.active_category}")
        else:
            for category, items in products.items():
                display_products(items, f"Featured {category}")

        display_features()
        display_footer()

        if st.session_state.cart:
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            display_cart_section()

    elif st.session_state.checkout_step == 1:
        display_cart_section()
    elif st.session_state.checkout_step == 2:
        display_customer_details()
    elif st.session_state.checkout_step == 3:
        display_payment_options()
    elif st.session_state.checkout_step == 4:
        display_order_confirmation()

if __name__ == "__main__":
    main()
