import json
import re

"""解决原Json文件太大VS无法进行格式化问题"""
def json_format(inputFile_path, outputFile_path):
    # 读取原始的JSON数据
    with open(inputFile_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 格式化JSON数据
    pretty_json = json.dumps(json_data, indent=2, ensure_ascii=False)

    # 将格式化后的JSON数据写入文件
    with open(outputFile_path, 'w', encoding='utf-8') as file:
        file.write(pretty_json)


"""处理ChatGPT答案:删除以```开头的整行"""
def delete_threePoint(input_string):
    # 将字符串按行拆分成列表
    lines = input_string.split('\n')
    # 迭代每一行，删除以```为开头和结尾的行
    filtered_lines = [line for line in lines if not line.startswith('```')]
    # 重新组合成字符串
    output_string = '\n'.join(filtered_lines)
    return output_string


"""抽取ChatGPT返回中的resolution"""
def extract_res_fromChatGPT(input_string):
    # 使用正则表达式匹配所有<resolution></resolution>内的内容
    matches = re.findall(r'<resolution>(.*?)</resolution>', input_string, re.DOTALL)
    if matches:
        last_resolution_content = matches[-1]
        return last_resolution_content
    else:
        return "null"
    
def extract_res_fromChatGPT2(input_string):
    # 使用正则表达式匹配所有<resolution></resolution>内的内容
    matches = re.findall(r'```java(.*?)```', input_string, re.DOTALL)
    if matches:
        last_resolution_content = matches[-1]
        return last_resolution_content
    else:
        return "null"


"""token-level result中的diff 标记都替换为不带文件地址的"""
def rewrite_DiffMarks(input_str):
    # 使用正则表达式进行替换
    output_str = re.sub(r'<<<<<<<.*|>>>>>>>.*|\|\|\|\|\|\|\|.*', 
                        lambda x: '<<<<<<<' if '<<<<<<<' in x.group(0) 
                        else ('>>>>>>>' if '>>>>>>>' in x.group(0) 
                        else '|||||||'), input_str)
    return output_str


"""使用a,o,b... 替换冲突块 得到答案"""
def replace_code_blocks_with_classification(input_str, token_conflict, choice):

    pattern = re.compile(r"<<<<<<<\s*.*?\s*=======\s*(.*?)\s*>>>>>>>", re.DOTALL)

    block_count = 0
    
    # 替换每个匹配的代码块
    def replace_block(match):
        nonlocal block_count
        block_count += 1

        if choice == "AB":
            replacement = token_conflict[block_count - 1].get("a_keyInfo", "") + token_conflict[block_count - 1].get("b_keyInfo", "")
        elif choice == "BA":
            replacement = token_conflict[block_count - 1].get("b_keyInfo", "") + token_conflict[block_count - 1].get("a_keyInfo", "")
        else:
            replacement = token_conflict[block_count - 1].get(choice, "")

        return replacement

    output_str = pattern.sub(replace_block, input_str)
    
    return output_str