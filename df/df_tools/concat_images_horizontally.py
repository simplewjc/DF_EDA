from PIL import Image

def concat_images_horizontally(img_path1, img_path2, output_path):
    # 打开两张图片
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)

    # 高度取最大，高度对齐，宽度相加
    h = max(img1.height, img2.height)
    w = img1.width + img2.width

    # 创建新图像（RGB 模式）
    new_img = Image.new('RGB', (w, h), color=(255, 255, 255))  # 白色背景

    # 粘贴图片
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1.width, 0))

    # 保存或展示
    new_img.save(output_path)
    #new_img.show()



#image1 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_319_vis.png'
#image2 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_1252_vis.png'
#image1 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_586_vis.png'
#image2 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_632_vis.png'
#image1 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_1300_vis.png'
#image2 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_1332_vis.png'
#image1 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_1757_vis.png'
#image2 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_1817_vis.png'
#image1 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_2191_vis.png'
#image2 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_2868_vis.png'
#image1 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_3617_vis.png'
#image2 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_3585_vis.png'
image1 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_2321_vis.png'
image2 ='/media/simple/Data/WorkSpace/DF_EDA/df/df_output/ex5/test_compare_gt_and_pred_2/0_vehicle_png/object_TYPE_VEHICLE_1673_vis.png'

combined = '/media/simple/Data/WorkSpace/DF_EDA/df_pred_result/pred_view/testA_vehicle_7.png'

# 示例调用
concat_images_horizontally(image1, image2, combined)
