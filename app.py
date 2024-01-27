import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Generate LLama2 model completion

def generate_response(topic, word_count, blog_style):
    llm = CTransformers(model = "LLM_Model/llama-2-7b.ggmlv3.q8_0.bin",
                        model_type = "llama",
                        config = {"max_new_tokens":256,
                                  "temperature":0.01})
    
    template ='''
    Write a short blog for {blog_style} on the topic {topic} within {word_count} words.
    '''

    prompt_template = PromptTemplate(
        input_variables=["blog_style","topic","word_count"],
        template=template
    )

    prompt = prompt_template.format(blog_style=blog_style, topic=topic, word_count=word_count)
    print(prompt)
    response = llm(prompt)
    print(response)
    return response

# Streamlit App Code

st.set_page_config(
    page_title="Blog Generation App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("Generate Blog 🤖")

topic = st.text_input("Enter the blog topic")

col1, col2 = st.columns(2)

word_count = col1.text_input("Number of words")
blog_style = col2.selectbox("Writing the blog for", ("Researchers", "Data Professionals", "Common people"), index=0)

submit = st.button("Generate", type="primary")

if submit:
    st.write(generate_response(topic, word_count, blog_style))
