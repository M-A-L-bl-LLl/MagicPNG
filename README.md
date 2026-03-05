<p align="center">
  <img src="Icons/MagicPngAppIcon_MagicPNG.ico" width="100" alt="MagicPNG logo"/>
</p>

<h1 align="center">MagicPNG</h1>

<p align="center">
  AI-powered background removal desktop app for Windows
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.1.0-blue" />
  <img src="https://img.shields.io/badge/platform-Windows-lightgrey" />
  <img src="https://img.shields.io/badge/python-3.12-yellow" />
</p>

<p align="center">
  <a href="https://github.com/M-A-L-bl-LLl/MagicPNG/releases/latest/download/MagicPNG_Setup.exe">
    <img src="https://img.shields.io/badge/⬇️ Download-MagicPNG_Setup.exe-brightgreen?style=for-the-badge" alt="Download"/>
  </a>
</p>

---

<br>

# <img src="https://flagcdn.com/w40/gb.png" height="20"/> English

---

**MagicPNG** is a desktop application for AI-powered background removal. Supports JPG and PNG input, saves the result as a transparent PNG or WebP.

---

### ✨ Features

- 🖼️ One-click background removal
- 📂 Batch processing of multiple files at once
- 🤖 5 AI models to choose from for different tasks
- 👁️ Side-by-side preview (original vs result)
- 💾 Save as PNG or WebP
- 🖱️ Drag & drop files directly into the window
- ⚡ Fast startup — model is downloaded only on first use

---

### 📦 Installation

The installer is located in the `installer/` folder. Run `MagicPNG_Setup.exe` — it will create shortcuts on the desktop and in the Start menu.

> ⚠️ On the first click of the **Erase** button, the app will automatically download the AI model (~170 MB). An internet connection is required.

---

### 🚀 How to use

1. **Select an image** — click the folder icon next to "Direction to your Image" or drag & drop file(s) directly into the field. Supported formats: `.jpg`, `.jpeg`, `.png`.

2. **Select an output folder** — click the folder icon next to "Direction to export Folder".

3. **Choose a model** (optional):

   - `u2net` — Universal, works well for most images
   - `u2netp` — Fast and lightweight
   - `u2net_human_seg` — Optimized for people
   - `isnet` — High quality
   - `silueta` — Best for products and objects

4. **Choose output format** — PNG or WebP.

5. **Click Erase** — processing will begin. On first run, the model will be downloaded automatically.

6. When done, a **preview** window will open showing the original and result side by side. The **Open Folder** button will open the output folder.

---

### 🛠️ Run from source

```bash
pip install rembg customtkinter Pillow tkinterdnd2
python main.py
```

### 🔨 Build

```bash
python -m PyInstaller MagicPNG.spec -y
"C:\...\Inno Setup 6\ISCC.exe" installer.iss
```

---

<br>

# <img src="https://flagcdn.com/w40/ru.png" height="20"/> Русский

---

**MagicPNG** — десктопное приложение для удаления фона с изображений с помощью ИИ. Поддерживает JPG и PNG, сохраняет результат в PNG с прозрачным фоном или WebP.

---

### ✨ Возможности

- 🖼️ Удаление фона одним кликом
- 📂 Пакетная обработка нескольких файлов сразу
- 🤖 5 AI-моделей на выбор под разные задачи
- 👁️ Предпросмотр результата (оригинал vs результат)
- 💾 Сохранение в PNG или WebP
- 🖱️ Перетаскивание файлов прямо в окно (drag & drop)
- ⚡ Быстрый запуск — модель загружается только при первом использовании

---

### 📦 Установка

Установщик находится в папке `installer/`. Запусти `MagicPNG_Setup.exe` — он создаст ярлыки на рабочем столе и в меню Пуск.

> ⚠️ При первом нажатии кнопки **Erase** приложение автоматически скачает AI-модель (~170 МБ). Требуется интернет-соединение.

---

### 🚀 Как пользоваться

1. **Выбери изображение** — нажми на иконку папки рядом с полем "Direction to your Image" или перетащи файл(ы) прямо в поле. Поддерживаются форматы `.jpg`, `.jpeg`, `.png`.

2. **Выбери папку для сохранения** — нажми на иконку папки рядом с полем "Direction to export Folder".

3. **Выбери модель** (опционально):

   - `u2net` — Универсальная, подходит для большинства изображений
   - `u2netp` — Быстрая и лёгкая
   - `u2net_human_seg` — Оптимизирована для людей
   - `isnet` — Высокое качество
   - `silueta` — Для товаров и предметов

4. **Выбери формат** — PNG или WebP.

5. **Нажми Erase** — начнётся обработка. При первом запуске модель скачается автоматически.

6. После завершения откроется **предпросмотр** с оригиналом и результатом рядом. Кнопка **Open Folder** откроет папку с готовыми файлами.

---

### 🛠️ Запуск из исходников

```bash
pip install rembg customtkinter Pillow tkinterdnd2
python main.py
```

### 🔨 Сборка

```bash
python -m PyInstaller MagicPNG.spec -y
"C:\...\Inno Setup 6\ISCC.exe" installer.iss
```
