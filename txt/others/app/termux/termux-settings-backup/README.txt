
e others/app/termux/termux-settings-backup/README.txt

『-』:backup
cp -iv ~/.termux/termux.properties others/app/termux/termux-settings-backup/termux.properties-20250120

『+』:new-version
cp -iv ~/.termux/termux.properties others/app/termux/termux-settings-backup/termux.properties+20250120
e others/app/termux/termux-settings-backup/termux.properties+20250120
mv -iv ~/.termux/termux.properties ~/.termux/termux.properties-20250120
cp -iv others/app/termux/termux-settings-backup/termux.properties+20250120  ~/.termux/termux.properties
