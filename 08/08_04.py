class Book:
    total_books = 0#总藏书量
    total_borrowed = 0#当前借出数量

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False#借阅状态
        Book.total_books += 1
        print(f'图书{Book.total_books}：《{self.title}》作者：{self.author}，ISBN：{self.isbn}')

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            Book.total_borrowed += 1
            print(f'《{self.title}》借阅成功！')
        else:
            print(f'《{self.title}》已被借出，无法再次借阅')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            Book.total_borrowed -= 1
            print(f'《{self.title}》归还成功！')
        else:
            print(f'《{self.title}》未被借出，无需归还')

    def info(self):
        status = '已借出' if self.is_borrowed else '可借阅'
        return f'《{self.title}》 - 作者：{self.author} - ISBN：{self.isbn} - 状态：{status}'

    @classmethod
    def get_statistics(cls):
        return f"总藏书量：{cls.total_books}本\n当前借出数量：{cls.total_borrowed}本"

    @classmethod
    def search_by_title(cls, books, keyword):
        found_books = [book for book in books if keyword in book.title]
        return found_books

    @staticmethod
    def validate_isbn(isbn):
        return len(isbn) == 13 and isbn.isdigit()
    
if __name__ == '__main__':
    print('===== 创建图书 =====')
    book1 = Book('Python编程', '张三', '9787123456789')
    book2 = Book('数据结构', '李四', '9789876543210')
    book3 = Book('算法导论', '王五', '9781112223334')
    print(Book.get_statistics(), '\n')

    print('===== 借阅图书 =====')
    book1.borrow()
    book2.borrow()
    book2.borrow()  # 尝试再次借阅
    print(Book.get_statistics(), '\n')

    print('===== 归还图书 =====')
    book2.return_book()
    print(Book.get_statistics(), '\n')

    print('===== 图书信息 =====')
    print(book1.info())
    print(book2.info())
    print(book3.info(), '\n')

    print('===== 搜索图书 =====')
    keyword = "Python"
    found_books = Book.search_by_title([book1, book2, book3], keyword)
    print(f'搜索关键字"{keyword}"：')
    for book in found_books:
        print(f'找到1本：{book.title}')