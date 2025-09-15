from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtGui import QPainter

class ChartsScreen(QWidget):
    def __init__(self, navigate_to):
        super().__init__()
        layout = QVBoxLayout()

        series = QPieSeries()
        series.append("Fantasy", 10)
        series.append("Science", 5)
        series.append("History", 8)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("📊 ספרים לפי קטגוריה")

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(chart_view)
        self.setLayout(layout)
