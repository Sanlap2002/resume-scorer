import os
from openai import OpenAI
from string import Template
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_result(type,resume_text, job_desc):
    prompt_template=""

    if type=="score":
        prompt_template = Template(
            """Here's some resume text:- 
            "$rt"

            And here's the job description:- 
            "$jd"

            Based on the resume text, give only a numeric score out of 100 and no extra text — the answer should be only a single number between 1 and 100."""
        )
    else:
        prompt_template = Template(
            """Here's some resume text:- 
            "$rt"

            And here's the job description:- 
            "$jd"

            Based on the resume text, suggest me the major improvements in a concise form"""
        )

    message = prompt_template.substitute(rt=resume_text, jd=job_desc)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY,
    )

    completion = client.chat.completions.create(
        model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    return completion.choices[0].message.content
