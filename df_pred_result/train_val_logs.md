# 实验记录

按照实验逻辑顺序命名 EX1 - EX6

## EX1 train_df100_val_df100_batch8_epoch30

使用 100% df_train 数据集训练模型 30 轮(后续补充实验训练到 50 轮)，并在 100% df_val 数据集进行模型评估

最佳结果：

```
checkpoint_epoch_30.pth

2025-04-14 15:25:57,928   INFO  *************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/1/checkpoint_epoch_30.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3818,      0.8249,      1.6070,      0.1916,            
   PEDESTRIAN      0.4004,      0.3808,      0.7803,      0.0864,            
      CYCLIST      0.2721,      0.7922,      1.5792,      0.2285,            
          Avg      0.3514,      0.6659,      1.3222,      0.1688,   
```

### 训练过程

训练数据：df_train 100% 数据   Total scenes after filters: 73477
超参数：batch_size=8, epoch=30
GPU: Quadro RTX 6000
final smoothed: about 80
time_cost(epoch): 2:23:23
time_cost(all): 71:45:00
acc_iter=275550, cur_iter=9184/9185
训练日志节选：
2025-04-13 22:01:01,744   INFO  epoch: 29/30, acc_iter=275400, cur_iter=9034/9185, batch_size=8, iter_cost=0.94s, time_cost(epoch): 2:21:02/02:21, time_cost(all): 71:42:39/02:21, ade_TYPE_VEHICLE_layer_5=0.608, ade_TYPE_PEDESTRIAN_layer_5=0.202, ade_TYPE_CYCLIST_layer_5=0.277, loss=-16.497, lr=6.25e-06
2025-04-13 22:02:36,231   INFO  epoch: 29/30, acc_iter=275500, cur_iter=9134/9185, batch_size=8, iter_cost=0.94s, time_cost(epoch): 2:22:36/00:47, time_cost(all): 71:44:13/00:47, ade_TYPE_VEHICLE_layer_5=0.492, ade_TYPE_PEDESTRIAN_layer_5=0.190, ade_TYPE_CYCLIST_layer_5=0.432, loss=-108.925, lr=6.25e-06
2025-04-13 22:03:23,228   INFO  epoch: 29/30, acc_iter=275550, cur_iter=9184/9185, batch_size=5, iter_cost=0.94s, time_cost(epoch): 2:23:23/00:00, time_cost(all): 71:45:00/00:00, ade_TYPE_VEHICLE_layer_5=0.467, ade_TYPE_PEDESTRIAN_layer_5=0.215, ade_TYPE_CYCLIST_layer_5=0.370, loss=-36.790, lr=6.25e-06

### 评估结果

评估数据：df_val 100% 数据  Total scenes after filters: 15745
GPU: GeForce RTX 3060
time cost: about 17 min
batch_size:3

####  checkpoint_epoch_20.pth

2025-04-14 16:05:36,688   INFO  *************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/1/checkpoint_epoch_20.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3517,      0.8554,      1.6765,      0.2065,            
   PEDESTRIAN      0.3786,      0.4035,      0.8311,      0.0940,            
      CYCLIST      0.2527,      0.8098,      1.6436,      0.2425,            
          Avg      0.3277,      0.6896,      1.3837,      0.1810,  

####  checkpoint_epoch_30.pth

2025-04-14 15:25:57,928   INFO  *************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/1/checkpoint_epoch_30.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3818,      0.8249,      1.6070,      0.1916,            
   PEDESTRIAN      0.4004,      0.3808,      0.7803,      0.0864,            
      CYCLIST      0.2721,      0.7922,      1.5792,      0.2285,            
          Avg      0.3514,      0.6659,      1.3222,      0.1688,           

#### plus + checkpoint_epoch_40.pth
2025-04-16 14:58:30,911   INFO  *************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/1/checkpoint_epoch_40.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3724,      0.8543,      1.6338,      0.1960,            
   PEDESTRIAN      0.4022,      0.3855,      0.7877,      0.0854,            
      CYCLIST      0.2627,      0.8082,      1.6084,      0.2378,            
          Avg      0.3458,      0.6827,      1.3433,      0.1731,            

#### plus + checkpoint_epoch_44.pth
*************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/1/checkpoint_epoch_44.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3737,      0.8446,      1.6294,      0.1967,            
   PEDESTRIAN      0.4085,      0.3954,      0.8066,      0.0855,            
      CYCLIST      0.2652,      0.8111,      1.6086,      0.2357,            
          Avg      0.3491,      0.6837,      1.3482,      0.1726,     

