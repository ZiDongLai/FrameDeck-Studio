from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices, QPixmap
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from core.app_paths import APP_NAME, APP_VERSION, resource_path


PROJECT_URL = "https://github.com/lzy4107932-commits/FrameDeck-Studio"


class LicenseDialog(QDialog):
    """Small read-only viewer for the bundled MIT license."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("许可证 / License")
        self.resize(720, 560)
        layout = QVBoxLayout(self)
        viewer = QTextBrowser(self)
        viewer.setOpenExternalLinks(False)
        try:
            license_text = Path(resource_path("LICENSE")).read_text(
                encoding="utf-8"
            )
        except OSError as exc:
            license_text = f"无法读取许可证文件：{exc}"
        viewer.setPlainText(license_text)
        layout.addWidget(viewer)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close, self)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)


class AboutDialog(QDialog):
    """About, feedback, and optional support information."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("AboutDialog")
        self.setWindowTitle("关于 FrameDeck Studio")
        self.setMinimumSize(760, 640)
        self.resize(820, 760)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(18, 16, 18, 14)
        outer.setSpacing(12)

        header = QHBoxLayout()
        logo = QLabel(self)
        logo.setPixmap(
            QPixmap(resource_path("resources/icon.png")).scaled(
                64,
                64,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        header.addWidget(logo)
        title_box = QVBoxLayout()
        title = QLabel(APP_NAME, self)
        title.setObjectName("AboutTitle")
        version = QLabel(f"版本 {APP_VERSION}", self)
        version.setObjectName("AboutVersion")
        title_box.addWidget(title)
        title_box.addWidget(version)
        header.addLayout(title_box)
        header.addStretch(1)
        outer.addLayout(header)

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(4, 4, 10, 4)
        content_layout.setSpacing(10)

        intro = QLabel(
            "FrameDeck Studio 是一款开源桌面图片排版工具，帮助你将图片集合整理为结构清晰、可继续编辑的多页版面，并导出为 PowerPoint、PDF 或单页图片。",
            content,
        )
        intro.setWordWrap(True)
        content_layout.addWidget(intro)

        features = QGroupBox("主要功能", content)
        feature_layout = QVBoxLayout(features)
        feature_layout.addWidget(
            QLabel(
                "• 连续或分组自动排版，支持跨页拖拽和手动调整\n"
                "• 图片标题、页面标题、间距与主题设置\n"
                "• JPG、PNG、WEBP、TIFF、HEIF/HEIC 导入\n"
                "• PowerPoint、PDF 和页面图片导出\n"
                "• .fds 工程保存、撤销/重做与自动恢复",
                features,
            )
        )
        content_layout.addWidget(features)

        plans = QGroupBox("后续计划", content)
        plans_layout = QVBoxLayout(plans)
        plans_layout.addWidget(
            QLabel(
                "继续优化大批量素材管理和导出稳定性，补充更多可复用模板，并根据实际反馈改善跨平台体验。",
                plans,
            )
        )
        content_layout.addWidget(plans)

        project = QGroupBox("项目与许可证", content)
        project_layout = QFormLayout(project)
        license_button = QPushButton("查看 MIT License", project)
        license_button.clicked.connect(self._show_license)
        project_layout.addRow("开源许可证", license_button)
        home_button = QPushButton(PROJECT_URL, project)
        home_button.setCursor(Qt.CursorShape.PointingHandCursor)
        home_button.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(PROJECT_URL))
        )
        project_layout.addRow("项目主页", home_button)
        content_layout.addWidget(project)

        feedback = QGroupBox("反馈与交流", content)
        feedback_layout = QVBoxLayout(feedback)
        feedback_layout.addWidget(QLabel("QQ群：软件小工具@交流群2（748934113）", feedback))
        feedback_layout.addWidget(
            QLabel("微信群：目前未公开固定加入方式，请留意项目主页后续信息。", feedback)
        )
        feedback_layout.addWidget(
            QLabel(
                "反馈时请尽量提供操作系统、软件版本、问题复现步骤和截图。请不要上传包含隐私或敏感内容的文件。",
                feedback,
            )
        )
        content_layout.addWidget(feedback)

        support = QGroupBox("支持开发", content)
        support_layout = QVBoxLayout(support)
        support_layout.addWidget(
            QLabel(
                "如果这个工具对你有所帮助，也欢迎自愿支持后续维护。相关支持将用于持续开发、测试、构建和发布。是否支持完全自愿，不影响任何功能的正常使用。",
                support,
            )
        )
        qr_row = QHBoxLayout()
        for label, filename in (
            ("微信", "wechat_qr.jpg"),
            ("支付宝", "alipay_qr.jpg"),
        ):
            card = QVBoxLayout()
            image = QLabel(support)
            image.setAlignment(Qt.AlignmentFlag.AlignCenter)
            pixmap = QPixmap(resource_path(f"resources/support/{filename}"))
            if not pixmap.isNull():
                image.setPixmap(
                    pixmap.scaled(
                        230,
                        230,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                )
            else:
                image.setText("二维码资源不可用")
            card.addWidget(image)
            caption = QLabel(label, support)
            caption.setAlignment(Qt.AlignmentFlag.AlignCenter)
            card.addWidget(caption)
            qr_row.addLayout(card)
        support_layout.addLayout(qr_row)
        content_layout.addWidget(support)
        content_layout.addStretch(1)

        scroll.setWidget(content)
        outer.addWidget(scroll, 1)

        close_button = QPushButton("关闭", self)
        close_button.clicked.connect(self.accept)
        close_button.setDefault(True)
        outer.addWidget(close_button, 0, Qt.AlignmentFlag.AlignRight)

        self._translations = {
            "关于 FrameDeck Studio": "About FrameDeck Studio",
            "版本 ": "Version ",
            "FrameDeck Studio 是一款开源桌面图片排版工具，帮助你将图片集合整理为结构清晰、可继续编辑的多页版面，并导出为 PowerPoint、PDF 或单页图片。": "FrameDeck Studio is an open-source desktop layout tool that turns image collections into structured, editable pages for PowerPoint, PDF, or image export.",
            "• 连续或分组自动排版，支持跨页拖拽和手动调整\n• 图片标题、页面标题、间距与主题设置\n• JPG、PNG、WEBP、TIFF、HEIF/HEIC 导入\n• PowerPoint、PDF 和页面图片导出\n• .fds 工程保存、撤销/重做与自动恢复": "• Continuous or grouped auto layout with cross-page drag and manual adjustment\n• Image/page titles, spacing, and theme controls\n• JPG, PNG, WEBP, TIFF, and HEIF/HEIC import\n• PowerPoint, PDF, and page-image export\n• .fds projects, undo/redo, and automatic recovery",
            "继续优化大批量素材管理和导出稳定性，补充更多可复用模板，并根据实际反馈改善跨平台体验。": "Continue improving large-collection management and export stability, add reusable templates, and refine cross-platform behavior based on feedback.",
            "QQ群：软件小工具@交流群2（748934113）": "QQ group: 软件小工具@交流群2 (748934113)",
            "主要功能": "Key features",
            "后续计划": "Roadmap",
            "项目与许可证": "Project and license",
            "反馈与交流": "Feedback and community",
            "支持开发": "Support development",
            "开源许可证": "Open-source license",
            "项目主页": "Project homepage",
            "查看 MIT License": "View MIT License",
            "关闭": "Close",
            "微信": "WeChat",
            "支付宝": "Alipay",
            "二维码资源不可用": "QR resource unavailable",
            "微信群：目前未公开固定加入方式，请留意项目主页后续信息。": "WeChat group: no fixed joining method is public yet; please check the project homepage for updates.",
            "反馈时请尽量提供操作系统、软件版本、问题复现步骤和截图。请不要上传包含隐私或敏感内容的文件。": "When reporting an issue, please include your operating system, app version, reproduction steps, and screenshots. Do not upload files containing private or sensitive information.",
            "如果这个工具对你有所帮助，也欢迎自愿支持后续维护。相关支持将用于持续开发、测试、构建和发布。是否支持完全自愿，不影响任何功能的正常使用。": "If this tool is useful to you, you are welcome to support its continued maintenance. Support helps with development, testing, builds, and releases. It is entirely voluntary and does not affect any feature.",
        }
        if getattr(parent, "_language", "zh_CN") == "en_US":
            self.set_language("en_US")

    def _show_license(self):
        dialog = LicenseDialog(self)
        dialog.exec()

    def set_language(self, language):
        english = str(language).lower().startswith("en")
        for widget in self.findChildren(QLabel) + self.findChildren(QPushButton):
            current = widget.text()
            if english:
                target = self._translations.get(current, current)
                if current.startswith("版本 "):
                    target = "Version " + current[3:]
            else:
                target = next(
                    (source for source, translated in self._translations.items() if translated == current),
                    current,
                )
                if current.startswith("Version "):
                    target = "版本 " + current[8:]
            if target != current:
                widget.setText(target)
        for group in self.findChildren(QGroupBox):
            current = group.title()
            if english:
                target = self._translations.get(current, current)
            else:
                target = next(
                    (source for source, translated in self._translations.items() if translated == current),
                    current,
                )
            group.setTitle(target)
        self.setWindowTitle(
            "About FrameDeck Studio" if english else "关于 FrameDeck Studio"
        )
