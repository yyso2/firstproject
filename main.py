import streamlit as st
import random

# 🌈 Streamlit 설정
st.set_page_config(page_title="가위✌️바위✊보🖐️ 게임", page_icon="🎮", layout="centered")

# 🌟 스타일링용 이모지
icons = {
    "가위": "✌️",
    "바위": "✊",
    "보": "🖐️"
}

st.markdown("<h1 style='text-align: center; color: gold;'>🎮 가위 ✌️ 바위 ✊ 보 🖐️ 게임에 오신 걸 환영합니다! 🎉</h1>", unsafe_allow_html=True)

st.markdown("## 😎 당신의 선택은?")

# 🧑 사용자 선택
user_choice = st.radio("👇 아래에서 선택하세요!", ["가위", "바위", "보"], horizontal=True)

# 🖥️ 컴퓨터 선택
computer_choice = random.choice(["가위", "바위", "보"])

# 🥊 승부 판단
def get_result(user, computer):
    if user == computer:
        return "🤝 무승부입니다!"
    elif (user == "가위" and computer == "보") or \
         (user == "바위" and computer == "가위") or \
         (user == "보" and computer == "바위"):
        return "🎉 당신이 이겼어요! 멋져요! 😎"
    else:
        return "😢 컴퓨터가 이겼네요... 다시 도전해봐요!"

if st.button("🔥 대결 시작!"):
    st.markdown("---")
    st.markdown(f"### 🧑 당신: **{user_choice} {icons[user_choice]}**")
    st.markdown(f"### 💻 컴퓨터: **{computer_choice} {icons[computer_choice]}**")
    st.markdown("## 🏆 결과:")
    st.success(get_result(user_choice, computer_choice))
    st.balloons()
else:
    st.markdown("👉 왼쪽에서 선택 후 '대결 시작!' 버튼을 눌러주세요!")

st.markdown("---")
st.markdown("<h3 style='text-align: center;'>💡 팁: 페이지를 새로 고치면 컴퓨터 선택도 바뀌어요!</h3>", unsafe_allow_html=True)

