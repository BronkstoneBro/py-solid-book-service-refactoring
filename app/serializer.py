import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from .book import Book


class BookSerializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(BookSerializer):
    def serialize(self, book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")


class SerializerFactory:
    @staticmethod
    def create_serializer(serialize_type: str) -> BookSerializer:
        if serialize_type == "json":
            return JsonSerializer()
        elif serialize_type == "xml":
            return XmlSerializer()
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
