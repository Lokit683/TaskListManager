from tkinter import *
from tkinter import ttk
import pickledb
 
TasksDb = pickledb.load("tasks.db", False)

root = Tk()
root.title("TaskList")
root.geometry("450x220")
root["bg"] = "gray22"

if TasksDb.get("needwork") == False:
	EmptyList = []
	TasksDb.set("needwork", EmptyList)
	TasksDb.set("Inwork", EmptyList)
	TasksDb.set("good", EmptyList)
	print("db created")
	TasksDb.dump()

selectData = None

def editList(task, oldlist, newlist):
	OneTaskList = TasksDb.get(oldlist)
	OneTaskList.remove(task)
	TasksDb.set(oldlist, OneTaskList)	
	TwoTaskList = TasksDb.get(newlist)
	TwoTaskList.append(task)
	TasksDb.set(newlist, TwoTaskList)
	TasksDb.dump()

def toNew():
	if str(Needwork_listbox.curselection()) != "()":
		selected_indices = Needwork_listbox.curselection()
		selected_langs = ",".join([Needwork_listbox.get(i) for i in selected_indices])
		Needwork_listbox.delete(selected_indices[0])
		Inwork_listbox.insert(0, selected_langs)
		editList(selected_langs, "needwork", "Inwork")


	if str(Inwork_listbox.curselection()) != "()":
		selected_indices = Inwork_listbox.curselection()
		selected_langs = ",".join([Inwork_listbox.get(i) for i in selected_indices])
		Inwork_listbox.delete(selected_indices[0])
		good_listbox.insert(0, selected_langs)
		editList(selected_langs, "Inwork", "good")

def toBack():
	if str(Inwork_listbox.curselection()) != "()":
		selected_indices = Inwork_listbox.curselection()
		selected_langs = ",".join([Inwork_listbox.get(i) for i in selected_indices])
		Inwork_listbox.delete(selected_indices[0])
		Needwork_listbox.insert(0, selected_langs)
		editList(selected_langs, "Inwork", "needwork")

	if str(good_listbox.curselection()) != "()":
		selected_indices = good_listbox.curselection()
		selected_langs = ",".join([good_listbox.get(i) for i in selected_indices])
		good_listbox.delete(selected_indices[0])
		Inwork_listbox.insert(0, selected_langs)
		editList(selected_langs, "good", "Inwork")

def add():
	task = Entry.get()
	needwork = TasksDb.get("needwork")
	needwork.append(task)
	TasksDb.set("needwork", needwork)
	TasksDb.dump()
	Needwork_listbox.insert(0, task)

def remove():
	if str(Needwork_listbox.curselection()) != "()":
		selected_indices = Needwork_listbox.curselection()
		selected_langs = ",".join([Needwork_listbox.get(i) for i in selected_indices])
		Needwork_listbox.delete(selected_indices[0])
		needwork = TasksDb.get("needwork")
		needwork.remove(selected_langs)
		TasksDb.set("needwork", needwork)
		TasksDb.dump()		

	if str(Inwork_listbox.curselection()) != "()":
		selected_indices = Inwork_listbox.curselection()
		selected_langs = ",".join([Inwork_listbox.get(i) for i in selected_indices])
		Inwork_listbox.delete(selected_indices[0])
		Inwork = TasksDb.get("Inwork")
		Inwork.remove(selected_langs)
		TasksDb.set("Inwork", Inwork)
		TasksDb.dump()		

	if str(good_listbox.curselection()) != "()":
		selected_indices = good_listbox.curselection()
		selected_langs = ",".join([good_listbox.get(i) for i in selected_indices])
		good_listbox.delete(selected_indices[0])
		good = TasksDb.get("good")
		good.remove(selected_langs)
		TasksDb.set("good", good)
		TasksDb.dump()	

# Добавляем карочи экранчики
Needwork = TasksDb.get("needwork")
Needwork_var = Variable(value=Needwork)
Needwork_listbox = Listbox(listvariable=Needwork_var, bg="#473f39", fg="#ffffff")
Needwork_listbox.place(width=140,x=0, y=20)

Inwork = TasksDb.get("Inwork")
Inwork_var = Variable(value=Inwork)
Inwork_listbox = Listbox(listvariable=Inwork_var, bg="#6b653d", fg="#ffffff")
Inwork_listbox.place(width=140, x=150, y=20)

good = TasksDb.get("good")
good_var = Variable(value=good)
good_listbox = Listbox(listvariable=good_var, bg="#39473b", fg="#ffffff")
good_listbox.place(width=140, x=305, y=20)

label = ttk.Label(text=" К выполнению                        В работе                                  Выполнено", background="gray22",  foreground="#ffffff")
label.place(x=5)

#Кнопаки чтобы перевигать
ttk.Button(text=">", command=toNew).place(width=30, x=240, y=190)
ttk.Button(text="<", command=toBack).place(width=30, x=210, y=190)

#Добавляем новые таски
Entry = ttk.Entry()
Entry.place(y=192)
ttk.Button(text="Добавить", command=add).place(x=130, y=190)

#кнопкачка для удаления
ttk.Button(text="Удалить", command=remove).place(x=370, y=190)

#запускаем шарманку
root.mainloop()