#### plus + checkpoint_epoch_48.pth
*************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/1/checkpoint_epoch_48.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3712,      0.8459,      1.6353,      0.1974,            
   PEDESTRIAN      0.3950,      0.3782,      0.7738,      0.0866,            
      CYCLIST      0.2669,      0.7967,      1.5878,      0.2314,            
          Avg      0.3444,      0.6736,      1.3323,      0.1718, 
#### summary
在df训练数据有限的且不更改学习率的前提下模型无法达到较好的效果

## EX2 train_waymo50_val_df100_batch8_epoch30

使用 50% waymo 训练数据集训练模型 30 轮，并在 100% df_val 数据集进行模型评估

最佳结果：
```
checkpoint_epoch_30

2025-04-08 12:22:06,811   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_30.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4606,      0.6720,      1.3167,      0.1200,            
   PEDESTRIAN      0.4472,      0.3634,      0.7355,      0.0659,            
      CYCLIST      0.3880,      0.6676,      1.3496,      0.1763,            
          Avg      0.4320,      0.5676,      1.1339,      0.1208,            
```

### 训练过程

训练数据： waymo 前 50% 左右  Total scenes after filters: 243992
超参数：batch_size=8, epoch=30
GPU: Quadro RTX 6000
final smoothed: about 95
time_cost(epoch): 7:23:40
time_cost(all): 222:23:55
acc_iter=914970, cur_iter=30499
训练日志节选：
2025-04-08 04:43:17,629   INFO  epoch: 29/30, acc_iter=914750, cur_iter=30278/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:20:27/03:12, time_cost(all): 222:20:42/03:12, ade_TYPE_VEHICLE_layer_5=0.453, ade_TYPE_PEDESTRIAN_layer_5=0.327, ade_TYPE_CYCLIST_layer_5=-0.000, loss=11.941, lr=6.25e-06
2025-04-08 04:44:01,720   INFO  epoch: 29/30, acc_iter=914800, cur_iter=30328/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:21:11/02:29, time_cost(all): 222:21:26/02:29, ade_TYPE_VEHICLE_layer_5=0.467, ade_TYPE_PEDESTRIAN_layer_5=0.168, ade_TYPE_CYCLIST_layer_5=-0.000, loss=12.713, lr=6.25e-06
2025-04-08 04:44:46,294   INFO  epoch: 29/30, acc_iter=914850, cur_iter=30378/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:21:55/01:45, time_cost(all): 222:22:10/01:45, ade_TYPE_VEHICLE_layer_5=0.456, ade_TYPE_PEDESTRIAN_layer_5=0.161, ade_TYPE_CYCLIST_layer_5=-0.000, loss=61.067, lr=6.25e-06
2025-04-08 04:45:30,764   INFO  epoch: 29/30, acc_iter=914900, cur_iter=30428/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:22:40/01:01, time_cost(all): 222:22:55/01:01, ade_TYPE_VEHICLE_layer_5=0.444, ade_TYPE_PEDESTRIAN_layer_5=0.180, ade_TYPE_CYCLIST_layer_5=0.347, loss=-43.358, lr=6.25e-06
2025-04-08 04:46:13,556   INFO  epoch: 29/30, acc_iter=914950, cur_iter=30478/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:23:22/00:18, time_cost(all): 222:23:38/00:18, ade_TYPE_VEHICLE_layer_5=0.456, ade_TYPE_PEDESTRIAN_layer_5=0.185, ade_TYPE_CYCLIST_layer_5=-0.000, loss=-23.835, lr=6.25e-06
2025-04-08 04:46:30,736   INFO  epoch: 29/30, acc_iter=914970, cur_iter=30498/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:23:40/00:00, time_cost(all): 222:23:55/00:00, ade_TYPE_VEHICLE_layer_5=0.514, ade_TYPE_PEDESTRIAN_layer_5=0.179, ade_TYPE_CYCLIST_layer_5=0.746, loss=248.652, lr=6.25e-06

### 评估结果

评估数据：df_val 100% 数据  Total scenes after filters: 15745
GPU: GeForce RTX 3060
time cost: about 17 min
batch_size:3

