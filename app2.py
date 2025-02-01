import streamlit as st

def calculate_bmi(weight, height):
    # BMIを計算する関数
    bmi = weight / (height / 100) ** 2
    return bmi

def main():
    st.title("BMI計算アプリ")

    weight = st.number_input("体重 (kg)", min_value=0.0, format="%.1f")
    height = st.number_input("身長 (cm)", min_value=0.0, format="%.1f")

    if st.button("BMIを計算"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.write(f"あなたのBMIは {bmi:.2f} です。")
            if bmi < 18.5:
                st.write("低体重です。")
                st.image("ダウンロード.jpeg", caption="低体重")
            elif 18.5 <= bmi < 24.9:
                st.write("普通体重です。")
                st.image("normal.png", caption="普通体重")
            elif 25 <= bmi < 29.9:
                st.write("過体重です。")
                st.image("overweight.png", caption="過体重")
            else:
                st.write("肥満です。")
                st.image("OIP.jpeg", caption="肥満")
        else:
            st.write("正しい体重と身長を入力してください。")

if __name__ == "__main__":
    main()
