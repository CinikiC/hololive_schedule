# hololive_schedule

`hololive_schedule` is a macOS status bar plugin using BitBar. It can help you get the streaming information of hololive members conveniently, just in your status bar.

> BitBar can run your scripts regularly and put the output on your status bar. You can go to [here](https://getbitbar.com/) to install BitBar and know how it works.

![image.png](https://i.loli.net/2020/06/30/AWCIRSb9cB7F46f.png)

## Features

1. Get liveroom information from [hololive offical schedule website](https://schedule.hololive.tv/lives/all), contains live time ( date and time ), liver's name and liveroom link;
2. Classify the liverooms into "Streaming now", "Upcoming" and "Stream over" (from hololive offical schedule website and YouTube liveroom). The liverooms which are streaming will be at the top and have marks;
3. Auto detect the user's timezone and display the accurate time (not in default Tokyo time).

## How to use

1. [Install BitBar](https://getbitbar.com/) and run it once to set the plugins folder;
2. Download the script and copy it at the plugins folder;
3. Refresh the plugin in your status bar and enjoy it.

## 注意事项

1. Need Python3 or above ;
2. Need `bs4` and `requests` packages, you can install them with `pip3 install bs4 requests` ;
3. If your `python3` is not at `/usr/local/bin/python3` , you might need to change the python3 interpreter's path at the first line of the script;
4. You can rename the script as `hololive_schedule.{xxx}.py` to let BitBar run the script with a custom time interval. For example, `hololive_schedule.90s.py` means run the script every 90s;
5. Because there are many URLs to get, the script might need a little long time to run. On my device and network environment (MacBook Air 2018 & **CANNOT** connect to YouTube directly), it will take about 90s to refresh once;
6. You will need a proxy if you cann't get access to YouTube directly;
7. Beacuse there are only YouTube liveroom links on the hololive offical schedule website, no BiliBili links are provided.