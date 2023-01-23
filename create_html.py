import sys
def create(data):
    file = 'data.html'

    html = '<html>\n'
    html += '<body>\n'
    html += '<table style="border-collapse:collapse;">\n'
    html += '<tr>\n'
    html += '<th style="border: 1px solid black;padding:5px;">Имя</th>\n'
    html += '<th style="border: 1px solid black;padding:5px;">Фамилия</th>\n'
    html += '<th style="border: 1px solid black;padding:5px;">Отчество</th>\n'
    html += '<th style="border: 1px solid black;padding:5px;">Номер телефона</th>\n'
    html += '<th style="border: 1px solid black;padding:5px;">Комментарий</th>\n'
    html += '</tr>\n'

    for user in data:
        html += '<tr>\n'
        for prop in user:
            html += '<td style="border: 1px solid black;padding:5px;">' + prop + '</td>\n'
        html += '</tr>\n'
    
    html += '</table>\n'
    html += '</body>\n'
    html += '</html>\n'


    with open(file, 'w') as file_handler:
        file_handler.write(html)

def create_from_txt (path):
    res_list = []
    path = 'data.txt'
    with open (path, 'r', encoding='utf-8') as file:
        flag = True
        while flag:
            k = 0
            user = []
            for i in range(0, 5):
                my_book = file.readline()
                if not my_book:
                    flag = False
                    break
                if(i != 5):
                    user.append(my_book.rstrip())
            if(user): res_list.append(user)
            file.readline()
            k += 1
    create(res_list)
            