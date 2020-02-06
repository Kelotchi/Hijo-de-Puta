from tkinter import *
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt
from tkinter import messagebox
import pandas as pd



root = Tk()
root.title('Graph Analizer')
root.geometry("1100x600")

DF = [] # Lista en donde se guardan los dataframes de los csv seleccionados

# Funcion para seleccionar programa
def Programas(s):
    open = messagebox.askquestion('Adding graph', 'Do you want more graphs?',)
    while open == 'yes':
        file = askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
        if s == 'Agilent 1':
            df = pd.read_csv(file, header=None, names=['Temperatura', 'Frecuencia', 'Capacitancia', 'Conductancia'])
        elif s == 'Agilent 3':
            df = pd.read_csv(file, header=None, names=['Temperatura', 'Capacitancia', 'Conductancia', 'Frecuencia'])
        elif s == 'Agilent 4':
            df = pd.read_csv(file, header=None, names=['Voltaje (Vds)', 'Capacitancia'])
        elif s == 'Agilent 5':
            df = pd.read_csv(file, header=None, names=['Capacitancia', 'Conductancia', 'Frecuencia'])
        elif s == 'Agilent 6':
            df = pd.read_csv(file, header=None, names=['Voltaje (Vds)', 'Capacitancia'])
        elif s == 'Agilent 7':
            df = pd.read_csv(file, header=None, names=['Voltaje (Vds)', 'Capacitancia', 'Frecuencia'])
        elif s == 'Agilent 8':
            df = pd.read_csv(file, header=None, names=['Capacitancia', 'Condictancia', 'Frecuencia', 'Voltaje (Vds)'])
        elif s == 'Agilent 9':
            df = pd.read_csv(file, header=None, names=['Frecuencia', 'Capacitancia', 'Conductancia'])
        elif s == 'Current temp nanovolt':
            df = pd.read_csv(file, header=None, names=['Temperatura', 'Voltaje (Vds)'])
        elif s == 'Current with temp with fixed voltage':
            df = pd.read_csv(file, header=None, names=['Temperatura', 'Corriente (Ids)'])
        elif s == 'Current with time with fixed voltage':
            df = pd.read_csv(file, header=None, names=['Corriente (Ids)', 'Tiempo'])
        elif s == 'Current with time with fixed voltage + gatesweep':
            df = pd.read_csv(file, header=None, names=['Corriente (Ids)', 'Tiempo', 'Voltaje (Vgs)', 'Corriente (Igs)'])
        elif s == 'FVMI3':
            df = pd.read_csv(file, header=None, names=['Voltaje (Vds)', 'Corriente (Ids)'])
        elif s == 'FVMI3 + Sourcemeter1':
            df = pd.read_csv(file, header=None,
                             names=['Voltaje (Vds)', 'Corriente (Ids)', 'Voltaje (Vgs)', 'Corriente (Igs)'])
            df.loc[:, [Y_axis.get()]] *= y
            df.loc[:,[X_axis.get()]] *= x
            fig, ax = plt.subplots()
            plt.scatter(df[X_axis.get()], df[Y_axis.get()], c=df[Z_axis.get()], cmap='jet')
            plt.xlabel(entry_6.get())
            plt.ylabel(entry_7.get())
            cbar = plt.colorbar()
            cbar.set_label(entry_8.get(), rotation=270, labelpad=15)
            plt.show()
            break
        elif s == 'FVMI9':
            df = pd.read_csv(file, header=None, names=['Voltaje (Vds)', 'Corriente (Ids)'])
        elif s == 'FVMI9 + Sourcemeter1':
            df = pd.read_csv(file, header=None,
                             names=['Voltaje (Vds)', 'Corriente (Ids)', 'Voltaje (Vgs)', 'Corriente (Igs)'])

        elif s == 'Sourcemeter1':
            df = pd.read_csv(file, header=None,
                             names=['Voltaje (Vgs)', 'Corriente (Igs)', 'Voltaje (Vgs2)', 'Corriente (Ids)'])
        elif s == 'Sourcemter1 with temp control':
            df = pd.read_csv(file, header=None,
                             names=['Voltaje (Vgs)', 'Corriente (Igs)', 'Voltaje (Vgs2)', 'Corriente (Ids)', 'Temperatura'])
            df.loc[:, [Y_axis.get()]] *= y
            df.loc[:, [X_axis.get()]] *= x
            fig, ax = plt.subplots()
            plt.scatter(df[X_axis.get()], df[Y_axis.get()], c=df[Z_axis.get()], cmap='jet')
            plt.xlabel(entry_6.get())
            plt.ylabel(entry_7.get())
            cbar = plt.colorbar()
            cbar.set_label(entry_8.get(), rotation=270, labelpad=15)
            plt.show()
            break

        df.loc[:,[Y_axis.get()]] *= y
        df.loc[:,[X_axis.get()]] *= x
        DF.append(df)
        open = messagebox.askquestion('Adding graph', 'Do you want more graphs?')
    if open == 'no':
      for i in DF:
        plt.plot(i[X_axis.get()], i[Y_axis.get()],)
        plt.xlabel(entry_6.get())
        plt.ylabel(entry_7.get())
    plt.show()





k = StringVar(value="Programas")

Calculos = OptionMenu(root, k, 'Agilent 1', 'Agilent 3', 'Agilent 4', 'Agilent 5', 'Agilent 6', 'Agilent 7',
                      'Agilent 8',
                      'Agilent 9', 'Current temp nanovolt', "Current with temp with fixed voltage",
                      "Current with time with fixed voltage", "Current with time with fixed voltage + gatesweep",
                      "FVMI3", "FVMI3 + Sourcemeter1", "FVMI9", "FVMI9 + Sourcemeter1", "Sourcemeter1", \
                      'Sourcemter1 with temp control', command=Programas)
