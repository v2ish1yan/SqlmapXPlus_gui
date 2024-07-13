import tkinter as tk
import tkinter.ttk as ttk
import subprocess as sub
import os
import getpass
import shutil

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('SqlmapXPlus_gui by v2ish1yan v1.0')
        screen_x = self.winfo_screenwidth()
        screen_y = self.winfo_screenheight()
        position_x = (screen_x - 1012) //2
        position_y = (screen_y - 600) //2
        # position_x = (screen_x) / 2 - 300
        # position_y = (screen_y) / 2 - 150
        self.geometry('{}x{}+{}+{}'.format(1012, 600, int(position_x), int(position_y)))
        #主容器
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #创建所有页面，将他们保存在字典里
        # for F in (Page1, Page2, Page3):
        #     frame = F(container, self)
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, stick='nsew')
        for F in (Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, stick='nsew')

        self.show_frame(Page1)

        #创建菜单
        menu = tk.Menu(self)
        self.config(menu=menu)
        menu.add_command(label="基础功能", command=lambda: self.show_frame(Page1))
        menu.add_command(label="数据显示", command=lambda: self.show_frame(Page2))
        # menu.add_command(label="功能3", command=lambda: self.show_frame(Page3))

    def show_frame(self, count):
        #显示指定页面
        frame = self.frames[count]
        frame.tkraise()


