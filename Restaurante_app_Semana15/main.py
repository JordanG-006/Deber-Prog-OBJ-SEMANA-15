import tkinter as tk
import os
from ui.main_view import MainView

def main():
    # Asegurar que existan los directorios necesarios
    os.makedirs("datos", exist_ok=True)
    os.makedirs("assets", exist_ok=True)
    
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
