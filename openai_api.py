import sys
from openai import OpenAI
import time
from utils import delete_threePoint, extract_res_fromChatGPT, extract_res_fromChatGPT2
sys.argv=['']
del sys

"""配置API key(若是中转 则需要配置中转链接)"""

client = OpenAI(
    base_url="https://xiaoai.plus/v1", # Tao 2024年4月28日12:47:37 30刀-sk-ZByhW5X77gttGkRL3eCf55C4F3Eb4bCa9a3527A01aC82f9a
    api_key="sk-ZByhW5X77gttGkRL3eCf55C4F3Eb4bCa9a3527A01aC82f9a" 
)

print(f"""OpenAI API_KEY Configuration completed in {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}""")

"""ChatGPT(GPT-3.5) 一次对话"""
def ChatGPT_35Code(question, number, role, truth_resolution):

    all_responses = [] 
    print(question)
    print(f"\n<Truth Resolution>:-------->\n{truth_resolution}\n</Truth Resolution>-------->")
    for i in range(number):
        print(f"\n---------------ChatGPT的第{i + 1}个Resolution：---------------")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106", # gpt-3.5-turbo-1106 # gpt-3.5-turbo
            messages=[
                {
                "role": "system", "content": role # 指定角色(Java高级开发工程师)
                },
                {
                "role": "user", "content": question
                }
            ], 
            max_tokens = 2048, # This model's maximum context length is 4097 tokens.
            temperature = 0, # 0-2之间，越大越随机，越小越确定 0.01
        )
        
        current_response = response.choices[0].message.content
        # 这里是easy prompt 的处理
        # print(extract_code(current_response))
        # all_responses.append(extract_code(current_response))

        # 这里是COT的处理
        print(current_response)
        only_code = delete_threePoint(extract_res_fromChatGPT(current_response))
        if only_code == "null" or only_code == "":
            only_code = delete_threePoint(extract_res_fromChatGPT2(current_response))
            all_responses.append(only_code)
        else:
            all_responses.append(only_code)

    return all_responses

# 老版本的api
# def ChatGPT_35Code(question, number, role, truth_resolution):
#     response = client.chat.completions.create(
#         # 使用GPT-3.5模型 即ChatGPT模型
#         model="gpt-3.5-turbo-1106", # gpt-3.5-turbo-1106 # gpt-3.5-turbo
#         # model="gpt-4",
#         messages=[
#             {
#             "role": "system", "content": role # 指定角色(Java高级开发工程师)
#             },
#             {
#             "role": "user", "content": question
#             }
#         ], 
#         max_tokens = 2048, # This model's maximum context length is 4097 tokens.
#         temperature = 0.01, # 0-2之间，越大越随机，越小越确定 0.01
#         n=number 
#     )

#     all_responses = [] 
#     print(question)
#     print(f"\n<Truth Resolution>:-------->\n{truth_resolution}\n</Truth Resolution>-------->")
#     for i in range(number):
#         print(f"\n---------------ChatGPT的第{i + 1}个Resolution：---------------")
        
#         current_response = response.get("choices")[i]["message"]["content"]
#         # 这里是easy prompt 的处理
#         # print(extract_code(current_response))
#         # all_responses.append(extract_code(current_response))

#         # 这里是COT的处理
#         print(current_response)
#         only_code = delete_threePoint(extract_res_fromChatGPT(current_response))
#         if only_code == "null" or only_code == "":
#             only_code = delete_threePoint(extract_res_fromChatGPT2(current_response))
#             all_responses.append(only_code)
#         else:
#             all_responses.append(only_code)

#     return all_responses


"""ChatGPT(GPT-4.0) 一次对话"""
def ChatGPT_40Code(question, number, role):
    response = openai.ChatCompletion.create(
        # 使用GPT-4.0模型 即ChatGPT模型
        model="gpt-4-1106-preview",
        # model="gpt-4",
        messages=[
            {
            "role": "system", "content": role # 指定角色(Java高级开发工程师)
            },
            {
            "role": "user", "content": question
            }
        ], 
        max_tokens=2048,
        temperature=0.1, 
        n=number 
    )

    all_responses = [] 
    print(question)
    for i in range(number):
        print(f"\n-----------ChatGPT的第{i + 1}个Resolution：-----------")
        current_response = response.get("choices")[i]["message"]["content"]
        print(extract_code(current_response))
        all_responses.append(extract_code(current_response))

    return all_responses


"""ChatGPT(GPT-3.5) 一次对话"""
def ChatGPT_35(question, number, role):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106", # gpt-3.5-turbo-1106 # gpt-3.5-turbo
        # model="gpt-4",
        messages=[
            {
            "role": "system", "content": role 
            },
            {
            "role": "user", "content": question
            }
        ], 
        max_tokens=2048,
        temperature=0.1,
        n=number
    
    )
    for i in range(number):
        print(f"\n-----------第{i+1}个回答：-----------")
        print(response.get("choices")[i]["message"]["content"])


"""针对ChatGPT回答 过滤出真正的代码部分"""
def extract_code(input_str):
    if input_str[:7] == "```java":
        return input_str[7:-3].strip()
    elif input_str[:1] == "【":
        return input_str[1:-1].strip()
    else:
        return input_str