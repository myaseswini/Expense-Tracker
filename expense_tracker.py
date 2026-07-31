from tkinter import *
from tkinter import messagebox

# ---------------- Window ----------------
root = Tk()
root.title("💰 Expense Tracker")
root.geometry("700x550")
root.config(bg="#E8F6F3")

expenses = []

# ---------------- Functions ----------------
def add_expense():
    item = entry_item.get()
    amount = entry_amount.get()

    if item == "" or amount == "":
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        amount = float(amount)
    except:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    expenses.append((item, amount))
    listbox.insert(END, f"{item:<20} ₹{amount:.2f}")

    entry_item.delete(0, END)
    entry_amount.delete(0, END)

    total_spending()


def total_spending():
    total = 0
    for expense in expenses:
        total += expense[1]

    total_label.config(text=f"Total Spending : ₹{total:.2f}")


def delete_expense():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        expenses.pop(index)
        total_spending()
    except:
        messagebox.showwarning("Warning", "Select an expense first.")


def clear_expenses():
    answer = messagebox.askyesno("Confirm", "Delete all expenses?")
    if answer:
        expenses.clear()
        listbox.delete(0, END)
        total_spending()


# ---------------- Heading ----------------
title = Label(root,
              text="💰 Expense Tracker",
              font=("Arial", 22, "bold"),
              bg="#16A085",
              fg="white",
              pady=10)

title.pack(fill=X)

# ---------------- Input Frame ----------------
frame = Frame(root, bg="#E8F6F3")
frame.pack(pady=20)

Label(frame,
      text="Expense Name",
      font=("Arial",12,"bold"),
      bg="#E8F6F3").grid(row=0,column=0,padx=10,pady=10)

entry_item = Entry(frame,font=("Arial",12),width=20)
entry_item.grid(row=0,column=1)

Label(frame,
      text="Amount (₹)",
      font=("Arial",12,"bold"),
      bg="#E8F6F3").grid(row=1,column=0,padx=10,pady=10)

entry_amount = Entry(frame,font=("Arial",12),width=20)
entry_amount.grid(row=1,column=1)

# ---------------- Buttons ----------------
button_frame = Frame(root,bg="#E8F6F3")
button_frame.pack()

Button(button_frame,
       text="➕ Add Expense",
       command=add_expense,
       bg="#27AE60",
       fg="white",
       font=("Arial",11,"bold"),
       width=15).grid(row=0,column=0,padx=10,pady=10)

Button(button_frame,
       text="❌ Delete",
       command=delete_expense,
       bg="#E74C3C",
       fg="white",
       font=("Arial",11,"bold"),
       width=15).grid(row=0,column=1,padx=10)

Button(button_frame,
       text="🗑 Clear All",
       command=clear_expenses,
       bg="#F39C12",
       fg="white",
       font=("Arial",11,"bold"),
       width=15).grid(row=0,column=2,padx=10)

# ---------------- Expense List ----------------
list_frame = Frame(root,bg="#E8F6F3")
list_frame.pack(pady=15)

scroll = Scrollbar(list_frame)

listbox = Listbox(list_frame,
                  width=55,
                  height=12,
                  font=("Courier New",12),
                  bg="#FDFEFE",
                  fg="#2C3E50",
                  yscrollcommand=scroll.set)

scroll.config(command=listbox.yview)

listbox.pack(side=LEFT)
scroll.pack(side=RIGHT,fill=Y)

# ---------------- Total ----------------
total_label = Label(root,
                    text="Total Spending : ₹0.00",
                    font=("Arial",16,"bold"),
                    bg="#1ABC9C",
                    fg="white",
                    padx=20,
                    pady=10)

total_label.pack(fill=X,pady=15)

# ---------------- Footer ----------------
footer = Label(root,
               text="Track your daily expenses wisely 💸",
               font=("Arial",10,"italic"),
               bg="#E8F6F3",
               fg="#566573")

footer.pack()

root.mainloop()