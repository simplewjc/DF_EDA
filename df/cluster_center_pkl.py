import os
import pickle

def view_cluster_center_dick_pkl(cluster_pkl_dir):
    with open(cluster_pkl_dir, 'rb') as f:
        # add stop point here to check cluster_scene_data
        cluster_scene_data = pickle.load(f)
    
    print(cluster_scene_data)


if __name__ == '__main__':
    cluster_pkl_dir = './MTR/data/waymo/cluster_64_center_dict.pkl'
    view_cluster_center_dick_pkl(cluster_pkl_dir)