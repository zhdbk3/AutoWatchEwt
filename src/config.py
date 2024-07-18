import json

with open('config.json', 'r') as f:
    config = json.load(f)
browser_name: str = config['browser_name']
driver_path: str = config['driver_path']
lesson_list_url: str = config['lesson_list_url']
username: str = config['username']
password: str = config['password']


def print_config() -> None:
    print('读取到配置：')
    print('浏览器名称', 'browser_name:', browser_name)
    print('驱动路径', 'driver_path:', driver_path)
    print('课程列表链接', 'lesson_list_url:', lesson_list_url)
    print('用户名', 'username:', '*' * len(username))
    print('密码', 'password:', '*' * len(password))


if __name__ == '__main__':
    print_config()
