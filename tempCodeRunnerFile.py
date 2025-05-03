from tkinter import messagebox
subcode = cursor[0][0]
cur1 = conn.execute(F"SELECT SUBTYPE FROM SUBJECTS WHERE SUBCODE='{subcode}'")
cur1 = list(cur1)
subtype = cur1[0][0]
butt_grid[i][j]['fg'] = 'black' 
if subtype == 'T':
    butt_grid[i][j]['bg'] = 'green'
elif subtype == 'P':
    butt_grid[i][j]['bg'] = 'blue'

    butt_grid[i][j]['text'] = str(cursor[0][0]) + '\n' + str(cursor[0][1])
    butt_grid[i][j].update()
    print(i, j, cursor[0][0])
else:
    butt_grid[i][j]['fg'] = 'black'
    butt_grid[i][j]['text'] = "No Class"
    butt_grid[i][j].update()



def process_button(d, p, sec):
    details = tk.Tk()
    cursor = conn.execute(f"SELECT SUBCODE, FINI FROM SCHEDULE\
                WHERE ID='{section+str((d*periods)+p)}'")
    cursor = list(cursor)
    if len(cursor) != 0:
        subcode = str(cursor[0][0]) 
        fini =  str(cursor[0][1])

        cur1 = conn.execute(f"SELECT SUBNAME, SUBTYPE FROM SUBJECTS\
            WHERE SUBCODE='{subcode}'")
        cur1 = list(cur1)
        subname = str(cur1[0][0])
        subtype = str(cur1[0][1])

        cur2 = conn.execute(f"SELECT NAME, EMAIL FROM FACULTY\
            WHERE INI='{fini}'")
        cur2 = list(cur2)
        fname = str(cur2[0][0])
        femail = str(cur2[0][1]) 

        if subtype == 'T':
            subtype = 'Theory'
        elif subtype == 'P':
            subtype = 'Practical'

    else:
        subcode = fini = subname = subtype = fname = femail = 'None'

    print(subcode, fini, subname, subtype, fname, femail)
    tk.Label(details, text='Class Details', font=('Consolas', 15, 'bold')).pack(pady=15)
    tk.Label(details, text='Day: '+day_names[d], font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Period: '+str(p+1), font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subject Code: '+subcode, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subect Name: '+subname, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Subject Type: '+subtype, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Initials: '+fini, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Name: '+fname, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)
    tk.Label(details, text='Faculty Email: '+femail, font=('Consolas'), anchor="w").pack(expand=1, fill=tk.X, padx=20)

    tk.Button(
        details,
        text="OK",
        font=('Consolas'),
        width=10,
        command=details.destroy
    ).pack(pady=10)

    details.mainloop()



def student_tt_frame(tt, sec):
    title_lab = tk.Label(
        tt,
        text='T  I  M  E  T  A  B  L  E',
        font=('Consolas', 20, 'bold'),
        pady=5
    )
    title_lab.pack()

    legend_f = tk.Frame(tt)
    legend_f.pack(pady=15)
    tk.Label(
        legend_f,
        text='Legend: ',
        font=('Consolas', 10, 'italic')
    ).pack(side=tk.LEFT)

    tk.Label(
        legend_f,
        text='Theory Classes',
        bg='green',
        fg='white',
        relief='raised',
        font=('Consolas', 10, 'italic'),
        height=2
    ).pack(side=tk.LEFT, padx=10)

    tk.Label(
        legend_f,
        text='Practical Classes',
        bg='blue',
        fg='white',
        relief='raised',
        font=('Consolas', 10, 'italic'),
        height=2
    ).pack(side=tk.LEFT, padx=10)
    
    global butt_grid
    global section
    section = sec

    table = tk.Frame(tt)
    table.pack()

    first_half = tk.Frame(table)
    first_half.pack(side='left')

    short_frame = tk.Frame(table)
    short_frame.pack(side='left')

    second_half = tk.Frame(table)
    second_half.pack(side='left')

    lunch_frame = tk.Frame(table)
    lunch_frame.pack(side='left')

    third_half = tk.Frame(table)
    third_half.pack(side='left')

    short = tk.Label()
