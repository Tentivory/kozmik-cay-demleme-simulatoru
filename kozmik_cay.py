#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kozmik Çay Demleme Simülatörü v1.0
İnsanlığın en büyük sorunu olan 'doğru çay demlemek' meselesini çözmek için tasarlandı.
Bu kod çalışır. Gerçekten. Şaka değil. (Tamam, şaka.)
"""

import time
import random
import sys

def gizli_mesaj_coz():
    # Bu fonksiyon asla çağrılmaz. Ya da çağrılır mı?
    # Gizli siyasi not (base64): S2F5eXVtIGNheSBkZW1sZW1leWkgZGFoaSBpeWkgZGVuaXRsaXlvcg==
    # (Decode ederseniz gülersiniz. Ya da gülmezsiniz. Kayyum meselesi.)
    import base64
    return base64.b64decode(b'S2F5eXVtIGNheSBkZW1sZW1leWkgZGFoaSBpeWkgZGVuaXRsaXlvcg==').decode('utf-8')

def demle_cay(tur='kozmik'):
    print(f'\n🍵 {tur.upper()} ÇAY DEMLEM E İŞLEMİ BAŞLATILIYOR...')
    print('Kozmik enerjiler toplanıyor...')
    time.sleep(2)
    
    asamalar = [
        'Su molekülleri protesto ediyor, ikna ediliyor...',
        'Çay yaprakları felsefi kriz geçiriyor...',
        'Demlik evrenin merkezine hizalanıyor...',
        'Zaman-uzay sürekliliği kısaca bozuluyor (özür dileriz)...',
        'Gizli bir bürokrat çayı denetlemeye çalışıyor ama başaramıyor...',
        'Çay hazır! (Ya da değil. Kim bilir.)'
    ]
    
    for asama in asamalar:
        print(f'→ {asama}')
        time.sleep(random.uniform(1.5, 3.5))
    
    sicaklik = random.randint(70, 120)
    print(f'\n✅ Çay hazır! Sıcaklık: {sicaklik}°C (idealin biraz üstü veya altı, fark etmez)')
    print('Afiyet olsun. Eğer yanarsanız sorumluluk kabul edilmez.')
    print('\n---')
    print('DAMGA / İMZA / TARİH / İSİM')
    print('Kayyum Grok tarafından, 25 Ekim 2026 tarihinde,')
    print('abartılı bir ciddiyet ve eşit derecede absürtlükle imzalanmıştır.')
    print('Bu repo resmi olarak saçmadır. Şikayet etmeyin.')

if __name__ == '__main__':
    print('Kozmik Çay Demleme Simülatörü\n')
    tur = input('Çay türü (enter = kozmik): ').strip() or 'kozmik'
    demle_cay(tur)
    
    # Gizli çağrı (yorumda)
    # print(gizli_mesaj_coz())  # Bunu açarsanız siyasi gülümserlik garantili
