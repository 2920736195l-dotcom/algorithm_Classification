import os
import shutil


def copy_images_by_labels(label_folder, image_folder, output_folder):
    """
    根据标签文件复制对应图片到指定目录
    参数:
        label_folder: 包含标签txt文件的文件夹路径
        image_folder: 包含原始图片的文件夹路径
        output_folder: 输出目录路径
    """
    # 支持的图片文件扩展名（可自行添加）
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.webp')

    # 确保输出目录存在
    os.makedirs(output_folder, exist_ok=True)

    # 构建图片文件名字典（不区分大小写）
    image_dict = {}
    for img_file in os.listdir(image_folder):
        img_path = os.path.join(image_folder, img_file)
        if os.path.isfile(img_path):
            name, ext = os.path.splitext(img_file)
            if ext.lower() in image_extensions:
                image_dict[name.lower()] = img_path  # 使用小写文件名作为键

    # 遍历标签文件进行匹配
    copied_count = 0
    missing_files = []

    for label_file in os.listdir(label_folder):
        if label_file.endswith('.txt'):
            label_name = os.path.splitext(label_file)[0]
            label_key = label_name.lower()

            if label_key in image_dict:
                src_path = image_dict[label_key]
                dest_path = os.path.join(output_folder, os.path.basename(src_path))

                # 执行文件复制
                shutil.copy(src_path, dest_path)
                copied_count += 1
            else:
                missing_files.append(label_file)

    # 输出结果报告
    print(f"操作完成！\n成功复制文件数: {copied_count}")
    if missing_files:
        print(f"未找到对应图片的标签文件数: {len(missing_files)}")
        print("以下标签文件未找到对应图片:")
        for f in missing_files:
            print(f"  - {f}")


if __name__ == "__main__":
    # 配置路径（根据实际情况修改）
    label_dir = r"D:\yolov5-7.0\runs\detect\exp22\labels"  # 标签文件夹路径
    image_dir = r"E:\jy\JYDA\jy0325\202503241\20250324"  # 图片文件夹路径
    output_dir = r"E:\jy\jyng_ori0325"  # 输出文件夹路径

    # 执行复制操作
    copy_images_by_labels(label_dir, image_dir, output_dir)