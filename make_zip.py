import shutil

"""生成导入使用的 settings.zip 文件"""

ret = shutil.make_archive(base_name=r"settings", format='zip',root_dir=r"settings")