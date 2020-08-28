## sudo 免密码
sudo 命令免密码：
visudo 专门来编辑

ubuntu:
```shell
vi /etc/sudoers
andy ALL=NOPASSWD:ALL # 添加这句

#或者
%sudo    ALL=(ALL:ALL) NOPASSWD: ALL
```
centos:
```shell
#  %wheel        ALL=(ALL)       NOPASSWD: ALL
andy    ALL=(ALL)       NOPASSWD: ALL

```
## ubuntu dpkg lock
### 找出进程
```shell
sudo lsof /var/lib/dpkg/lock
```

### 杀死该进程
```shell
kill -9 pid
```

### 删除lock
```shell
sudo rm /var/lib/dpkg/lock
```
### 修复
```shell
sudo dpkg --configure -a
```

## 手动安装 zsh
### 步驟
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
![终端字体](vimages/20200205235123141_2540.png =672x)

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

如果windows 安装会出现python报错:
将78~88修改为：
```python
sep = '\\\\' if os.sep == '\\' else os.sep
regex_no_sep = '[^' + sep + ']*'
regex_no_sep_end = regex_no_sep + '$'
regex_one_sep = regex_no_sep + sep + regex_no_sep
```
ref：<http://leetschau.github.io/autojump-in-windows-console.html> 




## zsh 一键安装脚本
```shell
#!/bin/bash
#        Author Andy963 
#        repo:
#        install zsh oh-my-zsh by oneKey
#        support ubuntu & centos & macOS
#

install_autojump(){
        # 安装 autojump
        git clone git://github.com/joelthelion/autojump.git /tmp/.autojump && cd /tmp/.autojump
        ./install.py
        rm -rf /tmp/.autojump
}

install_ubuntu(){

        # apt-get install sudo -y
        sudo apt-get update -y
        sudo apt-get install tmux -y
        sudo apt-get install git -y
        sudo apt-get install git -y 
        sudo apt-get install curl -y 
        sudo apt-get install zsh -y

        #optional
        #sudo apt-get install terminator -y 
        sudo apt-get install vim -y 
        sudo apt-get install python-pip -y

        install_autojump
        echo "[!] need to add autojump in ~/.zshrc plugin and logoff manually!"
}


install_centos(){

        sudo yum update -y
        sudo yum install tmux -y
        sudo yum install git -y
        sudo yum install git -y
        sudo yum install curl -y 
        sudo yum install zsh -y

        #optional
        #sudo yum install terminator -y 
        sudo yum install vim -y 
        sudo yum install python-pip -y

        install_autojump
}

install_macOS(){

        # brew needed
        echo "[+] brew install some dependencies..."

        # brew update && brew upgrade
        brew install git
        brew install curl
        brew install zsh
        brew install tmux

        install_autojump
}


install_dependencies(){
        # 根据系统安装
        if [[ "$OSTYPE" == "linux-gnu" ]]; then
            source /etc/os-release
            echo "OS: ", $ID 
                # linux
            if [ $ID == "centos" ]; then
              install_centos
            elif [ $ID == "ubuntu" ]; then
              install_ubuntu
            else
              echo "[!] cannot support your OS. (not centos or ubuntu)"
              exit
            fi 
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            echo "OS: macOS"
            install_macOS
        else
            echo "[!] cannot support your OS. (not linux or macOS)"
            exit
        fi
}


# need to exit manually
install_zsh(){
        echo "##########################"
        echo "请手动输入 exit 让程序继续!"
        echo "##########################"
        sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
}


config_zshrc(){
        bash_aliases=$(cat ~/.zshrc | grep "~/.bash_aliases")
        if [ -z "$bash_aliases" ];then
          echo "[*] add ~/.bash_aliases in ~/.zshrc"
cat <<EOF  >>~/.zshrc
# add ~/.bash_aliases 
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
EOF
        else
          echo "[*] ~/.bash_aliases exists in ~/.zshrc"
        fi
}


config_dircolors(){
        # only supported for linux
        if [[ "$OSTYPE" == "darwin"* ]]; then
            return
        fi
        # use dircolors
        echo "[*] add ~/.dircolors in ~/.zshrc"
        dircolors -p > ~/.dircolors
cat <<EOF  >>~/.zshrc
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
EOF
}


install_zsh_plugins(){
        # install powerline 字体
        if [ ! -d "$HOME/fonts" ]; then
          git clone https://github.com/powerline/fonts.git --depth=1 $HOME/fonts
          cd fonts/
          ./install.sh
          cd ..
          rm -rf fonts
        else
          echo "fonts folder exists..."
        fi

        # install zsh-autosuggestions
        if [ ! -d "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions" ]; then
          git clone git://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
          echo "source ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc 
        else
          echo "[*] ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions exists..."
        fi

        # install zsh-syntax-highlighting
        if [ ! -d "${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting" ]; then
          git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
          echo "source ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc
        else
          echo "[*] ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting exists...."
        fi

}


change_zsh_bash_history(){

cat <<EOF >>~/.zshrc
HISTFILE="\$HOME/.zsh_history"
HISTSIZE=10000
SAVEHIST=10000
EOF

}

config_change_default_shell(){
        # change zsh to default shell
        sudo chsh -s /bin/zsh
        chsh -s /bin/zsh
}

install_done(){
        echo "[!] need to add autojump in ~/.zshrc plugin and logoff manually!"
        echo "######################################################################"
        echo "在.zshrc中修改"
        echo '修改主题：ZSH_THEME="agnoster"'
        echo "添加刚安装的插件：plugins=(git autojump zsh-autosuggestions zsh-syntax-highlighting)"
        echo "[*] enjoy it!"
        echo "######################################################################"
        /bin/zsh
}

install_dependencies
install_zsh
config_zshrc
config_dircolors
install_zsh_plugins
change_zsh_bash_history
config_change_default_shell
install_done

# uninstall
# rm -rf ~/.oh-my-zsh
```


