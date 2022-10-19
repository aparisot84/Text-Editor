import tkinter as tk
from tkinter import filedialog as fd
from tkinter import font
#########################################################
# Functions

def load():

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    file = fd.askopenfilename(title='Open file', initialdir='../', filetypes=filetypes)

    name = file

    with open(file, 'r') as f:
        content = f.read()

    textarea.insert(1.0, content)

    root.title(name + ' - Notepad+-')

    #TODO: lógica que troca o nome da janela para omitir o caminho todo e exibir somente o nome do arquivo

def saveas():

    filetypes = (
        ('text files', '*.txt'),
    )

    file = fd.asksaveasfilename(title='Save as', initialdir='../', filetypes=filetypes)

    content = textarea.get(1.0, "end")

    with open(file + ".txt", 'w') as f:
        f.write(content)

def save():

    # Todo: colocar a lógica que controla o save as ou save caso o arquivo ainda nao tenha sido salvo nenhuma vez

    filetypes = (
        ('text files', 'txt'),
    )

    content = textarea.get(1.0, "end")

    file = fd.askopenfilename(title='Save', initialdir='../', filetypes=filetypes)

    with open(file, 'w') as f:
        f.write(content)

def clear():        # nao tem botao associado

    textarea.delete(1.0, "end")

def copy():

    selection = textarea.selection_get()

def paste():

    #textarea.insert(1.0, XXX) #TODO: inserir o texto copiado na poição em que está o cursor

    pass

def cut():

    pass

def bolder():

    bold_font = font.Font(textarea, textarea.cget('font'))

    bold_font.configure(weight='bold')

    textarea.tag_configure("bold", font="bold_font")

    current_tags = textarea.tag_names("sel.first")

    if "bold" in current_tags:
        textarea.tag_remove("bold", "sel.first", "sel.last")
    else:
        textarea.tag_add("bold", "sel.first", "sel.last")


    #TODO: colocar a logica de colocar bold se nao tiver e tirar bold se tiver bold na fonte

def popup(event):

    popup_menu.tk_popup(event.x_root, event.y_root)

def about_window():

    #TODO: organizar o texto e a decoração da janela about

    window = tk.Toplevel(root)
    window.geometry("400x300")
    window.title("About Notepad+-")

    #Create a Label in New window
    about_text = "O notepad +- foi uma iniciativa minha para\n " \
                 "aprender como funciona o Tkinter.\n" \
                 "\n" \
                 "Versão 0.1\n" \
                 "\n" \
                 "GNU General Public License v3.0.\n" \
                 "Permissions of this strong copyleft license are\n" \
                 "conditioned on making available complete source code \n" \
                 "of licensed works and modifications, which include \n" \
                 "larger works using a licensed work, under the same license.\n" \
                 "\n" \
                 " Copyright and license notices must be preserved.\n" \
                 "Contributors provide an express grant of patent rights."

    tk.Label(window, text=about_text, font=('Helvetica 12')).pack(pady=10)


#########################################################

# root window
root = tk.Tk()
root.title('Notepad+-')

#########################################################

# create the textarea scrollbars
text_yscroll = tk.Scrollbar(root)
text_yscroll.pack(side='right', fill="y")

# create the TextArea of notepad
textarea = tk.Text(root, undo=True, yscrollcommand=text_yscroll.set) ######
textarea.pack(expand=True, fill='both')

#########################################################

# create a menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

#########################################################

# create a File menu
file_menu = tk.Menu(menubar, tearoff=False)

# add a menu item to the File menu
file_menu.add_command(label='New', command=clear)       #TODO: abre uma janela nova do programa
file_menu.add_command(label='Open...', command=load)
file_menu.add_command(label='Save', command=save)
file_menu.add_command(label='Save as...', command=saveas)
file_menu.add_command(label='Print')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

# add the File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)

#########################################################

# create a Edit menu
edit_menu = tk.Menu(menubar, tearoff=False)

# add a menu item to the Edit menu
edit_menu.add_command(label='Undo', command=textarea.edit_undo)
edit_menu.add_command(label='Redo', command=textarea.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Delete')
edit_menu.add_separator()
edit_menu.add_command(label='Search')
edit_menu.add_command(label='Search Next')
edit_menu.add_command(label='Search Previous')
edit_menu.add_command(label='Replace')
edit_menu.add_command(label='Go to')
edit_menu.add_separator()
edit_menu.add_command(label='Select all')
edit_menu.add_command(label='Date Time')

# add the Edit menu to the menubar
menubar.add_cascade(label="Edit", menu=edit_menu)

#########################################################

# create the Format menu
format_menu = tk.Menu(menubar, tearoff=0)
format_menu.add_command(label='Font')
format_menu.add_separator()
format_menu.add_command(label='Bold', command=bolder)
format_menu.add_command(label='Italic')
format_menu.add_command(label='Size')

#TODO: font tem q ter submenu (size, style, italic, bold, riscado, highlighted etc)

# add the Help menu to the menubar
menubar.add_cascade(label="Format", menu=format_menu)

#########################################################

# create the Help menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label='About...', command=about_window)

# add the Help menu to the menubar
menubar.add_cascade(label="Help", menu=help_menu)

#########################################################

# create a popup menu
popup_menu = tk.Menu(root, tearoff=False)
popup_menu.add_command(label="Undo", command=textarea.edit_undo)
popup_menu.add_separator()
popup_menu.add_command(label="Cut", command=cut)
popup_menu.add_command(label="Copy", command=copy)
popup_menu.add_command(label="Paste", command=paste)
popup_menu.add_command(label="Delete", command=textarea.delete)
popup_menu.add_separator()
popup_menu.add_command(label="Select All", command=cut)

root.bind("<Button-3>", popup)

#########################################################

# create a Status Bar
status_bar = tk.Label(root, text="ready            ", anchor="e")
status_bar.pack(fill="x", side="bottom", ipady=5)

#########################################################

#TODO: colocar a barra lateral com o número de linhas

#TODO: adicionar o menu de opção de aparecer ou nao a linha na barra lateral

#TODO: Adicionar o campo lateral com a listagem dos arquivos e o form de buscar

#TODO: Implementar a lógica do modo de busca (buscar dentro de todos os documentos listados o termo escrito no form)

#TODO: implementar a lógica para carregar e salvar as configurações do programa de um arquivo (JSON é uma boa idéia)

#TODO: imlementar a lógica de abrir os arquivos em abas

#TODO: Implementar a lógica do autosave com menu de seleção on/off, do tempo de salvamento e salvar nas configurações

#TODO: colocar as funções em outro arquivo

#TODO: Implementar na barra da parte de baixo a quantidade de linhas/linha atual

#TODO: Implementar na barra da parte de baixo a quantidade de colunas/coluna atual

#TODO: Implementar na barra da parte de baixo a quantidade de palavras/palavra atual

#TODO: Implementar na barra da parte de baixo a quantidade de caracteres/caracter atual

#TODO: Implementar botões de atalho na barrra de menu (save, open...etc)

#TODO: Implementar a quebra de linha automática (de acordo com o tamanho da tela)

#TODO: implementar os atalhos do teclado

root.mainloop()