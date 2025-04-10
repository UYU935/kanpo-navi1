import openai
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()
# 環境変数からAPIキーを取得

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai.api_key)

def generate_kanpo_response(data):
    prompt = f"""
あなたは漢方薬の処方医です。以下の患者情報をもとに、主訴の改善に望ましい漢方薬の例を複数選別し、保険収載状況を考慮して最適なものを提示してください。

年齢: {data['age']}
性別: {data['gender']}
主訴: {data['main_complaint']}
付随する症状: {', '.join(data['symptoms'])} {data['other_symptoms']}
舌診: {', '.join(data['tongue'])} {data['other_tongue']}
腹診: {', '.join(data['abdomen'])} {data['other_abdomen']}

この情報をもとに、適切な漢方薬を複数提案し、その理由や効果をわかりやすく説明してください。保険収載状況も考慮し、最後に最も適していると思われる漢方薬を1つ紹介してください。
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたは漢方に精通した医師です。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