#### checkpoint_epoch_10
2025-04-06 11:58:38,720   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_10.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3466,      0.7975,      1.6009,      0.1674,            
   PEDESTRIAN      0.3717,      0.3977,      0.8180,      0.0884,            
      CYCLIST      0.2815,      0.8382,      1.7043,      0.2436,            
          Avg      0.3333,      0.6778,      1.3744,      0.1665,      

#### checkpoint_epoch_12
2025-04-16 17:10:47,424   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_12.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3631,      0.7720,      1.5866,      0.1688,            
   PEDESTRIAN      0.3718,      0.3979,      0.8202,      0.0860,            
      CYCLIST      0.2872,      0.7934,      1.6570,      0.2334,            
          Avg      0.3407,      0.6544,      1.3546,      0.1627,   

#### checkpoint_epoch_18
2025-04-06 12:25:26,511   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_18.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4080,      0.7345,      1.4998,      0.1534,            
   PEDESTRIAN      0.3726,      0.3873,      0.7958,      0.0883,            
      CYCLIST      0.3157,      0.7627,      1.5846,      0.2255,            
          Avg      0.3654,      0.6282,      1.2934,      0.1557, 

#### checkpoint_epoch_20                 
2025-04-16 18:33:21,880   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_20.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3919,      0.7484,      1.4803,      0.1498,            
   PEDESTRIAN      0.3919,      0.4045,      0.8220,      0.0792,            
      CYCLIST      0.2748,      0.8248,      1.6311,      0.2283,            
          Avg      0.3529,      0.6593,      1.3111,      0.1525,
          
#### checkpoint_epoch_21
2025-04-06 15:25:37,327   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_21.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3812,      0.7855,      1.5314,      0.1589,            
   PEDESTRIAN      0.3723,      0.3975,      0.8099,      0.0869,            
      CYCLIST      0.3322,      0.7620,      1.5968,      0.2216,            
          Avg      0.3619,      0.6483,      1.3127,      0.1558,   

#### checkpoint_epoch_22
2025-04-06 15:45:29,509   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_22.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.3962,      0.7486,      1.4662,      0.1460,            
   PEDESTRIAN      0.3905,      0.3819,      0.7823,      0.0789,            
      CYCLIST      0.3135,      0.7763,      1.5891,      0.2214,            
          Avg      0.3667,      0.6356,      1.2792,      0.1488,    

#### checkpoint_epoch_23
2025-04-06 16:06:12,369   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_23.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4221,      0.7111,      1.4074,      0.1342,            
   PEDESTRIAN      0.4144,      0.3748,      0.7625,      0.0729,            
      CYCLIST      0.3384,      0.7167,      1.4745,      0.2003,            
          Avg      0.3916,      0.6009,      1.2148,      0.1358,    

#### checkpoint_epoch_24
2025-04-06 12:44:28,966   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_24.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4268,      0.7223,      1.3983,      0.1348,            
   PEDESTRIAN      0.4227,      0.3902,      0.7895,      0.0707,            
      CYCLIST      0.3293,      0.7263,      1.4631,      0.2001,            
          Avg      0.3929,      0.6129,      1.2170,      0.1352,     

#### checkpoint_epoch_25
2025-04-16 16:51:30,797   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_25.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4464,      0.6778,      1.3509,      0.1249,            
   PEDESTRIAN      0.4409,      0.3696,      0.7520,      0.0687,            
      CYCLIST      0.3609,      0.6909,      1.4146,      0.1917,            
          Avg      0.4161,      0.5794,      1.1725,      0.1284,     

#### checkpoint_epoch_26
2025-04-08 11:31:53,803   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_26.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4357,      0.7172,      1.3742,      0.1297,            
   PEDESTRIAN      0.4354,      0.3791,      0.7661,      0.0691,            
      CYCLIST      0.3668,      0.7044,      1.4059,      0.1900,            
          Avg      0.4126,      0.6002,      1.1821,      0.1296,     

#### checkpoint_epoch_27
2025-04-08 11:13:34,943   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_27.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4528,      0.6839,      1.3417,      0.1236,            
   PEDESTRIAN      0.4288,      0.3580,      0.7288,      0.0695,            
      CYCLIST      0.3886,      0.6740,      1.3672,      0.1818,            
          Avg      0.4234,      0.5719,      1.1459,      0.1250,            

