# oh-my-zsh

#### 安装zsh
```shell
# 安装 Zsh
sudo apt install zsh

# 将 Zsh 设置为默认 Shell
chsh -s /bin/zsh
```

#### 安装 Oh My Zsh
```shell

wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
# 以上命令可能不好使，可使用如下两条命令
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
bash ./install.sh

#  如果上面出现443端口的错误，直接用git下载下来
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
#  拷贝一份配置文件
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

#### 安装powerline字体
```shell
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd ..
rm -rf fonts
```

#### 修改终端默认字体为Powerline
powerline支持图标，否则会乱码（如git)
![终端字体](vimages/20200205094300034_430335399.png)


#### 插件
```shell
#快速跳转
sudo apt install autojump
#自动补全
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
#语法高亮
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting


```

#### 修改配置文件 
```shell
# 设置命令行的主题
ZSH_THEME="agnoster"

# 以下内容去掉注释即可生效：
# 启动错误命令自动更正
ENABLE_CORRECTION="true"

# 在命令执行的过程中，使用小红点进行提示
COMPLETION_WAITING_DOTS="true"

# 启用已安装的插件
plugins=(
  git autojump zsh-autosuggestions zsh-syntax-highlighting
)
```

#### 细节
去掉前面显示的andy@Andy用户主机显示
```shell
#  使用的哪个主题修改哪个配置文件 
vim ~/.oh-my-zsh/themes/agnoster.zsh-theme

prompt_context() {
  if [[ "$USER" != "$DEFAULT_USER" || -n "$SSH_CLIENT" ]]; then
    prompt_segment black default "%(!.%{%F{yellow}%}.)$USER@%m" # 注释掉这行
  fi
}
```

agnoster主题的蓝色看不清字体
修改终端主题颜色和调色板为solarized
