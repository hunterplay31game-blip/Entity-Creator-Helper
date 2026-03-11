using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media.Animation;
using MessageBox = System.Windows.MessageBox;
using Microsoft.Win32;

namespace GModEntityCreator
{
    public partial class MainWindow : Window
    {
        private string _language = "en";
        private List<string> _customPresets = new();
        private readonly string _presetsFile = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "custom_presets.json");

        private string T(string key) => _texts.TryGetValue($"{_language}_{key}", out var val) ? val : key;

        private Dictionary<string, string> _texts = new()
        {
            ["en_title"] = "GMod Entity Creator",
            ["en_addon_folder"] = "📁 Addon Folder",
            ["en_browse"] = "📁 Browse",
            ["en_entity_properties"] = "🎯 Entity Properties",
            ["en_entity_name"] = "Entity Name:",
            ["en_entity_id"] = "Entity ID (Technical):",
            ["en_base_class"] = "Base Class:",
            ["en_model"] = "Model Path:",
            ["en_custom_functions"] = "Custom Functions (Lua):",
            ["en_weapon_damage"] = "Base Damage:",
            ["en_ammo_type"] = "Ammo Type:",
            ["en_custom_base"] = "Custom Base:",
            ["en_save_preset"] = "💾 Save Preset",
            ["en_saved_presets"] = "Saved Presets:",
            ["en_additional_options"] = "⚙️ Additional Options",
            ["en_category"] = "Category:",
            ["en_author"] = "Author:",
            ["en_spawnable"] = "Spawnable (available in spawn menu)",
            ["en_admin_only"] = "Admin Only (restricted to admins)",
            ["en_preview_code"] = "👁️ Preview Code",
            ["en_generate_files"] = "📄 Generate Files",
            ["en_code_preview"] = "📄 Code Preview",
            ["en_clear"] = "🗑️ Clear",
            ["en_export"] = "💾 Export",
            ["en_generating"] = "Generating files...",
            ["en_error_fill"] = "Please fill in entity name and ID",
            ["en_success"] = "Entity '{}' created successfully!",
            ["en_error"] = "Error",
            ["en_custom_code"] = "-- Add your custom Lua code here\nfunction ENT:CustomFunction()\n    -- Your code\nend",
            ["en_preview_ph"] = "Click 'Preview Code' to see generated Lua code.",
            
            ["ru_title"] = "GMod Entity Creator",
            ["ru_addon_folder"] = "📁 Папка аддона",
            ["ru_browse"] = "📁 Выбрать",
            ["ru_entity_properties"] = "🎯 Свойства сущности",
            ["ru_entity_name"] = "Имя сущности:",
            ["ru_entity_id"] = "ID сущности:",
            ["ru_base_class"] = "Базовый класс:",
            ["ru_model"] = "Путь к модели:",
            ["ru_custom_functions"] = "Пользовательские функции (Lua):",
            ["ru_weapon_damage"] = "Урон:",
            ["ru_ammo_type"] = "Тип патронов:",
            ["ru_custom_base"] = "Своя база:",
            ["ru_save_preset"] = "💾 Сохранить",
            ["ru_saved_presets"] = "Пресеты:",
            ["ru_additional_options"] = "⚙️ Опции",
            ["ru_category"] = "Категория:",
            ["ru_author"] = "Автор:",
            ["ru_spawnable"] = "Создаваемая",
            ["ru_admin_only"] = "Только админ",
            ["ru_preview_code"] = "👁️ Предпросмотр",
            ["ru_generate_files"] = "📄 Создать",
            ["ru_code_preview"] = "📄 Код",
            ["ru_clear"] = "🗑️ Очистить",
            ["ru_export"] = "💾 Экспорт",
            ["ru_generating"] = "Генерация...",
            ["ru_error_fill"] = "Заполните имя и ID сущности",
            ["ru_success"] = "Сущность '{}' создана!",
            ["ru_error"] = "Ошибка",
            ["ru_custom_code"] = "-- Ваш Lua код\nfunction ENT:CustomFunction()\n    -- Код\nend",
            ["ru_preview_ph"] = "Нажмите 'Предпросмотр' для просмотра кода."
        };

