import data_store



def add_student(id, name, department, grade, clubs):

    if id in data_store.students:

        print("Hata, girmiş olduğunuz öğrencinin kaydı sistemde bulunmaktadır.")

        return





    data_store.students[id] = {

        "name": name,

        "department": department,

        "grade" : grade,

        "clubs": set(clubs),

        "events": set()

        }

    print(f"{name} isimli ve {id} numaralı öğrenci başarıyla eklendi.")



def remove_student(id):

    if id in data_store.students:

        del data_store.students[id]

        print("Öğrenci silindi.")

    else:

        print("Bu öğrenci zaten bulunmuyor.")



def get_student(id):

    return data_store.students.get(id)



def list_students():

    return list(data_store.students.values())