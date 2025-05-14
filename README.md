# 东风预测比赛说明文档

## 参赛信息

Author name: 汪建成

Author school: 吉林大学

Author email: wjc24@mails.jlu.edu.cn (镜像中部分文件误写为 .com)

## Docker 中 DF_EDA 项目目录说明

/ckpt 目录提供本组进行的六组实验的关键 pth 权重文件,其中 ex5_checkpoint_epoch_39.pth 为最佳模型权重文件 （镜像中提供）

/df 目录包含比赛相关的测试及分析代码，包含 get_gt_data.py 、eval_gt_and_pred.py 、waymo_eval.py 、waymo_types.py 文件

/df_pred_reult 目录为比赛相关的结果分析文件，包含 testing_B1 的预测结果 result_processed_scenarios_testing_B1_part.pkl 文件（镜像中提供）和 testing_A1 的预测结果展示

/docs 为说明文档目录

/eda 及 /MTR 为项目模型实现代码

/output 为 train/val/test/pred/ 等默认输出路径

/tools 为脚本文件和配置参数目录

## 算法测试说明文档

算法测试说明文档见 [算法测试说明文档](算法测试说明文档.md)

主要包含 项目总体介绍、预测结果快速验证（基于 Python）、预测结果完整验证（基于 Docker）、项目完整复现流程（基于 Docker） 内容

其中 预测结果快速验证（基于 Python）、预测结果完整验证（基于 Docker）可以验证对 processed_scenarios_testing_B1_part 目录的预测效果，官方提供 part (1s) 历史信息，这里根据 1s 信息预测出未来 8s 的结果文件为：[result_processed_scenarios_testing_B1_part.pkl](df_pred_result/result_processed_scenarios_testing_B1_part.pkl)（镜像中提供）
需要官方后续进行评测，详细步骤见算法测试说明文档

## 算法说明文档

算法说明文档见 [算法说明文档](算法说明文档.md)
主要包含 算法设计、算法创新点、效果演示、未来改进方向、个人想法 内容

## 训练及评估日志总结
本人共基于 Waymo 及 DF 数据集进行六组实验，训练及评估日志总结详情见：

[训练及评估日志总结详细版](训练及评估日志总结详细版.md)
[训练及评估日志总结概要版](训练及评估日志总结概要版.md)

## Docker 镜像说明

本小组提供 simplewjc/df_eda_image:v3 镜像

采用 docker save 导出镜像：
```
docker save -o simplewjc__df_eda_image.tar simplewjc/df_eda_image:v3
```

请将提交的 simplewjc__df_eda_image.tar 文件下载到主机

通过 docker load 导入镜像：
```
docker load -i simplewjc__df_eda_image.tar
```
