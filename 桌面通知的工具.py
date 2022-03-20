from win10toast import ToastNotifier
import time
import datetime
from threading import Timer

# 初始化通知模块
toaster = ToastNotifier()
print("程序开始运行")


# 通知时间为25分钟

# 番茄钟提醒时间 #设置番茄时间
def pomodoro_work():  # 工作
    time_min = float(25)
    Pomodoro = time_min * 60

    header, text = push_content()
    text = text + '\n' + '专注时间开始。'
    desk_inform(header, text)

    timer = Timer(Pomodoro, pomodoro_rest)
    timer.start()
def pomodoro_rest():  # 休息
    time_min = float(5)
    Pomodoro = time_min * 60

    header, text = push_content()
    text = text + '\n' + '专注时间结束，休息五分钟。'
    desk_inform(header, text)

    timer = Timer(Pomodoro, pomodoro_work)
    timer.start()


# 输入标题和内容两个参数 推送通知，
def desk_inform(header, text):
    toaster.show_toast(f"{header}", f"{text}", duration=100, threaded=True, icon_path='favicon.ico')
    while toaster.notification_active():
        time.sleep(0.005)

# 定义推送内容：
def push_content(LeaveWorkTime='17:30', IntoWorkTime='8:30'):
    # 今年年份=time.strftime("%Y")
    NowYera = time.strftime("%Y")
    # 当前日期
    NowDate = datetime.datetime.strptime(time.strftime("%Y年%m月%d日"), "%Y年%m月%d日")
    # 明年的1月1日
    NextYear = datetime.datetime.strptime(str((int(time.strftime("%Y")) + 1)), "%Y")
    # 本年度剩余的天数
    NowDateRemaining = (NextYear - NowDate).days

    # 获得标题
    header = '\n今天是本年' + str(time.strftime("的第%j天,距离")) + str(int(NowYera) + 1) + "还剩" + str(NowDateRemaining) + '天。'

    # 上下班事件
    NowTime = datetime.datetime.strptime(time.strftime("%H:%M"), "%H:%M")  # 现在时间
    # 参数为下班时间：
    LeaveWork = datetime.datetime.strptime(LeaveWorkTime, "%H:%M")  # 下班时间
    # 参数为上班时间：
    IntoWork = datetime.datetime.strptime(IntoWorkTime, "%H:%M")  # 上班事件

    DistLeaveWork = str((LeaveWork - NowTime).seconds / 60)  # 距离上班时间
    DistIntoWork = str((NowTime - IntoWork).seconds / 60)  # 距离下班时间

    # 获得内容
    text = "现在是" + str(time.strftime("%H:%M")) + "分。距离下班还有" + DistLeaveWork + "分钟。"
    text2 = "现在是" + str(time.strftime("%H:%M")) + "分。已经上班" + DistIntoWork + "分钟。"
    print(header, '\n', text, '\n', text2)
    return header, text



if __name__ == '__main__':
    pomodoro_work()
