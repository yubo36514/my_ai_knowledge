import re
import json

def extract_json(text):
    find_text = re.search(r"{.*?}", text, re.DOTALL)
    if find_text:
        try:
            return json.loads(find_text.group(0))
        except json.JSONDecodeError:
            print(f"```{text}```不是一个合法的json格式")
    return None

# 示例1：有效的 JSON
s1 = '{"name": "John", "age": 30}'
print(extract_json(s1))  # {'name': 'John', 'age': 30}

# 示例2：无效的 JSON
s2 = '{name: "John", age: 30}'
print(extract_json(s2))  # None
# 示例3：无效 JSON（括号内的内容不是合法 JSON）
s3 = '代码块 { var x = 1; } 注释'
print(extract_json(s3))  # None