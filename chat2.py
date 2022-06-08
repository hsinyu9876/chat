def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    return chat


def convert(chat):
    person = None
    allen_words = 0
    allen_stickers = 0
    allen_images = 0
    viki_words = 0
    viki_stickers = 0
    viki_images = 0
    for c in chat:
        s = c.split(' ')
        time = s[0]
        person = s[1]
        if person == 'Allen':
            if s[2] == '貼圖':
                allen_stickers += 1
            elif s[2] == '圖片':
                allen_images += 1
            else:
                for m in s[2:]:
                    allen_words += len(m)
        elif person == 'Viki':
            if s[2] == '貼圖':
                viki_stickers += 1
            elif s[2] == '圖片':
                viki_images += 1
            else:
                for m in s[2:]:
                    viki_words += len(m)
    print('allen說了', allen_words , '傳了', allen_stickers, '張貼圖', allen_images, '張圖片')
    print('viki說了', viki_words, '傳了', viki_stickers, '張貼圖', viki_images, '張圖片')


def write_file(w_file, chat):
    with open(w_file, 'w') as f:
        for c in chat:
            f.write(c + '\n')


def main():
    chat = read_file('LINE-Viki.txt')
    chat = convert(chat)
    #write_file('output.txt', chat)


main()