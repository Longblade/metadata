import xml.dom.minidom as md
import os
from utils.XML_to_RAM_conversion import XMLToRAMTranslator

xml = md.parse(os.path.join("source_xmls/", "TASKS.xml"))
schema = XMLToRAMTranslator(xml).xml_to_ram()
print(schema.name)