        public MainWindow()
        {
            InitializeComponent();
            LoadCustomPresets();
            UpdateTexts();
            UpdateFieldVisibility();
            
            var fadeAnimation = new DoubleAnimation { From = 0, To = 1, Duration = TimeSpan.FromMilliseconds(400) };
            this.BeginAnimation(Window.OpacityProperty, fadeAnimation);
        }

        private void LoadCustomPresets()
        {
            try
            {
                if (File.Exists(_presetsFile))
                {
                    var json = File.ReadAllText(_presetsFile);
                    _customPresets = JsonSerializer.Deserialize<List<string>>(json) ?? new List<string>();
                    SavedPresetsComboBox.ItemsSource = _customPresets;
                }
            }
            catch { _customPresets = new List<string>(); }
        }

        private void SaveCustomPresets()
        {
            try
            {
                var options = new JsonSerializerOptions { WriteIndented = true };
                File.WriteAllText(_presetsFile, JsonSerializer.Serialize(_customPresets, options));
            }
            catch { }
        }

        private void UpdateTexts()
        {
            Title = T("title");
            AddonFolderTitle.Text = T("addon_folder");
            BrowseButton.Content = T("browse");
            EntityPropertiesTitle.Text = T("entity_properties");
            EntityNameLabel.Text = T("entity_name");
            EntityIdLabel.Text = T("entity_id");
            BaseClassLabel.Text = T("base_class");
            ModelLabel.Text = T("model");
            CustomFunctionsLabel.Text = T("custom_functions");
            CustomBaseLabel.Text = T("custom_base");
            SavePresetButton.Content = T("save_preset");
            SavedPresetsLabel.Text = T("saved_presets");
            WeaponDamageLabel.Text = T("weapon_damage");
            AmmoTypeLabel.Text = T("ammo_type");
            AdditionalOptionsTitle.Text = T("additional_options");
            CategoryLabel.Text = T("category");
            AuthorLabel.Text = T("author");
            CodePreviewTitle.Text = T("code_preview");
            ClearButton.Content = T("clear");
            ExportButton.Content = T("export");
            PreviewButton.Content = T("preview_code");
            GenerateButton.Content = T("generate_files");
            
            if (SpawnableCheckBox.Content is TextBlock sp) sp.Text = T("spawnable");
            if (AdminOnlyCheckBox.Content is TextBlock ad) ad.Text = T("admin_only");
            
            if (string.IsNullOrEmpty(CustomFunctionsTextBox.Text))
                CustomFunctionsTextBox.Text = T("custom_code");
            if (string.IsNullOrEmpty(PreviewTextBox.Text))
                PreviewTextBox.Text = T("preview_ph");
        }

        private void LanguageButton_Click(object sender, RoutedEventArgs e)
        {
            _language = _language == "en" ? "ru" : "en";
            LanguageButton.Content = _language == "en" ? "🇬🇧 EN" : "🇷🇺 RU";
            UpdateTexts();
        }

        private void BrowseButton_Click(object sender, RoutedEventArgs e)
        {
            var dialog = new System.Windows.Forms.FolderBrowserDialog { Description = "Select addon folder" };
            if (dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
                AddonPathTextBox.Text = dialog.SelectedPath;
        }

        private void UpdateFieldVisibility()
        {
            var selected = BaseClassComboBox.SelectedValue?.ToString();
            WeaponFields.Visibility = selected == "weapon_base" ? Visibility.Visible : Visibility.Collapsed;
            CustomBaseFields.Visibility = selected == "custom" ? Visibility.Visible : Visibility.Collapsed;
        }

        private void SavePresetButton_Click(object sender, RoutedEventArgs e)
        {
            var preset = CustomBaseTextBox.Text.Trim();
            if (!string.IsNullOrEmpty(preset) && !_customPresets.Contains(preset))
            {
                _customPresets.Add(preset);
                SaveCustomPresets();
                SavedPresetsComboBox.ItemsSource = null;
                SavedPresetsComboBox.ItemsSource = _customPresets;
            }
        }

        private void SavedPresetsComboBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if (SavedPresetsComboBox.SelectedItem is string preset)
                CustomBaseTextBox.Text = preset;
        }

