import uuid, pytz, io
import base64
import matplotlib
import japanize_matplotlib
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import VTD, VTDlog, Claims, Messages, Trades, AppClaims
from .forms import ClaimForm, GraphForm
from . import api
from django.contrib import messages as msgs
from django.core.handlers.wsgi import WSGIRequest

matplotlib.use("Agg")

# Create your views here.
@login_required
def Index(request: WSGIRequest):
    my_data = list(VTD.objects.filter(user=request.user))
    app_claims = list(AppClaims.objects.filter(target_user=request.user))
    claims = list(Claims.objects.filter(to_user=request.user))
    is_created = my_data != []
    if is_created:
        api.__PayAllAppClaims__(request.user)
        my_data = my_data[0]
    return render(request, "VTDbank/index.html", {'my_data': my_data, 'app_claims':app_claims, 'claims':claims, 'is_created': is_created})

@login_required
def Admin(request: WSGIRequest):
    vtd_datas = VTD.objects.all()
    return render(request, "VTDbank/admin.html", {'vtd_datas': vtd_datas})

@login_required
def Register(request: WSGIRequest):
    response = {
        'is_created': False
    }
    status = 200
    if request.method == 'POST':
        if VTD.objects.filter(user=request.user.id).count() == 0:
            VTD.objects.create(value=1000, user=request.user)
            return redirect('VTDbank:index')
        else:
            response['ERROR'] = 'conflict'
            status = 409
    else:
        response['ERROR'] = 'method not allowed'
        status = 405
    return JsonResponse(response, status=status)

@login_required
def Graph(request: WSGIRequest):
    def plt2png():
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=200, bbox_inches='tight', transparent=True)
        s = buf.getvalue()
        buf.close()
        g = base64.b64encode(s).decode()
        return g
    graph = ""
    form = GraphForm()
    if request.method == "POST":
        form = GraphForm(request.POST)
        
        if form.is_valid():
            logs = list(VTDlog.objects.filter(user=request.user.id).order_by("timestamp"))
            current_tz = pytz.timezone(form.cleaned_data['tz'])
            days = [log.timestamp.astimezone(current_tz).date().strftime("%m/%d") for log in logs]
            money = [log.amount for log in logs]
            lv = {}
            for date, value in zip(days, money):
                lv[date] = value
            plt.xlabel("日付", {"fontsize":10})
            plt.ylabel("所持金", {"fontsize":10})
            plt.plot(list(lv.keys())[-10:], list(lv.values())[-10:])
            graph = plt2png()
            plt.cla()
    return render(request, "VTDbank/graph.html", {'graph': graph, 'form': form})

@login_required
def AllGraph(request: WSGIRequest):
    def plt2png():
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=200, bbox_inches='tight', transparent=True)
        s = buf.getvalue()
        buf.close()
        g = base64.b64encode(s).decode()
        return g
    logs = list(VTDlog.objects.filter(user=request.user.id).order_by("timestamp"))
    money = [log.amount for log in logs]
    plt.ylabel("所持金", {"fontsize":10})
    plt.plot(money)
    graph = plt2png()
    plt.cla()
    return render(request, "VTDbank/graph.html", {'graph': graph})

@login_required
def Claim(request: WSGIRequest):
    form = ClaimForm()
    instance = Claims()
    if request.method == "POST":
        form = ClaimForm(request.POST, instance=instance)
        if form.is_valid():
            if instance.to_user.id == request.user.id:
                msgs.error(request, "請求先に自分を指定することはできません。")
            else:
                record = form.save(commit=False)
                record.from_user = request.user
                record.save()
                message = Messages(
                    user=instance.to_user,
                    message=f"{request.user.account_id}から請求が届きました。\n請求金額:{format(instance.amount,',')} VTD"
                    )
                message.save()
                msgs.success(request, "請求が作成されました。")
    return render(request, 'VTDbank/claim.html', {'form': form})

@login_required
def PayClaim(request: WSGIRequest, id):
    try:
        claim = Claims.objects.filter(id=id)[0]
        if request.method == "POST" and claim != None:
            if claim.to_user == request.user:
                currentVTD = VTD.objects.filter(user=request.user)[0].value
                if currentVTD >= claim.amount:
                    # それぞれのユーザーのVTDアカウントを取得
                    from_user = VTD.objects.filter(user=claim.from_user)[0]
                    to_user = VTD.objects.filter(user=claim.to_user)[0]
                    # 取引idの生成
                    trade_id = uuid.uuid4()
                    # 取引ログの保存
                    trade = Trades(
                        trade_id=trade_id,
                        from_user=claim.from_user,
                        to_user=claim.to_user,
                        amount=claim.amount,
                    )
                    trade.save()
                    # 請求の処理
                    from_user.value += claim.amount
                    to_user.value -= claim.amount
                    from_user.save()
                    to_user.save()
                    # 金額ログの保存
                    api.__CreateLog__(claim.from_user, from_user.value, trade_id, "プレイヤー間取引")
                    api.__CreateLog__(claim.to_user, to_user.value, trade_id, "プレイヤー間取引")
                    # 請求の削除
                    claim.delete()
    except IndexError:
        pass
    return redirect('VTDbank:index')

# @login_required
# def PayAppClaim(request: WSGIRequest, id):
#     claim = AppClaims.objects.filter(id=id)[0]
#     if request.method == "POST" and claim != None:
#         if claim.target_user == request.user:
#             currentVTD = VTD.objects.filter(user=request.user)[0].value
#             if currentVTD >= claim.amount:


@login_required
def Logs(request: WSGIRequest):
    logs = VTDlog.objects.filter(user=request.user)
    return render(request, 'VTDbank/logs.html', {'logs': logs})

# @login_required
# def ClaimAPI(request: WSGIRequest):
#     # userid: int, amount: int, auto: bool = True
#     form = AppClaimForm()
#     claims = AppClaims()
#     if request.method == "POST":
#         form = AppClaimForm(request.POST, instance=claims)
#         if form.is_valid():
#             currentVTD = VTD.objects.filter(user=request.user)[0].value