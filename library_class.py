import sqlite3
conn = sqlite3.connect("library.db")
c = conn.cursor()
class Library():

    def show_books(self):
        order = c.execute("SELECT * FROM book")
        for i in order:
            print("""
Book_ID : {0}
Title : {1}
Publishing date {2}
Version : {3}
Author_ID : {4}

            """.format(i[0], i[1], i[2], i[3], i[4]))

    @classmethod
    def showing_table(cls, method_self, request, row_numbers):
        from PyQt5 import QtCore, QtGui, QtWidgets
        from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
        exe_number = c.execute(row_numbers)
        Rnums = exe_number.fetchone()
        method_self.tableWidget.setRowCount(int(Rnums[0]))
        exe_show = c.execute(request)
        result = exe_show.fetchall()
        row = 0
        culomn =0       
        for i in result:
            for element in i:
                method_self.tableWidget.setItem(row, culomn, QTableWidgetItem(f"{str(element)}"))
                culomn+=1
            culomn = 0
            row +=1
#         order = c.execute("SELECT * FROM author")
#         for i in order:
#             print("""
# Author_ID : {0}
# Name : {1}
# Phone : {2}
# Email : {3}
#             """.format(i[0], i[1], i[2], i[3]))

    
    def add_author(self, name, phone, email, nationality):
        order = c.execute("insert into author(name, phone, email, Nationality) values('{0}', '{1}', '{2}', '{3}')".format(name, phone, email, nationality))
        conn.commit()

    def remove_author(self, author_id):
        c.execute(f"delete from author where author_id = {author_id}")
        conn.commit()
        
    def print_author(self):
        author_id =int(input("Author ID? "))
        order = c.execute(f"select * from author where author_id = {author_id}")
        for i in order:
            print("""
Name : {0}
Phone : {1}
Email : {2}
            """.format(i[1], i[2], i[3]))

    def print_author_books(self):
        author_id = int(input("Author ID? "))
        order = c.execute("""
SELECT book_id, title, version, book.author_id
from book
JOIN author 
 on book.author_id = author.author_id
WHERE book.author_id = {}
        """.format(author_id))
        for i in order:
            print("""
Author Name : {0}
Book ID : {1}
Book Title : {2}            
            """.format(i[0], i[1], i[2]))
            

    def add_book(self, title, PD, version, author_id):
        c.execute("""
        insert into book(title, publishing_date, version, author_id)
        values('{0}', '{1}', {2}, {3})
        """.format(title, PD, version, author_id))
        conn.commit()

    def remove_book(self, book_id):
        c.execute(f"delete from book where book_id = {book_id}")
        conn.commit()

    def print_book(self):
        book_id = int(input("Book ID? "))
        order = c.execute(f"select * from book where book_id = {book_id}")
        for i in order:
            print("""
Book Title : {0}
Book Publishing date : {1}
Book Version : {2}
Book's Author ID : {3}
            """.format(i[1], i[2], i[3], i[4]))





        