#### checkpoint_epoch_28
2025-04-07 23:10:04,803   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_28.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4586,      0.6792,      1.3311,      0.1230,            
   PEDESTRIAN      0.4489,      0.3621,      0.7368,      0.0666,            
      CYCLIST      0.3859,      0.6854,      1.3870,      0.1814,            
          Avg      0.4311,      0.5756,      1.1516,      0.1236,            

#### checkpoint_epoch_29
2025-04-07 22:48:57,750   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_29.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4641,      0.6605,      1.3138,      0.1190,            
   PEDESTRIAN      0.4405,      0.3562,      0.7245,      0.0672,            
      CYCLIST      0.3883,      0.6731,      1.3625,      0.1814,            
          Avg      0.4309,      0.5633,      1.1336,      0.1225,            

#### checkpoint_epoch_30
2025-04-08 12:22:06,811   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_30.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4606,      0.6720,      1.3167,      0.1200,            
   PEDESTRIAN      0.4472,      0.3634,      0.7355,      0.0659,            
      CYCLIST      0.3880,      0.6676,      1.3496,      0.1763,            
          Avg      0.4320,      0.5676,      1.1339,      0.1208,            

补充：epoch_30 为 mAP表现最好的 pth，说明模型有进一步训练潜力


## EX3 eda_b8_e30_t25_notv


## EX4 train_df100_batch8_epoch10_after_train_waymo50_batch8_epoch30_val_df100

先使用 50% waymo 训练数据集训练模型 30 轮（由于本人硬件配置限制，这里直接使用 EX1 得到的 checkpoint_epoch_30.pth），之后使用 100% df_train 数据集训练模型 10 轮，并在 100% df_val 数据集进行模型评估


最佳结果：
```
checkpoint_epoch_40

2025-04-14 16:31:52,160   INFO  *************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/eda_df_after_waymo/checkpoint_epoch_40.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4591,      0.6941,      1.3536,      0.1377,            
   PEDESTRIAN      0.4472,      0.3610,      0.7407,      0.0720,            
      CYCLIST      0.3709,      0.6830,      1.3725,      0.1825,            
          Avg      0.4257,      0.5794,      1.1556,      0.1308,    
```

### 训练过程

基础模型：train_waymo50_val_df100_batch8_epoch30   checkpoint_epoch_30.pth
训练数据： waymo 前 50% 左右  Total scenes after filters: 243992
超参数：batch_size=8, epoch=10
GPU: Quadro RTX 6000
final smoothed: about -60  注意这里严重过拟合
time_cost(epoch): 2:24:34
time_cost(all): 22:37:33
acc_iter=1001165, cur_iter=9184(base on acc_iter=914970, cur_iter=30499)
训练日志节选：
2025-04-09 21:16:56,309   INFO  epoch: 39/40, acc_iter=1000900, cur_iter=8919/9185, batch_size=8, iter_cost=0.94s, time_cost(epoch): 2:20:25/04:11, time_cost(all): 22:33:24/04:11, ade_TYPE_VEHICLE_layer_5=0.641, ade_TYPE_PEDESTRIAN_layer_5=0.182, ade_TYPE_CYCLIST_layer_5=0.491, loss=-18.639, lr=6.25e-06
2025-04-09 21:17:44,223   INFO  epoch: 39/40, acc_iter=1000950, cur_iter=8969/9185, batch_size=8, iter_cost=0.94s, time_cost(epoch): 2:21:13/03:24, time_cost(all): 22:34:12/03:24, ade_TYPE_VEHICLE_layer_5=0.576, ade_TYPE_PEDESTRIAN_layer_5=0.274, ade_TYPE_CYCLIST_layer_5=0.321, loss=41.739, lr=6.25e-06
2025-04-09 21:18:30,626   INFO  epoch: 39/40, acc_iter=1001000, cur_iter=9019/9185, batch_size=8, iter_cost=0.94s, time_cost(epoch): 2:22:00/02:36, time_cost(all): 22:34:59/02:36, ade_TYPE_VEHICLE_layer_5=0.504, ade_TYPE_PEDESTRIAN_layer_5=0.186, ade_TYPE_CYCLIST_layer_5=0.864, loss=-11.442, lr=6.25e-06
2025-04-09 21:19:18,209   INFO  epoch: 39/40, acc_iter=1001050, cur_iter=9069/9185, batch_size=8, iter_cost=0.94s, time_cost(epoch): 2:22:47/01:49, time_cost(all): 22:35:46/01:49, ade_TYPE_VEHICLE_layer_5=0.561, ade_TYPE_PEDESTRIAN_layer_5=0.275, ade_TYPE_CYCLIST_layer_5=0.317, loss=-7.292, lr=6.25e-06
2025-04-09 21:20:04,801   INFO  epoch: 39/40, acc_iter=1001100, cur_iter=9119/9185, batch_size=8, iter_cost=0.94s, time_cost(epoch): 2:23:34/01:02, time_cost(all): 22:36:33/01:02, ade_TYPE_VEHICLE_layer_5=0.522, ade_TYPE_PEDESTRIAN_layer_5=0.317, ade_TYPE_CYCLIST_layer_5=0.526, loss=-24.564, lr=6.25e-06
2025-04-09 21:20:51,508   INFO  epoch: 39/40, acc_iter=1001150, cur_iter=9169/9185, batch_size=8, iter_cost=0.94s, time_cost(epoch): 2:24:21/00:15, time_cost(all): 22:37:20/00:15, ade_TYPE_VEHICLE_layer_5=0.617, ade_TYPE_PEDESTRIAN_layer_5=0.182, ade_TYPE_CYCLIST_layer_5=0.840, loss=0.725, lr=6.25e-06
2025-04-09 21:21:04,514   INFO  epoch: 39/40, acc_iter=1001165, cur_iter=9184/9185, batch_size=5, iter_cost=0.94s, time_cost(epoch): 2:24:34/00:00, time_cost(all): 22:37:33/00:00, ade_TYPE_VEHICLE_layer_5=0.493, ade_TYPE_PEDESTRIAN_layer_5=0.189, ade_TYPE_CYCLIST_layer_5=0.714, loss=-4.151, lr=6.25e-06

