from dataclasses import dataclass


@dataclass
class Item:
    link: str
    img: str
    price: str
    comments: int = "Unknown"
    title: str = "Unknown"
    description: str = "Unknown"
