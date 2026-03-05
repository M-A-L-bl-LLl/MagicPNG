import json
import pathlib
import subprocess
import threading
import tkinter
from tkinter.messagebox import showinfo

import re
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog as fd
import customtkinter
from PIL import Image

VALID_SUFFIXES = {'.jpg', '.jpeg', '.png'}

import sys as _sys, os as _os
if getattr(_sys, 'frozen', False):
    _config_dir = pathlib.Path(_os.getenv('APPDATA')) / 'MagicPNG'
    _config_dir.mkdir(parents=True, exist_ok=True)
else:
    _config_dir = pathlib.Path(__file__).parent
CONFIG_FILE = _config_dir / 'config.json'
MODELS = {
    'u2net — universal':        'u2net',
    'u2netp — fast & light':    'u2netp',
    'u2net_human_seg — people': 'u2net_human_seg',
    'isnet — high quality':     'isnet-general-use',
    'silueta — products':       'silueta',
}


def load_config():
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {}


def save_config(key, value):
    cfg = load_config()
    cfg[key] = value
    CONFIG_FILE.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding='utf-8')


def process_batch(files, output_folder, model_name, fmt, app):
    app.after(0, lambda: app.eraseBtn.configure(text='Loading...'))
    from rembg import remove, new_session
    model_file = pathlib.Path.home() / '.u2net' / f'{model_name}.onnx'
    if not model_file.exists():
        app.after(0, lambda: app.eraseBtn.configure(text='Downloading model...'))
    session = new_session(model_name)
    ext = '.webp' if fmt == 'WebP' else '.png'
    total = len(files)
    last_input = last_output = None
    for i, input_file in enumerate(files, 1):
        app.after(0, lambda i=i: app.eraseBtn.configure(text=f'Processing {i}/{total}...'))
        output_file = pathlib.Path(output_folder) / f'{input_file.stem}_MagicPNG{ext}'
        output_img = remove(Image.open(input_file), session=session)
        output_img.save(output_file)
        last_input, last_output = input_file, output_file
    app.after(0, lambda: app.on_done(last_input, last_output, total))


