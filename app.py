import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import shutil
import auth

# Set page configurations
st.set_page_config(
    page_title="India Demographics & IT Dashboard",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Authentication State
auth.init_auth_state()

# Enforce Login
if not st.session_state.authenticated:
    # Inject styling on login page too
    if os.path.exists("assets/styles.css"):
        with open("assets/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    auth.render_login_page()
    st.stop()

# Helper function to load custom CSS
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply colorful styling from stylesheet
local_css("assets/styles.css")

# --- Programmatic Asset Handling ---
# Copy the generated banner image from the brain artifacts directory if the terminal copy command failed
assets_dir = "assets"
banner_dest = os.path.join(assets_dir, "dashboard_banner.png")
artifact_banner_src = "C:\\Users\\Prachi\\.gemini\\antigravity\\brain\\9433be04-8ecb-4be8-a5e9-981a7462388c\\dashboard_banner_1782018642264.png"

if not os.path.exists(banner_dest):
    os.makedirs(assets_dir, exist_ok=True)
    if os.path.exists(artifact_banner_src):
        try:
            shutil.copy(artifact_banner_src, banner_dest)
        except Exception as e:
            pass

# --- Data Loading ---
@st.cache_data
def load_data():
    csv_path = "india_demographics.csv"
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    else:
        st.error("Dataset 'india_demographics.csv' not found. Please run 'python generate_data.py' first to build the dataset.")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.stop()

# --- Sidebar Configuration ---
with st.sidebar:
    st.markdown(
        """
        <div style='text-align: center; padding: 10px 0;'>
            <span style='font-size: 3rem;'>🇮🇳</span>
            <h2 style='margin: 0; color: #818cf8;'>India Insights</h2>
            <p style='color: #64748b; font-size: 0.85rem;'>Demographics & IT Hubs</p>
        </div>
        <hr style='border-color: rgba(255,255,255,0.1); margin: 10px 0;'/>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(f"👥 **Logged in as:** `{st.session_state.username}`")
    
    # Reset filters helper
    if st.button("🔄 Reset Filters"):
        st.session_state.search_query = ""
        st.session_state.pop_slider = (float(df["Population (Millions)"].min()), float(df["Population (Millions)"].max()))
        st.session_state.it_slider = (int(df["IT Companies"].min()), int(df["IT Companies"].max()))
        st.rerun()

    st.write("### 🔍 Search & Filters")
    
    # 1. Search Bar
    search_query = st.text_input(
        "Search State/UT or Language", 
        key="search_query_input", 
        value=st.session_state.get("search_query", ""),
        placeholder="e.g. Karnataka, Hindi"
    )
    
    # 2. Type Filter
    selected_types = st.multiselect(
        "Region Type", 
        options=list(df["Type"].unique()), 
        default=list(df["Type"].unique())
    )
    
    # 3. Population Slider
    min_pop, max_pop = float(df["Population (Millions)"].min()), float(df["Population (Millions)"].max())
    pop_range = st.slider(
        "Population Range (Millions)",
        min_value=min_pop,
        max_value=max_pop,
        value=st.session_state.get("pop_slider", (min_pop, max_pop))
    )
    
    # 4. IT Companies Slider
    min_it, max_it = int(df["IT Companies"].min()), int(df["IT Companies"].max())
    it_range = st.slider(
        "IT Companies Count",
        min_value=min_it,
        max_value=max_it,
        value=st.session_state.get("it_slider", (min_it, max_it))
    )
    
    # Save filters in state
    st.session_state.search_query = search_query
    st.session_state.pop_slider = pop_range
    st.session_state.it_slider = it_range
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Logout Button
    if st.button("🚪 Log Out", key="logout_btn", use_container_width=True):
        auth.logout()

# --- Filtering logic ---
filtered_df = df.copy()

# Filter by type
filtered_df = filtered_df[filtered_df["Type"].isin(selected_types)]

# Filter by population range
filtered_df = filtered_df[
    (filtered_df["Population (Millions)"] >= pop_range[0]) & 
    (filtered_df["Population (Millions)"] <= pop_range[1])
]

# Filter by IT companies count
filtered_df = filtered_df[
    (filtered_df["IT Companies"] >= it_range[0]) & 
    (filtered_df["IT Companies"] <= it_range[1])
]

# Filter by search query
if search_query:
    q = search_query.lower()
    filtered_df = filtered_df[
        filtered_df["State/UT"].str.lower().str.contains(q) |
        filtered_df["Primary Language"].str.lower().str.contains(q) |
        filtered_df["Secondary Language"].str.lower().str.contains(q) |
        filtered_df["Major IT Hub"].str.lower().str.contains(q)
    ]

# --- Main Dashboard Header ---
if os.path.exists(banner_dest):
    st.image(banner_dest, use_container_width=True)
else:
    # Fallback styled header with pure colorful gradients if banner doesn't exist
    st.markdown(
        """
        <div style='background: linear-gradient(90deg, #4f46e5, #7c3aed, #ec4899); padding: 2.5rem; border-radius: 16px; margin-bottom: 2rem; text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.25);'>
            <h1 style='margin:0; font-size:3rem; font-weight:800; color:white;'>INDIA DEMOGRAPHICS & IT INDUSTRY EXPLORER</h1>
            <p style='margin:5px 0 0 0; font-size:1.2rem; color:#e2e8f0; font-weight:300;'>Insights into Population, Languages, and Technology Landscape</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Header Section
st.markdown(
    """
    <div style="margin-bottom: 1.5rem;">
        <h2 style="font-weight: 700; margin-bottom: 0px;">📊 India Demographics Dashboard</h2>
        <span style="color: #94a3b8; font-size: 0.95rem;">Interactive visualization of India's states, linguistic patterns, and growing IT footprints.</span>
    </div>
    """,
    unsafe_allow_html=True
)

if filtered_df.empty:
    st.warning("⚠️ No data matches your filter criteria. Try adjusting the search query or slider ranges in the sidebar.")
    st.stop()

# --- Key Metrics Cards ---
total_pop = filtered_df["Population (Millions)"].sum()
total_it = filtered_df["IT Companies"].sum()
avg_lit = filtered_df["Literacy Rate (%)"].mean()
top_lang = filtered_df["Primary Language"].mode().iloc[0] if not filtered_df["Primary Language"].empty else "N/A"

m_col1, m_col2, m_col3, m_col4 = st.columns(4)

with m_col1:
    st.markdown(
        f"""
        <div class="metric-card metric-accent-blue">
            <div class="metric-title">👥 Total Population</div>
            <div class="metric-value">{total_pop:.2f} M</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m_col2:
    st.markdown(
        f"""
        <div class="metric-card metric-accent-purple">
            <div class="metric-title">💻 IT Companies</div>
            <div class="metric-value">{total_it:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m_col3:
    st.markdown(
        f"""
        <div class="metric-card metric-accent-pink">
            <div class="metric-title">📚 Average Literacy</div>
            <div class="metric-value">{avg_lit:.1f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m_col4:
    st.markdown(
        f"""
        <div class="metric-card metric-accent-blue" style="border-left-color: #10b981;">
            <div class="metric-title">🗣️ Dominant Language</div>
            <div class="metric-value">{top_lang}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("<br>", unsafe_allow_html=True)

# --- Navigation Tabs ---
tab_overview, tab_it, tab_eda = st.tabs([
    "🏡 Overview & Demographics", 
    "🚀 IT Hubs & Industry", 
    "📈 Exploratory Data Analysis (EDA)"
])

# --- Tab 1: Overview & Demographics ---
with tab_overview:
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write("### Population Distribution by State/UT")
        # Color palettes matching our theme: sunset/viridis/plasma
        fig_pop = px.bar(
            filtered_df.sort_values(by="Population (Millions)", ascending=True),
            x="Population (Millions)",
            y="State/UT",
            orientation="h",
            color="Population (Millions)",
            color_continuous_scale="deep",
            hover_data=["Literacy Rate (%)", "Primary Language"],
            text_auto=".1f"
        )
        fig_pop.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#f1f5f9",
            height=600,
            xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)")
        )
        st.plotly_chart(fig_pop, use_container_width=True)
        
    with col2:
        st.write("### Major Languages Spoken (Primary)")
        
        # Aggregate primary languages
        lang_counts = filtered_df.groupby("Primary Language")["Population (Millions)"].sum().reset_index()
        
        fig_lang = px.pie(
            lang_counts,
            values="Population (Millions)",
            names="Primary Language",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            hole=0.4
        )
        fig_lang.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#f1f5f9",
            legend=dict(
                orientation="h",
                yanchor="top",
                y=-0.2,
                xanchor="center",
                x=0.5
            ),
            margin=dict(t=20, b=150, l=10, r=10),
            height=600
        )
        fig_lang.update_traces(
            textposition='inside',
            textinfo='percent+label',
            marker=dict(line=dict(color='rgba(30,41,59,0.7)', width=2))
        )
        st.plotly_chart(fig_lang, use_container_width=True)

# --- Tab 2: IT Hubs & Industry ---
with tab_it:
    col_it1, col_it2 = st.columns(2)
    
    with col_it1:
        st.write("### IT Companies Concentration (Share %)")
        it_share = filtered_df.groupby("State/UT")["IT Companies"].sum().reset_index()
        # Keep only states with > 0 companies
        it_share = it_share[it_share["IT Companies"] > 0]
        
        fig_it_pie = px.pie(
            it_share,
            values="IT Companies",
            names="State/UT",
            color_discrete_sequence=px.colors.sequential.Sunset_r,
            hover_name="State/UT"
        )
        fig_it_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            font_color="#f1f5f9",
            height=500,
            showlegend=False
        )
        fig_it_pie.update_traces(
            textposition='inside',
            textinfo='percent+label',
            marker=dict(line=dict(color='rgba(30,41,59,0.7)', width=1.5))
        )
        st.plotly_chart(fig_it_pie, use_container_width=True)
        
    with col_it2:
        st.write("### Average IT Salary vs. Number of IT Companies")
        
        fig_salary = px.scatter(
            filtered_df[filtered_df["IT Companies"] > 0],
            x="IT Companies",
            y="Avg IT Salary (LPA)",
            size="Population (Millions)",
            color="Literacy Rate (%)",
            color_continuous_scale="Plasma",
            hover_name="State/UT",
            hover_data=["Major IT Hub"],
            text="Major IT Hub"
        )
        fig_salary.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#f1f5f9",
            xaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)"),
            height=500
        )
        fig_salary.update_traces(textposition='top center')
        st.plotly_chart(fig_salary, use_container_width=True)
        
    st.write("### 🏬 Prominent IT Hubs & Major Cities")
    hubs_df = filtered_df[filtered_df["IT Companies"] > 10].sort_values(by="IT Companies", ascending=False)
    
    st.dataframe(
        hubs_df[["State/UT", "Major IT Hub", "IT Companies", "Avg IT Salary (LPA)", "Literacy Rate (%)"]].style.background_gradient(
            cmap="Purples", subset=["IT Companies"]
        ).background_gradient(
            cmap="Greens", subset=["Avg IT Salary (LPA)"]
        ),
        use_container_width=True
    )

