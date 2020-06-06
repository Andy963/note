```shell
# 安装jupyter
pip install jupyter

# 生成配置文件
jupyter notebook --generate config

# 此时提示没有文件
# cd /home/andy/
# touch config

# 修改启动时的文件夹
vim .jupyter/jupyter_notebook_config.py
c.NotebookApp.notebook_dir = '/mnt/d/code/anaconda study'

# 安装主题
pip install --upgrade jupyterthemes

# 显示主题列表
jt -l

# 设置主题样式
jt -t onedork -f roboto -fs 14 -nfs 14 -tfs 14 -ofs 11

# 安装扩展插件
pip install jupyter_contrib_nbextensions

# 更新config
Writing updated config file /home/andy/.jupyter/jupyter_nbconvert_config.json

# 创建扩展文件夹
mkdir -p $(jupyter --data-dir)/nbextensions

# 查看下文件路径
#echo $(jupyter --data-dir)nbextensions
#/home/andy/.local/share/jupyternbextensions

# 切换到文件扩展插件文件夹下
$ cd $(jupyter --data-dir)/nbextensions

# 下载vim扩展
git clone https://github.com/lambdalisue/jupyter-vim-binding
# 打开jupyter notebook时在Nbextensions选项卡中选择插件
```