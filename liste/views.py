from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseForbidden
from .models import Gorev

def kullanici_giris(request):
    if request.method == 'POST':
        kullanici_adi = request.POST.get('kullanici_adi')
        sifre = request.POST.get('sifre')
        kullanici = authenticate(request, username=kullanici_adi, password=sifre)
        if kullanici:
            login(request, kullanici)
            # Otomatik giriş (session hatırlansın)
            request.session.set_expiry(60 * 60 * 24 * 365)  # 365 gün açık kalsın
            return redirect('anasayfa')
        else:
            return render(request, 'giris.html', {'hata': 'Kullanıcı adı veya şifre hatalı.'})
    return render(request, 'giris.html')


def kullanici_kayit(request):
    return HttpResponseForbidden("Kayıt olma özelliği devre dışı bırakılmıştır.")

# def kullanici_kayit(request):
#     if request.method == 'POST':
#         kullanici_adi = request.POST.get('kullanici_adi')
#         sifre = request.POST.get('sifre')
#         if not User.objects.filter(username=kullanici_adi).exists():
#             User.objects.create_user(username=kullanici_adi, password=sifre)
#             return redirect('giris')
#         else:
#             return render(request, 'kayit.html', {'hata': 'Bu kullanıcı adı zaten alınmış.'})
#     return render(request, 'kayit.html')

def kullanici_cikis(request):
    logout(request)
    return redirect('giris')



@login_required(login_url='giris')
def anasayfa(request):
    gorevler = Gorev.objects.all().order_by('-olusturulma_tarihi')

    if request.method == 'POST':
        if 'yeni_gorev' in request.POST:
            baslik = request.POST.get('baslik')
            aciklama = request.POST.get('aciklama')
            if baslik:
                Gorev.objects.create(baslik=baslik, aciklama=aciklama)
        elif 'tamamla' in request.POST:
            gorev_id = request.POST.get('gorev_id')
            gorev = Gorev.objects.get(id=gorev_id)
            gorev.tamamlandi = True
            gorev.yapilma_tarihi = timezone.now()
            gorev.save()
        elif 'sil' in request.POST:
            gorev_id = request.POST.get('gorev_id')
            Gorev.objects.get(id=gorev_id).delete()
        return redirect('anasayfa')

    return render(request, 'anasayfa.html', {'gorevler': gorevler})
