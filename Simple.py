import cv2
import tkinter
from tkinter import filedialog, Tk, Button, messagebox, PhotoImage, Canvas, Label
from PIL import ImageTk, Image

root = Tk()
root.title("DOODLE CRAFT")
root.geometry("1200x400")
cv = Canvas(root, height=400, width=400)
image_path = ImageTk.PhotoImage(file=r"C:/Users/arun1/Downloads/my doodle craft.png")
bg_image = tkinter.Label(root, image=image_path)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)


def open_and_convert_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = cv2.imread(file_path)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inverted_image = 255 - gray_image
        blurred = cv2.GaussianBlur(inverted_image, (111, 111), 0)
        inverted_blurred = 255 - blurred
        pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
        new = cv2.resize(pencil_sketch, (1540, 800))
        cv2.imshow("pencil_sketch", new)

        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    def click():
        messagebox.askquestion("Warning", "Are you sure you want to exit")

    open_button = Button(root, command=open_and_convert_image, text="Open Image", activeforeground="Black",
                         activebackground="Grey", bg="Grey", fg="white", font=("Ariel", 15), pady=10, padx=50)
    b = Button(root, text="exit", command=click, activeforeground="Black", activebackground="Grey", bg="Grey",
               fg="white", font=("Ariel", 15), pady=10, padx=50)
    open_button.place(x=1230, y=705)
    b.place(x=1255, y=763)
    root.mainloop()


if __name__ == "__main__":
    main()