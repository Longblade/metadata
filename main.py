import os
import xml.dom.minidom as md
from utils.XML_to_RAM_conversion import XMLToRAMConverter
from utils.RAM_to_XML_conversion import RAMToXMLConverter
from utils.RAM_to_DBD_conversion import RAMToDBDConverter
from data_base_sources.DBD_const import SQL_DBD_Init


xml = md.parse(os.path.join("source_xmls/", "TASKS.xml"))
schema = XMLToRAMConverter(xml).xml_to_ram()

xml1 = RAMToXMLConverter(schema).ram_to_xml()
with open("./tt.xml", "wb") as f:
    f.write(xml1.toprettyxml(encoding="utf-8", indent="  "))

conv = RAMToDBDConverter(schema, "tasks.db", SQL_DBD_Init).ram_to_dbd()
