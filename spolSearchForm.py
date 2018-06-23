# -*- coding: utf-8 -*-

"""
/***************************************************************************
 vfkPluginDialog
                                 A QGIS plugin
 Plugin umoznujici praci s daty katastru nemovitosti
                             -------------------
        begin                : 2015-06-11
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Stepan Bambula
        email                : stepan.bambula@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtGui import *


from ui_spolsearchfrom import *

class SpolSearchForm(QWidget):

    def __init__(self, parent=None):
        super(SpolSearchForm, self).__init__(parent)

        # Set up the user interface from Designer.
        self.ui = Ui_SpolSearchForm()
        self.ui.setupUi(self)

    def CisloKatastr(self):
        return unicode(self.ui.kuLineEdit.text()).strip()

    def CisloZpmz(self):
        return unicode(self.ui.zpmzLineEdit.text()).strip()

    def CisloBodu(self):
        return unicode(self.ui.cbLineEdit.text()).strip()