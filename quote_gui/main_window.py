# Python Packages
import tkinter as tk
import views as views
import models as models


class MainWindow:

    def __init__(self):
        self._root = tk.Tk()

        self.bg = views.Background(root=self._root, image='Background.png')
        self.bp = views.ButtonPanel(
            frame=tk.Frame(master=self._root, height=100),
            button_handler=lambda *args: self.fetch_new_quote())
        self.qb = views.QuoteBox(frame=tk.Frame(master=self._root, height=100))
        self.qi = views.QuoteInfo(frame=tk.Frame(master=self._root, height=150))

        self.bg.frame.pack(fill=tk.X, expand=True)
        self.qb.frame.pack(fill=tk.X, expand=True)
        self.qi.frame.pack(fill=tk.X, expand=True)
        self.bp.frame.pack(fill=tk.X, expand=True)

    def run(self):
        self._root.title("Quote GUI")
        self._root.deiconify()
        self._root.resizable(False, False)
        self.fetch_new_quote()
        self._root.mainloop()


    def fetch_new_quote(self):
        form = models.Form(
            models.CATEGORIES.from_formatted(self.bp.category_var.get()),
            models.SUB_CATEGORIES.from_formatted(self.bp.sub_category_var.get()),
            models.LENGTHS.from_formatted(self.bp.length_var.get())
        )
        quote_data = form.get_quote_data()
        self.qb.quote_text.set(quote_data.text)
        self.qi.book.set(quote_data.title)
        self.qi.author.set(quote_data.author)


if __name__ == '__main__':
    mw = MainWindow()
    mw.run()
