"""Draw the original XML/settings app mark and package PNG and Windows ICO files."""

from __future__ import annotations

import struct
from pathlib import Path

from PySide6.QtCore import QBuffer, QByteArray, QIODevice, QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QGuiApplication, QImage, QPainter, QPainterPath, QPen

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "src/ue5_ubt_config_wizard/assets"
PACKAGING = ROOT / "packaging"


def draw_icon(size: int) -> QImage:
    image = QImage(size, size, QImage.Format.Format_ARGB32)
    image.fill(Qt.GlobalColor.transparent)
    painter = QPainter(image)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.scale(size / 256, size / 256)

    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(QColor("#173052"))
    painter.drawRoundedRect(QRectF(8, 8, 240, 240), 48, 48)

    document = QPainterPath()
    document.moveTo(64, 42)
    document.lineTo(158, 42)
    document.lineTo(198, 82)
    document.lineTo(198, 212)
    document.quadTo(198, 220, 190, 220)
    document.lineTo(64, 220)
    document.quadTo(56, 220, 56, 212)
    document.lineTo(56, 50)
    document.quadTo(56, 42, 64, 42)
    painter.setBrush(QColor("#f7fbff"))
    painter.drawPath(document)
    painter.setBrush(QColor("#bad2e9"))
    fold = QPainterPath()
    fold.moveTo(158, 42)
    fold.lineTo(158, 82)
    fold.lineTo(198, 82)
    fold.closeSubpath()
    painter.drawPath(fold)

    # Angle brackets suggest XML; the three short rows suggest settings.
    pen = QPen(QColor("#1678a8"), 10, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
    painter.setPen(pen)
    painter.drawLine(QPointF(99, 102), QPointF(79, 119))
    painter.drawLine(QPointF(79, 119), QPointF(99, 136))
    painter.drawLine(QPointF(151, 102), QPointF(171, 119))
    painter.drawLine(QPointF(171, 119), QPointF(151, 136))
    painter.setPen(QPen(QColor("#e89435"), 10, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
    painter.drawLine(QPointF(111, 143), QPointF(139, 95))
    painter.setPen(QPen(QColor("#88a9c8"), 8, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
    painter.drawLine(QPointF(82, 169), QPointF(172, 169))
    painter.drawLine(QPointF(82, 190), QPointF(149, 190))
    painter.end()
    return image


def png_bytes(image: QImage) -> bytes:
    output = QByteArray()
    buffer = QBuffer(output)
    buffer.open(QIODevice.OpenModeFlag.WriteOnly)
    if not image.save(buffer, "PNG"):
        raise RuntimeError("Qt could not encode the app icon")
    return bytes(output)


def main() -> None:
    application = QGuiApplication([])
    ASSETS.mkdir(parents=True, exist_ok=True)
    PACKAGING.mkdir(parents=True, exist_ok=True)
    sizes = (16, 32, 48, 64, 256)
    images = [png_bytes(draw_icon(size)) for size in sizes]
    (ASSETS / "app_icon.png").write_bytes(images[-1])

    # ICO accepts embedded PNG images on supported Windows versions.
    header = struct.pack("<HHH", 0, 1, len(images))
    offset = len(header) + len(images) * 16
    entries = []
    for size, data in zip(sizes, images, strict=True):
        entries.append(
            struct.pack("<BBBBHHII", size % 256, size % 256, 0, 0, 1, 32, len(data), offset)
        )
        offset += len(data)
    (PACKAGING / "app_icon.ico").write_bytes(header + b"".join(entries) + b"".join(images))
    del application


if __name__ == "__main__":
    main()
