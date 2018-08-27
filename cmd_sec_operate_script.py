import sys, tkinter

'''
这是一个信息框，按i输入信息，按enter确认输入信息，
全局获取该框的信息：PopUpBox.message
'''
class PopUpBox:

    flag = True
    message = ''

    def __init__(self):
        self.root = self._init_root()
        self.var = self._init_var()
        self.entry = self._init_entry()
        self.btn = self._init_btn()
        self.root.bind("<Return>", self._confirm)
        self.root.bind("<Key>", self._edit)

    def _init_root(self):
        root = tkinter.Tk(className='这是提交附加信息框,按i输入信息,默认提交信息update')
        root.geometry('500x100')
        return root

    def _init_var(self):
        var = tkinter.StringVar()
        var.set('update')
        return var

    def _init_entry(self):
        entry = tkinter.Entry(self.root, textvariable=self.var, width=500)
        entry.pack()
        return entry

    def _init_btn(self):
        btn = tkinter.Button(self.root, text='确定', command=self._confirm)
        btn.pack(side='right')
        return btn

    def _confirm(self, e=None):
        PopUpBox.message = self.var.get().strip()
        self.root.destroy()

    def _edit(self, e=None):
        if PopUpBox.flag and 'i' == e.char:
            self.var.set('')
            self.entry.focus_set()
            PopUpBox.flag = False

    def start(self):
        self.root.mainloop()

if len(sys.argv) >= 2:
    cmd = ' '.join(sys.argv[1:]).strip()
    if 'commit -m' in cmd:
        PopUpBox().start()
        cmd  = 'git commit -m "%s"'%(PopUpBox.message)
    print(cmd)
    #
