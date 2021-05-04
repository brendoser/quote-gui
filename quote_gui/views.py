# Python Packages
import io
import importlib
import tkinter as tk
from PIL import ImageTk, Image
from quote_gui.models import Form


class Background:

    def __init__(self, root):
        self._root = root
        self.frame = tk.Frame(master=self._root)
        image = importlib.resources.read_binary('quote_gui', 'Background.PNG')
        image = Image.open(io.BytesIO(image))
        image = image.resize((415, 150), Image.ANTIALIAS)
        background = ImageTk.PhotoImage(image)
        im_label = tk.Label(master=self.frame, image=background)
        im_label.image = background
        im_label.pack()


class ButtonPanel:

    def __init__(
            self,
            frame,
            button_handler,
            default_category=Form.CATEGORIES_LIST[0],
            default_sub_category=Form.SUB_CATEGORY_MAP[Form.CATEGORIES_LIST[0]][0],
            default_length=Form.LENGTHS_LIST[0],
    ):
        self.frame = frame

        self.category_var = tk.StringVar(self.frame)
        self.category_var.set(default_category)
        self.category_var.trace_add("write", callback=lambda *args: self.update_sub_category_menu())
        category_menu = tk.OptionMenu(self.frame, self.category_var, *Form.CATEGORIES_LIST)
        category_menu.pack(fill=tk.Y, side=tk.LEFT, expand=True)

        self.sub_category_var = tk.StringVar(self.frame)
        self.sub_category_var.set(default_sub_category)
        self._sub_category_menu = tk.OptionMenu(self.frame, self.sub_category_var,
                                                *Form.SUB_CATEGORY_MAP[default_category])
        self._sub_category_menu.pack(fill=tk.Y, side=tk.LEFT, expand=True)

        self.length_var = tk.StringVar(self.frame)
        self.length_var.set(default_length)
        length_menu = tk.OptionMenu(self.frame, self.length_var, *Form.LENGTHS_LIST)
        length_menu.pack(fill=tk.Y, side=tk.LEFT, expand=True)

        button = tk.Button(self.frame, text='New Quote')
        button.bind('<Button-1>', button_handler)
        button.pack(fill=tk.Y, side=tk.LEFT, expand=True)

    def update_sub_category_menu(self):
        category = self.category_var.get()
        options = Form.SUB_CATEGORY_MAP[category]
        menu = self._sub_category_menu["menu"]
        menu.delete(0, "end")
        for option in options:
            menu.add_command(label=option,
                             command=lambda val=option: self.sub_category_var.set(val))
        self.sub_category_var.set(options[0])


class QuoteBox:

    def __init__(self, frame):
        self.frame = frame
        self.quote_text = tk.StringVar()
        self.quote_text.set(" ")
        text_label = tk.Label(self.frame,
                              textvariable=self.quote_text,
                              wraplength=415,
                              justify="left"
                              )
        text_label.pack()


class QuoteInfo:

    def __init__(self, frame):
        self.frame = frame

        text1 = tk.StringVar()
        text1.set("An excerpt from: ")
        self.book = tk.StringVar()
        self.book.set(" ")
        text2 = tk.StringVar()
        text2.set("By: ")
        self.author = tk.StringVar()
        self.author.set(" ")

        text1_label = tk.Label(self.frame, textvariable=text1)
        book_label = tk.Label(self.frame,
                              textvariable=self.book,
                              wraplength=300)
        text2_label = tk.Label(self.frame, textvariable=text2)
        author_label = tk.Label(self.frame,
                                textvariable=self.author)

        text1_label.grid(row=0, column=0, sticky="ew")
        book_label.grid(row=0, column=1, sticky="ew")
        text2_label.grid(row=1, column=0, sticky="ew")
        author_label.grid(row=1, column=1, sticky="ew")
