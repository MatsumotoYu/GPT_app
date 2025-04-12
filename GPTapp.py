import streamlit as st  # Streamlitの機能をインポート
from openai import OpenAI  # OpenAIライブラリをインポート
import os
from dotenv import load_dotenv  # .envファイルの読み込みに使う

# .envファイルの読み込み（例：OPENAI_API_KEY=sk-xxxxx）
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# APIキーを指定してOpenAIのクライアントを作成
client = OpenAI(api_key=api_key)

content_kind_of = [
    "中立的で客観的な文章",
    "分かりやすい、簡潔な文章",
    "親しみやすいトーンの文章",
    "専門用語をできるだけ使わない、一般読者向けの文章",
    "言葉の使い方にこだわり、正確な表現を心がけた文章",
    "ユーモアを交えた文章",
    "シンプルかつわかりやすい文法を使った文章",
    "面白く、興味深い内容を伝える文章",
    "具体的でイメージしやすい表現を使った文章",
    "人間味のある、感情や思いを表現する文章",
    "引用や参考文献を適切に挿入した、信頼性の高い文章",
    "読み手の興味を引きつけるタイトルやサブタイトルを使った文章",
    "統計データや図表を用いたわかりやすい文章",
    "独自の見解や考え方を示した、論理的な文章",
    "問題提起から解決策までを網羅した、解説的な文章",
    "ニュース性の高い、旬なトピックを取り上げた文章",
    "エンターテイメント性のある、軽快な文章",
    "読者の関心に合わせた、専門的な内容を深く掘り下げた文章",
    "人物紹介やインタビューを取り入れた、読み物的な文章",
]

def run_gpt(content_text_to_gpt, content_kind_of_to_gpt, content_maxStr_to_gpt):
    request_to_gpt = (
        content_text_to_gpt
        + " また、これを記事として読めるように、記事のタイトル、目次、内容の順番で出力してください。"
        + content_maxStr_to_gpt
        + "文字以内で出力してください。"
        + "また、文章は"
        + content_kind_of_to_gpt
        + "にしてください。"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": request_to_gpt},
        ],
    )

    output_content = response.choices[0].message.content.strip()
    return output_content

st.title('GPTに記事書かせるアプリ')

content_text_to_gpt = st.text_input("書かせたい内容を入力してください！")
content_kind_of_to_gpt = st.selectbox("文章の種類", options=content_kind_of)
content_maxStr_to_gpt = str(st.slider("記事の最大文字数", 100, 3000, 1000))

if content_text_to_gpt:
    output_content_text = run_gpt(content_text_to_gpt, content_kind_of_to_gpt, content_maxStr_to_gpt)
    st.markdown("### 生成された記事")
    st.write(output_content_text)
