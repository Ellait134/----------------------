import tkinter as tk
from tkinter import messagebox
import random

class GhostGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра: Приведение Монти Холла")
        self.current_room = 1
        self.ghost_door = random.randint(1, 3)
        
        self.label = tk.Label(root, text="Добро пожаловать в игру 'Найди дверь без привидения'!")
        self.label.pack(pady=20)
        
        self.room_label = tk.Label(root, text=f"Вы находитесь в комнате {self.current_room}. Выберите дверь:")
        self.room_label.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)
        
        self.buttons = []
        for i in range(1, 4):
            button = tk.Button(self.button_frame, text=f"Дверь {i}", command=lambda i=i: self.check_door(i))
            button.grid(row=0, column=i-1, padx=10)
            self.buttons.append(button)
        
        self.reset_frame = tk.Frame(root)
        
        self.play_again_button = tk.Button(self.reset_frame, text="Играть снова", command=self.play_again)
        self.play_again_button.grid(row=0, column=0, padx=10)
        
        self.exit_button = tk.Button(self.reset_frame, text="Выйти", command=self.root.quit)
        self.exit_button.grid(row=0, column=1, padx=10)
        
    def check_door(self, choice):
        if choice == self.ghost_door:
            messagebox.showinfo("Игра закончена", f"Вы выбрали дверь с привидением! Игра закончена.\nВы дошли до комнаты {self.current_room}.")
            self.show_final_menu()
        else:
            self.current_room += 1
            self.ghost_door = random.randint(1, 3)
            self.room_label.config(text=f"Вы находитесь в комнате {self.current_room}. Выберите дверь:")
            messagebox.showinfo("Продолжайте", "Поздравляем! Вы выбрали дверь без привидения. Переходите в следующую комнату.")

    def show_final_menu(self):
        self.button_frame.pack_forget()
        self.reset_frame.pack(pady=20)
        
    def play_again(self):
        self.current_room = 1
        self.ghost_door = random.randint(1, 3)
        self.room_label.config(text=f"Вы находитесь в комнате {self.current_room}. Выберите дверь:")
        self.reset_frame.pack_forget()
        self.button_frame.pack(pady=20)

def main():
    root = tk.Tk()
    game = GhostGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