# --- Tab 3: Exploratory Data Analysis (EDA) ---
with tab_eda:
    st.write("### 🔢 Descriptive Statistics Summary")
    
    # Calculate stats summary
    summary_stats = filtered_df[["Population (Millions)", "Literacy Rate (%)", "IT Companies", "Avg IT Salary (LPA)"]].describe().T
    summary_stats.columns = ["Count", "Mean", "Std Dev", "Min", "25%", "50% (Median)", "75%", "Max"]
    
    st.dataframe(
        summary_stats.style.format("{:,.2f}").background_gradient(cmap="coolwarm", axis=1),
        use_container_width=True
    )
    
    st.write("### 🔗 Feature Correlations")
    corr_matrix = filtered_df[["Population (Millions)", "Literacy Rate (%)", "IT Companies", "Avg IT Salary (LPA)"]].corr()
    
    fig_corr = px.imshow(
        corr_matrix,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="RdBu_r",
        zmin=-1.0,
        zmax=1.0
    )
    fig_corr.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#f1f5f9",
        height=350
    )
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Search table and CSV downloader
    st.write("### 📋 Filtered Dataset Explorer")
    st.write(f"Showing **{len(filtered_df)}** regions matching criteria.")
    
    st.dataframe(filtered_df, use_container_width=True)
    
    # CSV download button
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_data,
        file_name="india_demographics_filtered.csv",
        mime="text/csv",
        use_container_width=True
    )