Calculos.grid(row=1, column=1, padx=15, pady=5)


# Tercer Cuadrante
Mob = []
z = []
def Plot():
    x = 0
    for i in Mob:
        x += 1
        z.append(x)
    plt.plot(z, Mob, 'o')
    plt.show()

def Ecuaciones (s):
    if s == 'Mobilidad':

        def Mobilidad ():
            gm = float(entry_3.get())
            L = float(entry_4.get())
            W = float(entry_5.get())
            Ci = float(entry_6.get())
            Vds = float(entry_7.get())

            entry_8.delete(0, END)
            entry_8.insert(0, (gm*L)/(W*Ci*Vds))
            Mob.append(entry_8.get())

        Label_8 = Label(root, text='Slope').grid(row=55, column=7)
        Label_9 = Label(root, text='Lenght').grid(row=56, column=7)
        Label_10 = Label(root, text='Width').grid(row=57, column=7)
        Label_11 = Label(root, text='Specific Capacitance').grid(row=58, column=7)
        Label_12 = Label(root, text='Voltage (Vds)').grid(row=59, column=7)

        entry_3 = Entry(root)
        entry_3.grid(row=55, column=8)
        entry_4 = Entry(root)
        entry_4.grid(row=56, column=8)
        entry_5 = Entry(root)
        entry_5.grid(row=57, column=8)
        entry_6 = Entry(root)
        entry_6.grid(row=58, column=8)
        entry_7 = Entry(root)
        entry_7.grid(row=59, column=8)
        entry_8 = Entry(root)
        entry_8.grid(row=60, column=8)

        button_19 = Button(root, text='Result', command=Mobilidad).grid(row=60, column=7)
        button_20 = Button(root, text="Plot", command=Plot).grid(row=61,column=7)

    elif s == 'Conductividad':

        Label_8 = Label(root, text='Resistance').grid(row=55, column=7)
        Label_9 = Label(root, text='Length').grid(row=56, column=7)
        Label_10 = Label(root, text='Width').grid(row=57, column=7)
        Label_11 = Label(root, text='Height').grid(row=58, column=7)


                                    # Drop Menu para los diferentes Calculos

k = StringVar(value="Ecuaciones")

Calculos = OptionMenu(root, k, 'Mobilidad', 'Conductividad',command=Ecuaciones)
Calculos.grid(row=55, column=6)


######
Label_1 = Label(root, text="Selecting axis").grid(row=55, padx=5, pady=5)
Label_2 = Label(root, text="Y axis").grid(row=54, column=3, padx=5, pady=5)
Label_6 = Label(root, text="X axis").grid(row=54, column=1, padx=5, pady=5)
Label_6 = Label(root, text="Z axis").grid(row=54, column=5, padx=5, pady=5)
Label_5 = Label(root, text='Chart Setting').grid(row=50, column=3, pady=20)
Label_7 = Label(root, text = 'Calculos:').grid(row=54, column=6)
Label_13 = Label(root, text='Axis names').grid(row=56, padx=5, pady=5)

# Drop Menu para los titulos de los Ejes
x = 0
y = 0
def Y_Units(s):
    global y
    if s == 'none':
        y = 1
    elif s == 'mili':
        y = 1e3
    elif s == 'micro':
        y = 1e6
    elif s == 'nano':
        y = 1e9
    elif s == 'pico':
        y = 1e12
    return y

def X_Units(s):
    global x
    if s == 'none':
        x =1
    elif s == 'mili':
        x = 1e3
    elif s == 'micro':
        x = 1e6
    elif s == 'nano':
        x = 1e9
    elif s == 'pico':
        x = 1e12

    return x



X_axis = StringVar(root)
Y_axis = StringVar(root)
Z_axis = StringVar(root)
X_units = StringVar(root)
Y_units = StringVar(root)


entry_1 = OptionMenu(root, X_axis, "Voltaje (Vds)", "Corriente (Ids)", "Voltaje (Vgs)", 'Corriente (Igs)', 'Tiempo',
               'Temperatura', 'Frecuencia', 'Capacitancia', 'Conductancia')
entry_1.grid(row=55, column=1, padx=5, pady=5, ipadx=5)

entry_2 = OptionMenu(root, Y_axis, "Voltaje (Vds)", "Corriente (Ids)", "Voltaje (Vgs)", 'Corriente (Igs)', 'Tiempo',
               'Temperatura', 'Frecuencia', 'Capacitancia', 'Conductancia')
entry_2.grid(row=55, column=3, padx=5, pady=5, ipadx=5)

entry_3 = OptionMenu(root, Z_axis, "Voltaje (Vds)", "Corriente (Ids)", "Voltaje (Vgs)", 'Corriente (Igs)', 'Tiempo',
               'Temperatura', 'Frecuencia', 'Capacitancia', 'Conductancia')
entry_3.grid(row=55, column=5, padx=5, pady=5, ipadx=5)

entry_4 = OptionMenu(root, X_units,'none', 'mili','micro','nano','pico', command=X_Units)
entry_4.grid(row=55, column=2, padx=5, pady=5, ipadx=5)

entry_5 = OptionMenu(root, Y_units,'none', 'mili','micro','nano','pico', command=Y_Units)
entry_5.grid(row=55, column=4, padx=5, pady=5, ipadx=5)

entry_6 = Entry(root)
entry_6.grid(row=56, column=1, padx=5, pady=5)
entry_7 = Entry(root)
entry_7.grid(row=56, column=3, padx=5, pady=5)
entry_8 = Entry(root)
entry_8.grid(row=56, column=5, padx=5, pady=5)







root.mainloop()
