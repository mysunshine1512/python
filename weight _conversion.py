from tkinter import*

wc = Tk()
wc.title('Weight Conversion')
wc.geometry('720x200')

def weight_conversion():
    kg = kg_entry.get()
    gram = float(kg) * 1000
    lbl_result_gram['text'] = f'{round(gram, 2)}'
    pounds = float(kg) * 2.20462
    lbl_result_pounds['text'] = f'{round(pounds, 2)}'
    ounce = float(kg) * 35.274
    lbl_result_ounce['text'] = f'{round(ounce, 2)}'
    
# Nhập kg và nút chuyển đổi
kg_frame = Frame(wc)
text_enter = Label(kg_frame, text='Enter the weight in Kg: ', font=('arial rounded mt', 20)).grid(row=0, column=0,sticky='w')
kg_entry = Entry(kg_frame, font=('arial rounded mt', 20))
kg_entry.grid(row=0, column=1)
Button(kg_frame, text='Convert', font=('arial rounded mt', 20), command=weight_conversion, relief=RIDGE).grid(row=0, column=2)
kg_frame.grid(row=0, column=0)
# Trả kết quả
result_gram_frame = Frame(wc)
text_gram = Label(result_gram_frame, text='Gram', font=('arial rounded mt', 20))
text_gram.grid(row=0, column=0)
lbl_result_gram = Label(result_gram_frame, font=('arial rounded mt', 20))
lbl_result_gram.grid(row=1,column=0)
result_gram_frame.place(x=70, y=100)
result_pounds_frame = Frame(wc)
text_puonds = Label(result_pounds_frame, text='Pounds', font=('arial rounded mt', 20))
text_puonds.grid(row=0, column=0)
lbl_result_pounds = Label(result_pounds_frame, font=('arial rounded mt', 20))
lbl_result_pounds.grid(row=1,column=0)
result_pounds_frame.place(x=310, y=100)
result_ounce_frame = Frame(wc)
text_ounce = Label(result_ounce_frame, text='Ounce', font=('arial rounded mt', 20))
text_ounce.grid(row=0, column=0)
lbl_result_ounce = Label(result_ounce_frame, font=('arial rounded mt', 20))
lbl_result_ounce.grid(row=1,column=0)
result_ounce_frame.place(x=550, y=100)

wc.mainloop()