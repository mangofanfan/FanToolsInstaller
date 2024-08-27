from colorama import Fore
from os import getenv, getcwd, remove

import requests
import zipfile


class Main:
    def __init__(self):
        self.dividing = Fore.GREEN + "————————————————" + Fore.RESET

        self._dataFile = getenv("LOCALAPPDATA")
        self._localFile = getcwd()

    def yesNo(self):
        a = input("请输入>>>（Y/N，大小写均可，其他输入均视作N）")
        if a == "Y" or a == "y":
            return True
        else:
            return False

    def run(self):
        """
        程序入口。
        :return:
        """
        print(self.dividing)
        print(Fore.YELLOW + "您正在操作的是" + Fore.BLUE + "芒果工具箱" + Fore.YELLOW + "的命令行安装工具！")
        print("我们需要在您的计算机上做一些准备工作，然后您便可以与工具箱见面。")
        print("这是完整安装流程，您必须过目每一个步骤方可完成安装。另外，您可能需要暂时关闭正在运行的网络代理工具，以确保下载顺利。")
        print("本安装工具也是开源哒，没有病毒哒！")
        print(Fore.RED + "在接下来的每一个步骤中，您都需要输入Y或N来确认或取消，Y将进入下一步，N将返回上一步。")
        print(self.dividing)
        print(Fore.CYAN + "查看我们（安装工具）将要进行的操作")
        a = self.yesNo()
        if a is True:
            self.guide()
        else:
            self.run()
        return None

    def guide(self):
        print(self.dividing)
        print(Fore.YELLOW + "为压缩工具箱本体的体积，工具箱引用的部分资源文件以外部文件的形式使用，同时工具箱也需要一个数据文件夹。")
        print("我们会将工具箱的数据文件夹放置在您的用户下的AppData中，无论您从本机何处启动工具箱实例，都可以同步工具箱的数据。")
        print(Fore.MAGENTA + "您也可以将工具箱扔到一个FanTools目录下，如果数据齐全，工具箱应当会使用目录中的数据，而非您用户下存储的数据。")
        print("在数据下载创建完毕后，我们将为您下载工具箱本体至当前目录下。")
        print(self.dividing)
        print(Fore.CYAN + "将进行操作：下载并创建数据、下载工具箱本体。确认以继续。")
        a = self.yesNo()
        if a is True:
            self.installData()
        else:
            self.guide()
        return None

    def installData(self):
        print(self.dividing)
        print(Fore.CYAN + "开始下载数据压缩包，请耐心等待……")
        try:
            self._downloadData()
            print(Fore.GREEN + "下载完成并且没有报错，也许成功了吧！")
        except Exception as e:
            print(Fore.RED + "下载过程中发生报错，以下是报错详细信息：")
            print(self.dividing)
            print(e)
            print(self.dividing)
            print(Fore.RED + "建议您将报错信息反馈至安装工具的GitHub仓库，或在上面寻找解决方案……")
            input("输入任意内容以退出……")
            return None

        print(Fore.CYAN + "解压并安装数据……")
        try:
            self._copyData()
            print(Fore.GREEN + "数据安装完成，并清除下载文件。")
        except Exception as e:
            print(Fore.RED + "处理数据过程中发生报错，以下是报错详细信息：")
            print(self.dividing)
            print(e)
            print(self.dividing)
            print(Fore.RED + "建议您将报错信息反馈至安装工具的GitHub仓库，或在上面寻找解决方案……")
            input("输入任意内容以退出……")
            return None

        print(Fore.CYAN + "数据安装完毕，接下来准备下载工具箱本体。")
        print(self.dividing)
        a = self.yesNo()
        if a is True:
            self.downloadExe()
        else:
            self.installData()
        return None

    def downloadExe(self):
        print(self.dividing)
        print("开始下载工具箱本体……")
        try:
            self._downloadExe()
            print(Fore.GREEN + "下载完成并且没有报错，也许成功了吧！")
        except Exception as e:
            print(Fore.RED + "下载过程中发生报错，以下是报错详细信息：")
            print(self.dividing)
            print(e)
            print(self.dividing)
            print(Fore.RED + "建议您将报错信息反馈至安装工具的GitHub仓库，或在上面寻找解决方案……")
            input("输入任意内容以退出……")
            return None
        print("工具箱下载完成！")
        print(self.dividing)
        a = self.yesNo()
        if a is True:
            self.finish()
        else:
            self.downloadExe()
        return None

    def finish(self):
        print(self.dividing)
        print(Fore.MAGENTA + "安装已经完成，目录下应当出现名为「芒果工具箱.exe」的应用程序。")
        print("您可以将该程序转移、复制到本机的任何位置，均不影响使用。")
        print(Fore.YELLOW + "如果您需要向其他人介绍工具箱，请分享本「命令行安装工具」而不是直接分享「工具箱程序」哦！")
        print(Fore.GREEN + "安装工具已完成运行，输入任意内容以退出。")
        input()
        return None

    def _downloadData(self):
        res = requests.get("https://file.mangofanfan.cn/s/2rnz7i", stream=True)
        with open(self._localFile + "/FanTools.zip", "wb") as f:
            for bl in res.iter_content(chunk_size=1024):
                if bl:
                    f.write(bl)
        return None

    def _copyData(self):
        zipfile.ZipFile(self._localFile + "/FanTools.zip", 'r').extractall(self._dataFile)
        remove(self._localFile + "/FanTools.zip")
        return None

    def _downloadExe(self):
        res = requests.get("https://file.mangofanfan.cn/s/kmpnbp", stream=True)
        with open(self._localFile + "/芒果工具箱.exe", "wb") as f:
            for bl in res.iter_content(chunk_size=1024):
                if bl:
                    f.write(bl)
        return None


if __name__ == '__main__':
    main = Main()
    main.run()
