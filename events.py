import data_store



def add_event(code, name, club, date, time, room, capacity):

 reservation_key = (room, date, time)

 if reservation_key in data_store.reservations:

    print("Zaten ilgili oda, tarih ve zaman içerisinde başka bir etkinlik bulunuyor.")

    return



 data_store.events[code] = {

    "name": name,

    "club": club,

    "date": (date, time),

    "room": room,

    "capacity": capacity,

    "participants": set()

 }



 data_store.reservations.add(reservation_key)

 print("Etkinlik oluşturuldu.")



def register(id, event_code):

 student = data_store.students.get(id)

 event = data_store.events.get(event_code)



 if not student:

    print("Öğrenci maalesef bulunamadı.")

    return

 elif not event:

    print("Etkinlik maalesef bulunamadı.")

    return



 elif len(event["participants"]) >= event["capacity"]:

    print("Hata, bu etkinlik tamamen dolu.")

    return



 student["events"].add(event_code)

 event["participants"].add(id)

 print("Etkinliğe başarıyla kayıt oluşturuldu.")







def cancel_registration(id, event_code):

 student = data_store.students.get(id)

 event = data_store.events.get(event_code)



 if student and event and (event_code in student["events"]):

        student["events"].remove(event_code)

        event["participants"].remove(id)

        print(f"Kayıt iptal edildi: {id} -> {event_code}")

 else:

    print("Hata: Kayıt bulunamadı.")



def list_events():

    """Tüm etkinlikleri döndürür."""

    return list(data_store.events.values())