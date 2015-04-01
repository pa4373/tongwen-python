

# Translate the plugin strings #
  1. Open the po folder.
    * **~/.local/share/gedit/plugins/tongwentang/po** for Gnome3.
    * **~/.gnome2/gedit/plugins/tongwentang/po** for Gnome2.
    * There should be a .pot file and several .sh scripts in the po folder.
  1. Run **sh make\_po.sh** in command line to generate your po file.
    * The file name will be YOUR\_LOCALE.po.
  1. Open the po file with gedit and start your translation.
    * Find the line "Last-Translator: Automatically generated\n" and enter your name and e-mail address.
    * Find the line "Content-Type: text/plain; charset=ASCII\n" and replace "ASCII" to "UTF-8".
    * Don't touch **msgid**, just translate **msgstr**.
  1. After translation, run **sh make\_mo.sh** to generate the mo file.
    * The mo file will be ../locale/YOUR\_LOCALE/LC\_MESSAGES/advancedfind.mo.
  1. Now you can install the mo file by running **sh install\_mo.sh**. Restart gedit and you can see your work.
  1. If there are new strings in new version of the plugin, run **sh update\_po.sh** to update the po file and do step3-5 again.

# Translate the plugin introduction in plugin list #
  1. Open the **tongwentang.plugin** or **tongwentang.gedit-plugin** file
    * ~/.gnome2/gedit/plugins/tongwentang.gedit-plugin for 2.x.
    * ~/.local/share/gedit/plugins/tongwentang.plugin for 3.x.
  1. Add two lines:
    * Name`[`YOUR\_LOCALE`]` = PLUGIN NAME IN YOUR LANGULE
    * Description`[`YOUR\_LOCALE`]` = A SHORT INTRODUCTION OF THE PLUGIN.