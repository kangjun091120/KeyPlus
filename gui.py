import webview

window = webview.create_window(
    title='百度一下,全是广告',
    url='http://www.baidu.com',
)
webview.start(gui='qt')

