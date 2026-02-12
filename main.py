import tkinter

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.geometry("250x300")
screen.iconbitmap("C:/Users/enis/PycharmProjects/BMICalculator/bmi.ico")

height_label = tkinter.Label(text="Enter your height (cm)", font=("Arial Bold", 10, "bold"))
height_label.pack(pady=(20, 0))
height_entry = tkinter.Entry(width=9, font=("Arial", 10))
height_entry.pack()

weight_label = tkinter.Label(text="Enter your weight (kg)", font=("Arial Bold", 10, "bold"))
weight_label.pack(pady=(5,0))
weight_entry = tkinter.Entry(width=9, font=("Arial", 10))
weight_entry.pack()

result_label = tkinter.Label(text="Result :", font=("Arial Bold", 10, "bold"))

note_label = tkinter.Label(text="Note : You can only use values \n"
                                       "that are positive.\n"
                                       "0 and negative values \n"
                                       "are not allowed !\n"
                                       "Example values: Height = 185 or 185.5\n"
                                       "Weight = 80 or 80.2", font=("Arial", 10, "bold"),fg="blue")
note_label.pack(side="bottom")

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    except ValueError:
        result_label.config(text="Error! You can only enter numbers \nfor height and weight!", fg="red")
        result_label.pack()
        return

    if height <= 0 or weight <= 0:
        result_label.config(text="Please enter a positive number \nfor both height and weight values!", fg="red")
        result_label.pack()
        return

    bmi = weight / ((height / 100) ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = "underweight"
        color = "#31bcf4"
    elif 18.5 <= bmi <= 24.9:
        category = "normal weight"
        color = "#8bc34a"
    elif 25 <= bmi <= 29.9:
        category = "overweight"
        color = "#fec107"
    elif 30 <= bmi <= 34.9:
        category = "Class I Obesity"
        color = "#fb8c00"
    elif 35 <= bmi <= 39.9:
        category = "Class II Obesity"
        color = "#e53935"
    else:
        category = "Class III Obesity"
        color = "#e53935"

    result_text = f"Your BMI index is {bmi}\nYou are {category}."
    result_label.config(text=result_text, fg=color)
    result_label.pack(pady=(5,0))

calculate_button = tkinter.Button(text="Calculate \n"
                                       "my BMI", font=("Arial Bold", 8, "bold"), width=7, height=2, command=calculate_bmi, fg="brown")
calculate_button.pack(pady=(5,0))

screen.mainloop()