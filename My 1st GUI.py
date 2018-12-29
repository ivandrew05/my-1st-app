from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class  Feedback:
     def __init__(self, master):

           master.title('王者荣耀英雄皮肤反馈系统')
           master.resizable(False,False)
           master.configure(background='#e1d8b9')

           self.style=ttk.Style()
           self.style.configure('TFrame',background='#e1d8b9')
           self.style.configure('TButton',background='#e1d8b9')
           self.style.configure('TLabel',background='#e1d8b9',font=('Arial',11))
           self.style.configure('Header.TLabel',font=('Arial', 15, 'bold'))
          
           self.frame_header=ttk.Frame(master)
           self.frame_header.pack()

           self.logo=PhotoImage(file="wzj.gif")
           ttk.Label(self.frame_header,image=self.logo).grid(row=0, column=0, rowspan=2)
           ttk.Label(self.frame_header,text='欢迎来到王者荣耀!', style= 'Header.TLabel').grid(row=0, column=1)
           ttk.Label(self.frame_header,wraplength=300,
                         text=("欢迎使用王者荣耀英雄皮肤反馈系统，请填写以下内容并提交，"
                                   "敌军还有五秒到达战场！")).grid(row=1, column=1)

           self.frame_content=ttk.Frame(master)
           self.frame_content.pack()

           ttk.Label(self.frame_content, text="英雄名称:").grid(row=0, column=0, padx=5, sticky="sw")
           ttk.Label(self.frame_content, text="皮肤名称:").grid(row=0, column=1, padx=5, sticky="sw")
           ttk.Label(self.frame_content, text="用户评论:").grid(row=2, column=0, padx=5, sticky="sw")

           self.entry_name=ttk.Entry(self.frame_content, width=24,font=('Arial',10))
           self.entry_email=ttk.Entry(self.frame_content, width=24,font=('Arial',10))
           self.text_comments=Text(self.frame_content, width=50, height=10,font=('Arial',10))
           
           self.entry_name.grid(row=1, column=0, padx=5)
           self.entry_email.grid(row=1, column=1, padx=5)
           self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)
 
           ttk.Button(self.frame_content, text="提交", command=self.submit).grid(row=4, column=0, padx=5, sticky="e")
           ttk.Button(self.frame_content, text="清除", command=self.clear).grid(row=4, column=1, padx=5, sticky="w")

     def submit(self):
           print('英雄名称:{}'.format(self.entry_name.get()))
           print('皮肤名称:{}'.format(self.entry_email.get()))
           print('用户评论:{}'.format(self.text_comments.get(1.0, 'end')))
           self.clear( )
           messagebox.showinfo(title="用户反馈系统", message="您的意见已提交，感谢使用!")

     def clear(self):
          self.entry_name.delete(0, 'end')
          self.entry_email.delete(0, 'end')
          self.text_comments.delete(1.0, 'end')
          
def main():

      root=Tk( )
      feedback = Feedback(root)
      root.mainloop( )

if __name__ == "__main__": main()

