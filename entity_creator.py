import customtkinter as ctk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import os
import json
import sys
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

texts = {
    "en": {
        "title": "GMod Entity Creator Helper",
        "addon_folder": "Addon Folder",
        "browse_folder": "📁 Browse Folder",
        "entity_properties": "Entity Properties",
        "entity_name": "Entity Name:",
        "entity_id": "Entity ID:",
        "base_class": "Base Class:",
        "model": "Model:",
        "custom_functions": "Custom Functions:",
        "custom_functions_placeholder": "Enter custom Lua code here (e.g., functions, hooks)",
        "weapon_damage": "Base Damage:",
        "ammo_type": "Ammo Type:",
        "custom_base": "Custom Base:",
        "additional_options": "Additional Options",
        "category": "Category:",
        "author": "Author:",
        "spawnable": "Spawnable",
        "admin_only": "Admin Only",
        "preview_code": "👁️ Preview Code",
        "generate_files": "📄 Generate Files",
        "code_preview": "Code Preview",
        "preview_placeholder": "Click 'Preview Code' to see the generated Lua code here.",
        "error_fill_fields": "Please fill in the entity name and ID.",
        "error_create_folder": "Failed to create folder: ",
        "error_save_files": "Failed to save files: ",
        "success": "Entity '{}' successfully created in '{}'!",
        "language": "Language:",
        "english": "English",
        "russian": "Русский",
        "close": "Close"
    },
    "ru": {
        "title": "GMod Entity Creator Helper",
        "addon_folder": "Папка аддона",
        "browse_folder": "📁 Выбрать папку",
        "entity_properties": "Свойства сущности",
        "entity_name": "Имя сущности:",
        "entity_id": "ID сущности:",
        "base_class": "Базовый класс:",
        "model": "Модель:",
        "custom_functions": "Пользовательские функции:",
        "custom_functions_placeholder": "Введите пользовательский Lua код здесь (например, функции, хуки)",
        "weapon_damage": "Базовый урон:",
        "ammo_type": "Тип патронов:",
        "custom_base": "Пользовательская база:",
        "additional_options": "Дополнительные опции",
        "category": "Категория:",
        "author": "Автор:",
        "spawnable": "Создаваемая",
        "admin_only": "Только админ",
        "preview_code": "👁️ Предпросмотр кода",
        "generate_files": "📄 Создать файлы",
        "code_preview": "Предпросмотр кода",
        "preview_placeholder": "Нажмите 'Предпросмотр кода', чтобы увидеть сгенерированный Lua код здесь.",
        "error_fill_fields": "Пожалуйста, заполните имя и ID сущности.",
        "error_create_folder": "Не удалось создать папку: ",
        "error_save_files": "Не удалось сохранить файлы: ",
        "success": "Сущность '{}' успешно создана в '{}'!",
        "language": "Язык:",
        "english": "English",
        "russian": "Русский",
        "close": "Закрыть"
    }
}

class EntityGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.language = "en"

        self.custom_presets_file = os.path.join(os.path.dirname(sys.executable), "custom_presets.json")
        self.custom_presets = self.load_custom_presets()

        self.title(texts[self.language]["title"])
        self.geometry("600x800")
        self.resizable(True, True)
        try:
            self.iconbitmap('Icone.ico')
        except:
            pass

        self.main_frame = ctk.CTkScrollableFrame(self, fg_color="#1e1e1e", corner_radius=15)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.title_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.title_frame.pack(pady=20)

        try:
            self.icon_image = ctk.CTkImage(light_image=Image.open('Icone.ico'), size=(48, 48))
            self.icon_label = ctk.CTkLabel(self.title_frame, image=self.icon_image, text="")
            self.icon_label.pack(side="left", padx=10)
        except:
            pass

        self.title_label = ctk.CTkLabel(self.title_frame, text=texts[self.language]["title"], font=ctk.CTkFont(size=28, weight="bold"), text_color="#00d4ff")
        self.title_label.pack(side="left")

        self.path_frame = ctk.CTkFrame(self.main_frame, fg_color="#3c3c3c", border_width=2, border_color="#555555", corner_radius=10)
        self.path_frame.pack(fill="x", pady=10, padx=10)
        self.path_title = ctk.CTkLabel(self.path_frame, text=texts[self.language]["addon_folder"], font=ctk.CTkFont(size=18, weight="bold"), text_color="#ffffff")
        self.path_title.pack(pady=10, padx=10, anchor="w")
        self.base_path = ctk.CTkEntry(self.path_frame, placeholder_text="Path to addon (addons/myaddon)")
        self.base_path.pack(pady=5, padx=10, fill="x")
        self.browse_button = ctk.CTkButton(self.path_frame, text=texts[self.language]["browse_folder"], command=self.browse_folder, fg_color="#007bff", hover_color="#0056b3")
        self.browse_button.pack(pady=10, padx=10)

        self.entity_frame = ctk.CTkFrame(self.main_frame, fg_color="#3c3c3c", border_width=2, border_color="#555555", corner_radius=10)
        self.entity_frame.pack(fill="x", pady=10, padx=10)
        self.entity_title = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["entity_properties"], font=ctk.CTkFont(size=18, weight="bold"), text_color="#ffffff")
        self.entity_title.pack(pady=10, padx=10, anchor="w")

        self.name_label = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["entity_name"], text_color="#cccccc")
        self.name_label.pack(pady=2, padx=10, anchor="w")
        self.ent_name = ctk.CTkEntry(self.entity_frame, placeholder_text="Display name (PrintName)")
        self.ent_name.pack(pady=5, padx=10, fill="x")

        self.id_label = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["entity_id"], text_color="#cccccc")
        self.id_label.pack(pady=2, padx=10, anchor="w")
        self.folder_name = ctk.CTkEntry(self.entity_frame, placeholder_text="Technical ID (e.g., my_entity)")
        self.folder_name.pack(pady=5, padx=10, fill="x")

        self.base_label = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["base_class"], text_color="#cccccc")
        self.base_label.pack(pady=2, padx=10, anchor="w")
        self.base_class = ctk.CTkOptionMenu(self.entity_frame, values=["base_class", "base_vehicle", "weapon_base", "custom"])
        self.base_class.pack(pady=5, padx=10, fill="x")

        self.model_label = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["model"], text_color="#cccccc")
        self.model_label.pack(pady=2, padx=10, anchor="w")
        self.model = ctk.CTkEntry(self.entity_frame, placeholder_text="Model path (models/...)")
        self.model.pack(pady=5, padx=10, fill="x")

        self.custom_functions_label = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["custom_functions"], text_color="#cccccc")
        self.custom_functions_label.pack(pady=2, padx=10, anchor="w")
        self.custom_functions = ctk.CTkTextbox(self.entity_frame, height=100, fg_color="#2b2b2b", text_color="#ffffff")
        self.custom_functions.pack(pady=5, padx=10, fill="x")

        self.weapon_damage_label = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["weapon_damage"], text_color="#cccccc")
        self.weapon_damage = ctk.CTkEntry(self.entity_frame, placeholder_text="e.g., 10")
        self.ammo_type_label = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["ammo_type"], text_color="#cccccc")
        self.ammo_type = ctk.CTkOptionMenu(self.entity_frame, values=["pistol", "smg1", "ar2", "buckshot", "357", "sniperround"])

        self.custom_base_label = ctk.CTkLabel(self.entity_frame, text=texts[self.language]["custom_base"], text_color="#cccccc")
        self.custom_base = ctk.CTkEntry(self.entity_frame, placeholder_text="e.g., base_myentity")
        self.saved_custom_label = ctk.CTkLabel(self.entity_frame, text="Saved Presets:", text_color="#cccccc")
        self.saved_custom = ctk.CTkOptionMenu(self.entity_frame, values=self.custom_presets, command=self.load_custom)
        self.save_custom_button = ctk.CTkButton(self.entity_frame, text="Save as Preset", command=self.save_custom_preset)

        self.base_class.configure(command=self.on_base_class_change)
        self.on_base_class_change(self.base_class.get())  # initial

        self.options_frame = ctk.CTkFrame(self.main_frame, fg_color="#3c3c3c", border_width=2, border_color="#555555", corner_radius=10)
        self.options_frame.pack(fill="x", pady=10, padx=10)
        self.options_title = ctk.CTkLabel(self.options_frame, text=texts[self.language]["additional_options"], font=ctk.CTkFont(size=18, weight="bold"), text_color="#ffffff")
        self.options_title.pack(pady=10, padx=10, anchor="w")

        self.category_label = ctk.CTkLabel(self.options_frame, text=texts[self.language]["category"], text_color="#cccccc")
        self.category_label.pack(pady=2, padx=10, anchor="w")
        self.category = ctk.CTkEntry(self.options_frame, placeholder_text="Spawn menu category")
        self.category.pack(pady=5, padx=10, fill="x")

        self.author_label = ctk.CTkLabel(self.options_frame, text=texts[self.language]["author"], text_color="#cccccc")
        self.author_label.pack(pady=2, padx=10, anchor="w")
        self.author = ctk.CTkEntry(self.options_frame, placeholder_text="Your name")
        self.author.pack(pady=5, padx=10, fill="x")

        self.checks_frame = ctk.CTkFrame(self.options_frame, fg_color="transparent")
        self.checks_frame.pack(pady=10, padx=10, fill="x")
        self.spawnable = ctk.CTkCheckBox(self.checks_frame, text=texts[self.language]["spawnable"])
        self.spawnable.pack(pady=5, padx=10, anchor="w")
        self.spawnable.select()

        self.admin_only = ctk.CTkCheckBox(self.checks_frame, text=texts[self.language]["admin_only"])
        self.admin_only.pack(pady=5, padx=10, anchor="w")

        self.buttons_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.buttons_frame.pack(pady=20, fill="x")

        self.settings_button = ctk.CTkButton(self.buttons_frame, text="⚙️ Settings", command=self.open_settings, fg_color="#6c757d", hover_color="#5a6268")
        self.settings_button.pack(side="left", padx=10)

        self.preview_button = ctk.CTkButton(self.buttons_frame, text=texts[self.language]["preview_code"], command=lambda: (self.animate_button(self.preview_button), self.preview_code()), fg_color="#28a745", hover_color="#1e7e34")
        self.preview_button.pack(side="left", padx=10)

        self.button = ctk.CTkButton(self.buttons_frame, text=texts[self.language]["generate_files"], command=lambda: (self.animate_button(self.button), self.generate()), font=ctk.CTkFont(size=16, weight="bold"), fg_color="#dc3545", hover_color="#c82333")
        self.button.pack(side="right", padx=10)

        self.preview_frame = ctk.CTkFrame(self.main_frame, fg_color="#3c3c3c", border_width=2, border_color="#555555", corner_radius=10)
        self.preview_frame.pack(fill="both", expand=True, pady=10, padx=10)
        self.preview_title = ctk.CTkLabel(self.preview_frame, text=texts[self.language]["code_preview"], font=ctk.CTkFont(size=18, weight="bold"), text_color="#ffffff")
        self.preview_title.pack(pady=10, padx=10, anchor="w")
        self.preview_text = ctk.CTkTextbox(self.preview_frame, wrap="word", fg_color="#2b2b2b", text_color="#ffffff")
        self.preview_text.pack(fill="both", expand=True, padx=10, pady=5)
        self.preview_text.insert("0.0", texts[self.language]["preview_placeholder"])

        self.progress_bar = ctk.CTkProgressBar(self.main_frame, width=400, height=20, fg_color="#555555", progress_color="#00d4ff")
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)
        self.progress_bar.pack_forget()

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.startup_animation()

    def startup_animation(self):
        self.attributes("-alpha", 0)
        def fade_in(alpha=0):
            if alpha < 1:
                self.attributes("-alpha", alpha)
                self.after(50, lambda: fade_in(alpha + 0.05))
            else:
                self.attributes("-alpha", 1)
        fade_in()

    def on_close(self):
        def fade_out(alpha=1):
            if alpha > 0:
                self.attributes("-alpha", alpha)
                self.after(50, lambda: fade_out(alpha - 0.05))
            else:
                self.destroy()
        fade_out()

    def change_language(self, selected):
        if selected == texts[self.language]["russian"]:
            self.language = "ru"
        else:
            self.language = "en"
        self.update_texts()

    def update_texts(self):
        self.title(texts[self.language]["title"])
        self.title_label.configure(text=texts[self.language]["title"])
        self.path_title.configure(text=texts[self.language]["addon_folder"])
        self.browse_button.configure(text=texts[self.language]["browse_folder"])
        self.entity_title.configure(text=texts[self.language]["entity_properties"])
        self.name_label.configure(text=texts[self.language]["entity_name"])
        self.id_label.configure(text=texts[self.language]["entity_id"])
        self.base_label.configure(text=texts[self.language]["base_class"])
        self.model_label.configure(text=texts[self.language]["model"])
        self.options_title.configure(text=texts[self.language]["additional_options"])
        self.category_label.configure(text=texts[self.language]["category"])
        self.author_label.configure(text=texts[self.language]["author"])
        self.spawnable.configure(text=texts[self.language]["spawnable"])
        self.admin_only.configure(text=texts[self.language]["admin_only"])
        self.preview_button.configure(text=texts[self.language]["preview_code"])
        self.button.configure(text=texts[self.language]["generate_files"])
        self.preview_title.configure(text=texts[self.language]["code_preview"])
        self.preview_text.delete("0.0", "end")
        self.preview_text.insert("0.0", texts[self.language]["preview_placeholder"])
        self.custom_functions_label.configure(text=texts[self.language]["custom_functions"])
        self.weapon_damage_label.configure(text=texts[self.language]["weapon_damage"])
        self.ammo_type_label.configure(text=texts[self.language]["ammo_type"])
        self.custom_base_label.configure(text=texts[self.language]["custom_base"])
        self.on_base_class_change(self.base_class.get())
        self.settings_button.configure(text="⚙️ " + ("Settings" if self.language == "en" else "Настройки"))

    def on_base_class_change(self, value):
        if value == "weapon_base":
            self.weapon_damage_label.pack(pady=2, padx=10, anchor="w")
            self.weapon_damage.pack(pady=5, padx=10, fill="x")
            self.ammo_type_label.pack(pady=2, padx=10, anchor="w")
            self.ammo_type.pack(pady=5, padx=10, fill="x")
        else:
            self.weapon_damage_label.pack_forget()
            self.weapon_damage.pack_forget()
            self.ammo_type_label.pack_forget()
            self.ammo_type.pack_forget()

        if value == "custom":
            self.custom_base_label.pack(pady=2, padx=10, anchor="w")
            self.custom_base.pack(pady=5, padx=10, fill="x")
            self.saved_custom_label.pack(pady=2, padx=10, anchor="w")
            self.saved_custom.pack(pady=5, padx=10, fill="x")
            self.save_custom_button.pack(pady=5, padx=10)
        else:
            self.custom_base_label.pack_forget()
            self.custom_base.pack_forget()
            self.saved_custom_label.pack_forget()
            self.saved_custom.pack_forget()
            self.save_custom_button.pack_forget()

    def load_custom_presets(self):
        try:
            if os.path.exists(self.custom_presets_file):
                with open(self.custom_presets_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return []

    def save_custom_presets(self):
        try:
            with open(self.custom_presets_file, 'w', encoding='utf-8') as f:
                json.dump(self.custom_presets, f)
        except:
            pass

    def load_custom(self, selected):
        self.custom_base.delete(0, ctk.END)
        self.custom_base.insert(0, selected)

    def save_custom_preset(self):
        preset = self.custom_base.get().strip()
        if preset and preset not in self.custom_presets:
            self.custom_presets.append(preset)
            self.save_custom_presets()
            self.saved_custom.configure(values=self.custom_presets)

    def generate_lua_code(self, name, folder, base, model, custom_code, damage_str, ammo, category, author, spawnable, admin_only):
        try:
            damage = int(damage_str.strip()) if damage_str.strip() else 10
        except ValueError:
            damage = 10

        if base == "weapon_base":
            shared = f"""-- Shared.lua - Shared weapon properties
SWEP.Base = "weapon_base"
SWEP.PrintName = "{name}"
SWEP.Author = "{author}"
SWEP.Spawnable = {str(bool(spawnable)).lower()}
SWEP.AdminOnly = {str(bool(admin_only)).lower()}
SWEP.Category = "{category}"
SWEP.Purpose = "A custom weapon"
SWEP.Instructions = "Equip and use as needed"
SWEP.ViewModel = "models/weapons/v_pistol.mdl"
SWEP.WorldModel = "{model}"

SWEP.Primary.Damage = {damage}
SWEP.Primary.Ammo = "{ammo}"
SWEP.Primary.ClipSize = 30
SWEP.Primary.DefaultClip = 90
SWEP.Primary.Automatic = false

function SWEP:Initialize()
    -- Weapon initialization
end

function SWEP:PrimaryAttack()
    -- Primary attack logic
    self:ShootBullet({damage}, 1, 0.01)
end

function SWEP:SecondaryAttack()
    -- Secondary attack logic
end

{custom_code}
"""

            init = f"""-- Init.lua - Serverside weapon initialization
include("shared.lua")
"""

            cl_init = f"""-- Cl_init.lua - Clientside weapon rendering
include("shared.lua")
"""
        else:
            ent_type = "anim"

            if base == "base_vehicle":
                shared = f"""-- Shared.lua - Shared vehicle properties
ENT.Type = "{ent_type}"
ENT.Base = "{base}"
ENT.PrintName = "{name}"
ENT.Author = "{author}"
ENT.Spawnable = {str(bool(spawnable)).lower()}
ENT.AdminOnly = {str(bool(admin_only)).lower()}
ENT.Category = "{category}"
ENT.Purpose = "A custom vehicle"
ENT.Instructions = "Spawn and enter the vehicle"
"""

                init = f"""-- Init.lua - Serverside vehicle initialization
include("shared.lua")

function ENT:Initialize()
    self:SetModel("{model}")
    self:PhysicsInit(SOLID_VPHYSICS)
    self:SetMoveType(MOVETYPE_VPHYSICS)
    self:SetSolid(SOLID_VPHYSICS)
    local phys = self:GetPhysicsObject()
    if phys:IsValid() then
        phys:Wake()
    end
    self:SetUseType(SIMPLE_USE)
end

function ENT:Use(activator, caller)
    if not activator:IsPlayer() then return end
    if activator:GetVehicle() == self then
        activator:ExitVehicle()
    else
        activator:EnterVehicle(self)
    end
end

{custom_code}
"""

                cl_init = f"""-- Cl_init.lua - Clientside vehicle rendering
include("shared.lua")

function ENT:Draw()
    self:DrawModel()
end
"""
            else:
                shared = f"""-- Shared.lua - Shared entity properties
ENT.Type = "{ent_type}"
ENT.Base = "{base}"
ENT.PrintName = "{name}"
ENT.Author = "{author}"
ENT.Spawnable = {str(bool(spawnable)).lower()}
ENT.AdminOnly = {str(bool(admin_only)).lower()}
ENT.Category = "{category}"
ENT.Purpose = "A custom entity"
ENT.Instructions = "Spawn and interact as needed"
"""

                init = f"""-- Init.lua - Serverside initialization
include("shared.lua")

function ENT:Initialize()
    self:SetModel("{model}")
    self:PhysicsInit(SOLID_VPHYSICS)
    self:SetMoveType(MOVETYPE_VPHYSICS)
    self:SetSolid(SOLID_VPHYSICS)
    local phys = self:GetPhysicsObject()
    if phys:IsValid() then
        phys:Wake()
    end
    if {spawnable} == 1 then
        self:SetUseType(SIMPLE_USE)
    end
end

function ENT:Use(activator, caller)
    -- Add your use logic here
    -- For example: activator:ChatPrint("You used the entity!")
end

{custom_code}
"""

                cl_init = f"""-- Cl_init.lua - Clientside rendering
include("shared.lua")

function ENT:Draw()
    self:DrawModel()
end
"""

        return shared, init, cl_init

    def animate_button(self, button):
        original_fg = button.cget("fg_color")
        button.configure(fg_color="#4CAF50")
        self.after(300, lambda: button.configure(fg_color=original_fg))

    def open_settings(self):
        settings_window = ctk.CTkToplevel(self)
        settings_window.title("Settings")
        settings_window.geometry("300x200")
        settings_window.resizable(False, False)

        ctk.CTkLabel(settings_window, text=texts[self.language]["language"], font=ctk.CTkFont(size=14)).pack(pady=10, padx=20, anchor="w")
        language_menu = ctk.CTkOptionMenu(settings_window, values=[texts[self.language]["english"], texts[self.language]["russian"]], command=lambda selected: self.change_language_from_settings(selected, settings_window))
        language_menu.set(texts[self.language]["english"] if self.language == "en" else texts[self.language]["russian"])
        language_menu.pack(pady=5, padx=20, fill="x")

        close_button = ctk.CTkButton(settings_window, text=texts[self.language]["close"], command=settings_window.destroy)
        close_button.pack(pady=20)

    def change_language_from_settings(self, selected, window):
        self.change_language(selected)
        window.destroy()
        self.open_settings()  # reopen to update texts

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.base_path.delete(0, ctk.END)
            self.base_path.insert(0, folder)

    def preview_code(self):
        name = self.ent_name.get().strip() or "My Entity"
        folder = self.folder_name.get().strip() or "my_entity"
        base = self.base_class.get()
        if base == "custom":
            base = self.custom_base.get().strip() or "base_gmodentity"
        model = self.model.get().strip() or "models/props_junk/watermelon01.mdl"
        custom_code = self.custom_functions.get("0.0", "end").strip()
        damage = self.weapon_damage.get().strip() or "10"
        ammo = self.ammo_type.get()
        category = self.category.get().strip() or "My Addon"
        author = self.author.get().strip() or "Your Name"
        spawnable = self.spawnable.get()
        admin_only = self.admin_only.get()

        shared, init, cl_init = self.generate_lua_code(name, folder, base, model, custom_code, damage, ammo, category, author, spawnable, admin_only)

        self.preview_text.delete("0.0", "end")
        self.preview_text.insert("0.0", f"shared.lua\n{shared}\n\ninit.lua\n{init}\n\ncl_init.lua\n{cl_init}")

    def generate(self):
        base_path = self.base_path.get().strip() or "."
        name = self.ent_name.get().strip()
        folder = self.folder_name.get().strip()
        base = self.base_class.get()
        if base == "custom":
            base = self.custom_base.get().strip() or "base_gmodentity"
        model = self.model.get().strip() or "models/props_junk/watermelon01.mdl"
        custom_code = self.custom_functions.get("0.0", "end").strip()
        damage = self.weapon_damage.get().strip() or "10"
        ammo = self.ammo_type.get()
        category = self.category.get().strip() or "My Addon"
        author = self.author.get().strip() or "Your Name"
        spawnable = self.spawnable.get()
        admin_only = self.admin_only.get()

        if not name or not folder:
            messagebox.showerror("Error" if self.language == "en" else "Ошибка", texts[self.language]["error_fill_fields"])
            return

        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0.5)

        try:
            script_type = "weapons" if base == "weapon_base" else "entities"
            entity_path = os.path.join(base_path, "lua", script_type, folder)
            os.makedirs(entity_path, exist_ok=True)
        except OSError as e:
            messagebox.showerror("Error" if self.language == "en" else "Ошибка", texts[self.language]["error_create_folder"] + str(e))
            return
        shared_template, init_template, cl_init_template = self.generate_lua_code(name, folder, base, model, custom_code, damage, ammo, category, author, spawnable, admin_only)
        try:
            with open(os.path.join(entity_path, "shared.lua"), "w", encoding="utf-8") as f:
                f.write(shared_template)
            with open(os.path.join(entity_path, "init.lua"), "w", encoding="utf-8") as f:
                f.write(init_template)
            with open(os.path.join(entity_path, "cl_init.lua"), "w", encoding="utf-8") as f:
                f.write(cl_init_template)
        except IOError as e:
            messagebox.showerror("Error" if self.language == "en" else "Ошибка", texts[self.language]["error_save_files"] + str(e))
            self.progress_bar.pack_forget()
            return

        self.progress_bar.set(1)
        self.after(500, lambda: self.progress_bar.pack_forget())

        messagebox.showinfo("Success" if self.language == "en" else "Успех", texts[self.language]["success"].format(name, entity_path))

if __name__ == "__main__":
    app = EntityGenerator()
    app.mainloop()
