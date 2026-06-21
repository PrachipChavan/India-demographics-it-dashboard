import streamlit as st
import time

def init_auth_state():
    """Initialize session state variables for authentication."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = None

def check_login(username, password):
    """Validate user credentials."""
    # Simple hardcoded credentials for demonstration
    # Can be replaced with database queries or hashing checks
    return username == "admin" and password == "india@2026"

def logout():
    """Clear session authentication state."""
    st.session_state.authenticated = False
    st.session_state.username = None
    st.success("Logged out successfully!")
    time.sleep(1)
    st.rerun()

def render_login_page():
    """Render a beautiful, colorful login page."""
    # Centered container using styling from styles.css
    st.markdown(
        """
        <div class="login-container">
            <div class="gradient-text">India Insights</div>
            <div class="gradient-subtext">Demographics & IT Hub Explorer</div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # login form block
    with st.form("login_form"):
        st.write("### Sign In to Dashboard")
        username_input = st.text_input("Username", placeholder="e.g. admin", value="admin")
        password_input = st.text_input("Password", type="password", placeholder="e.g. password", value="india@2026")
        
        submit_button = st.form_submit_button("Access Dashboard")
        
        if submit_button:
            if check_login(username_input, password_input):
                st.session_state.authenticated = True
                st.session_state.username = username_input
                st.success("Login successful! Loading dashboard...")
                time.sleep(1.2)
                st.rerun()
            else:
                st.error("Invalid Username or Password. Hint: admin / india@2026")

    # Add descriptive info below the login card
    st.markdown(
        """
        <div style="text-align: center; margin-top: 2rem; color: #64748b; font-size: 0.85rem;">
            Dashboard Demo Credentials:<br>
            <b>Username:</b> admin | <b>Password:</b> india@2026
        </div>
        """,
        unsafe_allow_html=True
    )
