from django.shortcuts import render
from datetime import datetime  # 日付を取得するためのモジュールをインポート
# Create your views here.


def indexView(request):
    '''
    index.htmlを表示するプログラム
    '''
    today = datetime.now().strftime("%m-%d")  # 今日の日付を取得

    # 今日がクリスマスだったら"YES"、それ以外なら"NO"を、変数"isItChristmas"格納する.
    isItChristmas = "YES" if today == "12-25" else "NO"

    # Djangoテンプレートをレンダリング
    # 'context'はDjangoテンプレートに渡すPythonオブジェクト
    return render(request, 'index.html', context={'isItChristmas': isItChristmas})
