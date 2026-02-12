自带的 bash 不太好用，这里推荐 zsh．

## 下载 zsh

Ubuntu 系统使用如下命令下载：

```bash
sudo apt-get install zsh
```

安装后，检查系统可用终端：

```bash
cat /etc/shells
```

## 设置默认终端

这条命令一定要在常用用户下运行，因为它只会修改当前用户的默认终端．

```bash
chsh -s /bin/zsh
```

不建议在 root 用户上使用．

## 配置 zsh

初始运行 zsh 会弹出如下提示：

```plaintext
This is the Z Shell configuration function for new users,
zsh-newuser-install.
You are seeing this message because you have no zsh startup files
(the files .zshenv, .zprofile, .zshrc, .zlogin in the directory
~).  This function can help you with a few settings that should
make your use of the shell easier.

You can:

(q)  Quit and do nothing.  The function will be run again next time.

(0)  Exit, creating the file ~/.zshrc containing just a comment.
     That will prevent this function being run again.

(1)  Continue to the main menu.

(2)  Populate your ~/.zshrc with the configuration recommended
     by the system administrator and exit (you will need to edit
     the file by hand, if so desired).

--- Type one of the keys in parentheses ---
```

这里按 ++0++ 即可，然后 zsh 会创建 `~/.zshrc` 文件，下一次运行将不会出现这个提示．

未配置的 zsh 是很朴素的，而自行配置又较繁琐，因此当然要用已经造好的轮子了！

---

确保本地已经安装 git，使用 curl 下载脚本并运行：

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### 配置样式

这个感觉 `~/.zshrc` 中的注释说的很清晰了：

```plaintext
# Set name of the theme to load --- if set to "random", it will
# load a random theme each time Oh My Zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )
```

从注释中提到的网站中选择一个喜欢的样式并配置即可．

### 配置插件

推荐三个插件：

+ `z` 是文件夹快速跳转插件，对于曾经访问过的文件夹，可以通过文件夹名称（而非路径）访问．
+ `zsh-autosuggestions` 是命令提示插件，基于曾经输入的命令进行推荐；
+ `zsh-syntax-highlighting` 是命令语法检查插件；

先将插件下载到插件目录下（`z` 无需下载）：

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
```

然后在 `~/.zshrc` 中添加：

```ini
plugins = (
    # other plugins...
    z
    zsh-autosuggestions
    zsh-syntax-highlighting
)
```
