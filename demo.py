import data_store
import events
import reports
import students



students.add_student("25101933", "Deniz", "Felsefe", 3, {"Öğrenci Dayanışma ve Destek"})
students.add_student("25812591", "Barış", "Yapay Zeka Mühendisliği", 2 ,{"AI", "US Volunteers", "Öğrenci Dayanışma ve Destek"})
students.add_student("25931035", "Evrim", "Yazılım Mühendisliği", 2 , {"AI"})
students.add_student("25736019", "Cem", "Tıp", 5 , {"Kardiyoloji Topluluğu", "Nöroloji Topluluğu", "AI"})
students.add_student("25021521", "Rüya", "Bilgisayar Mühendisliği", 3 , {"AI", "US Volunteers"})



events.add_event("AI656", "Yapay Zeka'da Öz Bilincin Güncel Durumu", "AI", "2026-01-05", "15:30", "Amfi 7", 10 )
events.add_event("CL201", "Mekanik Kalbin Vücut Entegrasyonu", "Kardiyoloji Topluluğu", "2026-01-03", "08:00", "Salon C", 150 )
events.add_event("US177", "About Independence Day", "US Volunteers", "2026-07-04", "10:00", "Salon B2", 50 )
events.add_event("US178", "State System in US - Zoom Conference", "US Volunteers", "2026-03-15", "19:00", "Online Zoom Conference", 50 )
events.add_event("ODD510", "Gönüllü Yardımlaşma Konferansı", "Öğrenci Dayanışma ve Destek", "2025-01-25", "14:00", "Salon A", 20 )


events.register("25101933", "ODD510")
events.register("25812591", "ODD510")

events.register("25812591", "AI656")
events.register("25931035", "AI656")
events.register("25021521", "AI656")

events.register("25812591", "US177")
events.register("25736019", "CL201")

print("RAPOR 1: EN POPÜLER ETKİNLİKLER")
for etkinlik in reports.popular_events():
    count = len(etkinlik['participants'])
    print(f"- {etkinlik['name']} (Katılımcı: {count})")


print("RAPOR 2: EN AKTİF ÖĞRENCİLER")
for ogrenci in reports.active_students():
    count = len(ogrenci['events'])
    print(f"- {ogrenci['name']} (Katıldığı Etkinlik Sayısı: {count})")


print("RAPOR 3: KULÜP İSTATİSTİKLERİ")
istatistik = reports.club_statistics()
for club, data in istatistik.items():
    print(f"- {club}: {data['event_count']} Etkinlik, Toplam {data['total_participants']} Katılımcı")


#events.add_event("AI656", "Etkinlik Deneme", "Nöroloji Topluluğu", "2026-01-05", "15:30", "Amfi 7", 10 )