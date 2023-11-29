
import xml.etree.ElementTree as ET
from xml.dom import minidom
from read import modules

def create_module(document, modulename, added_element):
    element = ET.Element("xs:element")
    element.set("name", modulename)
    element_comp = ET.Element("xs:complexType")
    element_sequ = ET.Element("xs:sequence")
    element_comp.append(element_sequ)
    element.append(element_comp)
    added_element.append(element)

    return element_sequ



def generateXSD(fileName):
    try:


        schemaElement = ET.Element("{http://www.w3.org/2001/XMLSchema}schema")
        schemaElement.set("attributeFormDefault", "unqualified")
        schemaElement.set("elementFormDefault", "qualified")

        document = ET.ElementTree(schemaElement)
        document.write(fileName, xml_declaration=True, encoding='utf-8')

        rootElement = ET.SubElement(schemaElement, "xs:element")
        rootElement.set("name", "root")
        rootComplexType = ET.SubElement(rootElement, "xs:complexType")
        rootSequence = ET.SubElement(rootComplexType, "xs:sequence")
        ulakTemplateElement = ET.SubElement(rootSequence, "xs:element")
        ulakTemplateElement.set("name", "ulak_template")
        ulakTemplateComplexType = ET.SubElement(ulakTemplateElement, "xs:complexType")
        ulakTemplateSequence = ET.SubElement(ulakTemplateComplexType, "xs:sequence")
        dataModelElement = ET.SubElement(ulakTemplateSequence, "xs:element")
        dataModelElement.set("name", "data_model")
        dataModelElement.set("type", "xs:string")
        neIdElement = ET.SubElement(ulakTemplateSequence, "xs:element")
        neIdElement.set("name", "neId")
        neIdElement.set("type", "xs:nonNegativeInteger")
        neIdElement.set("default", "17")

        tablesElement = ET.SubElement(ulakTemplateSequence, "xs:element")
        tablesElement.set("name", "tables")

        tablesComplexType = ET.SubElement(tablesElement, "xs:complexType")
        tablesSequence = ET.SubElement(tablesComplexType, "xs:sequence")

        # Create table element
        tableElement = ET.SubElement(tablesSequence, "xs:element")
        tableElement.set("name", "table")
        tableElement.set("maxOccurs", "unbounded")
        tableElement.set("minOccurs", "1")


        tableComplexType = ET.SubElement(tableElement, "xs:complexType")
        mainSequence = ET.SubElement(tableComplexType, "xs:sequence")

        print(modules[-1].name)
        for module in modules:
            print(module.name)

        item = create_module(document,"aseeekkeee", mainSequence)

        document = ET.ElementTree(schemaElement)
        document.write(fileName, xml_declaration=True, encoding='utf-8')

        xml_content = minidom.parseString(ET.tostring(schemaElement)).toprettyxml(indent="    ")
        with open(fileName, "w") as file:
            file.write(xml_content)

        print("XSD generated successfully and file name is2:", fileName)
    except Exception as e:
        print("Error:", str(e))

# Example usage:
generateXSD("xsddd_example.xsd")

