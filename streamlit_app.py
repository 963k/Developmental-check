
import streamlit as st

st.set_page_config(page_title="発達段階診断", page_icon="🧠", layout="centered")

st.title("🧠 発達段階セルフチェック（青年期向け）")
st.markdown("あなたの今の状態を確認し、成長のヒントを見つけましょう。")

# 年齢スライダー
age = st.slider("あなたの年齢を教えてください", 10, 80, 20)

# 青年期の範囲のみ表示
if 12 <= age <= 22:
    st.subheader("あなたは今、**青年期（12〜22歳）** の段階にいます。")
    st.markdown("以下の項目に**はい / いいえ**で答えてみてください。")

    questions = {
        "自分は何者なのか、よく考えることがある": None,
        "将来の進路や働き方について悩むことがある": None,
        "人との関係に不安を感じることがある": None,
        "親や教師より、友人との関係を優先することがある": None,
        "自分らしさを大事にしたいと思っている": None
    }

    answers = {}
    for q in questions:
        answers[q] = st.radio(q, ["はい", "いいえ"], key=q)

    if st.button("診断する"):
        yes_count = sum([1 for a in answers.values() if a == "はい"])
        st.subheader("◆ 診断結果")

        if yes_count >= 4:
            st.success("あなたは今、**自己理解と他者との関係の中で深く模索する時期**にいます。\n\nその悩みや違和感は、成長の証です。安心して、今の自分と対話を続けてください。")
        elif 2 <= yes_count < 4:
            st.info("あなたは今、**少しずつ自分らしさを掴み始めている段階**です。\n\nモヤモヤは悪いことではなく、“気づき”のきっかけ。焦らず進んで大丈夫。")
        else:
            st.warning("今はあまり違和感を感じていないかもしれません。\n\nでも、自分に問いかける時間をつくることで、今後の指針がクリアになるかもしれません。")

else:
    st.info("この診断は **青年期（12〜22歳）** に焦点を当てた内容です。対象年齢のときにぜひ試してみてください。")
