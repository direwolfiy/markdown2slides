from pathlib import Path
from revealjs_converter import MarkdownRevealjsConverter
import sys
# get the dir of current python file
code_dir = Path(__file__).absolute().parent

try:
    md_fname = sys.argv[1]      #得到
except:
    print("usage: python md2slide.py [markdown filename]") #运行失败提示操作命令
    exit()

config = dict()
config["path"] = code_dir/"config.json" #定位配置文件

#调用class MarkdownRevealjsConverter
converter = MarkdownRevealjsConverter(md_fname, **config)  
converter.convert()   #执行convert函数，最后自动预览slide