# 页面一 基础功能
class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # 测试级别 --level
        self.level_var = tk.StringVar(value='1')
        levle_label = ttk.Label(self, text="level")
        levle_label.grid(row=0, column=0, sticky='nesw')
        level_combo = ttk.Combobox(self, values=[str(i) for i in range(1, 6)], textvariable=self.level_var)
        level_combo.grid(row=1, column=0, sticky='nsew')

        #风险等级 --risk
        self.risk_var = tk.StringVar(value='1')
        risk_label = ttk.Label(self, text="risk")
        risk_label.grid(row=2, column=0, sticky='nswe')
        risk_combo = ttk.Combobox(self, values=[str(i) for i in range(1, 4)], textvariable=self.risk_var, width=20)
        risk_combo.grid(row=3, column=0, sticky='nsew')

        # 线程数 --threads
        self.threads_var = tk.StringVar(value='1')
        threads_label = ttk.Label(self, text="threads")
        threads_label.grid(row=4, column=0, sticky='nsew')
        threads_entry = ttk.Entry(self, textvariable=self.threads_var, width=20)
        threads_entry.grid(row=5, column=0, sticky='nsew')

        #指定库名
        ttk.Label(self, text="指定库名").grid(row=6, column=0, sticky='wnse')
        self.custom_db_var = tk.StringVar()
        custom_db_entry = ttk.Entry(self, textvariable=self.custom_db_var)
        custom_db_entry.grid(row=7, column=0, sticky='wnse')
        #指定表名
        ttk.Label(self, text="指定表名").grid(row=8, column=0, sticky='wnse')
        self.custom_table_var = tk.StringVar()
        custom_table_entry = ttk.Entry(self, textvariable=self.custom_table_var)
        custom_table_entry.grid(row=9, column=0, sticky='wnse')
        #指定字段名
        ttk.Label(self, text="指定字段名").grid(row=10, column=0, sticky='wnse')
        self.custom_column_var = tk.StringVar()
        custom_column_entry = ttk.Entry(self, textvariable=self.custom_column_var)
        custom_column_entry.grid(row=11, column=0, sticky='wnse')
        #分隔符
        sep = ttk.Separator(self, orient=tk.HORIZONTAL)
        sep.grid(row=12, column=0, sticky='wnse',pady=5)
        #设置代理
        ttk.Label(self, text="设置代理").grid(row=13, column=0, sticky='wnse')
        self.proxy_var = tk.StringVar()
        proxy_entry = ttk.Entry(self, textvariable=self.proxy_var)
        proxy_entry.grid(row=14, column=0, sticky='wnse')
        #代理身份验证
        ttk.Label(self, text="代理身份验证").grid(row=15, column=0, sticky='wnse')
        self.proxy_cred_var = tk.StringVar()
        proxy_cred_entry = ttk.Entry(self, textvariable=self.proxy_cred_var)
        proxy_cred_entry.grid(row=16, column=0, sticky='wnse')

        ## 枚举功能
        #当前用户
        self.current_user_var = tk.BooleanVar()
        current_user_checkbutton = ttk.Checkbutton(self, text="当前用户", variable=self.current_user_var)
        current_user_checkbutton.grid(row=0, column=2, sticky='wnse')
        #当前数据库
        self.current_db_var = tk.BooleanVar()
        current_db_checkbutton = ttk.Checkbutton(self, text="当前数据库", variable=self.current_db_var)
        current_db_checkbutton.grid(row=0, column=3, sticky='wnse')
        #检查权限
        self.is_dba_var = tk.BooleanVar()
        is_dba_checkbutton = ttk.Checkbutton(self, text="当前用户是否有DBA权限", variable=self.is_dba_var)
        is_dba_checkbutton.grid(row=0, column=4, sticky='wnse')
        #枚举库名
        self.dbs_var = tk.BooleanVar()
        dbs_checkbutton = ttk.Checkbutton(self, text="枚举库名", variable=self.dbs_var)
        dbs_checkbutton.grid(row=0, column=5, sticky='wnse')
        #枚举表名
        self.tables_var = tk.BooleanVar()
        tables_checkbutton = ttk.Checkbutton(self, text="枚举表名", variable=self.tables_var)
        tables_checkbutton.grid(row=0, column=6, sticky='wnse')
        #枚举列名
        self.columns_var = tk.BooleanVar()
        columns_checkbutton = ttk.Checkbutton(self, text="枚举列名", variable=self.columns_var)
        columns_checkbutton.grid(row=0, column=7, sticky='wnse')
        #枚举字段
        self.dump_var = tk.BooleanVar()
        dump_checkbutton = ttk.Checkbutton(self, text="枚举字段", variable=self.dump_var)
        dump_checkbutton.grid(row=1, column=2, sticky='wnse')
        #一键脱库
        self.dump_all_var = tk.BooleanVar()
        dump_all_checkbutton = ttk.Checkbutton(self, text="一键脱库", variable=self.dump_all_var)
        dump_all_checkbutton.grid(row=1, column=3, sticky='wnse')
        #OS交互式Shell
        self.os_shell_var = tk.BooleanVar()
        os_shell_checkbutton = ttk.Checkbutton(self, text="OS交互式Shell", variable=self.os_shell_var)
        os_shell_checkbutton.grid(row=1, column=4, sticky='wnse')
        #SQL交互式Shell
        self.sql_shell_var = tk.BooleanVar()
        sql_shell_checkbutton = ttk.Checkbutton(self, text="SQL交互式Shell", variable=self.sql_shell_var)
        sql_shell_checkbutton.grid(row=1, column=5, sticky='wnse')
        #一键去特征
        self.random_agent_var = tk.BooleanVar()
        random_agent_checkbutton = ttk.Checkbutton(self, text="一键去特征", variable=self.random_agent_var)
        random_agent_checkbutton.grid(row=1, column=6, sticky='wnse')
        #打开所有优化开关
        self.optimizations_var = tk.BooleanVar()
        optimizations_checkbutton = ttk.Checkbutton(self, text="打开所有优化开关", variable=self.optimizations_var)
        optimizations_checkbutton.grid(row=1, column=7, sticky='wnse')
        #默认应答
        self.batch_var = tk.BooleanVar()
        batch_checkbutton = ttk.Checkbutton(self, text="默认应答", variable=self.batch_var)
        batch_checkbutton.grid(row=2, column=2, sticky='wnse')
        #清除缓存
        self.purge_var = tk.BooleanVar()
        purge_checkbutton = ttk.Checkbutton(self, text="清除缓存", variable=self.purge_var)
        purge_checkbutton.grid(row=2, column=3, sticky='wnse')
        #强制SSL协议
        self.ssl_var = tk.BooleanVar()
        ssl_checkbutton = ttk.Checkbutton(self, text="强制SSL协议", variable=self.ssl_var)
        ssl_checkbutton.grid(row=2, column=4, sticky='wnse')
        # 竖着的分隔符
        sep = ttk.Separator(self, orient=tk.VERTICAL)
        sep.grid(row=0, column=8, sticky='wnse',rowspan=18)

        #注入类型
        techniques = ["", "全选", "盲注", "报错注入", "堆叠注入", "联合查询注入", "时间注入", "内联查询注入"]
        self.technique_var = tk.StringVar(value=techniques[0])
        ttk.Label(self, text="注入类型").grid(row=0, column=9, sticky='wnse')
        technique_combo = ttk.Combobox(self, values=techniques, textvariable=self.technique_var)
        technique_combo.grid(row=1, column=9, sticky='wnse')


        #指定数据库类型
        dbmss = ["", " Altibase", " Amazon Redshift", " Apache Derby", " Apache Ignite", " Aurora", " ClickHouse",
                 " CockroachDB", " CrateDB", " Cubrid", " Drizzle", " EnterpriseDB", " eXtremeDB", " Firebird",
                 " FrontBase", " Greenplum", " H2", " HSQLDB", " IBM DB2", " Informix", " InterSystems Cache", " Iris",
                 " MariaDB", " Mckoi", " MemSQL", " Microsoft Access", " Microsoft SQL Server", " MimerSQL", " MonetDB",
                 " MySQL", " OpenGauss", " Oracle", " Percona", " PostgreSQL", " Presto", " Raima Database Manager",
                 " SAP MaxDB", " SQLite", " Sybase", " TiDB", " Vertica", " Virtuoso", " Yellowbrick", " YugabyteDB"]
        self.dbms_type_var = tk.StringVar(value=techniques[0])
        ttk.Label(self, text="指定数据库类型").grid(row=2, column=9, sticky='wnse')
        dbms_type_entry = ttk.Combobox(self, values=dbmss, textvariable=self.dbms_type_var)
        dbms_type_entry.grid(row=3, column=9, sticky='wnse')
        #自定义参数
        ttk.Label(self, text="自定义参数").grid(row=4, column=9, sticky='wnse')
        self.custom_param_var = tk.StringVar()
        custom_param_entry = ttk.Entry(self, textvariable=self.custom_param_var)
        custom_param_entry.grid(row=5, column=9, sticky='wnse')
        #指定注入参数
        ttk.Label(self, text="指定注入参数").grid(row=6, column=9, sticky='wnse')
        self.testable_param_var = tk.StringVar()
        testable_param_entry = ttk.Entry(self, textvariable=self.testable_param_var)
        testable_param_entry.grid(row=7, column=9, sticky='wnse')


        ##数据显示
        self.command_output = tk.Text(self, wrap='word',height=1)
        self.command_output.insert("1.0", "执行的sqlmap语句")
        self.command_output.grid(row=3, column=2, sticky='wnse',columnspan=5,rowspan=2)
        ##执行
        run_button = ttk.Button(self, text="开始运行",command=self.run_command)
        run_button.grid(row=3, column=7, sticky='wnse',rowspan=2)
        ## 帮助
        sqlmap_help_button= ttk.Button(self, text="sqlmap帮助",command=self.sqlmap_help)
        sqlmap_help_button.grid(row=5, column=7, sticky='wnse',rowspan=2)
        # 横着的分隔符
        sep = ttk.Separator(self, orient=tk.HORIZONTAL)
        sep.grid(row=5, column=2, sticky='wnse',pady=10, columnspan=5)
        ## 数据输入

        self.sqlmap_text=tk.Text(self,wrap='word')
        self.sqlmap_text.grid(row=6, column=1, sticky='wnse',columnspan=6,rowspan=14)
    ##sqlmap帮助
    def sqlmap_help(self):
        cmd = ["python", "-Xfrozen_modules=off", "sqlmap.py", "-hh"]
        os.system(" ".join(cmd))
    #基础扫描
    def run_command(self):
        # --
        options1={
        'level': self.level_var.get(),
        'risk': self.risk_var.get(),
        'threads': self.threads_var.get(),
        'current-db': self.current_db_var.get(),
        'current-user': self.current_user_var.get(),
        'is-dba': self.is_dba_var.get(),
        'dbs': self.dbs_var.get(),
        'tables': self.tables_var.get(),
        'columns': self.columns_var.get(),
        'dump': self.dump_var.get(),
        'dump-all': self.dump_all_var.get(),
        'os-shell': self.os_shell_var.get(),
        'sql-shell': self.sql_shell_var.get(),
        'proxy': self.proxy_var.get(),
        'proxy-cred': self.proxy_cred_var.get(),
        'batch': self.batch_var.get(),
        'purge': self.purge_var.get(),
        'force-ssl' : self.ssl_var.get()
        }
        #-
        options2 = {
            'D': self.custom_db_var.get(),
            'T': self.custom_table_var.get(),
            'C': self.custom_column_var.get(),
            'o': self.optimizations_var.get(),
            'p': self.testable_param_var.get()
        }
        cmd = ["start", "cmd", "/k", "python", "-Xfrozen_modules=off", "sqlmap.py"]
        #判断是否使用url进行扫描
        if "http" in self.sqlmap_text.get("1.0","1.5"):
            cmd.append("-u")
            cmd.append(self.sqlmap_text.get("1.0","end-1c"))
        else:
            with open("url.txt","w",encoding="utf-8") as f:
                f.write(self.sqlmap_text.get("1.0","end-1c"))
            cmd.append("-r url.txt")

        #添加参数
        for option, value in options1.items():
            if value:
                cmd.append(f"--{option.replace('_','-')}")
                if str(value).lower() != 'true':
                    cmd.append(str(value))

        for option, value in options2.items():
            if value:
                cmd.append(f"-{option.replace('_', '-')}")
                if str(value).lower() != 'true':
                    cmd.append(str(value))

        if self.random_agent_var.get():
            cmd.extend(["--random-agent", "--tamper=between", "--flush-session", "--randomize=1"])

        #自定义参数
        if self.custom_param_var.get():
            cmd.append(str(self.custom_param_var.get()))
        #数据库类型
        if self.dbms_type_var.get():
            cmd.append("--dbms=" + str(self.dbms_type_var.get()))
        #注入类型
        if self.technique_var.get():
            cmd.append("--technique="+self.get_technique())


        ##命令执行
        os.system(" ".join(cmd))
        display=[part for part in cmd if part not in ["start", "cmd", "/k", "-Xfrozen_modules=off"]]
        self.command_output.delete(1.0, tk.END)
        self.command_output.insert(tk.END, " ".join(display))

        #执行完成后，将有漏洞的记录转移到新日志目录
        source_path = f"/Users/{getpass.getuser()}/.local/share/sqlmap/output"
        dest_path = f"/Users/{getpass.getuser()}/.local/share/sqlmap/vulnout"
        self.move_log_directories(source_path,dest_path)

    #筛选有漏洞的目标记录
    def move_log_directories(self,source_dir, target_dir):
        #  检查目标目录是否存在，如果不存在则创建
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        #  遍历源目录下的所有文件和子目录
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                #  检查文件是否是log文件
                if 'log' in file:
                    file_path = os.path.join(root, file)
                    #  检查.log文件是否有内容
                    if os.path.getsize(file_path) > 0:
                        #  移动包含.log文件的整个目录到目标目录
                        parent_dir = os.path.dirname(file_path)
                        shutil.move(parent_dir, target_dir)
    def get_technique(self):
        techniques_dict = {
            "全选": "BESUTQ",
            "盲注": "B",
            "报错注入": "E",
            "堆叠注入": "S",
            "联合查询注入": "U",
            "时间注入": "T",
            "内联查询注入": "Q"
        }
        return techniques_dict.get(self.technique_var.get(),'')







