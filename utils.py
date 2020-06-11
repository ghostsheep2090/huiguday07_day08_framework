# 读取登录数据
import json
import os


def read_login_data():
    login_data_path = os.path.dirname(os.path.abspath(__file__)) + "/data/login_data.json"
    with open(login_data_path, mode="r", encoding="utf-8")as f:
        jsonData = json.load(f)
        result_list = list()
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))
        print(result_list)
    return result_list

#调试
if __name__ == '__main__':
    read_login_data()
