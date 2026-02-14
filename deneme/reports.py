import data_store



def popular_events():

    siraliEtkinlikler = sorted(

        data_store.events.values(),

        key = lambda x: len(x["participants"]),

        reverse = True

    )

    return siraliEtkinlikler



def active_students():

    siraliOgrenciler = sorted(

        data_store.students.values(),

        key = lambda x: len(x["events"]),

        reverse=True

    )

    return siraliOgrenciler



def club_statistics():

   

    istatistik = {}

   

    for event in data_store.events.values():

        club = event["club"]

        participant_count = len(event["participants"])

       

        if club not in istatistik:

            istatistik[club] = {"event_count": 0, "total_participants": 0}

       

        istatistik[club]["event_count"] += 1

        istatistik[club]["total_participants"] += participant_count

       

    return istatistik