from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import qApp

from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from pyqt_custom_titlebar_window.customTitlebarWindow import CustomTitlebarWindow


class NewWindowHandler(QObject):
    def __init__(self, new_widget_type, icon_filename: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        qApp.installEventFilter(self)
        self.__windowDict = dict()
        self.__newWidgetType = new_widget_type
        self.__icon_filename = icon_filename
        self.__new()

    def __new(self):
        mainWindow = self.__newWidgetType()
        mainWindow.newClicked.connect(self.__new)
        titleBarWindow = CustomTitlebarSetter.getCustomTitleBarWindow(mainWindow, icon_filename=self.__icon_filename)
        titleBarWindow.setAttribute(Qt.WA_DeleteOnClose)
        titleBarWindow.destroyed.connect(self.__destroyed)
        titleBarWindow.show()

    def eventFilter(self, obj, e):
        if isinstance(obj, CustomTitlebarWindow):
            # catch the QShowEvent of CustomTitlebarWindow
            if e.type() == 17:
                w = self.__getInnerWidget(obj)
                self.__windowDict[w] = obj
        return super().eventFilter(obj, e)

    def __destroyed(self, w):
        w = self.__getInnerWidget(w)
        del(self.__windowDict[w])

    def __getInnerWidget(self, w):
        inner_widget = [c for c in w.children() if isinstance(c, self.__newWidgetType)][0]
        return inner_widget
