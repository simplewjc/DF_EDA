import os
import pickle
import pandas as pd

# 获取并打印当前工作目录
current_working_directory = os.getcwd()
print("当前工作目录是:", current_working_directory)

def load_pickle(file_path):
    """加载 pickle 文件并返回数据"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data


def print_data_info(data, data_name):
    """打印数据基本信息"""
    print(f"\n🔍 {data_name} 信息:")
    
    # 判断数据类型并打印基本性质
    if isinstance(data, list):
        print(f"- 数据类型: List，长度: {len(data)}")
        if len(data) > 0:
            print(f"- 示例数据: {data[0]}")
    
    elif isinstance(data, dict):
        print(f"- 数据类型: Dict，键数: {len(data.keys())}")
        print(f"- 前5个键: {list(data.keys())[:5]}")
    
    elif isinstance(data, tuple):
        print(f"- 数据类型: Tuple，长度: {len(data)}")
        if len(data) > 0:
            print(f"- 示例数据: {data[0]}")
    
    else:
        print(f"- 未知数据类型: {type(data)}")


def extract_scenario_ids(data, data_name):
    """提取 scenario_id 并返回集合"""
    if isinstance(data, pd.DataFrame):
        if 'scenario_id' in data.columns:
            return set(data['scenario_id'])
    elif isinstance(data, list):
        # 列表中包含 dict 时提取 scenario_id
        if isinstance(data[0], dict) and 'scenario_id' in data[0]:
            return set(item['scenario_id'] for item in data)
    elif isinstance(data, dict):
        # 如果是 dict，可能以 scenario_id 作为键
        if 'scenario_id' in data:
            return set(data['scenario_id'])
        return set(data.keys())
    
    print(f"⚠️ 无法从 {data_name} 提取 scenario_id")
    return set()


def compare_scenario_ids(df_ids, wa_train_ids, wa_val_ids, data_name):
    """比较 DFPred 数据与 Waymo 训练/验证数据的 scenario_id"""
    in_waymo_train = df_ids.intersection(wa_train_ids)
    in_waymo_val = df_ids.intersection(wa_val_ids)
    not_in_waymo = df_ids - wa_train_ids - wa_val_ids

    print(f"\n🔎 {data_name} 场景比对结果：")
    print(f"✅ {len(in_waymo_train)} 个场景在 Waymo 训练集中")
    print(f"✅ {len(in_waymo_val)} 个场景在 Waymo 验证集中")
    print(f"❌ {len(not_in_waymo)} 个场景不在 Waymo 训练集和验证集中")

    return not_in_waymo


def compare_df_waymo(wa_train_pkl, wa_val_pkl, df_train_pkl, df_val_pkl, df_test_pkl):
    """加载 Waymo 和 DFPred 数据并比较 scenario_id"""
    # 加载数据
    wa_train = load_pickle(wa_train_pkl)
    wa_val = load_pickle(wa_val_pkl)
    df_train = load_pickle(df_train_pkl)
    df_val = load_pickle(df_val_pkl)
    df_test = load_pickle(df_test_pkl)
    
    # 查看数据性质
    print_data_info(wa_train, "Waymo Train (50%)")
    print_data_info(wa_val, "Waymo Val (100%)")
    print_data_info(df_train, "DFPred Train (100%)")
    print_data_info(df_val, "DFPred Val (100%)")
    print_data_info(df_test, "DFPred Test A")

    # 提取 scenario_id
    wa_train_ids = extract_scenario_ids(wa_train, "Waymo Train (50%)")
    wa_val_ids = extract_scenario_ids(wa_val, "Waymo Val (100%)")
    df_train_ids = extract_scenario_ids(df_train, "DFPred Train (100%)")
    df_val_ids = extract_scenario_ids(df_val, "DFPred Val (100%)")
    df_test_ids = extract_scenario_ids(df_test, "DFPred Test A")

    # 比较 scenario_id
    train_not_in_waymo = compare_scenario_ids(df_train_ids, wa_train_ids, wa_val_ids, "DFPred Train (100%)")
    val_not_in_waymo = compare_scenario_ids(df_val_ids, wa_train_ids, wa_val_ids, "DFPred Val (100%)")
    test_not_in_waymo = compare_scenario_ids(df_test_ids, wa_train_ids, wa_val_ids, "DFPred Test A")

    # 将不匹配的 scenario_id 保存为 CSV
    save_path = "./df/df_output/"  # 替换为你希望保存的目录路径
    save_unmatched_ids(train_not_in_waymo, "train_not_in_waymo.csv", save_path)
    save_unmatched_ids(val_not_in_waymo, "val_not_in_waymo.csv", save_path)
    save_unmatched_ids(test_not_in_waymo, "test_not_in_waymo.csv", save_path)


def save_unmatched_ids(scenario_ids, file_name, save_path):
    """将不匹配的 scenario_id 保存为 CSV"""
    if scenario_ids:
        # 确保指定的路径存在
        os.makedirs(save_path, exist_ok=True)
        # 创建完整的文件路径
        file_path = os.path.join(save_path, file_name)
        # 将数据保存为 CSV
        df = pd.DataFrame(list(scenario_ids), columns=['scenario_id'])
        df.to_csv(file_path, index=False)
        print(f"📁 未匹配的 scenario_id 已保存到: {file_path}")


if __name__ == '__main__':
    # 文件路径
    waymo_train_50_pkl = "/media/simple/Data/MTRDataset/processed_scenarios_training_infos.pkl"
    waymo_val_100_pkl = "/media/simple/Data/MTRDataset/processed_scenarios_val_infos.pkl"
    df_train_100_pkl = "/media/simple/Data/DFPred_Dataset/processed_scenarios_training_infos.pkl"
    df_val_100_pkl = "/media/simple/Data/DFPred_Dataset/processed_scenarios_val_infos.pkl"
    df_test_100_pkl = "/media/simple/Data/DFPred_Dataset/processed_scenarios_testA_full_infos.pkl"
    
    # 比较数据
    compare_df_waymo(waymo_train_50_pkl, waymo_val_100_pkl, 
                     df_train_100_pkl, df_val_100_pkl, 
                     df_test_100_pkl)
