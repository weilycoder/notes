## 配置虚拟化功能

```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all
```

相关配置可以通过以下命令关闭：

```bash
dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux /norestart
dism.exe /online /disable-feature /featurename:VirtualMachinePlatform /norestart
```

更改完成后，重启计算机以使更改生效．

## 安装 WSL 发行版

通常情况下，可以在终端直接运行：

```bash
wsl --install
```

然而，由于网络问题，有时可能失效，此时可以尝试从 Github 直接下载．

- [WSL Latest Releases](https://github.com/microsoft/WSL/releases/latest)

## 安装 Linux 发行版

以 Ubuntu 22.04 LTS 为例．

### 从 Microsoft Store 下载

- [Ubuntu 22.04.5 LTS](https://apps.microsoft.com/detail/9pn20msr04dw)

这个我没试过．

### 从官方镜像下载

- [Jammy Jellyfish](https://cloud-images.ubuntu.com/wsl/jammy/current/)

然后使用 `wsl --import` 命令，具体命令参数含义可以使用 `wsl --help` 查看，这里提供一个示例：

```bash
wsl --import Ubuntu D:/WSL/Ubuntu22.04 ./ubuntu-jammy-wsl-amd64-ubuntu22.04lts.rootfs.tar.gz --version 2
```