### 评估结果

评估数据：df_val 100% 数据  Total scenes after filters: 15745
GPU: GeForce RTX 3060
time cost: about 17 min
batch_size:3

#### checkpoint_epoch_35
2025-04-09 21:48:32,876   INFO  *************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/eda_df_after_waymo/checkpoint_epoch_35.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4567,      0.6802,      1.3469,      0.1349,            
   PEDESTRIAN      0.4342,      0.3586,      0.7341,      0.0703,            
      CYCLIST      0.3729,      0.6802,      1.3785,      0.1818,            
          Avg      0.4213,      0.5730,      1.1532,      0.1290,          
          
#### checkpoint_epoch_39
2025-04-09 21:27:16,992   INFO  *************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/eda_df_after_waymo/checkpoint_epoch_39.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4590,      0.6871,      1.3509,      0.1373,            
   PEDESTRIAN      0.4419,      0.3659,      0.7505,      0.0711,            
      CYCLIST      0.3744,      0.6850,      1.3790,      0.1844,            
          Avg      0.4251,      0.5793,      1.1601,      0.1310,    

#### checkpoint_epoch_40
2025-04-14 16:31:52,160   INFO  *************** Performance of EPOCH ../output/dfPred/eda+100_percent_data/eda_df_after_waymo/checkpoint_epoch_40.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4591,      0.6941,      1.3536,      0.1377,            
   PEDESTRIAN      0.4472,      0.3610,      0.7407,      0.0720,            
      CYCLIST      0.3709,      0.6830,      1.3725,      0.1825,            
          Avg      0.4257,      0.5794,      1.1556,      0.1308,     

#### summary
在学习率较小的情况下已经无法进一步取得更好的效果，需要考虑预训练模型和后训练模型的学习率匹配的问题



## EX5 eda_b8_e40_t50_fine_tnue_25pth
观察 EX2 实验的 Loss 曲线后，进一步优化学习率相关参数：
OPTIMIZATIO.DECAY_STEP_LIST: [22, 24, 26, 28] 调整为 [22, 24, 29, 33, 37]
使用 50% waymo 训练数据集训练模型 40 轮(由于本人硬件配置限制，这里直接从 EX1 所得的checkpoint_epoch_25.pth 进行恢复训练)，并在 100% df_val 数据集进行模型评估

最佳结果：
```
checkpoint_epoch_39.pth 

2025-04-22 15:11:10,356   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_39.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4766,      0.6532,      1.2977,      0.1145,            
   PEDESTRIAN      0.4533,      0.3494,      0.7085,      0.0651,            
      CYCLIST      0.4119,      0.6458,      1.2979,      0.1739,            
          Avg      0.4473,      0.5495,      1.1014,      0.1178,       
```

