#!/usr/bin/python
import json
import sys
import os
import logging

from PySide.QtCore import *
from PySide.QtGui import *
from csgo import CueCSGO
from helpers import resource_path, setup_logging
from settings_dialog import Ui_SettingsDialog


class CUEThread(QThread):
    settings = Signal(str)

    def __init__(self):
        super(CUEThread, self).__init__()
        self.cue = CueCSGO()

    def run(self, *args, **kwargs):
        self.cue.start()


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)

        self.settings_dialog = SettingsDialog(self)
        self.settings_dialog.hidden.connect(self.set_settings)

        self.thread = CUEThread()
        self.thread.start()

        menu = QMenu(parent)

        settings_action = menu.addAction("Settings")
        settings_action.triggered.connect(self.open_settings)

        logs_action = menu.addAction("Logs")
        logs_action.triggered.connect(self.open_logs)

        menu.addSeparator()

        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(qApp.quit)

        self.setContextMenu(menu)

    def show(self, *args, **kwargs):
        super(SystemTrayIcon, self).show(*args, **kwargs)
        self.showMessage("CUE-CSGO", "CUE-CSGO is running in the tray!")

    def open_settings(self):
        self.settings_dialog.show(settings=self.thread.cue.settings)
        self.settings_dialog.raise_()

    def open_logs(self):
        os.startfile(resource_path("CUE_gamestate.log"))

    def set_settings(self):
        self.thread.settings = self.settings_dialog.new_settings()


class SettingsDialog(QDialog, Ui_SettingsDialog):
    hidden = Signal()

    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__()
        self.settings = None

        self.setupUi(self)

        self.background_button_ct_color.clicked.connect(self.ct_color_picker)
        self.background_button_t_color.clicked.connect(self.t_color_picker)

        self.button_save_settings.clicked.connect(self.set_settings)
        self.button_cancel_settings.clicked.connect(self.hide)

    def show(self, settings=None):
        super(SettingsDialog, self).show()
        if settings is not None:
            self.settings = settings
            self.general_update_interval.setValue(self.settings["update_interval"])

            background_settings = self.settings["renders"]["settings"]["BackgroundRender"]
            self.background_line_edit_ct_color.setText(background_settings["ct_color"])
            self.background_button_ct_color.setStyleSheet("background-color: {}"
                                                          .format(background_settings["ct_color"]))
            self.background_line_edit_t_color.setText(background_settings["t_color"])
            self.background_button_t_color.setStyleSheet("background-color: {}"
                                                         .format(background_settings["t_color"]))

            for render in self.settings["renders"]["active"]:
                if render == "HpRender":
                    self.healthbar_enabled.setChecked(True)
                if render == "WeaponRender":
                    self.weapons_enabled.setChecked(True)
                if render == "BombRender":
                    self.bomb_enabled.setChecked(True)
                if render == "FlashbangRender":
                    self.flashbang_enabled.setChecked(True)

            self.bomb_timer.setValue(self.settings["renders"]["settings"]["BombRender"]["explode_time"])
            self.flashbang_gradient.setChecked(self.settings["renders"]["settings"]["FlashbangRender"]["gradient"])

    def new_settings(self):
        self.settings["update_interval"] = self.general_update_interval.value()

        enabled_renders = ["BackgroundRender"]
        if self.healthbar_enabled.isChecked():
            enabled_renders.append("HpRender")
        if self.weapons_enabled.isChecked():
            enabled_renders.append("WeaponRender")
        if self.bomb_enabled.isChecked():
            enabled_renders.append("BombRender")
        if self.flashbang_enabled.isChecked():
            enabled_renders.append("FlashbangRender")

        self.settings["renders"]["active"] = enabled_renders
        self.settings["renders"]["settings"]["BombRender"]["explode_time"] = self.bomb_timer.value()
        self.settings["renders"]["settings"]["FlashbangRender"]["gradient"] = self.flashbang_gradient.isChecked()

        with open('settings.txt', 'w') as settings_file:
            json.dump(self.settings, settings_file)

        return self.settings

    def set_settings(self):
        # TODO: Save settings to file
        self.hidden.emit()
        self.hide()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def ct_color_picker(self):
        color = QColorDialog.getColor()
        if color != QColor():
            self.background_button_ct_color.setStyleSheet("background-color: {}" .format(color.name()))
            self.background_line_edit_ct_color.setText(color.name().upper())

    def t_color_picker(self):
        color = QColorDialog.getColor()
        if color != QColor():
            self.background_button_t_color.setStyleSheet("background-color: {}" .format(color.name()))
            self.background_line_edit_t_color.setText(color.name().upper())


def main():
    try:
        app = QApplication(sys.argv)
        w = QWidget()
        tray_icon = SystemTrayIcon(QIcon(resource_path("cue-cs.xpm")), w)
        tray_icon.show()
        app.exec_()
    except Exception:
        logging.exception()

if __name__ == '__main__':
    main()
