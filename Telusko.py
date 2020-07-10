# ctrl + space gives you list of commands you can use

'''
import math
print(math.sqrt(25))
print('The floor value of 3 .8 is ' , math.floor(3.8))               
print('The ceiling value of 3.8 is ', math.ceil(3.8))             #basically rounding off to its nearest value
'''

'''
import math as m       #no need to write math like above
print(m.sqrt(81))
'''
'''
a  = int(input('Enter the number you want to find the cube of: '))
b = a**3
print('The cube of ', str(a) + ' is', b)
'''
'''
a = int(input('Enter a number: '))
if a > 0:
    print('Number is positive')
else:
    print('negative')
'''
'''
i = 5
while i >= 1:
    print('Shaswot',i)
    i = i - 1
'''
# Code to print 1 to 100 but skip numbers divisible by 3 and 5
'''
for i in range(101):
    if i%3==0:
        continue
    if i%5==0:
        continue
    print (i)
'''
'''
for i in range(1,6):
    print('#'*5)
    i = i + 1
'''
'''
a = int(input('How many?'))
i = 1
while i <= a:
    if i == 80:
        break
    i += 1
    print ("here")
'''
'''
from array import *
vals = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(vals)
'''

'''
nums = [2,14,25,36,95]
nums.insert(2,77)
print(nums)
'''
'''
for i in range(3):
    for j in range(i+1):
        print('#', end = ' ')
    print()
'''
'''
for row in range(6):
    for column in range(7):
        if (row == 0 and column % 3 != 0) or (row == 1 and column % 3 == 0) or (row - column == 2) or (
                row + column == 8):
            print("*", end="")
        else:
            print(" ", end="")

    print()
'''



from tkinter import *
import tkinter.messagebox
# from tkinter import ttk     # for combobox
#from PIL import Image, ImageTk

#img2 = Image.open("C:/Users/Shaswot/Desktop/Supermarket Billing/aisle2.jpg")  # INSERTING A PICTURE
#pic2 = ImageTk.PhotoImage(img2)