### 训练过程
基础模型：train_waymo50_val_df100_batch8_epoch30   checkpoint_epoch_25.pth
训练数据： waymo 前 50% 左右  Total scenes after filters: 243992
超参数：batch_size=8, epoch=15
GPU: Quadro RTX 6000
final smoothed: about 60
time_cost(epoch):  7:23:53
time_cost(all): 110:44:16
acc_iter=1219960, cur_iter=30499
训练日志节选：
2025-04-21 11:30:36,821   INFO  Save latest model to /home/jacky/WorkSpace/DFPred/EDA/output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/latest_model
2025-04-21 11:30:40,408   INFO  epoch: 39/40, acc_iter=1219700, cur_iter=30238/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:20:05/03:47, time_cost(all): 110:40:28/03:47, ade_TYPE_VEHICLE_layer_5=0.476, ade_TYPE_PEDESTRIAN_layer_5=0.147, ade_TYPE_CYCLIST_layer_5=0.409, loss=4.687, lr=3.125e-06
2025-04-21 11:32:07,994   INFO  epoch: 39/40, acc_iter=1219800, cur_iter=30338/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:21:33/02:20, time_cost(all): 110:41:55/02:20, ade_TYPE_VEHICLE_layer_5=0.372, ade_TYPE_PEDESTRIAN_layer_5=0.404, ade_TYPE_CYCLIST_layer_5=0.332, loss=-51.819, lr=3.125e-06
2025-04-21 11:33:36,076   INFO  epoch: 39/40, acc_iter=1219900, cur_iter=30438/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:23:01/00:53, time_cost(all): 110:43:23/00:53, ade_TYPE_VEHICLE_layer_5=0.531, ade_TYPE_PEDESTRIAN_layer_5=0.567, ade_TYPE_CYCLIST_layer_5=-0.000, loss=62.178, lr=3.125e-06
2025-04-21 11:34:28,844   INFO  epoch: 39/40, acc_iter=1219960, cur_iter=30498/30499, batch_size=8, iter_cost=0.87s, time_cost(epoch): 7:23:53/00:00, time_cost(all): 110:44:16/00:00, ade_TYPE_VEHICLE_layer_5=0.418, ade_TYPE_PEDESTRIAN_layer_5=0.137, ade_TYPE_CYCLIST_layer_5=-0.000, loss=-10.796, lr=3.125e-06

### 评估结果

评估数据：df_val 100% 数据  Total scenes after filters: 15745
GPU: GeForce RTX 3060
time cost: about 17 min
batch_size:3

#### checkpoint_epoch_25
2025-04-16 16:51:30,797   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_25.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4464,      0.6778,      1.3509,      0.1249,            
   PEDESTRIAN      0.4409,      0.3696,      0.7520,      0.0687,            
      CYCLIST      0.3609,      0.6909,      1.4146,      0.1917,            
          Avg      0.4161,      0.5794,      1.1725,      0.1284,     

#### checkpoint_epoch_28.pth 
2025-04-22 10:35:47,948   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_28.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4586,      0.6669,      1.3378,      0.1222,            
   PEDESTRIAN      0.4389,      0.3640,      0.7431,      0.0684,            
      CYCLIST      0.3898,      0.6641,      1.3520,      0.1830,            
          Avg      0.4291,      0.5650,      1.1443,      0.1245, 

#### checkpoint_epoch_33.pth 
2025-04-22 11:00:41,209   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_33.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4604,      0.6813,      1.3260,      0.1202,            
   PEDESTRIAN      0.4437,      0.3537,      0.7181,      0.0668,            
      CYCLIST      0.3777,      0.6733,      1.3550,      0.1783,            
          Avg      0.4273,      0.5694,      1.1331,      0.1218,

#### checkpoint_epoch_34.pth           
2025-04-22 21:10:47,719   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_34.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4692,      0.6595,      1.2942,      0.1172,            
   PEDESTRIAN      0.4589,      0.3603,      0.7318,      0.0641,            
      CYCLIST      0.3963,      0.6600,      1.3155,      0.1751,            
          Avg      0.4415,      0.5599,      1.1138,      0.1188,  

#### checkpoint_epoch_36.pth          
2025-04-22 17:16:37,480   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_36.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4751,      0.6584,      1.3143,      0.1178,            
   PEDESTRIAN      0.4411,      0.3563,      0.7210,      0.0680,            
      CYCLIST      0.4057,      0.6478,      1.3031,      0.1750,            
          Avg      0.4407,      0.5542,      1.1128,      0.1202,   

