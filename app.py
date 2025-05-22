import streamlit as st
from logic.classify import classify_problem
from logic.solver_router import solve_problem

st.set_page_config(page_title="Supply Chain Bot", page_icon="📦")
st.title("📦 Supply Chain AI Solver")
st.markdown("Nhập bài toán SCM (bằng tiếng Việt hoặc English):")

question = st.text_area("📝 Nhập đề bài / Enter your problem:", height=250)

if st.button("🔍 Giải bài toán / Solve"):
    if question.strip():
        problem_type = classify_problem(question)
        result = solve_problem(question, problem_type)
        st.markdown("## ✅ Dạng bài toán / Detected Problem Type:")
        st.info(problem_type)
        st.markdown("## 📄 Lời giải / Solution:")
        st.write(result)
    else:
        st.warning("Vui lòng nhập đề bài / Please enter a problem to solve.")