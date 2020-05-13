# markdown2slides-pandoc

## 更新

- 在源代码上进行了修改，使其可以在windows系统运行
- 此版本只适用于windows系统（原版mac）
- 修正了windows系统中的编码问题
- 集成了pandoc文件
- 优化了pandoc路径不正确时的报错

## 使用方法

### 配置

- 打开revealjs_converter.py文件，找到pandoc_slide_md_to_revealjs函数
- 根据我的中文注释更改pandoc.exe的存储路径，保存关闭
- 修改config.json中需要修改的信息

### 文件准备

要生成slide，需要将你写好的markdown文件以.md格式保存在此目录下，如果有本地关联的文件，可以为它们创建一个文件夹（参见example文件夹中的示例）

### 命令

- 在此目录下打开命令行，或使用cd命令到此目录

- 执行命令
  ``python md2slide.py path/filename.md``

  将其中的`path/filename.md`改为你的markdown文件路径及名称
  例如对example下的myslide.md文件执行：

  ```python md2slide.py example/myslide.md```

- 执行成功则会自动打开网页，并且生成`temp.md` `temp.html`及一个export文件夹

- 如需脱离环境打开，则复制整个export文件夹，打开html文件即可

- 更详细的使用方法请看[王老师的文章](https://sspai.com/post/57095)

## 感谢

感谢王老师的[源代码](https://github.com/wshuyi/markdown2slides)，非常实用的工具！

关于pandoc，如果你想单独下载，请访问[这个链接](https://github.com/jgm/pandoc)，更详细的使用方法可以参考[手册](https://pandoc.org/index.html)

关于reveal.js，你可以直接访问[在线应用](https://slides.com/?ref=github)，其源代码在[这里](https://github.com/hakimel/reveal.js)

希望大家支持这些工具的原作者！