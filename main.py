from support import write, readln,deletef,update
def main():
    command=int(input('Добро пожаловать в справочник \n\nДля просмотра нажмите - 1 \n\nДля записи - 2\n\nДля удаление - 3\n\nДля изменение - 4\n\n'))
    while command!=1 and command!=2 and command!=3 and command!=4:
        command=int(input('Вы ввели неправильный номер,запишите его снова\n'))
    if command==1:
        readln()
    elif command==2:
        write()
    elif command==3:
        deletef()
    elif command==4:
        update()
main()