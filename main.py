import streamlit as st

from langchain_helper import generate_food_list

# Set Page Config
st.set_page_config(
    page_title="Nigerian Restaurant Generator", page_icon="🇳🇬", layout="wide"
)

# App Title & Description
st.markdown(
    "<h1 style='text-align: center; color: #ffffff;'>🇳🇬 Nigerian Restaurant & Menu Generator</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #ffffff;'>Discover traditional Nigerian restaurant names and their special delicacies!</p>",
    unsafe_allow_html=True,
)

# Sidebar - Tribe Selection
st.sidebar.markdown(
    "<h3 style='color: #008000;'>🌍 Choose a Nigerian Tribe</h3>",
    unsafe_allow_html=True,
)
nigerian_tribes = [
    "Hausa",
    "Yoruba",
    "Igbo",
    "Fulani",
    "Kanuri",
    "Tiv",
    "Ijaw",
    "Ibibio",
    "Nupe",
    "Gwari",
    "Efik",
    "Itsekiri",
    "Urhobo",
    "Jukun",
    "Igala",
    "Idoma",
    "Edo",
    "Isoko",
    "Ebira",
    "Berom",
    "Bachama",
    "Bajju",
    "Higgi",
    "Tarok",
    "Bini",
    "Bade",
    "Zarma",
    "Mumuye",
    "Angas",
    "Shuwa",
    "Kamuku",
    "Gbagyi",
    "Margi",
    "Mambila",
    "Dakka",
    "Dakarkari",
    "Bambora",
    "Babur",
    "Bolewa",
    "Chamba",
    "Kagoro",
    "Kilba",
    "Kaje",
    "Koro",
    "Kuteb",
    "Kambari",
]
chosen_tribe = st.sidebar.selectbox("🗺️ Select a Tribe", nigerian_tribes)


restaurant_name, food_list = generate_food_list(chosen_tribe)

# Display Restaurant Name
st.markdown(
    f"<h2 style='color: #ffffff;'>🏡 Restaurant Name: <b>{restaurant_name}</b></h2>",
    unsafe_allow_html=True,
)

# Display Food Menu
st.markdown(
    "<h3 style='color: #ffffff;'>🍛 Recommended Dishes:</h3>", unsafe_allow_html=True
)
st.markdown(
    "\n".join(
        [
            f"<p style='color: #ffffff;'>✅ {item.strip()}</p>"
            for item in food_list.split(",")
        ]
    ),
    unsafe_allow_html=True,
)
