# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_dialog.ui'
#
# Created: Wed Dec 30 17:12:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(282, 503)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(SettingsDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.general_update_interval = QtGui.QDoubleSpinBox(self.groupBox)
        self.general_update_interval.setDecimals(3)
        self.general_update_interval.setMinimum(0.001)
        self.general_update_interval.setMaximum(5.0)
        self.general_update_interval.setSingleStep(0.01)
        self.general_update_interval.setProperty("value", 0.001)
        self.general_update_interval.setObjectName("general_update_interval")
        self.horizontalLayout_5.addWidget(self.general_update_interval)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.general_debug = QtGui.QCheckBox(self.groupBox)
        self.general_debug.setObjectName("general_debug")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.general_debug)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.background_line_edit_ct_color = QtGui.QLineEdit(self.groupBox_3)
        self.background_line_edit_ct_color.setMaximumSize(QtCore.QSize(53, 16777215))
        self.background_line_edit_ct_color.setText("")
        self.background_line_edit_ct_color.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.background_line_edit_ct_color.setObjectName("background_line_edit_ct_color")
        self.horizontalLayout_6.addWidget(self.background_line_edit_ct_color)
        self.background_button_ct_color = QtGui.QPushButton(self.groupBox_3)
        self.background_button_ct_color.setMinimumSize(QtCore.QSize(0, 0))
        self.background_button_ct_color.setMaximumSize(QtCore.QSize(25, 16777215))
        self.background_button_ct_color.setText("")
        self.background_button_ct_color.setCheckable(False)
        self.background_button_ct_color.setDefault(False)
        self.background_button_ct_color.setFlat(False)
        self.background_button_ct_color.setObjectName("background_button_ct_color")
        self.horizontalLayout_6.addWidget(self.background_button_ct_color)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.background_line_edit_t_color = QtGui.QLineEdit(self.groupBox_3)
        self.background_line_edit_t_color.setMaximumSize(QtCore.QSize(53, 16777215))
        self.background_line_edit_t_color.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.background_line_edit_t_color.setObjectName("background_line_edit_t_color")
        self.horizontalLayout_7.addWidget(self.background_line_edit_t_color)
        self.background_button_t_color = QtGui.QPushButton(self.groupBox_3)
        self.background_button_t_color.setMinimumSize(QtCore.QSize(0, 0))
        self.background_button_t_color.setMaximumSize(QtCore.QSize(25, 16777215))
        self.background_button_t_color.setText("")
        self.background_button_t_color.setObjectName("background_button_t_color")
        self.horizontalLayout_7.addWidget(self.background_button_t_color)
        self.formLayout_3.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_7 = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout_7.setObjectName("formLayout_7")
        self.healthbar_enabled = QtGui.QCheckBox(self.groupBox_4)
        self.healthbar_enabled.setObjectName("healthbar_enabled")
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.healthbar_enabled)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.formLayout_7.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayout_5 = QtGui.QFormLayout(self.groupBox_5)
        self.formLayout_5.setObjectName("formLayout_5")
        self.weapons_enabled = QtGui.QCheckBox(self.groupBox_5)
        self.weapons_enabled.setObjectName("weapons_enabled")
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.weapons_enabled)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.formLayout_5.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox_6)
        self.formLayout_4.setObjectName("formLayout_4")
        self.bomb_enabled = QtGui.QCheckBox(self.groupBox_6)
        self.bomb_enabled.setObjectName("bomb_enabled")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.bomb_enabled)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.formLayout_4.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.label_6 = QtGui.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bomb_timer = QtGui.QSpinBox(self.groupBox_6)
        self.bomb_timer.setObjectName("bomb_timer")
        self.horizontalLayout.addWidget(self.bomb_timer)
        self.formLayout_4.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtGui.QGroupBox(SettingsDialog)
        self.groupBox_7.setObjectName("groupBox_7")
        self.formLayout_6 = QtGui.QFormLayout(self.groupBox_7)
        self.formLayout_6.setObjectName("formLayout_6")
        self.flashbang_enabled = QtGui.QCheckBox(self.groupBox_7)
        self.flashbang_enabled.setObjectName("flashbang_enabled")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.flashbang_enabled)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.formLayout_6.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.flashbang_gradient = QtGui.QCheckBox(self.groupBox_7)
        self.flashbang_gradient.setObjectName("flashbang_gradient")
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.flashbang_gradient)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(SettingsDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.button_save_settings = QtGui.QPushButton(SettingsDialog)
        self.button_save_settings.setObjectName("button_save_settings")
        self.horizontalLayout_2.addWidget(self.button_save_settings)
        self.button_cancel_settings = QtGui.QPushButton(SettingsDialog)
        self.button_cancel_settings.setObjectName("button_cancel_settings")
        self.horizontalLayout_2.addWidget(self.button_cancel_settings)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "CUE-CSGO Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsDialog", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingsDialog", "Update interval", None, QtGui.QApplication.UnicodeUTF8))
        self.general_debug.setText(QtGui.QApplication.translate("SettingsDialog", "Debug *", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SettingsDialog", "Background", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SettingsDialog", "CT Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SettingsDialog", "T Color", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("SettingsDialog", "Health bar", None, QtGui.QApplication.UnicodeUTF8))
        self.healthbar_enabled.setText(QtGui.QApplication.translate("SettingsDialog", "Enabled *", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("SettingsDialog", "Weapons", None, QtGui.QApplication.UnicodeUTF8))
        self.weapons_enabled.setText(QtGui.QApplication.translate("SettingsDialog", "Enabled *", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("SettingsDialog", "Bomb", None, QtGui.QApplication.UnicodeUTF8))
        self.bomb_enabled.setText(QtGui.QApplication.translate("SettingsDialog", "Enabled *", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("SettingsDialog", "Bomb timer:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("SettingsDialog", "Flashbang", None, QtGui.QApplication.UnicodeUTF8))
        self.flashbang_enabled.setText(QtGui.QApplication.translate("SettingsDialog", "Enabled *", None, QtGui.QApplication.UnicodeUTF8))
        self.flashbang_gradient.setText(QtGui.QApplication.translate("SettingsDialog", "Gradient", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialog", "* Restart is needed", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save_settings.setText(QtGui.QApplication.translate("SettingsDialog", "Save settings", None, QtGui.QApplication.UnicodeUTF8))
        self.button_cancel_settings.setText(QtGui.QApplication.translate("SettingsDialog", "Abort", None, QtGui.QApplication.UnicodeUTF8))

