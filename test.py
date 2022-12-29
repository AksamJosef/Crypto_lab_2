# 1 2 3 4 5 6
# 5 4 3 1 6 2


path_to_file = input ("Введите путь к файлу, который хотите зашифровать: \n")
with open(path_to_file, 'rb') as SFile: # открываем файл для чтения побайтово
    FileContain = bytearray(SFile.read()) # создаем байтовый массив
    TmpFile = []
    # print(FileContain)
    # TmpFile[0] = FileContain[0]
    while len(FileContain) % 6 != 0:
        FileContain.append(0)
    print (len(FileContain))
    for i, byte in enumerate(FileContain):
        # print(byte)
        # 1 2 3 4 5 6
        # 5 4 3 1 6 2
        if i % 6 == 0:
            TmpFile.append(FileContain[i+4])
            TmpFile.append(FileContain[i+3])
            TmpFile.append(FileContain[i+2])
            TmpFile.append(FileContain[i+0])
            TmpFile.append(FileContain[i+5])
            TmpFile.append(FileContain[i+1])

    while TmpFile[-1] == 0:
        del TmpFile[-1]
    BTmp = bytearray(TmpFile)

    # print(TmpFile)
    # TmpFile.append(FileContain[1])
    # for i in range(len(FileContain)):
    #     if i % 6 == 0:
            # TmpFile.append(FileContain[i])
            # TmpFile[i] = FileContain[i + 3]
            # TmpFile[i + 1] = FileContain[i + 5]
            # TmpFile[i + 2] = FileContain[i + 2]
            # TmpFile[i + 3] = FileContain[i + 1]
            # TmpFile[i + 4] = FileContain[i + 0]
            # TmpFile[i + 5] = FileContain[i + 4]

    print ('loh',BTmp)
    print(FileContain)