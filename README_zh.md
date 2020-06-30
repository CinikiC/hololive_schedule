# hololive_schedule

`hololive_schedule` 是一个依靠 BitBar 工作的 macOS 状态栏插件，它可以定期获取 hololive 成员们的直播日程并显示在状态栏菜单中，方便各位单推人及时获取直播信息。

> BitBar 是一个可以定期自动执行脚本并在状态栏显示输出的 macOS 工具，您可以前往 https://getbitbar.com/ 安装 BitBar 并详细了解 BitBar 的工作原理。

![image.png](https://i.loli.net/2020/06/30/AWCIRSb9cB7F46f.png)

## 特性

1. 自动获取主播的开播时间和直播间链接（从 hololive 官方提供的[日程表网站](https://schedule.hololive.tv/lives/all)中爬取），在菜单中点击相应条目即可打开浏览器跳转到直播间；
2. 自动识别直播间状态（从官方日程表网站和 YouTube 爬取），并按「正在直播」、「预定开播」和「已结束」分类显示，正在直播的直播间会显示在顶部并有醒目的标志提示；
3. 自动识别时区，按照用户所在时区显示直播开始时间。

## 使用方法

1. [安装 BitBar](https://getbitbar.com/) ，至少运行一次以指定插件文件夹位置；
2. 下载仓库中的 Python 脚本，拷贝到 BitBar 的插件目录下；
3. 在状态栏中刷新插件，即可正常工作。

## 注意事项

1. 脚本运行需要 Python3 及以上版本；
2. 需要安装 `bs4` 和 `requests` 两个库，可以使用 `pip3 install bs4 requests` 来安装；
3. 如果您的 python3 解释器的位置不是 `/usr/local/bin/python3` ，可能需要在脚本第一行更改 python3 解释器的位置才可以正常工作；
4. 可以更改脚本定时执行的时间间隔，只需要把文件名修改为 `hololive_schedule.{xxx}.py` 即可，其中 `{xxx}` 就是定时执行的时间间隔，建议以秒或分为单位。例如 `90s` 代表 90 秒钟执行一次；
5. 由于脚本需要爬取多个 URL ，脚本刷新完成的时间需要视网络状况而定，可能需要大约 90 秒的时间（作者测试）；
6. 由于脚本需要爬取 YouTube 链接，无法访问 YouTube 的地区需要自行准备代理工具；
7. 由于 hololive 的日程表网站只提供所有直播间的 YouTube 链接，所以暂时无法提供 BiliBili 的转播链接。