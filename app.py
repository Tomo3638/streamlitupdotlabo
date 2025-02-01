import streamlit as st

# タイトル
st.title("簡易計算アプリ")

# 入力
num1 = st.number_input("1つ目の数字を入力してください", value=0)
num2 = st.number_input("2つ目の数字を入力してください", value=0)

# 計算
sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "割り算は0で割ることはできません"

# 結果を表示
st.write(f"足し算: {sum_result}")
st.write(f"引き算: {sub_result}")
st.write(f"掛け算: {mul_result}")
st.write(f"割り算: {div_result}")

# 実行
if __name__ == '__main__':
    st.run()
