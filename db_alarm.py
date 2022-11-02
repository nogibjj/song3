from PySide6 import QtCore, QtGui, QtWidgets
import sqlite3
import random


class Alarm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Alarm, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle("Alarm")
        self.resize(420, 290)
        self.old_pos = 0

        self.list = QtWidgets.QListWidget(self)
        self.list.setGeometry(15, 15, 390, 200)

        self.datetimeedit = QtWidgets.QDateTimeEdit(self)
        self.datetimeedit.setGeometry(15, 235, 190, 35)
        self.currentDateTime = QtCore.QDateTime.currentDateTime()
        print(self.currentDateTime)

        self.datetimeedit.setDateTime(self.currentDateTime)
        self.datetimeedit.setDisplayFormat("yyyy-MM-dd hh:mm")

        btn_add = QtWidgets.QPushButton("Add Alarm", self)
        btn_add.setGeometry(240, 237, 80, 30)
        btn_add.clicked.connect(self.add)

        btn_del = QtWidgets.QPushButton("Delete Selection", self)
        btn_del.setGeometry(325, 237, 80, 30)
        btn_del.clicked.connect(self.delete)

        self.connect = sqlite3.connect("alarm_data.db")
        sql = """
        CREATE TABLE IF NOT EXISTS alarms (
            _idx INTEGER PRIMARY KEY AUTOINCREMENT,
            _datetime VARCHAR(100) NOT NULL
        )
        """
        cur = self.connect.cursor()
        cur.execute(sql)
        self.connect.commit()
        cur.close()

        self.show_datas()

    def add(self):
        dt = self.datetimeedit.dateTime()
        datetime = dt.toPython()
        str_dt = datetime.strftime("%Y-%m-%d %H:%M")
        query = "SELECT COUNT(*) FROM alrams WHERE _datetime=?"
        cur = self.connect.cursor()
        cur.execute(query, (str_dt,))
        cnt = cur.fetchone()[0]
        if cnt == 0:
            query = "INSERT INTO alrams (_datetime) VALUES (?)"
            cur.execute(query, (str_dt,))
            self.connect.commit()
            cur.close()
        else:
            QtWidgets.QMessageBox.question(
                self,
                "Error",
                "Data already exists.",
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok,
            )
        self.show_datas()

    def show_datas(self):
        self.list.clear()
        results = self.get_datas()
        for r in results:
            self.list.addItem(f'{r.get("idx")}#{r.get("datetime")}')
            self.parent.alrams.append(f'{r.get("datetime")}')

    def get_datas(self):
        results = []
        query = "SELECT _idx, _datetime FROM alarms"
        cur = self.connect.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        for r in rows:
            _idx = r[0]
            _datetime = r[1]
            results.append(
                {"idx": _idx, "datetime": _datetime,}
            )
        return results

    def delete(self):
        select_items = self.list.selectedItems()
        if select_items:
            for item in select_items:
                _idx = item.text().split("#")[0]
                _txt = item.text().split("#")[-1]
                query = "DELETE FROM alarms WHERE _idx=?"
                cur = self.connect.cursor()
                cur.execute(query, (_idx,))
                self.connect.commit()
                if _txt in self.parent.alarms:
                    self.parent.alarms.remove(_txt)
        self.show_datas()

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.old_pos = e.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            self.move(e.globalPosition().toPoint() - self.old_pos)


class AnalogClock(QtWidgets.QWidget):
    p_hour = QtGui.QPolygon(
        [QtCore.QPoint(5, 8), QtCore.QPoint(-5, 8), QtCore.QPoint(0, -40)]
    )

    p_min = QtGui.QPolygon(
        [QtCore.QPoint(5, 8), QtCore.QPoint(-5, 8), QtCore.QPoint(0, -70)]
    )

    p_sec = QtGui.QPolygon(
        [QtCore.QPoint(2, 8), QtCore.QPoint(-2, 8), QtCore.QPoint(0, -90)]
    )

    hourColor = QtGui.QColor(127, 0, 127)
    minuteColor = QtGui.QColor(127, 127, 191)
    secColor = QtGui.QColor(255, 0, 0)

    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)

        self.alrams = []
        self.alram = Alarm(self)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

        quitAction = QtGui.QAction(
            "End",
            self,
            shortcut="Ctrl+Q",
            triggered=QtWidgets.QApplication.instance().quit,
        )
        addAlram = QtGui.QAction(
            "Alarm", self, shortcut="Ctrl+A", triggered=self.addAlram
        )
        separator = QtGui.QAction(self)
        separator.setSeparator(True)
        self.addAction(addAlram)
        self.addAction(separator)
        self.addAction(quitAction)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        self.setWindowTitle("Analog Clock")
        self.resize(200, 200)
        self.old_pos = 0

        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.SplashScreen
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.is_play_mp3 = False

    def addAlram(self):
        self.alram.show()

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.old_pos = e.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if e.buttons() & QtCore.Qt.LeftButton:
            self.move(e.globalPosition().toPoint() - self.old_pos)

    def is_alarm(self, str_time):
        for a in self.alrams:
            if a.strip() == str_time.strip():
                return True
        return False

    def paintEvent(self, event):
        dt = QtCore.QDateTime.currentDateTime()
        dt = dt.toPython()
        _h = dt.hour
        _m = dt.minute
        _s = dt.second
        print(f"{_h}:{_m}:{_s}")
        str_time = dt.strftime("%Y-%m-%d %H:%M")
        alram_check = self.is_alarm(str_time)

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)

        if not alram_check:
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtCore.Qt.white)
        else:

            colorLine = "#" + "".join(
                [random.choice("0123456789ABCDEF") for j in range(6)]
            )
            colorBrush = "#" + "".join(
                [random.choice("0123456789ABCDEF") for j in range(6)]
            )
            pen = QtGui.QPen(QtGui.QColor(colorLine))
            brush = QtGui.QBrush(QtGui.QColor(colorBrush))
            pen.setWidth(random.randint(1, 5))
            painter.setPen(pen)
            painter.setBrush(brush)
        painter.drawEllipse(QtCore.QPoint(0, 0), 98, 98)

        painter.setPen(self.hourColor)
        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(self.minuteColor)
        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self.hourColor)
        painter.save()
        painter.rotate(30.0 * ((_h + _m / 60.0)))
        painter.drawConvexPolygon(self.p_hour)
        painter.restore()

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(self.minuteColor)
        painter.save()
        painter.rotate(6.0 * (_m + _s / 60.0))
        painter.drawConvexPolygon(self.p_min)
        painter.restore()

        painter.setBrush(self.secColor)
        painter.save()
        painter.rotate(_s * 6.0)
        painter.drawConvexPolygon(self.p_sec)
        painter.restore()

        painter.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    clock = AnalogClock()
    clock.show()
    app.exec()
