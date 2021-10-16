import re

phone_search = r"(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*"
phone_change = r"+7(\2)\3-\4-\5 \6\7"

def change_list(contacts_list):
    new_list = []

    for el in contacts_list:
        full_name = ' '.join(el[:3]).split(' ')
        res = [full_name[0], full_name[1], full_name[2], el[3], el[4], re.sub(phone_search, phone_change, el[5]), el[6]]
        new_list.append(res)

    return deleting_duplicates(new_list)

def deleting_duplicates(contacts):
    final_contacts = []
    directory_dict = {}

    for contact in contacts:
        full_name = ' '.join(contact[:2])

        if full_name not in directory_dict:
            directory_dict[full_name] = contact
        else:
            for i, val in enumerate(directory_dict[full_name]):
                if contact[i] > val:
                    directory_dict[full_name][i] = contact[i]

    for person_info in directory_dict.values():
        final_contacts.append(person_info)

    return final_contacts