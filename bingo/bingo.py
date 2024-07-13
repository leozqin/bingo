from tabulate import tabulate
from random import sample
from dataclasses import dataclass
from typing import List
from weasyprint import HTML
from pypdf import PdfWriter
from bingo.style import get_style
from io import BytesIO


@dataclass
class BingoCard:
    title: str
    variants: int
    size: int
    items: List
    center: str = None

    def validate(self):
        if self.size % 2 != 1:
            raise ValueError("The size of the card must be odd!")

        if self.size**2 > len(self.items) + (1 if self.center else 0):
            min_size = self.size**2
            raise ValueError(
                f"You must provide more than {min_size} items to prevent repetition"
            )

    def get(self):
        merged_pdf = PdfWriter()

        for i in range(self.variants):
            pdf = self.to_pdf(i)
            merged_pdf.append(BytesIO(pdf))

        merged_pdf.write(f"{self.title}.pdf")

    def generate_card(self) -> str:
        sample_size = self.size**2 - (1 if self.center else 0)
        items = sample(self.items, k=sample_size)

        if self.center:
            center_index = int((self.size**2) / 2)
            items.insert(center_index, self.center)

        segment = []
        segments = []

        for i in items:
            if len(segment) == self.size:
                segments.append(segment)
                segment = [i]
            else:
                segment.append(i)
        segments.append(segment)

        return tabulate(segments, tablefmt="html")

    def to_pdf(self, variant: int):
        card = self.generate_card()
        style = get_style(self.size)

        html = "\n".join([style, card])
        pdf = HTML(string=html).write_pdf()

        return pdf
