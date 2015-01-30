import os
import tempfile
import unittest
from time import time

import runner.constants as const
from runner.exporter     import Exporter
from runner.csv_exporter import CsvExporter
from runner.stats        import Statistics, StatisticsSet

class ExporterTestCase(unittest.TestCase):
    def setUp(self):
        self.ss = StatisticsSet(Statistics(), Statistics())
        self.exp = Exporter(self.ss)

    def test_init(self):
        self.assertEqual(self.exp.stats_set, self.ss)

    def test_export_methods(self):
        with self.assertRaises(NotImplementedError):
            self.exp.export('foobar', 'foobar', 'foobar')
        with self.assertRaises(NotImplementedError):
            self.exp.export_averages('foobar', 'foobar', 'foobar')
        with self.assertRaises(NotImplementedError):
            self.exp.export_averages_plot('foobar', 'foobar', 'foobar')

class CsvExporterTestCase(unittest.TestCase):
    def setUp(self):
        self.ss = StatisticsSet(Statistics(), Statistics())
        self.exp = CsvExporter(self.ss)

    def test_init(self):
        self.assertEqual(self.exp.stats_set, self.ss)

    def test_export(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            fname = os.path.join(tmpdirname, 'export.csv')
            self.assertFalse(os.path.exists(fname))
            self.exp.export(fname, 'mpl', 'runtime')
            self.assertTrue(os.path.exists(fname))

    def test_export_averages(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            fname = os.path.join(tmpdirname, 'averages.csv')
            self.assertFalse(os.path.exists(fname))
            self.exp.export_averages(fname, 'mpl', 'runtime')
            self.assertTrue(os.path.exists(fname))

    def test_export_averages_plot(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            fname = os.path.join(tmpdirname, 'plot.pdf')
            self.assertFalse(os.path.exists(fname))
            self.exp.export(fname, 'testplot', 'mpl', 'runtime')
            self.assertTrue(os.path.exists(fname))