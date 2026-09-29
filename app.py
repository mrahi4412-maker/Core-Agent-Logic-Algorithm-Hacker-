import streamlit as st
from agent import SocialMediaAIAgent

st.set_page_title_config(page_title="AI Social Media Manager & Algorithm Hacker", layout="wide")

st.title("🚀 Nova Studio & Rahi Nur - AI Social Media Manager")
st.markdown("### Bypass the Algorithm & Automate Your Growth Across IG, FB, and YouTube")

# Sidebar for API Key & Brand Setup
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    brand_name = st.text_input("Brand Name", value="Rahi Nur & Nova Studio")
    niche = st.text_input("Niche", value="Fashion E-commerce & Comedy Animation")

# Main Interface
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Enter Your Content / Video Idea")
    video_concept = st.text_area("Describe what your video or reel is about:", 
                                 placeholder="e.g., Balancing customer orders at Shahpur Hat boutique while shooting comedy reels...")
    
    if st.button("🔥 Hack Algorithm & Generate Blueprint"):
        if not api_key:
            st.error("Please enter your Gemini API Key in the sidebar.")
        elif not video_concept:
            st.warning("Please enter a video concept.")
        else:
            with st.spinner("Analyzing algorithm metrics and crafting viral blueprint..."):
                agent = SocialMediaAIAgent(api_key=api_key)
                blueprint = agent.generate_algorithm_blueprint(brand_name, niche, video_concept)
                
                st.session_state['blueprint'] = blueprint

with col2:
    st.subheader("📊 Algorithmic Growth Blueprint")
    if 'blueprint' in st.session_state:
        st.markdown(st.session_state['blueprint'])
        
        # Download button for the generated strategy
        st.download_button(
            label="📥 Download Strategy as Markdown",
            data=st.session_state['blueprint'],
            file_name="viral_algorithm_blueprint.md",
            mime="text/markdown"
        )
    else:
        st.info("Your customized algorithm-busting strategy will appear here once you click generate.")
