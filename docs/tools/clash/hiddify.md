我现在使用的 Clash 客户端，功能应该还挺全．

除了一般的代理功能，可以支持 TUN 模式和 ipv6 模式，前者是一种通过创建虚拟网卡实现全局接管流量的技术．

[下载链接 v2.5.7](https://github.com/hiddify/hiddify-app/releases/download/v2.5.7/Hiddify-Windows-Setup-x64.exe)．

这个链接是 Github 的，如果连接不顺利可以尝试 Github 代理．

---

但是这个客户端是不提供代理服务的，需要自行寻找/购买节点．

列举一些我看起来觉得比较靠谱的服务商：

+ [polarisnet](https://t.polarisnet.cloud/#/register?code=LeBGaDbl)

可以在服务商的网站里找到一个叫“订阅链接”的东西，一般复制这个链接之后在 Hiddify 选择 `主页/新的配置文件/从剪贴板粘贴` 即可．

这个订阅链接指向了一堆 base64 编码，解密后可以看到包含一堆网址和神秘 token 的东西，Hiddify 应该就是靠这个连接的．鉴权部分应该也包含在这里了，因此不要泄露这个链接．

然后可以在主页看到一个点击连接的按钮．
