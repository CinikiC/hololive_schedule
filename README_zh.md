# hololive_schedule

`hololive_schedule` 是一个依靠 BitBar 工作的 macOS 状态栏插件，它可以定期获取 hololive 成员们的直播日程并显示在状态栏菜单中，方便各位单推人及时获取直播信息。

> BitBar 是一个可以定期自动执行脚本并在状态栏显示输出的 macOS 工具，您可以前往 https://getbitbar.com/ 安装 BitBar 并详细了解 BitBar 的工作原理。

![a6opC9.png](https://s1.ax1x.com/2020/08/06/a6opC9.png)

[GIF 演示](https://s1.ax1x.com/2020/07/13/UJLbdA.gif)

## 特性

1. 只需要几秒钟就可以自动获取主播的开播时间和直播间链接（从 hololive 官方提供的[日程表网站](https://schedule.hololive.tv/lives/all)中爬取），在菜单中点击相应条目即可打开浏览器跳转到直播间；
2. 自动识别直播间状态（从官方日程表网站爬取），并按「正在直播」、「预定开播」和「已结束」分类显示，正在直播的直播间会显示在顶部并有醒目的标志提示；
3. 自动识别时区，按照用户所在时区显示直播开始时间。

## 使用方法

1. [安装 BitBar](https://getbitbar.com/) ，至少运行一次以指定插件文件夹位置；
2. 下载仓库中的 Python 脚本，拷贝到 BitBar 的插件目录下；
3. 在状态栏中刷新插件，即可正常工作。

## 关于 Windows 用户

由于 Windows 平台上没有类似 BitBar 这样的工具，因此 Windows 用户就没有通过任务栏菜单来使用这个脚本的体验了。不过你仍然可以直接在终端中运行这个脚本（只要正确配置了 Python3 并安装了 `bs4` 和 `requests` 这两个模块）。直接在终端中执行脚本也可以得到一样的输出。

## 注意事项

1. 脚本运行需要 Python3 及以上版本；
2. 需要安装 `bs4` 和 `requests` 两个库，可以使用 `pip3 install bs4 requests` 来安装；
3. 如果您的 python3 解释器的位置不是 `/usr/local/bin/python3` ，可能需要在脚本第一行更改 python3 解释器的位置才可以正常工作；
4. 可以更改脚本定时执行的时间间隔，只需要把文件名修改为 `hololive_schedule.{xxx}.py` 即可，其中 `{xxx}` 就是定时执行的时间间隔，建议以秒或分为单位。例如 `90s` 代表 90 秒钟执行一次；
5. ~~由于脚本需要爬取多个 URL ，脚本刷新完成的时间需要视网络状况而定，可能需要大约 90 秒的时间（作者测试）；~~
6. ~~由于脚本需要爬取 YouTube 链接，无法访问 YouTube 的地区需要自行准备代理工具；~~
7. 由于 hololive 的日程表网站只提供所有直播间的 YouTube 链接，所以暂时无法提供 BiliBili 的转播链接；
8. 你可能需要为脚本修改权限 `chmod +x hololive_schedule.py` 后脚本才能正常工作。

## 更新记录

### 2020-7-13

1. 现在可以显示每个 hololive 成员的应援标识了 (emoji)；
2. 增加了直接前往官方日程表网站的选项。

### 2020-8-5

1. 现在不需要爬取 YouTube 的链接也可以完整地得到所有直播间的状态了。这意味着一次刷新的时间可以从原来的 90 秒左右加快至几秒钟，同时无法直接访问 YouTube 的地区不需要使用代理了；
2. 添加了一段文字展示上次刷新所用的时间。

### 2020-8-23

增加了 hololive 5 期生的 emoji 信息。

## TODO

1. ~~优化爬取和解析 YouTube 链接的速度；~~
2. 支持 HoloCN 成员 (官方的站点虽然有 HoloCN 列表但是没有任何信息)；
3. 可以爬取 bilibili 直播间链接；
4. 为 Windows 用户提供可用于 Rainmeter 的移植插件。