import xml.dom.minidom

domtree = xml.dom.minidom.parse("E:\Python/1.xml")
group = domtree.documentElement

books = group.getElementsByTagName("Book")

for book in books:
    print("---BOOK---")
    if book.hasAttribute("id"):
        print("ID: {}".format(book.getAttribute("id")))

    print("Author: {}".format(book.getElementsByTagName('Author')[0].childNodes[0].data))
    print("Title: {}".format(book.getElementsByTagName('Title')[0].childNodes[0].data))
    print("Genre: {}".format(book.getElementsByTagName('Genre')[0].childNodes[0].data))
    print("Price: {}".format(book.getElementsByTagName('Price')[0].childNodes[0].data))


books[1].getElementsByTagName("Author")[0].childNodes[0].nodeValue = "Tomasz Lejkowski"
books[0].getElementsByTagName("Price")[0].childNodes[0].nodeValue = "45.55"
books[0].setAttribute('id', 'bk103')

domtree.writexml(open("E:\Python/1_v2.xml", 'w'))




