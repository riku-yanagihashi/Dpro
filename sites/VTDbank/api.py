import uuid
from .models import AppClaims, VTD, VTDlog, Claims

def CreateClaim(app_name :str, user, amount: int):
    """
    アプリケーションからの請求を作成します。

    :app_name(str): 請求元アプリケーション名
    :user(int | Any): 請求先ユーザー
    :amount(int): 請求金額
    """
    user = VTD.objects.filter(user=user)[0]
    currentVTD = user.value
    if (currentVTD < amount):
        claim = AppClaims(
            app_name=app_name,
            target_user=user.user,
            amount=amount
        )
        claim.save()
        return
    user.value -= amount
    user.save()
    __CreateLog__(user.user, currentVTD-amount, desc=f"ページ内請求/{app_name}")

def AddVTD(app_name :str, user, amount: int):
    """
    アプリケーションからVTDを追加します。

    :app_name(str): 請求元アプリケーション名
    :user(int | Any): 請求先ユーザー
    :amount(int): 請求金額
    """
    user = VTD.objects.filter(user=user)[0]
    currentVTD = user.value
    user.value += amount
    user.save()
    __CreateLog__(user.user, currentVTD+amount, desc=f"ページ内振込/{app_name}")


def __CreateLog__(user, amount: int, trade_id: str = None, desc: str = ""):
    vtdlog = VTDlog(
        user=user,
        amount=amount,
        trade_id=trade_id,
        description=desc
    )
    vtdlog.save()

def __PayAllAppClaims__(user):
    claims = list(AppClaims.objects.filter(target_user=user))
    userVTD = VTD.objects.filter(user=user)[0]
    for claim in claims:
        if (userVTD.value>=claim.amount):
            userVTD.value-=claim.amount
            claim.delete()
            __CreateLog__(user, userVTD.value, desc="ページ内請求")
    userVTD.save()

def __PayAllClaims__(user):
    claims = list(Claims.objects.filter(to_user=user))
    userVTD = VTD.objects.filter(user=user)[0]
    for claim in claims:
        if (userVTD.value>=claim.amount):
            userVTD.value-=claim.amount
            claim.delete()
            __CreateLog__(user, userVTD.value, desc="ページ内請求")
    userVTD.save()