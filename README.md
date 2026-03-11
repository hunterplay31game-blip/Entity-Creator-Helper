# 🎮 GMod Entity Creator

[![.NET](https://img.shields.io/badge/.NET-8.0-512BD4?logo=dotnet)](https://dotnet.microsoft.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/yourusername/GModEntityCreator?color=green)](../../releases)
[![Issues](https://img.shields.io/github/issues/yourusername/GModEntityCreator)](../../issues)

**English** | [Русский](#russian)

---

## 📖 Description

**GMod Entity Creator** is a modern, beautiful WPF desktop application for creating custom entities, weapons, and vehicles for **Garry's Mod** addons. Built with C# and .NET 8, it features a sleek dark theme interface and generates all necessary Lua files with the correct structure and code templates.

![Preview](https://via.placeholder.com/800x600/1e1e1e/00d4ff?text=GMod+Entity+Creator+Preview)

---

## ✨ Features

- 🎨 **Modern Dark UI** - Beautiful interface with smooth animations and a professional look
- 🔫 **Entity & Weapon Creation** - Generate entities based on different base classes (`base_anim`, `base_vehicle`, `weapon_base`)
- 💾 **Custom Presets** - Save and reuse your custom base classes
- 👁️ **Live Code Preview** - View generated Lua code before creating files
- 🌍 **Bilingual Interface** - Full English and Russian language support
- ⚙️ **Customizable Options** - Set spawnability, admin-only access, categories, authors, etc.
- 📁 **Auto File Generation** - Automatically creates folder structures and Lua files (`shared.lua`, `init.lua`, `cl_init.lua`)
- 🚀 **Export Function** - Export generated code to any folder

---

## 🚀 Quick Start

### Installation

1. **Download the latest release** from the
2. **Extract** the archive to any folder
3. **Run** `GModEntityCreator.exe`

### Building from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/GModEntityCreator.git
cd GModEntityCreator

# Build the project
dotnet build --configuration Release

# Run the application
dotnet run --project GModEntityCreator/GModEntityCreator.csproj
```

### Requirements

- **.NET 8.0 Runtime** or later ([Download](https://dotnet.microsoft.com/download/dotnet/8.0))
- **Windows 10/11** (WPF application)

---

## 📖 Usage Guide

### Creating an Entity

1. **Launch** the application
2. **Select Addon Folder** - Click "📁 Browse" and choose your addon directory (e.g., `garrysmod/addons/myaddon`)
3. **Fill Entity Properties**:
   - **Entity Name** - Display name (PrintName)
   - **Entity ID** - Technical identifier (folder name)
   - **Base Class** - Choose from `base_anim`, `base_vehicle`, `weapon_base`, or custom
   - **Model Path** - Path to the model file
   - **Custom Functions** - Add your own Lua code (optional)
4. **Configure Additional Options**:
   - **Category** - Spawn menu category
   - **Author** - Your name
   - **Spawnable** - Available in spawn menu
   - **Admin Only** - Restricted to admins
5. **Preview Code** - Click "👁️ Preview Code" to review generated Lua
6. **Generate Files** - Click "📄 Generate Files" to create all files in your addon folder

### Creating a Weapon

1. Select **`weapon_base`** as the Base Class
2. Additional fields will appear:
   - **Base Damage** - Weapon damage value
   - **Ammo Type** - Choose from pistol, smg1, ar2, buckshot, 357, sniperround
3. Fill in other properties and generate

### Saving Custom Presets

1. Select **`custom`** as the Base Class
2. Enter your custom base class name
3. Click **"💾 Save Preset"** to save for future use
4. Select from saved presets in the dropdown

### Exporting Code

Click **"💾 Export"** to save generated Lua files to any folder without creating the full addon structure.

---

## 📁 File Structure

```
youraddon/
└── lua/
    └── entities/ (or weapons/)
        └── your_entity_id/
            ├── shared.lua    # Shared properties
            ├── init.lua      # Server-side code
            └── cl_init.lua   # Client-side rendering
```

---

## 🛠️ Development

### Project Structure

```
GModEntityCreator/
├── App.xaml              # Application resources and styles
├── App.xaml.cs           # Application entry point
├── MainWindow.xaml       # Main UI layout
├── MainWindow.xaml.cs    # Main window logic
└── GModEntityCreator.csproj
```

### Building a Release

```bash
# Publish as single file (Windows x64)
dotnet publish GModEntityCreator/GModEntityCreator.csproj \
  -c Release \
  -r win-x64 \
  --self-contained true \
  -p:PublishSingleFile=true \
  -p:IncludeNativeLibrariesForSelfExtract=true \
  -o ./publish
```

---


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Changelog

### v1.0.0 (2026)
- ✨ Initial release
- 🎨 Modern dark theme UI
- 🌐 Bilingual support (EN/RU)
- 💾 Custom presets system
- 🔫 Entity and weapon generation
- 📁 Auto file generation

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for the Garry's Mod community**

[⬆ Back to Top](#-gmod-entity-creator)

</div>

---

<a name="russian"></a>

## 📖 Описание (Русский)

**GMod Entity Creator** — это современное, красивое WPF десктопное приложение для создания пользовательских сущностей, оружия и транспорта для аддонов **Garry's Mod**. Создано на C# и .NET 8, имеет стильный тёмный интерфейс и генерирует все необходимые Lua файлы с правильной структурой и шаблонами кода.

---

## ✨ Возможности

- 🎨 **Современный тёмный UI** - Красивый интерфейс с плавными анимациями
- 🔫 **Создание сущностей и оружия** - Генерация на основе разных базовых классов
- 💾 **Пользовательские пресеты** - Сохранение и повторное использование баз
- 👁️ **Предпросмотр кода** - Просмотр сгенерированного Lua кода
- 🌍 **Двуязычный интерфейс** - Полная поддержка английского и русского
- ⚙️ **Настраиваемые опции** - Спавн, доступ админам, категории и т.д.
- 📁 **Автогенерация файлов** - Создание структуры папок и Lua файлов
- 🚀 **Экспорт кода** - Экспорт в любую папку

---

## 🚀 Быстрый старт

### Установка

1. **Скачайте** последнюю версию со страницы
2. **Распакуйте** архив в любую папку
3. **Запустите** `GModEntityCreator.exe`

### Сборка из исходников

```bash
# Клонируйте репозиторий
git clone https://github.com/yourusername/GModEntityCreator.git
cd GModEntityCreator

# Соберите проект
dotnet build --configuration Release

# Запустите приложение
dotnet run --project GModEntityCreator/GModEntityCreator.csproj
```

### Требования

- **.NET 8.0 Runtime** или новее
- **Windows 10/11**

---

## 📖 Руководство по использованию

### Создание сущности

1. **Запустите** приложение
2. **Выберите папку аддона** - Нажмите "📁 Выбрать" и укажите путь к аддону
3. **Заполните свойства**:
   - **Имя сущности** - Отображаемое имя
   - **ID сущности** - Технический идентификатор
   - **Базовый класс** - Выберите из доступных или свой
   - **Путь к модели** - Путь к файлу модели
   - **Пользовательские функции** - Добавьте свой Lua код (опционально)
4. **Настройте опции**:
   - **Категория** - Категория в меню спавна
   - **Автор** - Ваше имя
   - **Создаваемая** - Доступна в меню спавна
   - **Только админ** - Только для администраторов
5. **Предпросмотр** - Нажмите "👁️ Предпросмотр кода"
6. **Создать файлы** - Нажмите "📄 Создать файлы"

### Создание оружия

1. Выберите **`weapon_base`** как базовый класс
2. Появятся дополнительные поля:
   - **Базовый урон** - Значение урона
   - **Тип патронов** - Выберите тип
3. Заполните остальные свойства и создайте

---

## 🤝 Вклад в проект

Вклад приветствуется!

---

## 📄 Лицензия

Проект лицензирован под **MIT License** - см. файл [LICENSE](LICENSE).

---

<div align="center">

**Сделано с ❤️ для сообщества Garry's Mod**

</div>
