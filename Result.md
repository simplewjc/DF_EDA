# 实验记录

## EX1 train_waymo50_val_df100_batch8_epoch30

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

#### checkpoint_epoch_18
2025-04-06 12:25:26,511   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_18.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4080,      0.7345,      1.4998,      0.1534,            
   PEDESTRIAN      0.3726,      0.3873,      0.7958,      0.0883,            
      CYCLIST      0.3157,      0.7627,      1.5846,      0.2255,            
          Avg      0.3654,      0.6282,      1.2934,      0.1557,        

#### checkpoint_epoch_26

2025-04-08 11:31:53,803   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_26.pth *****************
       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4357,      0.7172,      1.3742,      0.1297,            
   PEDESTRIAN      0.4354,      0.3791,      0.7661,      0.0691,            
      CYCLIST      0.3668,      0.7044,      1.4059,      0.1900,            
          Avg      0.4126,      0.6002,      1.1821,      0.1296,     

#### checkpoint_epoch_28
2025-04-07 23:10:04,803   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_28.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4586,      0.6792,      1.3311,      0.1230,            
   PEDESTRIAN      0.4489,      0.3621,      0.7368,      0.0666,            
      CYCLIST      0.3859,      0.6854,      1.3870,      0.1814,            
          Avg      0.4311,      0.5756,      1.1516,      0.1236,            

#### checkpoint_epoch_30
2025-04-08 12:22:06,811   INFO  *************** Performance of EPOCH ../output/waymo/eda+50_percent_data/eda_b8_e30_t50_v25_new/ckpt/checkpoint_epoch_30.pth *****************

       Waymo          mAP       minADE       minFDE     MissRate            
      VEHICLE      0.4606,      0.6720,      1.3167,      0.1200,            
   PEDESTRIAN      0.4472,      0.3634,      0.7355,      0.0659,            
      CYCLIST      0.3880,      0.6676,      1.3496,      0.1763,            
          Avg      0.4320,      0.5676,      1.1339,      0.1208,            

补充：epoch_30 为 mAP表现最好的 pth，说明模型有进一步训练潜力


## EX2 train_df100_val_df100_batch8_epoch30

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

#### plus + 

## EX3 train_df100_batch8_epoch10_after_train_waymo50_batch8_epoch30_val_df100

### 训练过程

基础模型：train_waymo50_val_df100_batch8_epoch30   checkpoint_epoch_30.pth
训练数据：df_train 100% 数据   Total scenes after filters: 73477
超参数：batch_size=8, epoch=10
GPU: Quadro RTX 6000
final smoothed: about -60   waymo 数据涵盖 df数据，且更具挑战性
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

#### 
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
