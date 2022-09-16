documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }


def find_people_by_number(documents, num):
    '''this function prints the name of a person using a document number'''
    # list_numbers = []
    # for document in documents:
    #     list_numbers.append(document['number'])
    # if num in list_numbers:
    #     for document in documents:
    #         if document['number'] == num:
    #             print(f'Документ №{num} принадлежит человеку по имени: {document["name"]}')
    # else:
    #     print(f'Ошибка! Документа №{num} нет в списке')
    for document in documents:
        if num == document['number']:
            print(f'Документ №{num} принадлежит человеку по имени: {document["name"]}')
            return
    print(f'Ошибка! Документа №{num} нет в списке')

def find_shelf_by_number(directories, num):
    '''this function prints the number of the shelf using a document number'''
    # for key, value in directories.items():
    #     if num in value:
    #         return print(f'Документ №{num} лежит на полке №{key}')
    # return print(f'Ошибка! Документа №{num} не существует')
    for key, value in directories.items():
        if num in value:
            print(f'Документ №{num} лежит на полке №{key}')
            return
    print(f'Ошибка! Документа №{num} не существует')


def find_all_documents(documents):
    '''this function prints all documents list'''
    for document in documents:
        document_list = (list(document.values()))
        print(f'{document_list[0]} "{document_list[1]}" "{document_list[2]}"')


def add_new_document(documents, directories, num, type, name, shelf):
    '''this function adds new document in the documents list and his number in the directories dict'''
    if shelf in list(directories.keys()):
        documents.append({"type": type, "number": num, "name": name})
        # for key, value in directories.items():
        #     if shelf == key:
        #         value.append(num)
        directories[shelf].append(num)
        print('Данные успешно добавлены!')
        print(documents)
        print(directories)
    else:
        print(f'Ошибка! Полки №{shelf} не существует. Вы можете добавить новую полку командой "as"')


def del_document_by_number(documents, directories, num):
    '''this function deletes document from documents list and directories dict'''
    if num in sum(directories.values(), []):
        for i, document in enumerate(documents):
            if document["number"] == num:
                documents.pop(i)
        for key, value in directories.items():
            if num in value:
                value.remove(num)
        print(f'Документ №{num} успешно удален!')
        print(documents)
        print(directories)
    else:
        print(f'Ошибка! Документа №{num} нет в списке.') 


def move_document(directories, num, shelf):
    '''this function transfer documents between directories shelfs'''
    # if num in sum(directories.values(), []):
    #     if shelf in list(directories.keys()):  
    #         for key, value in directories.items():
    #             if num in value:
    #                 if shelf == key:
    #                     print(f'Документ №{num} уже находится на полке №{shelf}')
    #                     return None
    #                 else:
    #                     value.remove(num)
    #             if shelf == key:
    #                 value.append(num)
    #         print(f'Документ №{num} успешно перемещен на полку №{shelf}')
    #         print(directories)
    #         print()
    #     else:
    #         print('Ошибка! Такой полки не существует. Вы можете добавить новую полку командой "as"')
    # else:
    #     print('Ошибка! Такого документа нет!')    
    if shelf not in directories:
        print('Ошибка! Такой полки не существует. Вы можете добавить новую полку командой "as"')
        return
    for key, value in directories.items():
        if num in value and key == shelf:
            print(f'Документ №{num} уже находится на полке №{shelf}')
            return
        elif num in value:
            value.remove(num)
            directories[shelf].append(num)
            print(f'Документ №{num} успешно перемещен на полку №{shelf}')
            print(directories)
            print()
            return
    print('Ошибка! Такого документа нет!')


def add_new_shelf(directories, shelf):
    '''this function create a new shelf in directories'''
    if shelf not in directories.keys():
        directories.setdefault(shelf, [])
        print(f'Полка №{shelf} успешно создана')
        print(directories)
    else:
        print(f'Полка №{shelf} уже существует!')


def main(documents, directories):
    '''this main function which completes the commands:
    q - exit from program
    p - find people
    s - find shelf
    l - find all documents
    a - add new document
    d - delete a document
    m - transfer a document
    as - add shelf

    Thank u for using my program :) Have a good day!'''
    while True:
        comand = input('Введите команду (p, s, l, a, d, m, as), для выхода из программы, введите "q": ')
        if comand == 'q':
            break
        elif comand == 'p':
            find_people_by_number(documents, input('Введите номер документа: '))
            print()
        elif comand == 's':
            find_shelf_by_number(directories, input('Введите номер документа: '))
            print()
        elif comand == 'l':
            find_all_documents(documents)
            print()
        elif comand == 'a':
            add_new_document(documents, directories, input('Введите номер документа: '), input('Введите тип документа: '), input('Введите имя человека: '), input('Введите номер полки: '))
            print()
        elif comand == 'd':
            del_document_by_number(documents, directories, input('Введите номер документа: '))
            print()
        elif comand == 'm':
            move_document(directories, input('Введите номер документа: '), input('Введите номер полки: '))
            print()
        elif comand == 'as':
            add_new_shelf(directories, input('Введите номер полки: '))
            print()


help(main)
main(documents, directories)

