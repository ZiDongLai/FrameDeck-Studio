from __future__ import annotations

import os
import unittest
from pathlib import Path

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication, QGroupBox, QLabel, QPushButton

from core.app_paths import APP_VERSION
from gui.about_dialog import AboutDialog


ROOT = Path(__file__).resolve().parents[1]
_APP = QApplication.instance() or QApplication([])


class AboutPageTests(unittest.TestCase):
    def test_about_dialog_contains_required_sections_and_resources(self):
        dialog = AboutDialog()
        groups = {group.title() for group in dialog.findChildren(QGroupBox)}
        self.assertTrue({"主要功能", "后续计划", "项目与许可证", "反馈与交流", "支持开发"} <= groups)
        self.assertTrue(any(APP_VERSION in label.text() for label in dialog.findChildren(QLabel)))
        self.assertTrue((ROOT / "resources" / "support" / "wechat_qr.jpg").is_file())
        self.assertTrue((ROOT / "resources" / "support" / "alipay_qr.jpg").is_file())
        self.assertTrue(any("748934113" in label.text() for label in dialog.findChildren(QLabel)))
        dialog.set_language("en_US")
        self.assertEqual(dialog.windowTitle(), "About FrameDeck Studio")
        self.assertTrue(any("Key features" == group.title() for group in dialog.findChildren(QGroupBox)))
        dialog.close()

    def test_version_is_semver_and_build_configs_use_new_minor(self):
        self.assertRegex(APP_VERSION, r"^\d+\.\d+\.\d+$")
        for relative in (
            "FrameDeck Studio macOS.spec",
            "build_macos.sh",
            "installer/FrameDeck_Studio_V12.iss",
            ".github/workflows/macos-build.yml",
        ):
            source = (ROOT / relative).read_text(encoding="utf-8-sig")
            self.assertIn("12.1.0", source, relative)


if __name__ == "__main__":
    unittest.main()
