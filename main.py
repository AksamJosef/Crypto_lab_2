# Вариант 22.

# 1 2 3 4 5 6
# 5 4 3 1 6 2

# Функция шифровки и записи в файл
def Encrypt ():
    try:
        path_to_file = input ("Введите путь к файлу, который хотите зашифровать: \n")
        with open(path_to_file, 'rb') as SFile: # открываем файл для чтения побайтово
            FileContain = bytearray(SFile.read()) # создаем байтовый массив
            TmpFile = [] #создаем пустой список для временного хранения символов, уже переставленных
            while len(FileContain) % 6 != 0: # для обработки исключения out of range необходимо,
                # чтобы длина строки была кратна 6, т.к. у нас блоки по 6 элементов. добиваем все нулями,
                # пока длина не будет соответствовать условию для начала шифровки
                FileContain.append(0)
            # print (FileContain)
            for i, byte in enumerate(FileContain):
                if i % 6 == 0:
                    # В список TmpFile присваимваем соответствующие значения из исходного содержимого
                    TmpFile.append(FileContain[i + 3])
                    TmpFile.append(FileContain[i + 5])
                    TmpFile.append(FileContain[i + 2])
                    TmpFile.append(FileContain[i + 1])
                    TmpFile.append(FileContain[i + 0])
                    TmpFile.append(FileContain[i + 4])

        ToFile = bytearray(TmpFile) # преобразуем список в байтовый массив для корректной записи в файл

        # открываем файл заново, иначе зашифрованное содержимое записывается в конец файла, а не вместо
        # исходного содержимого
        with open(path_to_file, "wb") as OFile:
            OFile.write (ToFile)
            print("Программа завершена успешно, файл зашифрован,"
                  " попробуйте его открыть и убедитесь, что он теперь битый :)")
    except FileNotFoundError: # на всякий случай обрабатываем исключение в случае, если файл не найден
                              # или прописан неверный путь к файлу
        print("Файл не найден, запустите заново программу и введите корректно")

# Функция дешифровки и запись в файл, устроена похожим образом как и функция шифровки,
# но алгоритм дешифровки уже обратный
def Decrypt ():
    try:
        path_to_file = input("Введите путь к файлу, который хотите зашифровать: \n")
        with open(path_to_file, 'rb') as SFile:
            FileContain = bytearray(SFile.read())
            TmpFile = []
            # print(FileContain)
            # TmpFile[0] = FileContain[0]
            if len(FileContain) % 6 != 0:
                print ("Не удается расшифровать файл при помощи этого алгоритма. "
                       "Зашифрованный файл был изменен вручную "
                       "(были добавлены или удалены символы)")

            for i, byte in enumerate(FileContain):
                if i % 6 == 0:
                    TmpFile.append(FileContain[i + 4])
                    TmpFile.append(FileContain[i + 3])
                    TmpFile.append(FileContain[i + 2])
                    TmpFile.append(FileContain[i + 0])
                    TmpFile.append(FileContain[i + 5])
                    TmpFile.append(FileContain[i + 1])

            while TmpFile[-1] == 0: # обратный алгоритм, для удаления нулей
                                    # из конца уже дешифрованного списка
                del TmpFile[-1]


            ToFile = bytearray(TmpFile)

        with open(path_to_file, 'wb') as OFile:
            OFile.write(ToFile)
            print("Файл расшифрован. Попробуйте его открыть, и он откроется :)")
    except FileNotFoundError:
        print("Файл не найден, запустите заново программу и введите корректно")




Selected = input("Введите 1 или 2, чтобы выбрать функцию программы:\n"
                 "1: Шифровка\n"
                 "2: Дешифровка\n")
if Selected == '1':
    Encrypt()

elif Selected == '2':
    Decrypt()

else:
    print("Вы ввели неправильный параметр. Запустите программу еще раз и введите правильно!\n")