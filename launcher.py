#импорт библеотек
from customtkinter import *
from tkinter import *
from tqdm import tqdm
from pathlib import Path
import os,sys,threading,time,requests,zipfile


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#создание окна
tk=CTk()
tk.title('Лаунчер SWMG')
tk.iconbitmap(default=resource_path("icon.ico"))
tk.geometry("900x550+400+300")
tk.minsize(900,550)
tk.maxsize(900,550)
set_appearance_mode("dark")

#функции
def sizeof_fmt(num: int | float) -> str:
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%.1f %s" % (num, x) 
        num /= 1024.0
    return "%.1f %s" % (num, 'TB')

'''def move_progress():
    steps=10
    for i in range(steps+1):
        value = (i * steps) / 100
        progress_bar.set(value)
        time.sleep(1)'''
def start():
    os.system('"ShadowWizardMoneyGang.exe"')
def dowloand():
    url = 'https://github.com/Flipmixplay/SWMG/raw/main/SWMG.zip'
    #url = 'https://github.com/Flipmixplay/SWMG/archive/refs/heads/main.zip'
    # Streaming, so we can iterate over the response.
    rs = requests.get(url, stream=True)

    # Total size in bytes.
    total_size = int(rs.headers.get('content-length', 0))
    print('Размер файла:', sizeof_fmt(total_size))

    chunk_size = 1024
    num_bars = int(total_size / chunk_size)
    file_name = os.path.basename(url)
    i=0
    with open(file_name, mode='wb') as f:
        for data in tqdm(rs.iter_content(chunk_size), total=num_bars, unit='KB', file=sys.stdout):
            f.write(data)
    #Проверяем размер файла
    file_data = open(file_name, mode='rb').read()
    print('Размер скачаного файла', sizeof_fmt(len(file_data)))
    
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()
    if check_var.get() == "on":
        os.remove("SWMG.zip")
    
#графический интерфейс    
Update_button=CTkButton(tk,text="Update",font=("MontCinabal", 40),
                 width=200,height=100,command=dowloand)
Update_button.place(relx=0.8,rely=0.8,anchor="center")

Start_button=CTkButton(tk,text="Start",font=("MontCinabal", 40),
                 width=200,height=100,command=start)
Start_button.place(relx=0.8,rely=0.6,anchor="center")

check_var = StringVar(value="on")
checkbox = CTkCheckBox(tk, text="Удалить архив после установки",font=("MontCinabal", 18),
                       variable=check_var, onvalue="on", offvalue="off")
checkbox.place(relx=0.815,rely=0.95,anchor="center")
#progress_bar = CTkProgressBar(tk, width=400,progress_color='green')
#progress_bar.place(x=20,y=20)

tk.mainloop()