## ssh config

```shell
Host github.com
    HostName www.github.com
    User Andy963
    IdentityFile ~/.ssh/git_id_rsa
    PreferredAuthentications publickey

Host gitee.com
    HostName www.gitee.com
    User Andy963
    IdentityFile ~/.ssh/git_id_rsa
    PreferredAuthentications publickey


Host centos
    HostName 192.168.16.8
    Port 22
    User root
    IdentityFile ~/.ssh/id_rsa
    PreferredAuthentications publickey

 Host gtw
    HostName 35.185.130.100
    Port 22
    User root
    IdentityFile ~/.ssh/id_rsa
    PreferredAuthentications publickey

 Host england
    HostName 89.107.59.180
    Port 22
    User root
    IdentityFile ~/.ssh/id_rsa
    PreferredAuthentications publickey

 Host vm
    HostName 198.23.200.188
    Port 5188
    User root
    IdentityFile ~/.ssh/id_rsa
    PreferredAuthentications publickey


 Host vm_site
    HostName 107.175.197.137
    Port 5188
    User root
    IdentityFile ~/.ssh/id_rsa
    PreferredAuthentications publickey

 Host vm_small
    HostName 107.174.101.162
    Port 22
    User root
    IdentityFile ~/.ssh/id_rsa
    PreferredAuthentications publickey
```

## linux 内核管理

### 查看当前使用内核
```shell
uname -r 
uname -a 
# ~  uname -a
Linux Andy 5.3.0-28-generic #30~18.04.1-Ubuntu SMP Fri Jan 17 06:14:09 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

### 查看系统中有哪些内核
```shell
dpkg --get-selections | grep linux
# 或者 dpkg --list |grep linux
```

### 删除不必要的内核版本

内核映像文件主要包括以下类型：

linux-image-版本号：内核映像文件

linux-headers-版本号：内核头文件

linux-image-extra-版本号：内核扩展文件
```shell
sudo apt-get purge linux-image-<版本号>
```
### 更新grub文件
```shell
sudo update-grub
```


## 禁止cron pam写入日志

```
vim /etc/pam.d/common-session-noninteractive
文件结尾附件找到
session required        pam_unix.so
前面加上：
session     [success=1 default=ignore] pam_succeed_if.so service in cron quiet use_uid
保存。

service cron restart
```

## 设置服务器支持中文
### 检查本机语言包
```shell
locale -a
```
### 安装语言包
```shell
sudo vim /etc/locale.gen
#将zh_CN.GBK GBK zh_CN.UTF8 UTF8的注释去掉，或者直接添加这两行内容

#下载语言包
sudo locale-gen
```

### 修改默认语言
```shell
sudo dpkg-reconfigure locales
```