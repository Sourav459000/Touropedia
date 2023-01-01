from tkinter import *
import random
from all import AllDict as Ad
from Historical import HistTour as Ht
from Shopping import ShopTour as St
from adventure import AdvTour as At
from pilgrimtour import PilTour as Pt
import statistics
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sourav@45",
    database='rating'
)
cur = mydb.cursor()


def rating_button(place_name):
    get_initial_rating_of_place = "select * from rating WHERE place_name = %s"
    place = [place_name]
    cur.execute(get_initial_rating_of_place,place)
    initial_rating = cur.fetchmany()
    initial_rating = float(initial_rating[0][2])
    get_user_rating_label = Label(text="Rate the place between 1 to 5:")
    get_user_rating_label.place(x=10, y=107)
    get_user_rating = Entry(width=5)
    get_user_rating.insert(END,string="4")
    get_user_rating.place(x=10, y=130)
    mean_ke_liye_ = float(get_user_rating.get())
    print(mean_ke_liye_)
    list_mean = [initial_rating,mean_ke_liye_]
    final_rating = statistics.mean(list_mean)
    updated_rating = "UPDATE rating SET rating = %s WHERE place_name = %s"
    p = [final_rating, place_name]
    cur.execute(updated_rating, p)
    mydb.commit()


def rating():
    """Accepts the rating on particular place from the user and perform mean operation with the rating in the
    database. Later, updates the mean value into the database. """
    reset()
    canvas = Canvas(width=1550, height=800, highlightthickness=0)
    bg_img1 = PhotoImage(file="Touropedia.png")
    canvas.create_image(500, 300, image=bg_img1)
    canvas.place(anchor=NW,x=0, y=0)
    rate_place_name = Label(text="Name of the place? ",font=("Arial",15))
    rate_place_name.place(x=10,y=10)
    rate_place_name_entry = Entry(width=30)
    rate_place_name_entry.place(x=10,y=42)
    get_rating_button = Button(text="Find place",font=("Arial",15),command=lambda:rating_button(rate_place_name_entry.get().title()))
    get_rating_button.place(x=10,y=65)
    window.mainloop()

def contact():
    """Provide the contact information."""
    reset()
    canvas = Canvas(width=1550, height=800, highlightthickness=0)
    bg_img1 = PhotoImage(file="Touropedia.png")
    canvas.create_image(500, 300, image=bg_img1)
    canvas.place(anchor=NW,x=0, y=0)
    Label(canvas,text='''It's me, touropedia, your perfect guide for exploring Pune's hidden gems. My goal is to''',font=("Arial",17),bg="#7DE5ED").place(anchor=W,x=5,y=110)
    Label(canvas,text='''help you find places to visit based on your mood. We offer a searchable database of places''',font=("Arial",17),bg="#7DE5ED").place(anchor=W,x=5,y=140)
    Label(canvas,text='''and a way to rate your favorites. For any further assistance you can get in touch with us.''',font=("Arial",17),bg="#7DE5ED").place(anchor=W,x=5,y=170)
    Label(canvas,text='''Contact details: ''',font=("Arial",17),bg="#7DE5ED").place(anchor=W,x=5,y=200)
    Label(canvas,text='''Mail: customercare.touropedia@gmail.com''',font=("Arial",17),bg="#7DE5ED").place(anchor=W,x=5,y=230)

    window.mainloop()


def particular():  # not sorted yet
    """Provides the information about particular place."""
    reset()
    canvas = Canvas(width=1550, height=800, highlightthickness=0)
    bg_img1 = PhotoImage(file="Touropedia.png")
    canvas.create_image(500, 300, image=bg_img1)
    canvas.place(anchor=NW,x=0, y=0)
    search_label = Label(window, text="Name of the place?     ")
    search_label.place(x=5, y=5)
    search_entry = Entry()
    search_entry.place(x=5, y=28)
    search_button = Button(text="Search",width=5,command=lambda: result(dictionary=Ad, destination=search_entry.get().title()))
    search_button.place(x=5, y=49)

    window.mainloop()


def result(dictionary, destination):
    """Prints the info by taking dictionary and destination as parameters"""
    my_label = Label()
    dict_destination = Label(text=f"Destination: {destination}",font=("Arial",13), bg="#7DE5ED")
    dict_location = Label(text=f"Location: {dictionary[destination]['Location']}",font=("Arial",13), bg="#7DE5ED")
    dict_about = Label(text=f"About the location: {dictionary[destination]['About the location']}",font=("Arial",13), bg="#7DE5ED")
    dict_timings = Label(text=f"Timings: {dictionary[destination]['Timings']}",font=("Arial",13), bg="#7DE5ED")
    dict_how_to_go = Label(text=f"How to go: {dictionary[destination]['How to go']}",font=("Arial",13), bg="#7DE5ED")
    dict_when_to_go = Label(text=f"When to go: {dictionary[destination]['When to go']}",font=("Arial",13), bg="#7DE5ED")
    my_label.grid(column=0,row=0,pady=30)
    dict_destination.grid(sticky=W, column=0, row=4,pady=2)
    dict_location.grid(sticky=W, column=0, row=5, pady=2)
    dict_about.grid(sticky=W, column=0, row=6, pady=2)
    dict_timings.grid(sticky=W, column=0,row=7,pady=2)
    dict_how_to_go.grid(sticky=W, column=0, row=8, pady=2)
    dict_when_to_go.grid(sticky=W, column=0, row=9, pady=2)


