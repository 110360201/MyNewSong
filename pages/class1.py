import streamlit as st

st.set_page_config(page_title="Sing a Song", page_icon="🎵", layout="wide")


st.title("Class 1")

if "apple" not in st.session_state:
    st.session_state.apple = 1

apple = 1


@st.fragment(run_every=1)
def video_loop():
    st.markdown(
        f"""
    # Session state apple: {st.session_state.apple}
    # Global apple: {apple}
    """
    )


video_loop()

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    if st.button("clear session state"):
        st.session_state.apple = 1

with col2:
    if st.button("Click me session state"):
        st.session_state.apple += 1

with col3:
    if st.button("Click me global"):
        apple += 1

with col4:
    if st.button("reload page"):
        st.rerun()


st.markdown("""video loop here""")