# 页面二
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="历史记录")
        label.grid(row=0, column=0, sticky='w')
        #刷新按钮
        refresh_button=ttk.Button(self, text="刷新", command=self.refresh)
        refresh_button.grid(row=0, column=1, sticky='w')
        #查看
        get_button=ttk.Button(self, text="查询", command=self.get)
        get_button.grid(row=0, column=2, sticky='w')
        self.target_log = tk.StringVar()
        #读取有漏洞的历史记录
        self.target_path = f"/Users/{getpass.getuser()}/.local/share/sqlmap/vulnout"
        file_list=os.listdir(self.target_path)
        log_combo = ttk.Combobox(self, values=[str(i) for i in file_list], textvariable=self.target_log,width=30,state='readonly')
        log_combo.grid(row=1, column=0, sticky='n',columnspan=3,rowspan=1)

        ##数据输出框
        self.log_output_text = tk.Text(self,width=80,height=40)
        self.log_output_text.grid(row=1, column=5, sticky='w', rowspan=10,columnspan=5)
        #读取log文件并输出
        self.log_file = tk.StringVar()
        if self.target_log.get():
            with open(f"{self.target_path}/{self.target_log.get()}/log","r",encoding="utf-8") as f:
                self.log_file.set(f.read())
                f.close()
                self.log_output_text.insert(tk.END, self.log_file.get())

    def refresh(self):
        #重建一个单选框
        self.target_path = f"/Users/{getpass.getuser()}/.local/share/sqlmap/vulnout"
        file_list=os.listdir(self.target_path)
        log_combo = ttk.Combobox(self, values=[str(i) for i in file_list], textvariable=self.target_log,width=30,state='readonly')
        log_combo.grid(row=1, column=0, sticky='n',columnspan=3,rowspan=1)
    def get(self):
        if self.target_log.get():
            with open(f"{self.target_path}/{self.target_log.get()}/log","r",encoding="utf-8") as f:
                self.log_file.set(f.read())
                f.close()
                self.log_output_text.delete(1.0, tk.END)
                self.log_output_text.insert(tk.END, self.log_file.get())

# 页面三
# class Page3(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="功能3")
#         label.grid(row=0, column=0, sticky='nsew')


if __name__ == "__main__":
    app = Application()
    app.mainloop()
