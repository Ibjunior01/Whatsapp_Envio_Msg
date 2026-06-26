from tkinter import messagebox


class Messages:

    @staticmethod
    def sucesso(texto):

        messagebox.showinfo(
            "Sucesso",
            texto
        )

    @staticmethod
    def erro(texto):

        messagebox.showerror(
            "Erro",
            texto
        )

    @staticmethod
    def aviso(texto):

        messagebox.showwarning(
            "Aviso",
            texto
        )