
import xml.etree.ElementTree as ET
from xml.dom import minidom
from read import modules

def create_module(modulename, added_element):
    element = ET.Element("xs:complexType")
    element_sequ = ET.Element("xs:sequence")

    element.set("name", modulename)
    element_anno = ET.Element("annotation")
    element_app = ET.Element("appinfo")
    name = ET.Element("name")
    tableref = ET.Element("tableRef")
    ref = ET.Element("ref")
    tableref.append(ref)
    max = ET.Element("maxEntries")
    min = ET.Element("minEntries")
    desc = ET.Element("description")
    access = ET.Element("accessMode")

    element_app.append(name)
    element_app.append(tableref)
    element_app.append(max)
    element_app.append(min)
    element_app.append(desc)
    element_app.append(access)


    (element_anno).append(element_app)
    element.append(element_anno)
    element.append(element_sequ)
    added_element.append(element)


    return element_sequ

def create_table(tablename, minEntries, maxEntries, disname, ref, desc, accesMode, added_element):
    element = ET.Element("xs:element")
    element.set("name", tablename)

    element_comp = ET.Element("xs:complexType")
    element.append(element_comp)
    element_anno = ET.Element("annotation")
    element_comp.append(element_anno)
    element_info = ET.Element("appinfo")
    element_anno.append(element_info)

    element_name = ET.Element("name")
    appinfo_desc = ET.Element("description")
    appinfo_null = ET.Element("nullValue")
    appinfo_access = ET.Element("accessMode")

    element_info.append(element_name)
    element_info.append(appinfo_desc)
    element_info.append(appinfo_null)
    element_info.append(appinfo_access)



    element_tableref = ET.Element("tableRef")

    element_ref = ET.Element("ref")
    element_ref.set("id", "1")
    appinfo_text1 = ET.Element("text")
    appinfo_text1.text = ref
    element_ref.append(appinfo_text1)
    element_tableref.append(element_ref)

    element_max = ET.Element("maxEntries")
    if maxEntries is not None and len(maxEntries) > 2:
        maxEntries = maxEntries[:-2]
    appinfo_text3 = ET.Element("text")
    appinfo_text3.text = maxEntries
    element_max.append(appinfo_text3)

    element_min = ET.Element("minEntries")
    if minEntries is not None and len(minEntries) > 2:
        minEntries = minEntries[:-2]
    appinfo_text4 = ET.Element("text")
    appinfo_text4.text = minEntries
    element_min.append(appinfo_text4)

    element_desc = ET.Element("description")
    appinfo_text5 = ET.Element("text")
    appinfo_text5.text = desc
    element_desc.append(appinfo_text5)

    element_acces = ET.Element("accessMode")
    appinfo_text6 = ET.Element("text")
    appinfo_text6.text = accesMode
    element_acces.append(appinfo_text6)

    element_info.append(element_name)
    element_info.append(element_tableref)
    element_info.append(element_max)
    element_info.append(element_min)
    element_info.append(element_desc)
    element_info.append(element_acces)

    element_anno.append(element_info)

    element_sequ = ET.Element("xs:sequence")

    element_comp.append(element_anno)
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
        tableSequenceType = ET.SubElement(tableComplexType, "xs:sequence")

        dataType = ET.SubElement(tableSequenceType, "xs:element")
        dataType.set("name", "ConfigDataType")
        dataTypeComplex = ET.SubElement(dataType, "xs:complexType")
        dataTypeSequence = ET.SubElement(dataTypeComplex, "xs:sequence")





        for module in modules:
            print(module.name)

        item = create_module("MODULE_NAME", dataTypeSequence)
        bitem = create_table("TABLE NAME", "234","3","disname","ref","desc","mode",item)

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

