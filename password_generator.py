import random
import string


def generate_password(length):
    # 定义密码可用字符：字母、数字、符号
    chars = string.ascii_letters + string.digits + string.punctuation

    # 随机生成密码
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


# 示例：生成 12 位随机密码
print(generate_password(12))