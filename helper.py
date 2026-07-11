import os,tkinter as tk
from tkinter import Tk
gpath=os.path.dirname(__file__)
general={}
class main(Tk):
    def __init__(s):
        super().__init__()
        s.geometry("700x200")
        s.label1=tk.Label(s,text="Titre:")
        s.entry1=tk.Entry(s,width=300)
        s.label2=tk.Label(s,text="Nombre de sous dossiers:")
        s.entry2=tk.Entry(s,width=40)
        s.validate=tk.Button(s,text="Valider",command=s.ert)
        s.label1.pack()
        s.entry1.pack()
        s.label2.pack()
        s.entry2.pack()
        s.validate.pack()
    def ert(s):
        general["ru"]=int(s.entry2.get())*"../"
        general["title"]=s.entry1.get()
        s.quit()


main()

def modiftitle(title:str):
    tt=os.path.splitext(title)[0]
    if "_Ap" in tt: return "Applications associées"
    tt=tt.replace(" correction"," (corr)")
    tt=tt.replace("-cor"," (corr)")
    tt=tt.replace(" - Cor"," (corr)")
    tt=tt.replace("-V1"," version 1")
    tt=tt.replace("-V2"," version 2")
    tt=tt.replace("TD","")
    return tt

txt1=[
    "<!doctype html>\n<html lang=\"fr\">\n<head>\n    <meta charset=\"utf-8\">\n    <title>",
    general["title"],
    "</title>\n    <link rel=\"stylesheet\" href=\"",
    general["ru"],
    "assets/general.css\">\n</head>\n<body>\n    <div class=\"invisible_header\"><a href=\"",
    general["ru"],
    "index.html\"><img class=\"images t035\" src=\"",
    general["ru"],
    "assets/link_menu.png\"></a></div>\n    <div class=\"centered_div main_mode tomanyobj\" style=\"gap:1.5rem;\">\n"
]
txt2=[]
for _ in os.listdir(gpath):
    if _ not in [".git","main.html","helper.py","helper.pyw"]:
        if os.path.isdir(gpath+"/"+_):
            txt2.append(f"<button class=\"button_g\" onclick=\"window.location.href='./{_}/main.html'\">{_}</button>\n")
        elif os.path.isfile(gpath+"/"+_):
            txt2.append(f"<a href=\"./{_}\" style=\"color: beige;font-size: 1.5rem;\" target=\"_blank\">{modiftitle(_)}</a>\n")


txt3=["    </div>\n</body>\n</html>"]


with open(gpath+"/main.html","w+",encoding="utf8") as f:
    f.write("".join(txt1+txt2+txt3))