#### checkpoint_epoch_37.pth 
2025-04-22 11:20:46,996   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_37.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4725,      0.6679,      1.3016,      0.1166,            
   PEDESTRIAN      0.4522,      0.3506,      0.7128,      0.0651,            
      CYCLIST      0.3996,      0.6597,      1.3275,      0.1737,            
          Avg      0.4414,      0.5594,      1.1140,      0.1185,      

#### checkpoint_epoch_38.pth 
2025-04-22 11:57:28,209   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_38.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4689,      0.6750,      1.3104,      0.1167,            
   PEDESTRIAN      0.4531,      0.3535,      0.7170,      0.0655,            
      CYCLIST      0.4080,      0.6613,      1.3138,      0.1757,            
          Avg      0.4433,      0.5633,      1.1137,      0.1193,    

#### checkpoint_epoch_39.pth  
2025-04-22 15:11:10,356   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_39.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4766,      0.6532,      1.2977,      0.1145,            
   PEDESTRIAN      0.4533,      0.3494,      0.7085,      0.0651,            
      CYCLIST      0.4119,      0.6458,      1.2979,      0.1739,            
          Avg      0.4473,      0.5495,      1.1014,      0.1178,       

#### checkpoint_epoch_40.pth 
2025-04-22 11:38:25,961   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data_fine_tune/eda_b8_e40_t50_fine_tnue_25pth/ckpt/checkpoint_epoch_40.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4578,      0.6990,      1.3345,      0.1213,            
   PEDESTRIAN      0.4512,      0.3547,      0.7189,      0.0673,            
      CYCLIST      0.4012,      0.6575,      1.3118,      0.1744,            
          Avg      0.4367,      0.5704,      1.1217,      0.1210,  


## EX6 eda_b8_e40_df_t100_fine_tune_25pth

类比 EX4，观察 EX2 实验的 Loss 曲线后，进一步优化学习率相关参数：
OPTIMIZATIO.DECAY_STEP_LIST: [22, 24, 26, 28] 调整为 [22, 24, 29, 33, 37]
使用 50% waymo 训练数据集训练模型 25 轮(由于本人硬件配置限制，这里直接从EX1所得的checkpoint_epoch_25.pth 进行恢复训练)，之后使用 100% df_train 数据集训练模型 15 轮（微调），并在 100% df_val 数据集进行模型评估

最佳结果：
```
checkpoint_epoch_38.pth 
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4649,      0.6580,      1.3185,      0.1198,            
   PEDESTRIAN      0.4386,      0.3571,      0.7289,      0.0672,            
      CYCLIST      0.3748,      0.6688,      1.3625,      0.1813,            
          Avg      0.4261,      0.5613,      1.1366,      0.1227, 
```

