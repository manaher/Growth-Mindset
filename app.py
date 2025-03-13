#streamlit
import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="💡")

st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This app helps you build a Growth Mindset with challenges and achievements! 💪")

#Quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("Your only limit is your mind. Embrace challenges, learn from failures, and grow beyond what you once thought possible 💪🚀")

st.header("💡 What's your challenge today?")
user_input = st.text_input("Describe a challenge you are facing:")

#condition
if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal! 💪")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on your learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")

else:
    st.info("Reflecting on past experience help ypu grow! Share your difficulties")

#achievements
st.header("🏆 Celebrate your win!")
achievement = st.text_input("Share something you have recently accomplished:")

if achievement:
    st.success(f"🌟 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievemnt counts! Share one now 😊")

#footer
st.write("- - -")
st.write("Keep believing in yourself, growth is a journey not a destination! 💪")
st.write("**©️ Created by Manaher Irfan**")