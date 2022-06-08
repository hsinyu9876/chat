def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    return chat

def convert(chat):
    new = []
    person = None
    for c in chat:
        if c == 'Allen':
            person = 'Allen'
            continue
        elif c == 'Tom':
            person = 'Tom'
            continue
        if person: #如果person有值才執行以下
            new.append(person + ': ' + c)
    return new

def write_file(w_file, chat):
    with open(w_file, 'w') as f:
        for c in chat:
            f.write(c + '\n')

def main():
    chat = read_file('input.txt')
    chat = convert(chat)
    write_file('output.txt', chat)

main()