基础模型：train_waymo50_val_df100_batch8_epoch30   checkpoint_epoch_25.pth
训练数据：df_train 100% 数据   Total scenes after filters: 73477
超参数：batch_size=8, epoch=15
GPU: Quadro RTX 6000
final smoothed: about 9   注意这里过拟合
time_cost(epoch): 2:27:28
time_cost(all): 36:55:21
acc_iter=900130, cur_iter=9184(base on acc_iter=914970, cur_iter=30499)
训练日志节选：
2025-04-24 09:52:02,159   INFO  Save latest model to /home/jacky/WorkSpace/DFPred/EDA/output/dfPred/eda+100_percent_data_fine_tune/eda_b8_e40_df_t100_fine_tune_25pth/ckpt/latest_model
2025-04-24 09:52:32,436   INFO  epoch: 39/40, acc_iter=899700, cur_iter=8754/9185, batch_size=8, iter_cost=0.96s, time_cost(epoch): 2:20:31/06:55, time_cost(all): 36:48:25/06:55, ade_TYPE_VEHICLE_layer_5=0.450, ade_TYPE_PEDESTRIAN_layer_5=0.223, ade_TYPE_CYCLIST_layer_5=0.321, loss=-32.805, lr=3.125e-06
2025-04-24 09:54:09,009   INFO  epoch: 39/40, acc_iter=899800, cur_iter=8854/9185, batch_size=8, iter_cost=0.96s, time_cost(epoch): 2:22:08/05:18, time_cost(all): 36:50:01/05:18, ade_TYPE_VEHICLE_layer_5=0.388, ade_TYPE_PEDESTRIAN_layer_5=0.210, ade_TYPE_CYCLIST_layer_5=0.654, loss=-58.423, lr=3.125e-06
2025-04-24 09:55:49,778   INFO  epoch: 39/40, acc_iter=899900, cur_iter=8954/9185, batch_size=8, iter_cost=0.96s, time_cost(epoch): 2:23:49/03:42, time_cost(all): 36:51:42/03:42, ade_TYPE_VEHICLE_layer_5=0.398, ade_TYPE_PEDESTRIAN_layer_5=0.211, ade_TYPE_CYCLIST_layer_5=0.334, loss=-69.414, lr=3.125e-06
2025-04-24 09:57:02,579   INFO  Save latest model to /home/jacky/WorkSpace/DFPred/EDA/output/dfPred/eda+100_percent_data_fine_tune/eda_b8_e40_df_t100_fine_tune_25pth/ckpt/latest_model
2025-04-24 09:57:27,163   INFO  epoch: 39/40, acc_iter=900000, cur_iter=9054/9185, batch_size=8, iter_cost=0.96s, time_cost(epoch): 2:25:26/02:06, time_cost(all): 36:53:19/02:06, ade_TYPE_VEHICLE_layer_5=0.510, ade_TYPE_PEDESTRIAN_layer_5=0.310, ade_TYPE_CYCLIST_layer_5=-0.000, loss=57.300, lr=3.125e-06
2025-04-24 09:59:01,607   INFO  epoch: 39/40, acc_iter=900100, cur_iter=9154/9185, batch_size=8, iter_cost=0.96s, time_cost(epoch): 2:27:01/00:29, time_cost(all): 36:54:54/00:29, ade_TYPE_VEHICLE_layer_5=0.513, ade_TYPE_PEDESTRIAN_layer_5=0.141, ade_TYPE_CYCLIST_layer_5=0.334, loss=14.051, lr=3.125e-06
2025-04-24 09:59:29,044   INFO  epoch: 39/40, acc_iter=900130, cur_iter=9184/9185, batch_size=5, iter_cost=0.96s, time_cost(epoch): 2:27:28/00:00, time_cost(all): 36:55:21/00:00, ade_TYPE_VEHICLE_layer_5=0.467, ade_TYPE_PEDESTRIAN_layer_5=0.238, ade_TYPE_CYCLIST_layer_5=0.402, loss=-49.422, lr=3.125e-06

### 评估结果

评估数据：df_val 100% 数据  Total scenes after filters: 15745
GPU: GeForce RTX 3060
time cost: about 17 min
batch_size:3

#### checkpoint_epoch_28.pth
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4619,      0.6622,      1.3256,      0.1210,            
   PEDESTRIAN      0.4349,      0.3605,      0.7356,      0.0684,            
      CYCLIST      0.3690,      0.6749,      1.3785,      0.1851,            
          Avg      0.4220,      0.5659,      1.1465,      0.1248,  
          
#### checkpoint_epoch_30.pth
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4613,      0.6591,      1.3234,      0.1189,            
   PEDESTRIAN      0.4323,      0.3582,      0.7307,      0.0691,            
      CYCLIST      0.3741,      0.6796,      1.3978,      0.1873,            
          Avg      0.4226,      0.5656,      1.1506,      0.1251,    

#### checkpoint_epoch_33.pth 
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4609,      0.6635,      1.3239,      0.1202,            
   PEDESTRIAN      0.4375,      0.3589,      0.7321,      0.0679,            
      CYCLIST      0.3688,      0.6739,      1.3703,      0.1865,            
          Avg      0.4224,      0.5654,      1.1421,      0.1249,       

#### checkpoint_epoch_38.pth 
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4649,      0.6580,      1.3185,      0.1198,            
   PEDESTRIAN      0.4386,      0.3571,      0.7289,      0.0672,            
      CYCLIST      0.3748,      0.6688,      1.3625,      0.1813,            
          Avg      0.4261,      0.5613,      1.1366,      0.1227,            

#### checkpoint_epoch_40.pth 
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4619,      0.6651,      1.3215,      0.1211,            
   PEDESTRIAN      0.4401,      0.3584,      0.7313,      0.0670,            
      CYCLIST      0.3737,      0.6705,      1.3588,      0.1807,            
          Avg      0.4252,      0.5647,      1.1372,      0.1229,  
