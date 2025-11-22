import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

from ceasor_cipher import encrypt_message, decrypt_message


class CaesarGUI:
    def __init__(self, root):
        self.root = root
        root.title('Caesar Cipher — GUI')

        main = ttk.Frame(root, padding=10)
        main.grid(row=0, column=0, sticky='nsew')

        # Configure grid
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)

        # Input label and text
        ttk.Label(main, text='Input Text:').grid(row=0, column=0, sticky='w')
        self.input_text = ScrolledText(main, width=60, height=10)
        self.input_text.grid(row=1, column=0, columnspan=4, sticky='nsew', pady=(0, 8))

        # Shift controls
        ttk.Label(main, text='Shift (0-25):').grid(row=2, column=0, sticky='w')
        self.shift_var = tk.IntVar(value=3)
        self.shift_spin = ttk.Spinbox(main, from_=0, to=25, textvariable=self.shift_var, width=5)
        self.shift_spin.grid(row=2, column=1, sticky='w')

        # Buttons
        self.encrypt_btn = ttk.Button(main, text='Encrypt →', command=self.on_encrypt)
        self.encrypt_btn.grid(row=2, column=2, sticky='e')

        self.decrypt_btn = ttk.Button(main, text='← Decrypt', command=self.on_decrypt)
        self.decrypt_btn.grid(row=2, column=3, sticky='w')

        # Output label and text
        ttk.Label(main, text='Output Text:').grid(row=3, column=0, sticky='w', pady=(8, 0))
        self.output_text = ScrolledText(main, width=60, height=10)
        self.output_text.grid(row=4, column=0, columnspan=4, sticky='nsew')
        self.output_text.configure(state='disabled')

        # Action buttons
        btn_frame = ttk.Frame(main)
        btn_frame.grid(row=5, column=0, columnspan=4, pady=(8, 0), sticky='ew')
        ttk.Button(btn_frame, text='Copy Output', command=self.copy_output).grid(row=0, column=0, padx=4)
        ttk.Button(btn_frame, text='Clear', command=self.clear_all).grid(row=0, column=1, padx=4)
        ttk.Button(btn_frame, text='Load From File', command=self.load_file).grid(row=0, column=2, padx=4)
        ttk.Button(btn_frame, text='Save Output', command=self.save_output).grid(row=0, column=3, padx=4)

        # Status
        self.status = tk.StringVar(value='Ready')
        ttk.Label(main, textvariable=self.status).grid(row=6, column=0, columnspan=4, sticky='w', pady=(6, 0))

        # Keyboard bindings
        root.bind('<Control-e>', lambda e: self.on_encrypt())
        root.bind('<Control-d>', lambda e: self.on_decrypt())

    def _set_status(self, text):
        self.status.set(text)

    def _write_output(self, text):
        self.output_text.configure(state='normal')
        self.output_text.delete('1.0', 'end')
        self.output_text.insert('1.0', text)
        self.output_text.configure(state='disabled')

    def on_encrypt(self):
        plain = self.input_text.get('1.0', 'end').rstrip('\n')
        try:
            shift = int(self.shift_var.get())
        except Exception:
            messagebox.showerror('Invalid shift', 'Shift must be an integer between 0 and 25')
            return
        result = encrypt_message(plain, shift)
        self._write_output(result)
        self._set_status(f'Encrypted with shift={shift}')

    def on_decrypt(self):
        cipher = self.input_text.get('1.0', 'end').rstrip('\n')
        try:
            shift = int(self.shift_var.get())
        except Exception:
            messagebox.showerror('Invalid shift', 'Shift must be an integer between 0 and 25')
            return
        result = decrypt_message(cipher, shift)
        self._write_output(result)
        self._set_status(f'Decrypted with shift={shift}')

    def copy_output(self):
        self.root.clipboard_clear()
        text = self.output_text.get('1.0', 'end')
        self.root.clipboard_append(text)
        self._set_status('Output copied to clipboard')

    def clear_all(self):
        self.input_text.delete('1.0', 'end')
        self.output_text.configure(state='normal')
        self.output_text.delete('1.0', 'end')
        self.output_text.configure(state='disabled')
        self._set_status('Cleared')

    def load_file(self):
        path = filedialog.askopenfilename(title='Open text file', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if not path:
            return
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = f.read()
        except Exception as e:
            messagebox.showerror('Error', f'Could not read file: {e}')
            return
        self.input_text.delete('1.0', 'end')
        self.input_text.insert('1.0', data)
        self._set_status(f'Loaded {path}')

    def save_output(self):
        path = filedialog.asksaveasfilename(title='Save output', defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if not path:
            return
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(self.output_text.get('1.0', 'end'))
        except Exception as e:
            messagebox.showerror('Error', f'Could not write file: {e}')
            return
        self._set_status(f'Saved output to {path}')


def main():
    root = tk.Tk()
    app = CaesarGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
