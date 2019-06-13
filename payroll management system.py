import time
import datetime
from tkinter import*

root = Tk()
root.title("Payroll Management System")#for title
root.geometry('1350x650+0+0')
#=======================================================================for frame======================================================================
Tops = Frame(root, width=1350, height=50,bd=8, relief="raise")
Tops.pack(side=TOP)#first frame
f1 = Frame(root, width=600, height=600,bd=8, relief="raise")
f1.pack(side=LEFT)#second frame
f2 = Frame(root, width=300, height=700,bd=8, relief="raise")
f2.pack(side=RIGHT)#third frame

fla = Frame(f1, width=600, height=200,bd=20, relief="raise")
fla.pack(side=TOP)
flb = Frame(f1, width=600, height=600,bd=20, relief="raise")
flb.pack(side=TOP)

lblinfo=Label(Tops, font=('arial',60, 'bold'), text="   Payroll Management System   " ,bd=10)
lblinfo.grid(row=0,column=0)

def iExit():
    qExit=messagebox.askyesno("Payroll Management System","Do you want to exit")
    if qExit>0:
        root.destroy()
        return

def Reset():
    Name.set("")
    Address.set("")
    Employer.set("")
    Number.set("")
    HoursWorked.set("")
    HourlyRate.set("")
    Tax.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    WeekyWages.set("")
    txtPaySlip.delete("1.0",END)

def EnterInfo():
    txtPaySlip.insert(END,"\t\tPaySlip\n\n")
    txtPaySlip.insert(END,"Name\t\t"+Name.get()+"\n\n")
    txtPaySlip.insert(END,"Address\t\t"+Address.get()+"\n\n")
    txtPaySlip.insert(END,"Employer\t\t"+Employer.get()+"\n\n")
    txtPaySlip.insert(END,"Number\t\t"+Number.get()+"\n\n")
    txtPaySlip.insert(END,"HoursWorked\t\t"+HoursWorked.get()+"\n\n")
    txtPaySlip.insert(END,"HourlyRate\t\t"+HourlyRate.get()+"\n\n")
    txtPaySlip.insert(END,"Tax\t\t"+Tax.get()+"\n\n")
    txtPaySlip.insert(END,"OverTime\t\t"+OverTime.get()+"\n\n")
    txtPaySlip.insert(END,"NetPay\t\t"+NetPay.get()+"\n\n")
    txtPaySlip.insert(END,"GrossPay\t\t"+GrossPay.get()+"\n\n")

def WeeklyWages():
    HoursWorkedPerWeek=float(HoursWorked.get())
    WagesPerHours=float(HourlyRate.get)
    paydue=WagesPerHour*HoursWorkedPerWeek
    PaymentDue="$", str('%.2f' %(paydue))
    NetPay.set(PaymentDue)

    Tax =paydue*0.2
    Taxables="$", str ('%.2f' %(tax))
    Tax.set(NetPays)

    if HoursWorkedPerWeek>40:
        overTimeHours=(HoursWorkedPerWeek-40)+WagesPerHours * 1.5
        overtimehrs="$", str('%0.2f' %(overTimeHours))
        OverTime.set(overtimehrs)
    elif HoursWorkedPerWeek<= 40:
        overTimePay=(HoursWorkedPerWeek-40)+WagesPerHours*1.5
        overTimehrs="$",str('%.2f' %(overtimePay))
        OverTime.set(overtimehrs)
    return
    
    
        


    
    


    
    
    
    
#======================================================================variables=====================================================================
Name=StringVar()
Address=StringVar()
Employer=StringVar()
Number=StringVar()
HoursWorked=StringVar()
HourlyRate=StringVar()
Tax=StringVar()
OverTime=StringVar()
GrossPay=StringVar()
NetPay=StringVar()
DateOfOrder=StringVar()
TimeOfOrder=StringVar()
WeekyWages=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))
#=====================================================================for labels======================================================================
lblName=Label(fla, text="Name", font=('arial',16, 'bold'),bd=20).grid(row=0,column=0)
lblAddress=Label(fla, text="Address", font=('arial',16, 'bold'),bd=20).grid(row=0,column=2)
lblEmployer=Label(fla, text="Employer", font=('arial',16, 'bold'),bd=20).grid(row=1,column=0)
lblNumber=Label(fla, text="Number", font=('arial',16, 'bold'),bd=20).grid(row=1,column=2)
lblHoursWorked=Label(fla, text="HoursWorked", font=('arial',16, 'bold'),bd=20).grid(row=2,column=0)
lblHourlyRate=Label(fla, text="HourlyRate", font=('arial',16, 'bold'),bd=20).grid(row=2,column=2)
lblTax=Label(fla, text="Tax", font=('arial',16, 'bold'),bd=20, anchor='w').grid(row=3,column=0)
lblOverTime=Label(fla, text="OverTime", font=('arial',16, 'bold'),bd=20).grid(row=3,column=2)
lblGrossPay=Label(fla, text="GrossPay", font=('arial',16, 'bold'),bd=20).grid(row=4,column=0)
lblNetPay=Label(fla, text="NetPay", font=('arial',16, 'bold'),bd=20).grid(row=4,column=2)
#==============================================================================for entry==============================================================
etxtName= Entry(fla,textvariable=Name,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtName.grid(row=0,column=1)
etxtAddress= Entry(fla,textvariable=Address,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtAddress.grid(row=0,column=3)
etxtEmployer= Entry(fla,textvariable=Employer,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtEmployer.grid(row=1,column=1)
etxtNumber= Entry(fla,textvariable=Number,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtNumber.grid(row=1,column=3)
etxtHoursWorked= Entry(fla,textvariable=HoursWorked,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtHoursWorked.grid(row=2,column=1)
etxtHourlyRate= Entry(fla,textvariable=HourlyRate,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtHourlyRate.grid(row=2,column=3)
etxtTax= Entry(fla,textvariable=Tax,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtTax.grid(row=3,column=1)
etxtOverTime= Entry(fla,textvariable=OverTime,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtOverTime.grid(row=3,column=3)
etxtGrossPay= Entry(fla,textvariable=GrossPay,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtGrossPay.grid(row=4,column=1)
etxtNetPay= Entry(fla,textvariable=NetPay,  font=('arial',16, 'bold'),bd=16, width=22, justify='left')
etxtNetPay.grid(row=4,column=3)
#============================================================for text====================
lblPaySlip=Label(f2, textvariable=DateOfOrder, font=('arial',21, 'bold')).grid(row=0,column=0)
txtPaySlip=Text(f2, height=22, width=34, bd=16, font=('arial',12, 'bold'))
txtPaySlip.grid(row=1,column=0)

#==========================================================buttons=============================
btnSalary=Button(flb, text='Weekly Salary',  padx=16,pady=16,bd=8, fg="black",
                 font=('arial',16, 'bold'),height=1, width=14,command=WeeklyWages).grid(row=0,column=0)
btnReset=Button(flb, text='Reset',  padx=16,pady=16,bd=8, fg="black",
                 font=('arial',16, 'bold'),height=1, width=14,command=Reset).grid(row=0,column=1)                 
btnPaySlip =Button(flb, text='View PaySlip', padx=16,pady=16,bd=8, fg="black",
                 font=('arial',16, 'bold'),height=1, width=14,command=EnterInfo).grid(row=0,column=2)
btnExit=Button(flb, text='Exit system',  padx=16,pady=16,bd=8, fg="black",
                 font=('arial',16, 'bold'),height=1, width=14,command=iExit).grid(row=0,column=3)



























root.mainloop()
