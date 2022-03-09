from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import qApp

from pyqt_style_setter import StyleSetter
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from pyqt_custom_titlebar_window import CustomTitlebarWindow


class NewWindowHandler(QObject):
    def __init__(self, new_widget_type, icon_filename: str, exclude_type_lst: list = [], *args, **kwargs):
        super().__init__(*args, **kwargs)
        qApp.installEventFilter(self)
        self.__windowDict = dict()
        self.__newWidgetType = new_widget_type
        self.__icon_filename = icon_filename
        self.__new(exclude_type_lst)

    def __new(self, exclude_type_lst: list):
        mainWindow = self.__newWidgetType()
        mainWindow.newClicked.connect(self.__new)
        StyleSetter.setWindowStyle(mainWindow, exclude_type_lst=exclude_type_lst)
        titleBarWindow = CustomTitlebarSetter.getCustomTitleBar(mainWindow, icon_filename=self.__icon_filename)
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