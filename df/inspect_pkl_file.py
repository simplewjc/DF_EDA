import pickle


#file_path = "/media/simple/Data/DFPred_Dataset/processed_scenarios_training_infos.pkl"
#file_path = "/media/simple/Data/DFPred_Dataset/processed_training_testing_A_full/gt_data_df_test_A.pkl"
file_path = "/media/simple/Data/DFPred_Dataset/processed_scenarios_training_cyclist_infos.pkl"


# 加载数据
with open(file_path, "rb") as f:
    data = pickle.load(f)

print(type(data))
# 如果是字典或列表，打印出前几个样本
if isinstance(data, dict):
    for key in list(data.keys())[:5]:
        print(f"{key}: {data[key]}")
elif isinstance(data, list):
    print(data[:5])
