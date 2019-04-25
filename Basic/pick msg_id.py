import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
import fileinput

file = 'v20_aixmsg.xml'
doc = minidom.parse(file)


def tag_count():
    count = 0
    tree = ET.parse(file)
    for item in tree.findall(".//MESSAGE"):
            count += 1
    print('No of message Ids:', count)
    return count

if __name__ == "__main__":
    msg_count = tag_count()
    i = 0
    m = []
    out = open('%s.txt' %file, 'w')
    out.close()
    while i < msg_count:

        msg = doc.getElementsByTagName('MESSAGE')[i]
        print(''.join([node.data for node in msg.childNodes]))
        message_id = msg.getAttribute('id1')
        print(message_id)
        i += 1

        out = open('%s.txt' %file, 'a')
        m.append(out.write(message_id + "\n"))
        m.sort()
        out.close()

    with fileinput.FileInput(file, inplace=True, backup='.bak') as f:
        for line in f:
            print(line.replace('-', '\n'), end='')

        o = open(file, 'r')
        lines = o.readline()
        for line in lines:
            line.split('(')


