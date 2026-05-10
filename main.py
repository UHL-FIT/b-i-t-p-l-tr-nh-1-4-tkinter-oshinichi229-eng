import tkinter as tk
#1.khoi tao cua so goc
root=tk.Tk()
root.title("ung dung dau tien-UHL")
root.geometry("500x500")
#2.tao thanh phan hien thi van ban (label)
nhan_chao=tk.Label(root,text="nguyen thi bich ngoc")
nhan_chao.pack(pady=50)#dua nhan vao cua so tao khoang cach le
#duy tri cua so (vong lap chinh)
root.mainloop()