def locate(dictionary):
    """locates the place by taking dictionary as the only input"""
    reset()
    a = random.choice(list(dictionary))
    canvas = Canvas(width=1550, height=800, highlightthickness=0)
    bg_img1 = PhotoImage(file="Touropedia.png")
    canvas.create_image(500, 300, image=bg_img1)
    label_text1 = canvas.create_text(480, 50, text=a, font=("arial", 30),fill='black')
    label_box1 = canvas.bbox(label_text1)
    canvas.create_rectangle(label_box1,outline="black",width=3,fill="white")
    label_text1 = canvas.create_text(480, 50, text=a, font=("arial", 30),fill='black')
    canvas.place(anchor=NW,x=0, y=0)
    result(dictionary=dictionary, destination=a)
    satisfied = Label(text="Is the suggestion satisfactory to you?",font=("Arial",13), bg="#7DE5ED")
    y = Button(text="Yes",font=("Arial",13), bg="#7DE5ED")
    n = Button(text="No",font=("Arial",13), bg="#7DE5ED", command=lambda:locate(dictionary))

    satisfied.grid(sticky=W, column=0, row=10)
    y.grid(sticky=W, column=0, row=11, pady=3)
    n.grid(sticky=W, column=0, row=12, pady=3)

    window.mainloop()


def reset():
    global window
    window.destroy()
    window = Tk()
    window.title("Tour Guide")
    window.geometry('1000x600+0+0')
    # window.config(bg="#7DE5ED")


def find():
    """Gets user's interests."""
    reset()
    canvas = Canvas(width=1550, height=800, highlightthickness=0)
    bg_img1 = PhotoImage(file="Touropedia.png")
    canvas.create_image(500, 300, image=bg_img1)
    label_text1 = canvas.create_text(480, 50, text="    Let us know about your interests!", font=("arial", 30),fill='black')
    label_box1 = canvas.bbox(label_text1)
    canvas.create_rectangle(label_box1,outline="black",width=3,fill="white")
    label_text1 = canvas.create_text(480, 50, text="    Let us know about your interests!", font=("arial", 30),fill='black')
    canvas.place(anchor=NW,x=0, y=0)

    option1 = Button(canvas,text="Educational tour",font=("Arial",15), bg="#7DE5ED", width=20)
    option1.place(x=380, y=90)

    option2 = Button(canvas,text="Pilgrimage tour",font=("Arial",15), bg="#7DE5ED", command=lambda:locate(Pt), width=20)
    option2.place(x=380, y=135)

    option3 = Button(canvas,text="Adventure",font=("Arial",15), bg="#7DE5ED", command=lambda:locate(At), width=20)
    option3.place(x=380, y=180)

    option4 = Button(canvas,text="Shopping",font=("Arial",15), bg="#7DE5ED", command=lambda:locate(St), width=20)
    option4.place(x=380, y=225)

    option5 = Button(canvas,text="Historical places",font=("Arial",15), bg="#7DE5ED", command=lambda:locate(Ht), width=20)
    option5.place(x=380, y=270)

    option6 = Button(canvas,text="Nature",font=("Arial",15), bg="#7DE5ED", width=20)
    option6.place(x=380, y=315)

    option7 = Button(canvas,text="Top picks",font=("Arial",15), bg="#7DE5ED", width=20)
    option7.place(x=380, y=360)

    window.mainloop()


def touropedia():
    global window
    window = Tk()
    window.title("Tour Guide")
    window.geometry('1000x600+0+0')
    # window.config(bg="#7DE5ED")

    canvas = Canvas(width=1550, height=800, highlightthickness=0)
    bg_img = PhotoImage(file="Touropedia.png")
    canvas.create_image(500, 300, image=bg_img)
    label_text = canvas.create_text(230, 50, text="TOUROPEDIA", font=("Arial", 50, "italic"),fill='#F91A1A')
    label_box = canvas.bbox(label_text)
    canvas.create_rectangle(label_box,outline="black",width=3,fill="white")
    label_text = canvas.create_text(230, 50, text="TOUROPEDIA", font=("Arial", 50, "italic"),fill='#F91A1A')
    canvas.grid(column=0, row=0)

    Label(window, text='''Greetings!,''', font=("Arial", 20)).place(anchor="w", x=8, y=150)
    Label(window, text="I will help you find perfect places to visit in Pune.",font=("Arial", 20)).place(anchor="w", x=8, y=190)

    find_button = Button(window,text="Select destination", bg="#7DE5ED", fg="black",font=("Arial",15),command=lambda:find(), width=40)
    find_button.place(x=8, y=250)

    rating_button = Button(window,text="Rate the location", bg="#7DE5ED",font=("Arial",15), fg="black", width=40,command=rating)
    rating_button.place(x=8, y=295)

    specific_search = Button(window,text="Search for the destination", bg="#7DE5ED", fg="black",font=("Arial",15), command=lambda: particular(),width=40)
    specific_search.place(x=8, y=340)

    contact_button = Button(window,text="About Us", bg="#7DE5ED", fg="black",font=("Arial",15), command=lambda: contact(), width=40)
    contact_button.place(x=8, y=385)

    window.mainloop()


touropedia()