class App(customtkinter.CTk, TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        TkinterDnD._require(self)

        self.selected_files = []
        import sys
        self.dir_path = pathlib.Path(sys._MEIPASS) if getattr(sys, 'frozen', False) else pathlib.Path(__file__).parent

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.geometry('800x600')
        self.title("MagicPNG")
        self.resizable(False, False)
        self.iconbitmap(self.dir_path / 'Icons' / 'MagicPngAppIcon_MagicPNG.ico')

        self._build_ui()

    def _build_ui(self):
        bg_pil = Image.open(self.dir_path / 'Icons' / 'bg.png')
        bg = customtkinter.CTkImage(bg_pil, size=bg_pil.size)
        l1 = customtkinter.CTkLabel(master=self, image=bg, text="")
        l1.pack()

        frame = customtkinter.CTkFrame(master=l1, width=600, height=400, corner_radius=0)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        customtkinter.CTkLabel(master=frame, text="Direction to your Image", font=('Century Gothic', 25)).place(x=200, y=45)

        folder_img = customtkinter.CTkImage(Image.open(self.dir_path / 'Icons' / 'folder.png'))

        self.textbox_file = customtkinter.CTkTextbox(master=frame, width=500, height=20, state='disabled')
        self.textbox_file.place(x=30, y=100)
        self.textbox_file.drop_target_register(DND_FILES)
        self.textbox_file.dnd_bind('<<Drop>>', self.handle_drop)

        customtkinter.CTkButton(master=frame, text='', image=folder_img, width=20, height=20, command=self.select_file).place(x=540, y=100)

        customtkinter.CTkLabel(master=frame, text="Model:", font=('Century Gothic', 16)).place(x=30, y=155)
        self.model_menu = customtkinter.CTkOptionMenu(master=frame, values=list(MODELS.keys()), width=280)
        self.model_menu.place(x=110, y=152)

        customtkinter.CTkLabel(master=frame, text="Direction to export Folder", font=('Century Gothic', 25)).place(x=200, y=200)

        self.textbox_path = customtkinter.CTkTextbox(master=frame, width=500, height=20, state='disabled')
        self.textbox_path.place(x=30, y=250)
        cfg = load_config()
        if last_out := cfg.get('last_output_dir'):
            self.textbox_path.configure(state='normal')
            self.textbox_path.insert("0.0", last_out)
            self.textbox_path.configure(state='disabled')

        customtkinter.CTkButton(master=frame, text='', image=folder_img, width=20, height=20, command=self.select_path).place(x=540, y=250)

        customtkinter.CTkLabel(master=frame, text="Format:", font=('Century Gothic', 16)).place(x=30, y=290)
        self.format_btn = customtkinter.CTkSegmentedButton(master=frame, values=['PNG', 'WebP'])
        self.format_btn.set('PNG')
        self.format_btn.place(x=115, y=287)

        self.eraseBtn = customtkinter.CTkButton(master=frame, text='Erase', width=150, height=50, font=('Century Gothic', 25), command=self.erase_bg)
        self.eraseBtn.place(x=250, y=335)

        self.openFolderBtn = customtkinter.CTkButton(master=frame, text='📂 Open Folder', width=150, height=50, font=('Century Gothic', 18))

        self.progressbar = customtkinter.CTkProgressBar(master=frame, width=300, mode='indeterminate')

    def handle_drop(self, event):
        raw_paths = re.findall(r'\{[^}]+\}|[^\s]+', event.data)
        paths = [pathlib.Path(p.strip('{}')) for p in raw_paths]
        valid = [p for p in paths if p.suffix.lower() in VALID_SUFFIXES]
        if not valid:
            return
        self.selected_files = valid
        label = str(valid[0]) if len(valid) == 1 else f'{len(valid)} files selected'
        self.textbox_file.configure(state='normal')
        self.textbox_file.delete("0.0", "end")
        self.textbox_file.insert("0.0", label)
        self.textbox_file.configure(state='disabled')

    def select_file(self):
        cfg = load_config()
        names = fd.askopenfilenames(
            filetypes=(('Images', '*.jpg *.png'), ('JPG', '*.jpg'), ('PNG', '*.png')),
            initialdir=cfg.get('last_input_dir')
        )
        if not names:
            return
        self.selected_files = [pathlib.Path(n) for n in names]
        save_config('last_input_dir', str(pathlib.Path(names[0]).parent))
        label = names[0] if len(names) == 1 else f'{len(names)} files selected'
        self.textbox_file.configure(state='normal')
        self.textbox_file.delete("0.0", "end")
        self.textbox_file.insert("0.0", label)
        self.textbox_file.configure(state='disabled')

    def select_path(self):
        cfg = load_config()
        path = fd.askdirectory(initialdir=cfg.get('last_output_dir'))
        if not path:
            return
        save_config('last_output_dir', path)
        self.textbox_path.configure(state='normal')
        self.textbox_path.delete("0.0", "end")
        self.textbox_path.insert("0.0", path)
        self.textbox_path.configure(state='disabled')

    def erase_bg(self):
        if not self.selected_files or len(self.textbox_path.get("0.0", "end-1c")) == 0:
            showinfo(title="Fail", message="Choose Image and Folder!")
            return
        output_folder = self.textbox_path.get("1.0", 'end-1c')
        model_name = MODELS[self.model_menu.get()]
        fmt = self.format_btn.get()
        self.eraseBtn.configure(state='disabled', text='Processing...')
        self.progressbar.place(x=150, y=395)
        self.progressbar.start()
        threading.Thread(
            target=process_batch,
            args=(list(self.selected_files), output_folder, model_name, fmt, self),
            daemon=True
        ).start()

    def on_done(self, last_input, last_output, total):
        self.progressbar.stop()
        self.progressbar.place_forget()
        self.eraseBtn.configure(state='normal', text='Erase')
        output_folder = last_output.parent
        self.openFolderBtn.configure(state='normal', command=lambda: subprocess.Popen(f'explorer "{output_folder}"'))
        self.openFolderBtn.place(x=420, y=342)
        title = "Preview" if total == 1 else f"Preview — last of {total} processed"
        self.show_preview(last_input, last_output, title)

    def show_preview(self, input_file, output_file, title="Preview"):
        PREVIEW_SIZE = (350, 350)
        preview = customtkinter.CTkToplevel(self)
        preview.title(title)
        preview.resizable(False, False)
        preview.attributes('-topmost', True)
        preview.after(300, lambda: preview.attributes('-topmost', False))

        original = Image.open(input_file).convert("RGBA")
        original.thumbnail(PREVIEW_SIZE)
        result = Image.open(output_file).convert("RGBA")
        result.thumbnail(PREVIEW_SIZE)

        img_original = customtkinter.CTkImage(original, size=original.size)
        img_result = customtkinter.CTkImage(result, size=result.size)

        frame_preview = customtkinter.CTkFrame(preview)
        frame_preview.pack(padx=20, pady=20)

        customtkinter.CTkLabel(frame_preview, text="Original", font=('Century Gothic', 16)).grid(row=0, column=0, padx=10)
        customtkinter.CTkLabel(frame_preview, text="Result", font=('Century Gothic', 16)).grid(row=0, column=1, padx=10)
        customtkinter.CTkLabel(frame_preview, image=img_original, text="").grid(row=1, column=0, padx=10, pady=10)
        customtkinter.CTkLabel(frame_preview, image=img_result, text="").grid(row=1, column=1, padx=10, pady=10)


if __name__ == '__main__':
    app = App()
    app.mainloop()
