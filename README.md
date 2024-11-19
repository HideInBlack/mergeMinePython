# mergeMinePython

# 一.运行环境

> - Python 3.7.9
> - Notebook
> - Openai api

# 二.内容介绍

![img](https://ovxmsaoguz.feishu.cn/space/api/box/stream/download/asynccode/?code=NTA5ODlmNDFiODMwM2ZmZjdiNTRkNDBiZTBkYzBiNzdfOXdlNzhHRlhKb2JqNVBuUmJKY3htWE5ucEVZeTVTWHhfVG9rZW46Wk1LSGJJMjN3b1U5bWZ4R3p1emNUdnl1bnNmXzE3MzIwMjQyNjA6MTczMjAyNzg2MF9WNA)

> ----文件夹----
>
> - codebert：存放下载的codebert模型
> - joern：使用joern的工具类以及切片工具类
> - json：输入文件夹
> - output：输出文件夹
> - print：打印内容
>
> ----文件----
>
> - merge_gpt:
>   - 基于73779个冲突块按照真实实际占比抽取对应示例
>   - ChatGPT api调用实际运行对应所抽取数据集
> - merge_thread1:
>   - merge_gpt的并行运行版本（可忽略）
> - openai_api:
>   - openai官方api调用使用：一次对话、多次对话等
> - prompt_role:
>   - prompt不同提示风格的提示内容
> - utils:
>   - 工具类：一些常规工具方法
> - zzz_utils:
>   - 工具类：一些常规数据处理的方法（随时写随时丢）