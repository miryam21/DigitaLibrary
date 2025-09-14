import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtGui import QPainter

app = QApplication(sys.argv)

# חלון ראשי
window = QMainWindow()
window.setWindowTitle("Digital Library - PySide6 Test")

# יצירת גרף
series = QLineSeries()
series.append(0, 6)
series.append(2, 4)
series.append(3, 8)
series.append(7, 4)
series.append(10, 5)

chart = QChart()
chart.addSeries(series)
chart.setTitle("Example Chart - QtCharts")

chart_view = QChartView(chart)
chart_view.setRenderHint(QPainter.Antialiasing)

window.setCentralWidget(chart_view)
window.resize(800, 600)
window.show()

sys.exit(app.exec())
