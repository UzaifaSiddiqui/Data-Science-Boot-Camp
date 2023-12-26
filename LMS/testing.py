from tkinter import *
from tkinter import messagebox,ttk
from datetime import datetime
now = datetime.now()
root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

 
def date_time_name(t,id_name):
  with open("datetime.txt","a") as f:
     lines=","+str(t)+" "+id_name
     f.writelines(lines)
     
def operator_name(id_name):
  name=str(id_name).upper()
  return(name)
  
def signin():
  username=user.get()
  code=password.get()
  with open("id_pass.txt","r") as e:
     txt=0
     while True:
       read=e.readlines()
       if not read:
           break
       txt=read[:]
  for i in txt:
    id_pass=i.split(",")
  j=0
  flag0=0
  flag1=1
  lst=[]
  while True:
    lst1=[]
    if(flag1+j<len(id_pass)):
      flag0+j
      flag1+j
      lst1.append(id_pass[flag0+j])
      lst1.append(id_pass[flag1+j])
      lst.append(lst1)
      j+=2
    else:
      break
  e=0
  while e+1<=len(lst):
      if username==str(lst[e][0]) and code==str(lst[e][1]):
         axis="Match found"
         id_name = str(lst[e][0])
         op_name=operator_name(id_name)
         t=now.strftime("%Y-%m-%d %H:%M:%S")
         date_time_name(t,id_name)
         break
      else:
         e+=1
  else:
      messagebox.showerror("Invalid" , "Enter Correct Username and Password")

  if axis=="Match found":
    screen=Toplevel(root)
    screen.title("Admin Panel")
    screen.geometry("1366x768")
    screen.config(bg="#fff")

    def reading_collection():
        with open("bookco.txt","r") as f:
         txt=0
         while True:
           read=f.readlines()
           if not read:
               break
           txt=read[:]
        for dat in txt:
          books=dat.split(",")
        return(books)
    ulevel1=reading_collection()

 
    def collection_books():


            header=Frame(screen,bg="#1A1A1A")
            header.place(x="300",y="0",width=1070,height=60)

            operator_n=Label(screen,text=operator_name(id_name),fg="white",bg="#1A1A1A",font=("City Bold",17,"bold"))
            operator_n.place(x=1172,y=15)

            photo2=PhotoImage(file="C:/Users/Lenovo X240/Downloads/profile.1.png")
            profile=Label(screen,image=photo2,bg="#1A1A1A")
            profile.image=photo2
            profile.place(x=1117,y=3)

            
            Frame(screen,width=1,height=65,bg="white").place(x=1282,y=0)
            Frame(screen,width=1,height=65,bg="white").place(x=1108,y=0)

            log_photo1 =PhotoImage(file="C:/Users/Lenovo X240/Downloads/logout.png") 

            logout1 = Button(screen,image=log_photo,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2")
            logout1.place(x=1293,y=3)


            sidebar=Frame(screen,bg="#1A1A1A")
            sidebar.place(x="0",y="0",width=300,height=750)
            photo=PhotoImage(file="C:/Users/Lenovo X240/Downloads/icon2.1.png")
            logo=Label(sidebar,image=photo,bg="#1A1A1A")
            logo.image=photo
            logo.place(x=9,y=-40)

            title= Label(sidebar,text="YC BOOKS",fg="white",bg="#1A1A1A",font=("Cooper Black",18,"bold"))
            title.place(x=69, y=169)




            dashboard_text=Button(sidebar,text="Collection",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=collection_books)
            dashboard_text.place(x=80,y=292)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=325)

            issue_book=Button(sidebar,text="Issue Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=sanction_books)
            issue_book.place(x=80,y=375)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=408)

            return_book=Button(sidebar,text="Submit Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=returned_books)
            return_book.place(x=80,y=458)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=491)

            clock_photo4=PhotoImage(file="C:/Users/Lenovo X240/Downloads/clock.png")
            clock4 = Button(screen,image=clock_photo1,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2",command=time_log)
            clock4.place(x=1042,y=3)

            Frame(screen,width=1,height=65,bg="white").place(x=1028,y=0)

            def add_code():
              with open("bookcode.txt","r") as f:
               txt=0
               while True:
                 read=f.readlines()
                 if not read:
                   with open ("bookcode.txt","w") as e:
                     lines="1"
                     e.writelines(lines)
                 if read:
                   txt = read[:]
                 for code in txt:
                   codes=code.split(",")
                 i = len(codes)-1
                 index = int(codes[i])
                 with open ("bookcode.txt","a") as g:
                   lines = ","+str(index+1)
                   g.writelines(lines)
                   break

                

            def add_book():
                with open("bookco.txt","r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                     with open ("bookco.txt","w") as e:
                       lines=str(add_book.get())
                       e.writelines(lines)
                   if read:
                     with open ("bookco.txt","a") as g:
                       lines = ","+str(add_book.get())
                       g.writelines(lines)
                       break
                 add_code()

             




            bodyframe=Frame(screen,bg="white")
            bodyframe.place(x="328",y="110",width=1040,height=650)


            add_icon1 =PhotoImage(file="C:/Users/Lenovo X240/Downloads/add.png") 

            add1=Button(bodyframe,image=add_icon,bg="white",bd=0,cursor="hand2",command=add_book)
            add1.place(x=755,y=-5)


            def on_enter(e):
              add_book.delete(0, "end")

            def on_leave(e):
              name=add_book.get()
              if name=="":
                add_book.insert(0,"Add Book")




            add_book=Entry(bodyframe,width=20,fg="#1A1A1A",border=0,bg="white",font=("Microsoft YaHei UI Light",15))
            add_book.place(x=810,y=5)
            add_book.insert(0,"Add Book")
            add_book.bind("<FocusIn>",on_enter)
            add_book.bind("<FocusOut>",on_leave)
            Frame(bodyframe,width=210,height=2,bg="#1A1A1A").place(x=810,y=32)



            bar=Frame(bodyframe,bg="#1A1A1A")
            bar.place(x="0",y="55",width=1040,height=30)            

            button= Label(bodyframe,text="Name",fg="white",bg="#1A1A1A",font=("Bastion",14,"bold"))
            button.place(x=140,y=55)

            button2= Label(bodyframe,text="ID",fg="white",bg="#1A1A1A",font=("Bastion",14,"bold"))
            button2.place(x=55,y=55)

            button2= Label(bodyframe,text="Status",fg="white",bg="#1A1A1A",font=("Bastion",14,"bold"))
            button2.place(x=850,y=55)


            def reading_collection():
                with open("bookco.txt","r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                       break
                   txt=read[:]
                for dat in txt:
                  books=dat.split(",")
                return(books)
            ulevel1=reading_collection()






            def button_collection(book_name,height):
              button=Label(bodyframe,text=str(book_name),fg="#000000",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
              button.place(x=140,y=height)

            def button(e,height):
              button=Label(bodyframe,text=str(e),fg="#000000",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
              button.place(x=55,y=height)



            def print_collection(ulevel1):
              lst=ulevel1[:]
              height=90
              e=1
              for i in lst:
                  #delete_button(i,height)
                  button_collection(i,height)
                  button(e,height)
                  height+=30
                  e+=1

            print_collection(ulevel1)

##           
##
##
##            def delete_button(book_name,height):
##              delete=Button(bodyframe,text="Delete",fg="#000000",bg="#EE2C2C",font=("Microsoft YaHei UI Light",12,"bold"),bd=0,cursor="hand2",activebackground="white")
##              delete.place(x=900,y=height)
##          
##
 

    def sanction_books():

            header=Frame(screen,bg="#1A1A1A")
            header.place(x="300",y="0",width=1070,height=60)

            operator_n=Label(screen,text=operator_name(id_name),fg="white",bg="#1A1A1A",font=("City Bold",17,"bold"))
            operator_n.place(x=1172,y=15)

            photo2=PhotoImage(file="C:/Users/Lenovo X240/Downloads/profile.1.png")
            profile=Label(screen,image=photo2,bg="#1A1A1A")
            profile.image=photo2
            profile.place(x=1117,y=3)
            
            Frame(screen,width=1,height=65,bg="white").place(x=1282,y=0)
            Frame(screen,width=1,height=65,bg="white").place(x=1108,y=0)

            log_photo2 =PhotoImage(file="C:/Users/Lenovo X240/Downloads/logout.png") 

            logout2 = Button(screen,image=log_photo,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2")
            logout2.place(x=1293,y=3)


            sidebar=Frame(screen,bg="#1A1A1A")
            sidebar.place(x="0",y="0",width=300,height=750)
            photo=PhotoImage(file="C:/Users/Lenovo X240/Downloads/icon2.1.png")
            logo=Label(sidebar,image=photo,bg="#1A1A1A")
            logo.image=photo
            logo.place(x=9,y=-40)

            title= Label(sidebar,text="YC BOOKS",fg="white",bg="#1A1A1A",font=("Cooper Black",18,"bold"))
            title.place(x=69, y=169)




            dashboard_text=Button(sidebar,text="Collection",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=collection_books)
            dashboard_text.place(x=80,y=292)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=325)

            issue_book=Button(sidebar,text="Issue Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=sanction_books)
            issue_book.place(x=80,y=375)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=408)

            return_book=Button(sidebar,text="Submit Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=returned_books)
            return_book.place(x=80,y=458)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=491)

            clock_photo3=PhotoImage(file="C:/Users/Lenovo X240/Downloads/clock.png")
            clock3 = Button(screen,image=clock_photo1,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2",command=time_log)
            clock3.place(x=1042,y=3)

            Frame(screen,width=1,height=65,bg="white").place(x=1028,y=0)



            bodyframe=Frame(screen,bg="white")
            bodyframe.place(x="328",y="110",width=1040,height=650)

            
            def get_member_id():
              with open("members.txt","r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                       break
                   txt=read[:]
                 for dat in txt:
                    books=dat.split(",")
                 i=0
                 e=1
                 lst=[]
                 while e<len(books):
                   lst1=[]
                   lst1.append(books[i])
                   lst1.append(books[e])
                   lst.append(lst1)
                   i+=2
                   e+=2
                 return(lst)
                
            def get_bookcode():
                with open("bookcode.txt","r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                       break
                   txt=read[:]
                for dat in txt:
                 code=dat.split(",")
                new=len(code)-1
                lst=[]
                for j in range(new):
                    lst.append(j)
                print(lst)    
                m=0
                lines=str(lst[m])
                m+=1
                while m<len(lst):
                  line = ","+str(m)
                  lines+=line
                  m+=1
                print(lines)
                with open ("bookcode.txt","w") as e:
                  e.writelines(lines)
                  
            def to_delete(name):
                with open("bookco.txt","r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                       break
                   txt=read[:]
                for dat in txt:
                  books=dat.split(",")
                i_book = books.index(name)
                i=0
                for i in range(len(books)):
                    if i_book == i:
                        books.pop(i)
                        break
                m=0
                lines=str(books[m])
                m+=1
                while m < len(books):
                  line = ","+str(books[m])
                  lines+=line
                  m+=1
                with open ("bookco.txt","w") as e:
                  e.writelines(lines)
                get_bookcode() 

            ulevel2=get_member_id()
            def save_data(name,book_name):
              member=str(name)+".txt"
              with open(member,"r") as f:
                   txt=0
                   while True:
                     read=f.readlines()
                     if not read:
                         with open(member,"w") as e:
                             lines1=str(book_name)
                             e.writelines(lines1)
                         break
                     if read:   
                         with open(member,"a") as i:
                             lines2=","+str(book_name)
                             i.writelines(lines2)
                         break
             
                          
            def sanc_file(book_name):
              with open("sancbook.txt","r") as f:
                   txt=0
                   while True:
                     read=f.readlines()
                     if not read:
                         with open("sancbook.txt","w") as e:
                             lines1=str(book_name)
                             e.writelines(lines1)
                         break
                     else:
                         with open("sancbook.txt","a") as i:
                          lines2=","+str(book_name)
                          i.writelines(lines2)
                         break




            def date_time(t,file):
              file_name =str(file)+"datetime.txt"
              with open(file_name,"r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                       with open(file_name,"w") as e:
                           lines1=str(t)
                           e.writelines(lines1)
                       break
                   elif read:
                        txt=read[:]
                        for dat in txt:
                           books=dat.split(",")
                        else:
                           with open(file_name,"a") as i:
                              lines2=","+str(t)
                              i.writelines(lines2)
                           break
            
            def check_length(member_name):  
              member =str(member_name)+".txt"
              with open(member,"r") as e:
               txt=0
               while True:
                 read=e.readlines()
                 if not read:
                     val = 0
                     break
                 else:
                     txt=read[:]
                     for dat in txt:
                        books=dat.split(",")
                     val=(len(books))
               return(val)
            
            
            def check_membership():
                member_name=member.get()
                member_no=membership.get()
                book_name=combo.get()
                new = datetime.now()
                with open("bookco.txt","r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                       break
                   txt=read[:]
                for dat in txt:
                  books=dat.split(",")
                lst=ulevel2[:]
                i=0
                while i<len(lst):
                  if member_name == lst[i][0] and member_no == lst[i][1]:
                     for e in range(len(books)):
                       if book_name==books[e]:
                         length = check_length(member_name)
                         print(length)
                         if length >= 3:
                           messagebox.showerror("Invalid" , "ALREADY THREE BOOKS BEEN SANCTIONED")
                           print("Sorry can not assign more books")
                         if length < 3:
                           save_data(member_name,book_name)
                           sanc_file(book_name)
                           to_delete(book_name)
                           t=new.strftime("%Y-%m-%d %H:%M:%S")
                           date_time(t,member_name)
                           sanction_books()
                           print("assigned")               
                         break   
                     break  
                  i+=1     
            
            
            bodyframe=Frame(screen,bg="white")
            bodyframe.place(x="328",y="110",width=1040,height=650)
            
            
            
##            def display_selection():
##                # Get the selected value.
##                selection = combo.get()
##                messagebox.showinfo(message=f"The selected value is: {selection}",title="Selection")
              
            combo = ttk.Combobox(bodyframe,width=55,height=55,state="readonly",values=reading_collection())
            combo.place(x=540, y=135)
            button = ttk.Button(bodyframe,text="Select")
            button.place(x=895, y=132)

            field1= Label(bodyframe,text="Select Book",fg="#1A1A1A",bg="white",font=("Microsoft YaHei UI Light",15))
            field1.place(x=426, y=130)

            field_bar= Label(bodyframe,bg="#1A1A1A")
            field_bar.place(x="0",y="20",width=1040,height=35)

             
            field= Label(bodyframe,text="Information Fields",fg="#E3CF57",bg="#1A1A1A",font=("BinnerD",16,"bold"))
            field.place(x=10, y=22)



            def on_enter(e):
              member.delete(0, "end")

            def on_leave(e):
              name=member.get()
              if name=="":
                member.insert(0,"Member Name")



            
            member=Entry(bodyframe,width=25,fg="#1A1A1A",border=0,bg="white",font=("Microsoft YaHei UI Light",15))
            member.place(x=10,y=130)
            member.insert(0,"Member Name")
            member.bind("<FocusIn>",on_enter)
            member.bind("<FocusOut>",on_leave)
            Frame(bodyframe,width=292,height=2,bg="#CDBE70").place(x=10,y=163)



            def on_enter(e):
              membership.delete(0, "end")

            def on_leave(e):
              name=membership.get()
              if name=="":
                membership.insert(0,"Member Id")


            membership=Entry(bodyframe,width=25,fg="#1A1A1A",border=0,bg="white",font=("Microsoft YaHei UI Light",15))
            membership.place(x=10,y=275)
            membership.insert(0,"Member Id")
            membership.bind("<FocusIn>",on_enter)
            membership.bind("<FocusOut>",on_leave)
            Frame(bodyframe,width=292,height=2,bg="#CDBE70").place(x=10,y=308)

            submit=Button(bodyframe,text="Submit",fg="white",bg="#1A1A1A",font=("Microsoft YaHei UI Light",13,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=check_membership)
            submit.place(x=10,y=348)



            
    def returned_books():



            header=Frame(screen,bg="#1A1A1A")
            header.place(x="300",y="0",width=1070,height=60)

            operator_n=Label(screen,text=operator_name(id_name),fg="white",bg="#1A1A1A",font=("City Bold",17,"bold"))
            operator_n.place(x=1172,y=15)


            photo2=PhotoImage(file="C:/Users/Lenovo X240/Downloads/profile.1.png")
            profile=Label(screen,image=photo2,bg="#1A1A1A")
            profile.image=photo2
            profile.place(x=1117,y=3)
            
            Frame(screen,width=1,height=65,bg="white").place(x=1282,y=0)
            Frame(screen,width=1,height=65,bg="white").place(x=1108,y=0)

            log_photo3 =PhotoImage(file="C:/Users/Lenovo X240/Downloads/logout.png") 

            logout3 = Button(screen,image=log_photo,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2")
            logout3.place(x=1293,y=3)

            sidebar=Frame(screen,bg="#1A1A1A")
            sidebar.place(x="0",y="0",width=300,height=750)
            photo=PhotoImage(file="C:/Users/Lenovo X240/Downloads/icon2.1.png")
            logo=Label(sidebar,image=photo,bg="#1A1A1A")
            logo.image=photo
            logo.place(x=9,y=-40)

            title= Label(sidebar,text="YC BOOKS",fg="white",bg="#1A1A1A",font=("Cooper Black",18,"bold"))
            title.place(x=69, y=169)




            dashboard_text=Button(sidebar,text="Collection",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=collection_books)
            dashboard_text.place(x=80,y=292)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=325)

            issue_book=Button(sidebar,text="Issue Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=sanction_books)
            issue_book.place(x=80,y=375)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=408)

            return_book=Button(sidebar,text="Submit Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=returned_books)
            return_book.place(x=80,y=458)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=491)

            clock_photo2=PhotoImage(file="C:/Users/Lenovo X240/Downloads/clock.png")
            clock2 = Button(screen,image=clock_photo1,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2",command=time_log)
            clock2.place(x=1042,y=3)

            Frame(screen,width=1,height=65,bg="white").place(x=1028,y=0)
            
            
            
            def reading_collection_sanction():
              with open("sancbook.txt","r") as f:
               txt=0
               while True:
                 read=f.readlines()
                 if not read:
                  return(None) 
                  break
                 if read:
                     txt=read[:]
                     for dat in txt:
                        books=dat.split(",")
                     return(books)
                     break
                


            bodyframe=Frame(screen,bg="white")
            bodyframe.place(x="328",y="110",width=1040,height=650)
 

            combo = ttk.Combobox(bodyframe,width=55,height=55,state="readonly",values=reading_collection_sanction())
            combo.place(x=540, y=135)
            button = ttk.Button(bodyframe,text="Select")
            button.place(x=895, y=132)

            field1= Label(bodyframe,text="Select Book",fg="#1A1A1A",bg="white",font=("Microsoft YaHei UI Light",15))
            field1.place(x=426, y=130)


            field_bar= Label(bodyframe,bg="#1A1A1A")
            field_bar.place(x="0",y="20",width=1040,height=35)
             
            field= Label(bodyframe,text="Returned Fields",fg="#E3CF57",bg="#1A1A1A",font=("BinnerD",16,"bold"))     
            field.place(x=10, y=22)

 


            def on_enter(e):
              mem.delete(0, "end")

            def on_leave(e):
              name=mem.get()
              if name=="":
                mem.insert(0,"Member Name")



            
            mem=Entry(bodyframe,width=25,fg="#1A1A1A",border=0,bg="white",font=("Microsoft YaHei UI Light",15))
            mem.place(x=10,y=130)
            mem.insert(0,"Member Name")
            mem.bind("<FocusIn>",on_enter)
            mem.bind("<FocusOut>",on_leave)
            Frame(bodyframe,width=292,height=2,bg="#CDBE70").place(x=10,y=163)



            def on_enter(e):
              memship.delete(0, "end")

            def on_leave(e):
              name=memship.get()
              if name=="":
                memship.insert(0,"Member Id")


            memship=Entry(bodyframe,width=25,fg="#1A1A1A",border=0,bg="white",font=("Microsoft YaHei UI Light",15))
            memship.place(x=10,y=275)
            memship.insert(0,"Member Id")
            memship.bind("<FocusIn>",on_enter)
            memship.bind("<FocusOut>",on_leave)
            Frame(bodyframe,width=292,height=2,bg="#CDBE70").place(x=10,y=308)

 
            def to_delete_from(book_name):
              file = "sancbook.txt"
              with open(file , "r") as f:
                text =0
                while True:
                  read = f.readlines()
                  if not read:
                    print("No Record Such Book")
                  if read:
                    text = read[:]
                    for i in text:
                      book = i.split(",")
                    position = book.index(book_name)
                    book.pop(position)
                  if len(book) == 0:
                    with open(file,"w")as e:
                      line = ""
                      e.writelines(line)
                    break
                  if len(book) != 0 :
                    with open(file ,"w") as e :
                      length = 0
                      while length < (len(book)-1):
                        line = str(book[length])+","
                        e.writelines(line)
                        length+=1
                      e.writelines(str(book[length]))
                      break
                  break
                      
                  
              


            def to_delete(member_name,book_name):
              file = str(member_name)+".txt"
              with open(file , "r") as f:
                text =0
                while True:
                  read = f.readlines()
                  if not read:
                    print("No Record Such Book")
                  if read:
                    text = read[:]
                    for i in text:
                      book = i.split(",")
                    position = book.index(book_name)
                    book.pop(position)
                  if len(book) == 0:
                    with open(file,"w")as e:
                      line = ""
                      e.writelines(line)
                    break
                  if len(book) != 0 :
                    with open(file ,"w") as e :
                      length = 0
                      while length < (len(book)-1):
                        line = str(book[length])+","
                        e.writelines(line)
                        length+=1
                      e.writelines(str(book[length]))
                      break
                  break

            def to_delete_time(member_name,index):
              file = str(member_name)+"datetime.txt"
              with open(file , "r") as f:
                text =0
                while True:
                  read = f.readlines()
                  if not read:
                    print("No Record Of Such Time")
                  if read:
                    text = read[:]
                    for i in text:
                      time = i.split(",")
                    time.pop(index)
                  if len(time) == 0:
                    with open(file,"w")as e:
                      line = ""
                      e.writelines(line)
                    break
                  if len(time) != 0 :
                    with open(file ,"w") as e :
                      length = 0
                      while length < (len(time)-1):
                        line = str(time[length])+","
                        e.writelines(line)
                        length +=1
                      e.writelines(str(time[length]))
                      break
                  break
            
            
            
            def add_code():
              with open("bookcode.txt","r") as f:
               txt=0
               while True:
                 read=f.readlines()
                 if not read:
                   with open ("bookcode.txt","w") as e:
                     lines="1"
                     e.writelines(lines)
                 if read:
                   txt = read[:]
                 for code in txt:
                   codes=code.split(",")
                 i = len(codes)-1
                 index = int(codes[i])
                 with open ("bookcode.txt","a") as g:
                   lines = ","+str(index+1)
                   g.writelines(lines)
                   break

                

            def add_book(book_name):
                with open("bookco.txt","r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                     with open ("bookco.txt","w") as e:
                       lines=str(book_name)
                       e.writelines(lines)
                   if read:
                     with open ("bookco.txt","a") as g:
                       lines = ","+str(book_name)
                       g.writelines(lines)
                       break
                 add_code()

                  

                 
            def return_date_time(i,member):
              member_name=member
              date=str(member_name)+"datetime.txt"
              with open(date,"r") as e:
                 txt=0
                 while True:
                   read=e.readlines()
                   if not read:
                       break
                   if read:
                       txt=read[:]
                       lst=[]
                       for dat in txt:
                          dtcollection=dat.split(",")
                       for time in dtcollection:
                          collect=time.split(" ")
                          lst.append(collect)
                       file = lst[i][0]
                       files = file.split("-")
                       return(files[1])

            def transcript():
                root=Tk()
                window=root
                window.title("Transcript")
                window.geometry("600x100")
                window.config(bg="#1A1A1A")
                statement = Label(window,text="Fined of $50 for exceeding the time limit of three days for returning a book",fg="white",bg="#1A1A1A",font=("BinnerD",11,"bold"))
                statement.place(x=30, y=40)
                window.mainloop()
                      
            
            def returned_function():
                member_name=mem.get()
                member_no=memship.get()
                book_name=combo.get()
                lst = reading_collection_sanction()
                member =str(member_name)+".txt"
                with open(member,"r") as f:
                 txt=0
                 while True:
                   read=f.readlines()
                   if not read:
                       break
                   txt=read[:]
                 for dat in txt:
                   books=dat.split(",")
                 i=0
                 flag = True
                 while flag:
                   if book_name==books[i]:
                     note= return_date_time(i,member_name)
                     date_time = datetime.now()
                     t=now.strftime("%Y-%m-%d %H:%M:%S")
                     collect=t.split(" ")
                     file = collect[0]
                     files = file.split("-")
                     diff = int(files[1]) - int(note)
                     if int(diff) > 3:
                       print("fined")
                       transcript()
                       to_delete_(member_name,book_name)
                       to_delete_from(book_name)
                       to_delete_time(member_name,i)
                       add_book(book_name)
                       returned_books()
                       flag = False
                     else:
                       print("not fined")
                       to_delete(member_name,book_name)
                       to_delete_from(book_name)
                       to_delete_time(member_name,i)
                       add_book(book_name)
                       returned_books()
                       flag = False
                   i+=1

            rt=Button(bodyframe,text="Return",fg="white",bg="#1A1A1A",font=("Microsoft YaHei UI Light",13,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=returned_function)
            rt.place(x=10,y=348)

    def time_log():



            header=Frame(screen,bg="#1A1A1A")
            header.place(x="300",y="0",width=1070,height=60)

            operator_n=Label(screen,text=operator_name(id_name),fg="white",bg="#1A1A1A",font=("City Bold",17,"bold"))
            operator_n.place(x=1172,y=15)


            photo2=PhotoImage(file="C:/Users/Lenovo X240/Downloads/profile.1.png")
            profile=Label(screen,image=photo2,bg="#1A1A1A")
            profile.image=photo2
            profile.place(x=1117,y=3)
            
            Frame(screen,width=1,height=65,bg="white").place(x=1282,y=0)
            Frame(screen,width=1,height=65,bg="white").place(x=1108,y=0)

            log_photo3 =PhotoImage(file="C:/Users/Lenovo X240/Downloads/logout.png") 

            logout3 = Button(screen,image=log_photo,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2")
            logout3.place(x=1293,y=3)

            sidebar=Frame(screen,bg="#1A1A1A")
            sidebar.place(x="0",y="0",width=300,height=750)
            photo=PhotoImage(file="C:/Users/Lenovo X240/Downloads/icon2.1.png")
            logo=Label(sidebar,image=photo,bg="#1A1A1A")
            logo.image=photo
            logo.place(x=9,y=-40)

            title= Label(sidebar,text="YC BOOKS",fg="white",bg="#1A1A1A",font=("Cooper Black",18,"bold"))
            title.place(x=69, y=169)




            dashboard_text=Button(sidebar,text="Collection",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=collection_books)
            dashboard_text.place(x=80,y=292)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=325)

            issue_book=Button(sidebar,text="Issue Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=sanction_books)
            issue_book.place(x=80,y=375)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=408)

            return_book=Button(sidebar,text="Submit Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=returned_books)
            return_book.place(x=80,y=458)
            Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=491)

            clock_photo2=PhotoImage(file="C:/Users/Lenovo X240/Downloads/clock.png")
            clock1 = Button(screen,image=clock_photo1,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2",command=time_log)
            clock1.place(x=1042,y=3)

            Frame(screen,width=1,height=65,bg="white").place(x=1028,y=0)



            bodyframe=Frame(screen,bg="white")
            bodyframe.place(x="328",y="110",width=1040,height=650)


            log_time_label=Label(bodyframe,text="Log Time",fg="#030303",bg="white",font=("Latin W.",28,"bold"))
            log_time_label.place(x=10,y=14)


            update=Label(bodyframe,text="(Upto Last 8 Sessions)",fg="#030303",bg="white",font=("Latin W.",20,"bold"))
            update.place(x=185,y=23)


            def get_date_time_name():
              with open("datetime.txt","r") as e:
                 txt=0
                 while True:
                   read=e.readlines()
                   if not read:
                       break
                   txt=read[:]
              lst=[]
              for dat in txt:
                  dtcollection=dat.split(",")
              for tim in dtcollection:
                collect=tim.split(" ")
                lst.append(collect)
              return(lst)

            ulevel0=get_date_time_name()



            def record():

             lst=[]
             lst=ulevel0[:]
             e = 0
             i = len(lst)-1
             while e<9:
              dname=lst[i][2]
              dtime=lst[i][1]
              ddate=lst[i][0]

              bar=Frame(bodyframe,bg="#8B8B7A")
              bar.place(x="0",y="60",width=1040,height=30)

              bar2=Frame(bodyframe,bg="#CDCDB4")
              bar2.place(x="0",y="90",width=1040,height=30)

              bar3=Frame(bodyframe,bg="#8B8B7A")
              bar3.place(x="0",y="120",width=1040,height=30)

              bar4=Frame(bodyframe,bg="#CDCDB4")
              bar4.place(x="0",y="150",width=1040,height=30)

              bar5=Frame(bodyframe,bg="#8B8B7A")
              bar5.place(x="0",y="180",width=1040,height=30)

              bar6=Frame(bodyframe,bg="#CDCDB4")
              bar6.place(x="0",y="210",width=1040,height=30)

              bar7=Frame(bodyframe,bg="#8B8B7A")
              bar7.place(x="0",y="240",width=1040,height=30)

              bar8=Frame(bodyframe,bg="#CDCDB4")
              bar8.place(x="0",y="270",width=1040,height=30)

              bar9=Frame(bodyframe,bg="#8B8B7A")
              bar9.place(x="0",y="300",width=1040,height=30)


              bd=Label(bar,text=str(lst[i][0]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd.place(x=100,y=5)

              bd2=Label(bar,text=str(lst[i][1]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd2.place(x=500,y=5)
               
              bd3=Label(bar,text=str(lst[i][2]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd3.place(x=900,y=5)

              i-=1
              e+=1
              #################################################################################
              bd4=Label(bar2,text=str(lst[i][0]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd4.place(x=100,y=6)

              bd5=Label(bar2,text=str(lst[i][1]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd5.place(x=500,y=6)
               
              bd6=Label(bar2,text=str(lst[i][2]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd6.place(x=900,y=6)

              i-=1
              e+=1
              ###################################################################################
              bd7=Label(bar3,text=str(lst[i][0]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd7.place(x=100,y=6.8)

              bd8=Label(bar3,text=str(lst[i][1]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd8.place(x=500,y=6.8)
               
              bd9=Label(bar3,text=str(lst[i][2]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd9.place(x=900,y=6.8)

              i-=1
              e+=1  
              ##################################################################################
              bd10=Label(bar4,text=str(lst[i][0]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd10.place(x=100,y=7.8)

              bd11=Label(bar4,text=str(lst[i][1]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd11.place(x=500,y=7.8)
               
              bd12=Label(bar4,text=str(lst[i][2]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd12.place(x=900,y=7.8)

              i-=1
              e+=1  
              ##################################################################################
              bd13=Label(bar5,text=str(lst[i][0]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd13.place(x=100,y=8.8)

              bd14=Label(bar5,text=str(lst[i][1]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd14.place(x=500,y=8.8)
               
              bd15=Label(bar5,text=str(lst[i][2]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd15.place(x=900,y=8.8)

              i-=1
              e+=1  
              ##################################################################################
              bd16=Label(bar6,text=str(lst[i][0]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd16.place(x=100,y=9.8)

              bd17=Label(bar6,text=str(lst[i][1]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd17.place(x=500,y=9.8)
               
              bd18=Label(bar6,text=str(lst[i][2]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd18.place(x=900,y=9.8)

              i-=1
              e+=1  
              ##################################################################################
              bd19=Label(bar7,text=str(lst[i][0]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd19.place(x=100,y=9.5)

              bd20=Label(bar7,text=str(lst[i][1]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd20.place(x=500,y=9.5)
               
              bd21=Label(bar7,text=str(lst[i][2]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd21.place(x=900,y=9.5)

              i-=1
              e+=1  
              ##################################################################################
              bd22=Label(bar8,text=str(lst[i][0]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd22.place(x=100,y=10.5)

              bd23=Label(bar8,text=str(lst[i][1]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd23.place(x=500,y=10.5)
               
              bd24=Label(bar8,text=str(lst[i][2]),fg="black",bg="#CDCDB4",font=("Square Blk.",13,"bold"))
              bd24.place(x=900,y=10.5)

              i-=1
              e+=1  
              ##################################################################################
              bd25=Label(bar9,text=str(lst[i][0]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd25.place(x=100,y=10.6)

              bd26=Label(bar9,text=str(lst[i][1]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd26.place(x=500,y=10.6)
               
              bd27=Label(bar9,text=str(lst[i][2]),fg="black",bg="#8B8B7A",font=("Square Blk.",13,"bold"))
              bd27.place(x=900,y=10.6)

              i-=1
              e+=1  

            record()




            


############################################################################################################################################################


    header=Frame(screen,bg="#1A1A1A")
    header.place(x="300",y="0",width=1070,height=60)

    operator_n=Label(screen,text=operator_name(id_name),fg="white",bg="#1A1A1A",font=("City Bold",17,"bold"))
    operator_n.place(x=1172,y=15)

    clock_photo1=PhotoImage(file="C:/Users/Lenovo X240/Downloads/clock.png")
    clock = Button(screen,image=clock_photo1,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2",command=time_log)
    clock.place(x=1042,y=3)

    photo2=PhotoImage(file="C:/Users/Lenovo X240/Downloads/profile.1.png")
    profile=Label(screen,image=photo2,bg="#1A1A1A")
    profile.image=photo2
    profile.place(x=1117,y=3)


    
    Frame(screen,width=1,height=65,bg="white").place(x=1282,y=0)
    Frame(screen,width=1,height=65,bg="white").place(x=1108,y=0)

    log_photo =PhotoImage(file="C:/Users/Lenovo X240/Downloads/logout.png") 

    logout = Button(screen,image=log_photo,bg="#1A1A1A",fg="#F5F5DC",font=("City Bold",13,"bold"),bd=0,cursor="hand2")
    logout.place(x=1293,y=3)

    sidebar=Frame(screen,bg="#1A1A1A")
    sidebar.place(x="0",y="0",width=300,height=750)
    photo=PhotoImage(file="C:/Users/Lenovo X240/Downloads/icon2.1.png")
    logo=Label(sidebar,image=photo,bg="#1A1A1A")
    logo.image=photo
    logo.place(x=9,y=-40)

    title= Label(sidebar,text="YC BOOKS",fg="white",bg="#1A1A1A",font=("Cooper Black",18,"bold"))
    title.place(x=69, y=169)




    dashboard_text=Button(sidebar,text="Collection",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=collection_books)
    dashboard_text.place(x=80,y=292)
    Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=325)

    issue_book=Button(sidebar,text="Issue Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=sanction_books)
    issue_book.place(x=80,y=375)
    Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=408)

    return_book=Button(sidebar,text="Submit Book",fg="white",bg="#1A1A1A",font=("Bastion",17,"bold"),bd=0,cursor="hand2",activebackground="#1A1A1A",command=returned_books)
    return_book.place(x=80,y=458)
    Frame(sidebar,width=292,height=2,bg="#CDBE70").place(x=55,y=491)
 
    Frame(screen,width=1,height=65,bg="white").place(x=1028,y=0)

    def add_code():
      with open("bookcode.txt","r") as f:
       txt=0
       while True:
         read=f.readlines()
         if not read:
           with open ("bookcode.txt","w") as e:
             lines="1"
             e.writelines(lines)
         if read:
           txt = read[:]
         for code in txt:
           codes=code.split(",")
         i = len(codes)-1
         index = int(codes[i])
         with open ("bookcode.txt","a") as g:
           lines = ","+str(index+1)
           g.writelines(lines)
           break

        

    def add_book():
        with open("bookco.txt","r") as f:
         txt=0
         while True:
           read=f.readlines()
           if not read:
             with open ("bookco.txt","w") as e:
               lines=str(add_book.get())
               e.writelines(lines)
           if read:
             with open ("bookco.txt","a") as g:
               lines = ","+str(add_book.get())
               g.writelines(lines)
               break
         add_code()

     




    bodyframe=Frame(screen,bg="white")
    bodyframe.place(x="328",y="110",width=1040,height=650)


    add_icon =PhotoImage(file="C:/Users/Lenovo X240/Downloads/add.png") 

    add=Button(bodyframe,image=add_icon,bg="white",bd=0,cursor="hand2",command=add_book)
    add.place(x=755,y=-5)


    def on_enter(e):
      add_book.delete(0, "end")

    def on_leave(e):
      name=add_book.get()
      if name=="":
        add_book.insert(0,"Add Book")




    add_book=Entry(bodyframe,width=20,fg="#1A1A1A",border=0,bg="white",font=("Microsoft YaHei UI Light",15))
    add_book.place(x=810,y=5)
    add_book.insert(0,"Add Book")
    add_book.bind("<FocusIn>",on_enter)
    add_book.bind("<FocusOut>",on_leave)
    Frame(bodyframe,width=210,height=2,bg="#1A1A1A").place(x=810,y=32)



    bar=Frame(bodyframe,bg="#1A1A1A")
    bar.place(x="0",y="55",width=1040,height=30)            

    button= Label(bodyframe,text="Name",fg="white",bg="#1A1A1A",font=("Bastion",14,"bold"))
    button.place(x=140,y=55)

    button2= Label(bodyframe,text="ID",fg="white",bg="#1A1A1A",font=("Bastion",14,"bold"))
    button2.place(x=55,y=55)

    button2= Label(bodyframe,text="Status",fg="white",bg="#1A1A1A",font=("Bastion",14,"bold"))
    button2.place(x=850,y=55)


    def reading_collection():
        with open("bookco.txt","r") as f:
         txt=0
         while True:
           read=f.readlines()
           if not read:
               break
           txt=read[:]
        for dat in txt:
          books=dat.split(",")
        return(books)
    ulevel1=reading_collection()






    def button_collection(book_name,height):
      button=Label(bodyframe,text=str(book_name),fg="#000000",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
      button.place(x=140,y=height)

    def button(e,height):
      button=Label(bodyframe,text=str(e),fg="#000000",bg="white",font=("Microsoft YaHei UI Light",12,"bold"))
      button.place(x=55,y=height)



    def print_collection(ulevel1):
      lst=ulevel1[:]
      height=90
      e=1
      for i in lst:
          #delete_button(i,height)
          button_collection(i,height)
          button(e,height)
          height+=30
          e+=1

    print_collection(ulevel1)
    



 

    
#############################################################################################################################################################
##    bodyframe=Frame(screen,bg="white")
##    bodyframe.place(x="328",y="110",width=1040,height=650)

##    panel=Label(bodyframe,text="Admin Panel",fg="black",bg="white",font=("Microsoft YaHei UI Light",15,"bold"))
##    panel.place(x=10,y=20)
##
##    bar=Frame(bodyframe,bg="#030303")
##    bar.place(x="0",y="60",width=1040,height=30)

     
    

##    bd1=Label(bar,text="Date",fg="#E3CF57",bg="#030303",font=("Microsoft YaHei UI Light",14,"bold"))
##    bd1.place(x=100,y=0)
##
##    bd2=Label(bar,text="Time",fg="#E3CF57",bg="#030303",font=("Microsoft YaHei UI Light",14,"bold"))
##    bd2.place(x=500,y=0)
##
##    bd3=Label(bar,text="Name",fg="#E3CF57",bg="#030303",font=("Microsoft YaHei UI Light",14,"bold"))
##    bd3.place(x=900,y=0)

 
    screen.mainloop()



img=PhotoImage(file="C:/Users/Lenovo X240/Downloads/login.png")
img_label=Label(root,image=img)
img_label.pack()
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)
heading=Label(frame,text="Sign-in",fg="#8A360F",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)

###########################################################################################################################

def on_enter(e):
  user.delete(0, "end")

def on_leave(e):
  name=user.get()
  if name=="":
    user.insert(0,"Username")



user=Entry(frame,width=25,fg="#8A360F",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="#8A360F").place(x=25,y=107)


###########################################################################################################################

def on_enter(e):
  password.delete(0, "end")

def on_leave(e):
  name=password.get()
  if name=="":
    password.insert(0,"Password")


password=Entry(frame,width=25,fg="#8A360F",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
password.place(x=30,y=150)
password.insert(0,"Password")
password.bind("<FocusIn>",on_enter)
password.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg="#8A360F").place(x=25,y=177)

###########################################################################################################################

Button(frame,width=39,pady=7,text="Sign-in",bg="#E3CF57",fg="#8A360F",border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Forget Password ?",fg="#8A360F",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=35,y=255)

root.mainloop()