#pic_show2 = Label(image=pic2)
#pic_show2.pack()
class Bill_system:
    def __init__(self, main):
        self.main = main
        self.main.geometry("1525x700+0+0")
        self.main.title("Welcome to the SuperMarket Billing System")

        title = Label(self.main,text="Nepal SuperMarket Billing",bd=10,relief="solid",bg="#808000",fg="#F7E7CE",font=("Arial", 28, "bold")).pack(fill=X)
        # =========================VARIABLES===================
        #== Food==
        self.pringles = IntVar()
        self.tuna = IntVar()
        self.oats = IntVar()
        self.cornflakes = IntVar()
        self.chnuggets = IntVar()
        self.momo = IntVar()

        #== Drinks ==
        self.cokefanta = IntVar()
        self.cider = IntVar()
        self.warsteiner = IntVar()
        self.juice = IntVar()
        self.natura = IntVar()
        self.lecoc = IntVar()

        #== Self - Care ==
        self.shampoo = IntVar()
        self.colgate = IntVar()
        self.radia = IntVar()
        self.nailpolish = IntVar()
        self.ketain = IntVar()
        self.facemask = IntVar()

        #== Tools ==
        self.hammer = IntVar()
        self.chainsaw = IntVar()
        self.drill = IntVar()
        self.nails = IntVar()
        self.toolbox = IntVar()
        self.pliers = IntVar()

        #== BILLING statement section ==
        self.total_food_price = StringVar()
        self.total_drink_price = StringVar()
        self.total_selfcare_price = StringVar()
        self.total_tool_price = StringVar()
        self.vat = StringVar()
        self.total = StringVar()

        #== Bill Details ==
        self.billnum = StringVar()
        self.date = StringVar()
        self.cashiername = StringVar()
        #self.billtxtarea = StringVar()


        # LabelFrame is basically a frame where you add your other attributes
        # ============ FRAME FROM DETAILS OF THE BILL =======

        a3 = LabelFrame(self.main,bd=12,relief="ridge", text="Bill Details",font=(" MS Serif",12,"bold"),fg="maroon")
        a3.place(x=0,y=80,relwidth=1)
            # ALL the attributes are within Frame a3..
        bill_num = Label(a3,text="Bill Number :",font=("arial",18,"bold"),fg="green").grid(row=0,column=0,padx=20)
        e2_bill_num = Entry(a3, width=15,textvariable=self.billnum, font="arial 15",bd=5).grid(row=0, column=1) # Here bd is border

        d_ate = Label(a3,text="Date :",font=("arial",18,"bold"),fg="green").grid(row=0,column=30,padx=100) # pad_x=100 is the space after bill num for date
        e3_date = Entry(a3, width=15,textvariable=self.date, font="arial 15",bd=5).place(x=580,y=0)

        cashier_n = Label(a3,text="Cashier's Name :",font=("Comic Sans MS",18,"italic"),fg="green").grid(row=0,column=80,padx=280)
        e4_c_name = Entry(a3,textvariable=self.cashiername, width=22, font="arial,17",bd=5).place(x=1150,y=0)


        # paid_by = Label(a3, text="Paid with :",font=("arial",18,"italic"),fg="red").grid(row=0,column=80,padx=230)
        # NEED TO PUT A CHECKBOX WITH CARD AND CREDIT CARD OPTION

        #============== Frame for the CATEGORIES =========== f1=food1, f2 =food2[setting the variables this way]

        a4 = LabelFrame(self.main,bd=10,relief="solid",text="Food",font=("Comic Sans MS",18,"bold"),fg="#003153")
        a4.place(x=10,y=170,width=305,height=350)

        #scroll_in_y1 = Scrollbar(a4, orient="vertical")  # SETTING UP A SCROLL BAR
        #self.siny = Text(a4, yscrollcommand=scroll_in_y1.set)
        #scroll_in_y1.grid(sticky="w")
        #scroll_in_y1.config(command=self.siny.yview)


        f1 = Label(a4,text="Pringles",font=("arial",10,"bold"),bg="white",fg="black")
        f1.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        f1_ent = Entry(a4,width=5,textvariable=self.pringles,font=("arial",10),bd=5,relief="sunken").grid(row=0,column=1,padx=120,pady=10)

        f2 = Label(a4, text="Canned Tuna", font=("arial", 10, "bold"), bg="white", fg="black")
        f2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        f2_ent = Entry(a4, width=5, textvariable=self.tuna,font=("arial", 10), bd=5, relief="sunken").grid(row=1, column=1, padx=120, pady=10)

        f3 = Label(a4, text="Oats", font=("arial", 10, "bold"), bg="white", fg="black")
        f3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        f3_ent = Entry(a4, width=5,textvariable=self.oats, font=("arial", 10), bd=5, relief="sunken").grid(row=2, column=1, padx=120, pady=10)

        f4 = Label(a4, text="Corn Flakes", font=("arial", 10, "bold"), bg="white", fg="black")
        f4.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        f4_ent = Entry(a4, width=5,textvariable=self.cornflakes, font=("arial", 10), bd=5, relief="sunken").grid(row=3, column=1, padx=120, pady=10)

        f5 = Label(a4, text="Ch.Nuggets", font=("arial", 10, "bold"), bg="white", fg="black")
        f5.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        f5_ent = Entry(a4, width=5,textvariable=self.chnuggets, font=("arial", 10), bd=5, relief="sunken").grid(row=4, column=1, padx=120, pady=10)

        f6 = Label(a4, text="Frozen Momo", font=("arial", 10, "bold"), bg="white", fg="black")
        f6.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        f6_ent = Entry(a4, width=5,textvariable=self.momo, font=("arial", 10), bd=5, relief="sunken").grid(row=5, column=1, padx=120, pady=10)

        # 2nd Category ==== DRINKS

        a5 = LabelFrame(self.main, bd=10, relief="solid", text="Drinks", font=("Comic Sans MS", 18, "bold"), fg="#003153")
        a5.place(x=320, y=170, width=305, height=350)

        d1 = Label(a5, text="Coke/Fanta/Sprite", font=("arial", 10, "bold"), bg="white", fg="black")
        d1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        d1_ent = Entry(a5, width=5,textvariable=self.cokefanta, font=("arial", 10), bd=5, relief="sunken").grid(row=0, column=1,padx=70, pady=10)

        d2 = Label(a5, text="Apple Cider", font=("arial", 10, "bold"), bg="white", fg="black")
        d2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        d2_ent = Entry(a5, width=5,textvariable=self.cider, font=("arial", 10), bd=5, relief="sunken").grid(row=1, column=1,padx=70, pady=10)

        d3 = Label(a5,text="Warsteiner Beer", font=("arial", 10, "bold"), bg="white", fg="black")
        d3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        d3_ent = Entry(a5, width=5,textvariable=self.warsteiner, font=("arial", 10), bd=5, relief="sunken").grid(row=2, column=1,padx=70, pady=10)

        d4 = Label(a5, text="Orange/Mango Juice", font=("arial", 10, "bold"), bg="white", fg="black")
        d4.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        d4_ent = Entry(a5, width=5,textvariable=self.juice, font=("arial", 10), bd=5, relief="sunken").grid(row=3, column=1, padx=70, pady=10)

        d5 = Label(a5, text="Nepal Ice Natura", font=("arial", 10, "bold"), bg="white", fg="black")
        d5.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        d5_ent = Entry(a5, width=5,textvariable=self.natura, font=("arial", 10), bd=5, relief="sunken").grid(row=4, column=1, padx=70, pady=10)

        d6 = Label(a5, text="Le Coq Cocktail", font=("arial", 10, "bold"), bg="white", fg="black")
        d6.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        d6_ent = Entry(a5, width=5,textvariable=self.lecoc, font=("arial", 10), bd=5, relief="sunken").grid(row=5, column=1,padx=70, pady=10)

        # 3rd Category==== SELF CARE

        a6 = LabelFrame(self.main, bd=10, relief="solid", text="Self-Care", font=("Comic Sans MS", 18, "bold"), fg="#003153")
        a6.place(x=630, y=170, width=305, height=350)

        sc1 = Label(a6, text="Beer Shampoo", font=("arial", 10, "bold"), bg="white", fg="black")
        sc1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        sc1_ent = Entry(a6, width=5,textvariable=self.shampoo, font=("arial", 10), bd=5, relief="sunken").grid(row=0, column=1, padx=70, pady=10)

        sc2 = Label(a6, text="Colgate", font=("arial", 10, "bold"), bg="white", fg="black")
        sc2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        sc2_ent = Entry(a6, width=5,textvariable=self.colgate, font=("arial", 10), bd=5, relief="sunken").grid(row=1, column=1, padx=70, pady=10)

        sc3 = Label(a6, text="RADIA Conditioner", font=("arial", 10, "bold"), bg="white", fg="black")
        sc3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        sc3_ent = Entry(a6, width=5,textvariable=self.radia, font=("arial", 10), bd=5, relief="sunken").grid(row=2, column=1, padx=70, pady=10)

        sc4 = Label(a6, text="JamBayla NailPolish", font=("arial", 10, "bold"), bg="white", fg="black")
        sc4.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        sc4_ent = Entry(a6, width=5,textvariable=self.nailpolish, font=("arial", 10), bd=5, relief="sunken").grid(row=3, column=1, padx=70, pady=10)

        sc5 = Label(a6, text="Keratin Cream", font=("arial", 10, "bold"), bg="white", fg="black")
        sc5.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        sc5_ent = Entry(a6, width=5,textvariable=self.ketain,font=("arial", 10), bd=5, relief="sunken").grid(row=4, column=1, padx=70, pady=10)

        sc6 = Label(a6, text="MUD Face Mask", font=("arial", 10, "bold"), bg="white", fg="black")
        sc6.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        sc6_ent = Entry(a6, width=5,textvariable=self.facemask, font=("arial", 10), bd=5, relief="sunken").grid(row=5, column=1, padx=70, pady=10)

        # 4th CATEGORY
        a7 = LabelFrame(self.main, bd=10, relief="solid", text="Tools", font=("Comic Sans MS", 18, "bold"), fg="#003153")
        a7.place(x=940, y=170, width=305, height=350)

        t1 = Label(a7, text="Makita Hammer", font=("arial", 10, "bold"), bg="white", fg="black")
        t1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        t1_ent = Entry(a7, width=5,textvariable=self.hammer, font=("arial", 10), bd=5, relief="sunken").grid(row=0, column=1, padx=70, pady=10)

        t2 = Label(a7, text="Bosche Chainsaw", font=("arial", 10, "bold"), bg="white", fg="black")
        t2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        t2_ent = Entry(a7, width=5,textvariable=self.chainsaw, font=("arial", 10), bd=5, relief="sunken").grid(row=1, column=1, padx=70, pady=10)

        t3 = Label(a7, text="PW Electric Drill", font=("arial", 10, "bold"), bg="white", fg="black")
        t3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        t3_ent = Entry(a7, width=5,textvariable=self.drill, font=("arial", 10), bd=5, relief="sunken").grid(row=2, column=1, padx=70, pady=10)

        t4 = Label(a7, text="Nails", font=("arial", 10, "bold"), bg="white", fg="black")
        t4.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        t4_ent = Entry(a7, width=5,textvariable=self.nails, font=("arial", 10), bd=5, relief="sunken").grid(row=3, column=1, padx=70, pady=10)

        t5 = Label(a7, text="Kee TOOLBoX", font=("arial", 10, "bold"), bg="white", fg="black")
        t5.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        t5_ent = Entry(a7, width=5,textvariable=self.toolbox, font=("arial", 10), bd=5, relief="sunken").grid(row=4, column=1, padx=70, pady=10)

        t6 = Label(a7, text="Ridge Pliers", font=("arial", 10, "bold"), bg="white", fg="black")
        t6.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        t6_ent = Entry(a7, width=5,textvariable=self.pliers, font=("arial", 10), bd=5, relief="sunken").grid(row=5, column=1, padx=70, pady=10)

        # DISPLAY BILL

        a6 = Frame(self.main, bd=10, relief="sunken")
        a6.place(x=1250, y=180, width=270, height=480)

        display_bill = Label(a6,text=" BILL ",font=("Verdana",15,"bold"),bd=7,relief="groove",bg="#40826D",fg="white").pack(fill=X)
        # display_bill.place(x=1150,y=170,width=270,height=300)

        scroll_in_y = Scrollbar(a6,orient="vertical")        # SETTING UP A SCROLL BAR
        self.siny = Text(a6,yscrollcommand=scroll_in_y.set)
        scroll_in_y.pack(side="right",fill=Y)
        scroll_in_y.config(command=self.siny.yview)
        self.siny.pack(fill="both",expand=1)



        # LAST FRAME
        a8 = LabelFrame(self.main, bd=10, relief="solid", text="Billing Statement", font=("Comic Sans MS", 18, "bold"), fg="#00A86B")
        a8.place(x=5, y=520, width=1240, height=180)

        ttl_food = Label(a8,text="Total Food Price :",font=("arial",14,"bold"),bg="#FFBF00").grid(row=0,column=0,padx=20,pady=1,sticky="w")
        ttl_food_en = Entry(a8,width=10,textvariable=self.total_food_price,font=("arial",10),bd=5,relief="sunken").grid(row=0,column=2,padx=10,pady=10)

        ttl_drinks = Label(a8, text="Total Drinks Price :", font=("arial", 14, "bold"), bg="#FFBF00").grid(row=1, column=0,padx=20, pady=1,sticky="w")
        t_drinks_en = Entry(a8, width=10,textvariable=self.total_drink_price, font=("arial", 10), bd=5, relief="sunken").grid(row=1, column=2, padx=10,pady=10)

        ttl_selfcare = Label(a8, text="Total Self-Care Price :", font=("arial", 14, "bold"), bg="#FFBF00").grid(row=2,column=0,padx=20,pady=1,sticky="w")
        t_selfcare_en = Entry(a8, width=10,textvariable=self.total_selfcare_price, font=("arial", 10), bd=5, relief="sunken").grid(row=2, column=2, padx=10,pady=5)

        ttl_tools = Label(a8, text="Total Tools Price :", font=("arial", 14, "bold"), bg="#FFBF00").grid(row=0,column=5,padx=20,pady=1,sticky="w")
        t_tools_en = Entry(a8, width=10,textvariable=self.total_tool_price, font=("arial", 10), bd=5, relief="sunken").grid(row=0, column=7, padx=10,pady=10)

        ttl_price = Label(a8,text="TOTAL PRICE :",font=("arial",14,"bold"),bg="#FFBF00").grid(row=1,column=5,padx=20,pady=1,sticky="w")
        t_tprice_en = Entry(a8,width=10,textvariable=self.total,font=("arial",10),bd=5,relief="sunken").grid(row=1,column=7,padx=10,pady=10)

        vat = Label(a8,text="13% VAT  ON TOTAL :",font=("arial",14,"bold"),bg="#FFBF00").grid(row=2,column=5,padx=20,pady=1,sticky="w")
        vat_entry = Entry(a8,width=10,textvariable=self.vat,font=("arial", 10),bd=5,relief="sunken").grid(row=2,column=7,padx=10,pady=5)

        # FRAME FOR BUTTON and BUTTONS

        button_fr = Frame(a8,bd=7,relief="solid").place(x=700,width=500,height=130)

        but_total = Button(button_fr,command=lambda: self.show_total(),width=10,bd=5,text="Total",font=("Comic Sans MS",15,"bold"),bg="#CC7722",fg="black",pady=15)
        but_total.place(x=730,y=570)

        but_genbill = Button(button_fr,command=lambda: self.show_bill(),width=11,bd=5, text="Generate Bill", font=("Comic Sans MS", 15,"bold"), bg="#CC7722", fg="black",pady=15)
        but_genbill.place(x=880, y=570)

        but_clear = Button(button_fr, width=5,bd=8, text="Clear", font=("Comic Sans MS", 10, "bold"), bg="#CC7722", fg="black", pady=15)
        but_clear.place(x=1050, y=575)

        self.show_bill()           # Calling the function defined below

        def exit_msg():             # For ExitCODE IN LOC after this func
            ex = tkinter.messagebox.askyesno("SuperMarket Billing Software", "Are you sure you want to exit?")
            if ex > 0:
                exit()
        but_exit = Button(button_fr, width=5, bd=8, text="EXIT", font=("Comic Sans MS", 10, "bold"), bg="#CC7722",fg="black", pady=15, command=lambda:exit_msg())
        but_exit.place(x=1130, y=575)

    def show_total(self):           # This is for the TOTAL button to work AND ALSO giving products price
        self.showtotal_food = float(
                                (self.pringles.get()*200) +               # ASSIGNING PRICES
                                (self.tuna.get()*130) +
                                (self.oats.get() * 250) +
                                (self.cornflakes.get() * 525) +
                                (self.chnuggets.get() * 630) +
                                (self.momo.get() * 275)
                              )
        self.total_food_price.set("Rs." + str(self.showtotal_food))

        self.showtotal_drinks = float(
                                (self.cokefanta.get() * 75) +                                 # ASSIGNING PRICES FOR THE PRODUCTS
                                (self.cider.get() * 130) +
                                (self.warsteiner.get() * 295) +
                                (self.juice.get() * 230) +
                                (self.natura.get() * 300) +
                                (self.lecoc.get() * 450)
                            )
        self.total_drink_price.set("Rs." + str(self.showtotal_drinks))

        self.showtotal_selfcare = float(
                                (self.shampoo.get() * 248) +  # ASSIGNING PRICES FOR THE PRODUCTS
                                (self.colgate.get() * 165) +
                                (self.radia.get() * 3600) +
                                (self.nailpolish.get() * 845) +
                                (self.ketain.get() * 2800) +
                                (self.facemask.get() * 480)
                            )
        self.total_selfcare_price.set("Rs." + str(self.showtotal_selfcare))

        self.showtotal_tools = float(
                                (self.hammer.get() * 1600) +  # ASSIGNING PRICES FOR THE PRODUCTS
                                (self.chainsaw.get() * 22500) +
                                (self.drill.get() * 3700) +
                                (self.nails.get() * 5) +
                                (self.toolbox.get() * 3490) +
                                (self.pliers.get() * 700)
                            )
        self.total_tool_price.set("Rs." + str(self.showtotal_tools))

        self.showtotal = float(
            self.showtotal_food +
            self.showtotal_drinks +
            self.showtotal_selfcare +
            self.showtotal_tools

                            )
        self.total.set("Rs." + str(self.showtotal))


        self.showvat = float((self.showtotal)*0.13)
        self.vat.set(str(self.showvat))
        self.total.set(str(self.showtotal + self.showvat))  # ADDING VAT AMOUNT IN TOTAL

    def show_bill(self):
        # self.txtarea.delete("1.0", END)
        self.txtarea.insert(END, "\t Nepal SuperMarket\n")
        # self.txtarea.insert(END, f"\n Customer Name:{self.billnum.get()}")
        # self.txtarea.insert(END, f"\n Contact Number:{self.date.get()}\n")
        # self.txtarea.insert(END, f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::")
        # self.txtarea.insert(END, f"\nProduct\t\t\tQty\t\tPrice")
        # self.txtarea.insert(END, f"\n::::::::::::::::::::::::::::::::::::::::::::::::::::")


    def bill_area(self):
         pass






main = Tk()
main.resizable(FALSE, FALSE)
obj1 = Bill_system(main)  # object = class
main.mainloop()

    





