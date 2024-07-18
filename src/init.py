import config


def init() -> None:
    print('开源仓库：https://github.com/zhdbk3/AutoWatchEwt | 开源协议：GPL-3.0 license')
    print('# 自动观看e网通视频')
    print('**:warning:警告：本项目仅用于学习`Python`技术，请勿用于完成学校作业！**')
    print('**开始使用本程序即代表您同意'
          '项目作者[MC着火的冰块](https://space.bilibili.com/551409211)不为您的行为承担任何责任。**')
    print('=' * 100)
    print('请确保已正确配置配置文件')
    config.print_config()


if __name__ == '__main__':
    init()
