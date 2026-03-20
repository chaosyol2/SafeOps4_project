import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Config & Custom Theme (ใส่ CSS เพื่อคุมโทนน้ำเงิน-เขียว)
st.set_page_config(page_title="Industrial Monitor", layout="wide")

st.markdown("""
    <style>
    /* พื้นหลังหลักโทนน้ำเงินเข้ม */
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }
    /* ปรับแต่งส่วน Metric Card */
    [data-testid="stMetric"] {
        background-color: #1B2635;
        border-left: 5px solid #00FFC8; /* เส้นขอบสีเขียว Cyber */
        padding: 20px;
        border-radius: 10px;
    }
    /* ปรับแต่งสีตัวหนังสือ Metric */
    [data-testid="stMetricValue"] {
        color: #00FFC8;
    }
    /* Tab Menu */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: #0E1117;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        color: #808080;
    }
    .stTabs [aria-selected="true"] {
        color: #00FFC8 !important;
        border-bottom-color: #00FFC8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.title("🛡️ Smart Monitoring System")
st.markdown("<p style='color: #00FFC8;'>Factory Real-time Operation Center</p>", unsafe_allow_html=True)

# 2. Navigation Tabs
tabs = st.tabs(["🏠 Dashboard", "🔍 Machine Detail", "🤖 AI Prediction", "💡 Recommendation", "🔔 Alert", "📊 Report"])

# --- Tab 1: Real-time Dashboard ---
with tabs[0]:
    # KPI Row
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Machines", "12")
    c2.metric("Active Alerts", "02", delta="Critical", delta_color="inverse")
    c3.metric("Efficiency (OEE)", "94.2%", delta="2.1%")
    c4.metric("Energy Usage", "450 kW")

    st.write("") # เว้นวรรค

    # Main Content Area
    col_left, col_right = st.columns([1, 1.5])

    with col_left:
        st.subheader("Machine Status List")
        # ใช้ HTML เพื่อคุมสีสถานะให้เป๊ะตามธีม
        st.markdown("""
            <div style='background: #1B2635; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <b style='color: #FF4B4B;'>🔴 Machine A</b> <br> <small>Vibration: 82% (Critical)</small>
            </div>
            <div style='background: #1B2635; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <b style='color: #FFD700;'>🟡 Machine B</b> <br> <small>Temperature: 55% (Warning)</small>
            </div>
            <div style='background: #1B2635; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                <b style='color: #00FFC8;'>🟢 Machine C</b> <br> <small>Status: Normal (20%)</small>
            </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.subheader("Live Performance (Vibration & Temp)")
        # ปรับสีกราฟให้เข้ากับธีมน้ำเงินเขียว
        df = pd.DataFrame(np.random.randn(50, 2), columns=['Vib', 'Temp'])
        fig = px.line(df, color_discrete_sequence=['#00FFC8', '#1F77B4'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#E0E0E0',
            margin=dict(l=0, r=0, t=30, b=0),
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)

# ส่วน Tabs อื่นๆ ก็สามารถใส่เนื้อหาตามโครงเดิมได้เลย...
