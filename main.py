import streamlit as st
from stat_app import calculate_stats

# Set page configuration
st.set_page_config(page_title="📊 Stat App", page_icon="📈", layout="centered")

def main():
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>📊 Statistical Analysis Tool</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Enter a list of numbers to compute common statistical metrics.</p>", unsafe_allow_html=True)
    st.write("---")

    user_input = st.text_input("🔢 Enter numbers separated by spaces:")

    if st.button("Run Analysis"):
        if user_input:
            stats = calculate_stats(user_input)

            if isinstance(stats, str):
                st.error(stats)
            else:
                mean, median, mode, variance, std_dev = stats

                st.success("✅ Analysis Complete!")
                st.markdown("### 📈 Statistics Summary")
                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Mean", f"{mean:.2f}")
                    st.metric("Median", f"{median:.2f}")
                    st.metric("Mode", str(mode))

                with col2:
                    st.metric("Variance", f"{variance:.2f}")
                    st.metric("Std Deviation", f"{std_dev:.2f}")
        else:
            st.warning("⚠️ Please enter numbers before clicking the button.")

    st.write("---")
    st.caption("Developed by Jersil G M | Python | Data Analysis App")

if __name__ == "__main__":
    main()
