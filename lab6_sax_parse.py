import xml.sax

class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if self.current == "Book":
            print("--BOOK--")
            print("ID: {}".format(attrs['id']))

    def characters(self, content):
        if self.current == "Author":
            self.Author = content
        elif self.current == "Title":
            self.Title = content
        elif self.current == "Genre":
            self.Genre = content
        elif self.current == "Price":
            self.Price = content
        elif self.current == "PublishDate":
            self.PublishDate = content
        elif self.current == "Description":
            self.Description = content

    def endElement(self, name):
        if self.current == "Book":
            print("Book: {}".format(self.id))
        if self.current == "Title":
            print("Title: {}".format(self.Title))
        if self.current == "Author":
            print("Author: {}".format(self.Author))

    def startDocument(self):
        print('About to start!')

    def endDocument(self):
        print('Finishing up!')



handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("E:\Python/1.xml")