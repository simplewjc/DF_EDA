import pickle

# 原始 pkl 文件路径
input_file = "/media/simple/Data/DFPred_Dataset/processed_scenarios_training_infos.pkl"
# 新的 pkl 文件路径
output_file = "/media/simple/Data/DFPred_Dataset/processed_scenarios_training_cyclist_infos.pkl"

# 读取 pkl 文件
with open(input_file, 'rb') as f:
    data = pickle.load(f)

print(f"原始数据总量: {len(data)}")
print(f"- 原始数据示例: {data[0]}")

# 筛选包含 TYPE_CYCLIST 的场景
filtered_data = [
    scenario for scenario in data
    if 'tracks_to_predict' in scenario and
    any(obj_type == 'TYPE_CYCLIST' for obj_type in scenario['tracks_to_predict']['object_type'])
]

print(f"筛选后包含 TYPE_CYCLIST 的场景数量: {len(filtered_data)}")
print(f"- 筛选后数据示例: {filtered_data[0]}")

# 将筛选后的数据写入新的 pkl 文件
with open(output_file, 'wb') as f:
    pickle.dump(filtered_data, f)

print(f"已将筛选后的数据保存到: {output_file}")
