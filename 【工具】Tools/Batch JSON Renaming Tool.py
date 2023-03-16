# 导入argparse模块，用于解析命令行参数
import argparse
# 导入os模块，用于操作文件和目录
import os
# 导入json模块，用于处理JSON数据
import json

# 创建ArgumentParser对象，设置命令行参数的描述信息
parser = argparse.ArgumentParser(description="对多个JSON文件进行重命名")
# 添加directory_path参数，用于指定包含JSON文件的目录的路径
parser.add_argument("directory_path", help="包含JSON文件的目录的路径")
# 添加new_name_prefix参数，用于指定新名称值的前缀
parser.add_argument("new_name_prefix", help="新名称值的前缀")
# 解析命令行参数，并将结果保存到args变量中
args = parser.parse_args()
# 初始化计数器count为1
count = 1

# 遍历指定目录下的所有文件和目录
for filename in os.listdir(args.directory_path):
    # 如果文件名以.json结尾
    if filename.endswith(".json"):
        # 打开文件，读取文件内容，并将结果保存到data变量中
        with open(os.path.join(args.directory_path, filename), "r") as f:
            data = json.load(f)
        # 修改JSON数据中的"name"字段的值
        data["name"] = args.new_name_prefix + str(count)
        # 打开文件，写入修改后的JSON数据
        with open(os.path.join(args.directory_path, filename), "w") as f:
            json.dump(data, f)
        # 创建新目录路径
        new_directory_path = args.directory_path + "new"
        # 创建新目录
        os.makedirs(new_directory_path, exist_ok=True)
        # 将修改后的文件保存到新目录下，并重命名
        os.rename(os.path.join(args.directory_path, filename), os.path.join(new_directory_path, data["name"] + ".json"))
        # 计数器加1
        count += 1
# 输出处理的文件数量 
print("处理了", count - 1, "个文件。")