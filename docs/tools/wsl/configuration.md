## 建立用户

现在可以运行 `wsl` 进入子系统．

然而，此时默认进入 root 用户，一般认为这是不安全的．

使用 `adduser` 建立新用户：

```bash
adduser <username>
```

一般希望将自己的用户加入 sudu 组：

```bash
usermod -aG sudo <username>
```

也可以考虑使用 `visudo`，这里不展开了．

## 设置默认用户

打开 `/etc/wsl.conf`：

```bash
vi /etc/wsl.conf
```

添加以下内容：

```ini
[user]
default=<username>
```

保存文件，退出 WSL，运行 `wsl --shutdown`．

后文认为你的 WSL 在非 root 用户下运行．