        private void ClearButton_Click(object sender, RoutedEventArgs e)
        {
            EntityNameTextBox.Text = "My Custom Entity";
            EntityIdTextBox.Text = "my_custom_entity";
            BaseClassComboBox.SelectedIndex = 0;
            ModelTextBox.Text = "models/props_junk/watermelon01.mdl";
            CustomFunctionsTextBox.Text = T("custom_code");
            WeaponDamageTextBox.Text = "10";
            AmmoTypeComboBox.SelectedIndex = 0;
            CustomBaseTextBox.Text = "";
            CategoryTextBox.Text = "My Addon";
            AuthorTextBox.Text = "Your Name";
            SpawnableCheckBox.IsChecked = true;
            AdminOnlyCheckBox.IsChecked = false;
            PreviewTextBox.Text = T("preview_ph");
            UpdateFieldVisibility();
        }

        private string GetBaseClass()
        {
            var selected = BaseClassComboBox.SelectedValue?.ToString();
            return selected == "custom" 
                ? (string.IsNullOrEmpty(CustomBaseTextBox.Text.Trim()) ? "base_gmodentity" : CustomBaseTextBox.Text.Trim())
                : (selected ?? "base_anim");
        }

        private void ExportButton_Click(object sender, RoutedEventArgs e)
        {
            var dialog = new System.Windows.Forms.FolderBrowserDialog { Description = "Select export folder" };
            if (dialog.ShowDialog() != System.Windows.Forms.DialogResult.OK) return;

            var code = GenerateLuaCode(
                EntityNameTextBox.Text, EntityIdTextBox.Text, GetBaseClass(), ModelTextBox.Text,
                CustomFunctionsTextBox.Text, WeaponDamageTextBox.Text,
                AmmoTypeComboBox.SelectedValue?.ToString() ?? "pistol",
                CategoryTextBox.Text, AuthorTextBox.Text,
                SpawnableCheckBox.IsChecked == true, AdminOnlyCheckBox.IsChecked == true);

            File.WriteAllText(Path.Combine(dialog.SelectedPath, "shared.lua"), code.shared);
            File.WriteAllText(Path.Combine(dialog.SelectedPath, "init.lua"), code.init);
            File.WriteAllText(Path.Combine(dialog.SelectedPath, "cl_init.lua"), code.clInit);
            MessageBox.Show("Code exported!", "Success", MessageBoxButton.OK, MessageBoxImage.Information);
        }

        private void PreviewButton_Click(object sender, RoutedEventArgs e)
        {
            var code = GenerateLuaCode(
                EntityNameTextBox.Text, EntityIdTextBox.Text, GetBaseClass(), ModelTextBox.Text,
                CustomFunctionsTextBox.Text, WeaponDamageTextBox.Text,
                AmmoTypeComboBox.SelectedValue?.ToString() ?? "pistol",
                CategoryTextBox.Text, AuthorTextBox.Text,
                SpawnableCheckBox.IsChecked == true, AdminOnlyCheckBox.IsChecked == true);
            PreviewTextBox.Text = $"-- shared.lua\n{code.shared}\n\n-- init.lua\n{code.init}\n\n-- cl_init.lua\n{code.clInit}";
        }

