Title: How To Uninstall Ubuntu Touch And Restore Android
Category: General
Date: 2017-04-21 21:04
Modified: 2017-04-21 21:04
Slug: how-to-restore-android

Hi! Today I would like to share a small cheat sheet on how to uninstall Ubuntu
Touch and restore Android on your smartphone. 

Firstly, find and download a proper Android build from [here][u1]. In my case it
was occam-lmy48t-factory-c43c7cfd.zip since my smarphone is Nexus 4.

Secondly, make sure you have `adb` tool installed. I personnaly use Arch Linux
where this tool is part of android-tools package:

```
$ sudo pacman -S android-tools
```

Now on your smarphone go to System Settings -> About -> Developer Mode and enable
the developer mode. Make sure your smarphone is visiable in `adb devices`:

```
$ adb devices
List of devices attached
04edbc16db97b0a8    device
```

Afterwards say:

```
$ adb reboot bootloader
$ unzip occam-lmy48t-factory-c43c7cfd.zip
$ cd occam-lmy48t
$ sudo ./flash-all.sh
```

That's it!

[u1]: https://developers.google.com/android/images
