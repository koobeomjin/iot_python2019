# from ../sound/echo import echo_test
# 위의 코드는 파일 IO 상대경로의 문법은 허용하지 않는다.
from ..sound.echo import echo_test
def render_test():
    print('render')
    echo_test()