        private async void GenerateButton_Click(object sender, RoutedEventArgs e)
        {
            var name = EntityNameTextBox.Text.Trim();
            var folder = EntityIdTextBox.Text.Trim();

            if (string.IsNullOrEmpty(name) || string.IsNullOrEmpty(folder))
            {
                MessageBox.Show(T("error_fill"), T("error"), MessageBoxButton.OK, MessageBoxImage.Warning);
                return;
            }

            ProgressOverlay.Visibility = Visibility.Visible;
            await System.Threading.Tasks.Task.Delay(100);

            var code = GenerateLuaCode(
                name, folder, GetBaseClass(), ModelTextBox.Text,
                CustomFunctionsTextBox.Text, WeaponDamageTextBox.Text,
                AmmoTypeComboBox.SelectedValue?.ToString() ?? "pistol",
                CategoryTextBox.Text, AuthorTextBox.Text,
                SpawnableCheckBox.IsChecked == true, AdminOnlyCheckBox.IsChecked == true);

            try
            {
                var basePath = string.IsNullOrEmpty(AddonPathTextBox.Text.Trim()) ? "." : AddonPathTextBox.Text.Trim();
                var scriptType = GetBaseClass() == "weapon_base" ? "weapons" : "entities";
                var entityPath = Path.Combine(basePath, "lua", scriptType, folder);
                Directory.CreateDirectory(entityPath);

                File.WriteAllText(Path.Combine(entityPath, "shared.lua"), code.shared);
                File.WriteAllText(Path.Combine(entityPath, "init.lua"), code.init);
                File.WriteAllText(Path.Combine(entityPath, "cl_init.lua"), code.clInit);

                ProgressOverlay.Visibility = Visibility.Collapsed;
                MessageBox.Show(string.Format(T("success"), name), "Success", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            catch (Exception ex)
            {
                ProgressOverlay.Visibility = Visibility.Collapsed;
                MessageBox.Show($"{T("error")}: {ex.Message}", T("error"), MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private (string shared, string init, string clInit) GenerateLuaCode(
            string name, string folder, string baseClass, string model,
            string customCode, string damageStr, string ammo,
            string category, string author, bool spawnable, bool adminOnly)
        {
            int.TryParse(damageStr, out int damage);
            if (damage <= 0) damage = 10;
            var spawnStr = spawnable ? "true" : "false";
            var adminStr = adminOnly ? "true" : "false";

            if (baseClass == "weapon_base")
            {
                return (
$@"-- Shared.lua
SWEP.Base = ""weapon_base""
SWEP.PrintName = ""{name}""
SWEP.Author = ""{author}""
SWEP.Spawnable = {spawnStr}
SWEP.AdminOnly = {adminStr}
SWEP.Category = ""{category}""
SWEP.ViewModel = ""models/weapons/v_pistol.mdl""
SWEP.WorldModel = ""{model}""
SWEP.Primary.Damage = {damage}
SWEP.Primary.Ammo = ""{ammo}""
SWEP.Primary.ClipSize = 30

function SWEP:Initialize() end
function SWEP:PrimaryAttack() self:ShootBullet({damage}, 1, 0.01) end
function SWEP:SecondaryAttack() end
{customCode}",
$@"-- Init.lua
include(""shared.lua"")",
$@"-- Cl_init.lua
include(""shared.lua"")");
            }

            var entType = "anim";
            var shared = $@"-- Shared.lua
ENT.Type = ""{entType}""
ENT.Base = ""{baseClass}""
ENT.PrintName = ""{name}""
ENT.Author = ""{author}""
ENT.Spawnable = {spawnStr}
ENT.AdminOnly = {adminStr}
ENT.Category = ""{category}""";

            string init;
            if (baseClass == "base_vehicle")
            {
                init = $@"-- Init.lua
include(""shared.lua"")

function ENT:Initialize()
    self:SetModel(""{model}"")
    self:PhysicsInit(SOLID_VPHYSICS)
    self:SetMoveType(MOVETYPE_VPHYSICS)
    local phys = self:GetPhysicsObject()
    if phys:IsValid() then phys:Wake() end
end

function ENT:Use(activator)
    if not activator:IsPlayer() then return end
    if activator:GetVehicle() == self then activator:ExitVehicle()
    else activator:EnterVehicle(self) end
end
{customCode}";
            }
            else
            {
                init = $@"-- Init.lua
include(""shared.lua"")

function ENT:Initialize()
    self:SetModel(""{model}"")
    self:PhysicsInit(SOLID_VPHYSICS)
    self:SetMoveType(MOVETYPE_VPHYSICS)
    local phys = self:GetPhysicsObject()
    if phys:IsValid() then phys:Wake() end
end

function ENT:Use(activator)
    -- Use logic here
end
{customCode}";
            }

            return (shared, init, $@"-- Cl_init.lua
include(""shared.lua"")

function ENT:Draw()
    self:DrawModel()
end");
        }
    }
}
