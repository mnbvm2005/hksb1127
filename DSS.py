from openai import OpenAI
import streamlit as st
import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
import altair as alt
import numpy as np
import json

st.set_page_config(page_title="决策支持系统分析工具", layout="wide")

api_key = "sk-0eC1yRepDAgia0zFDe51D63688C742C69b1e46C8Bb26B1D3"
api_base = "http://maas-api.cn-huabei-1.xf-yun.com/v1"
MODEL_ID = "xop3qwen1b7"
client = OpenAI(api_key=api_key, base_url=api_base)


def ask_ai(messages, json_type=True, model_id=MODEL_ID):
    json_messages = [{"role": "user", "content": messages}]
    if json_type:
        extra_body = {
            "response_format": {"type": "json_object"},
            "search_disable": True
        }
    else:
        extra_body = {}
    response = client.chat.completions.create(
        model=model_id,
        messages=json_messages,
        extra_body=extra_body
    )
    message = response.choices[0].message.content
    if json_type:
        message = json.loads(message)
    return message


def ai_explain(task, method, ds_name, highlights):
    prompt = f"""
你是数据科学助教。请用中文简要解读下面的模型结果，并给出3-5条面向管理者的可执行建议（使用•项目符号，不要输出代码）。
任务：{task}；方法：{method}；数据集：{ds_name}
关键结果：{highlights}
请先用1-2句话说明结果意味着什么，再给出建议；尽量避免术语，聚焦业务含义。
"""
    return ask_ai(prompt, json_type=False)


def load_data(task, ds_name):
    ds = sk.datasets
    if task == "分类":
        if ds_name.startswith("Iris"):
            d = ds.load_iris()
        elif ds_name.startswith("Wine"):
            d = ds.load_wine()
        else:
            d = ds.load_breast_cancer()
        return d.data, d.target, d.feature_names, list(d.target_names)
    return None, None, None, None


def train_model(task, method, ds_name, test_size=0.2):
    X, y, _, target_names = load_data(task, ds_name)
    if X is None:
        st.error("数据加载失败")
        return

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=test_size, random_state=0
    )

    if method == "DecisionTree":
        model = sk.tree.DecisionTreeClassifier(random_state=0)
    else:
        model = LGBMClassifier(random_state=0)
    model.fit(X_tr, y_tr)
    y_pred = model.predict(X_te)

    acc = sk.metrics.accuracy_score(y_te, y_pred)
    cm = sk.metrics.confusion_matrix(y_te, y_pred)

    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.subheader("📊 模型评估结果")
        st.metric("准确率（Accuracy）", f"{acc:.3f}")

        cm_df = pd.DataFrame(
            cm,
            index=[f"实际: {t}" for t in target_names],
            columns=[f"预测: {t}" for t in target_names]
        )
        heat = alt.Chart(cm_df.reset_index().melt("index")).mark_rect().encode(
            x=alt.X("variable:N", title="预测类别"),
            y=alt.Y("index:N", title="实际类别"),
            color=alt.Color("value:Q", title="数量"),
            tooltip=["index", "variable", "value"]
        ).properties(title="混淆矩阵")
        st.altair_chart(heat, use_container_width=True)

    with right_col:
        st.subheader("🤖 AI解读与管理建议")
        highlights = f"准确率={acc:.3f}；混淆矩阵规模={cm.shape}。"
        with st.spinner("AI生成解读中..."):
            ai_text = ai_explain(task, method, ds_name, highlights)
            if ai_text:
                st.write(ai_text)
            else:
                st.warning("未能生成AI解读，请重试")


def main():
    st.title("决策支持系统模型分析工具")

    with st.sidebar:
        st.header("参数设置")
        task = st.selectbox("任务类型", ["分类"])
        ds_name = st.selectbox("选择数据集", ["Iris（鸢尾花）", "Wine（葡萄酒）", "Breast Cancer（乳腺癌）"])
        method = st.selectbox("选择模型", ["DecisionTree（决策树）", "LGBM（梯度提升树）"])
        test_size = st.slider("测试集比例", 0.1, 0.5, 0.2)

        if st.button("开始分析"):
            with st.spinner("正在运行分析..."):
                model_short = method.split("（")[0]
                train_model(task, model_short, ds_name, test_size)

    with st.expander("📚 常见决策支持系统模型类型", expanded=True):
        try:
            messages = """
            请帮我整理下决策支持系统有哪些常见的模型类型，
            返回json结构，包含名称，适用问题，边界条件
            输出结构如下
            {
             'system 1': {'name': XXX, 'question_type': XXX, 'boundary': XXX},
             'system 2': {'name': XXX, 'question_type': XXX, 'boundary': XXX},
             ...
             }
            """
            res = ask_ai(messages)
            st.dataframe(pd.DataFrame(res).T, use_container_width=True)
        except Exception as e:
            st.warning(f"加载模型类型失败: {str(e)}")


if __name__ == "__main__":
    main()