from io import StringIO
import io
import json
import sys
import traceback
import xml.etree.ElementTree as ET

from lxml import etree
import xml.etree.ElementTree as ET
from jadnxml.utils.utils import get_xml_file, get_xsd_file


def validate_xml_data(xsd_str: str, xml_str: str):
    print(f"Validating xsd data against xml schema")
    
    try:
        # XSD
        xsd_stringio = StringIO(xsd_str)
        xmlschema_tree = etree.parse(xsd_stringio)
        xmlschema = etree.XMLSchema(xmlschema_tree)
        
        # XML
        xml_str = xml_str.replace("\n", "")
        xml_str = xml_str.strip()
        xml_stringio = StringIO(xml_str)
        xml_tree = etree.parse(xml_stringio)
        
        # Validate XML against XSD
        # Left off here, everything was passing....=^/ 
        xmlschema.validate(xml_tree)     
      
    except Exception as e:
        err_msg = e.args[0]
        print("XML Validation Error: " + err_msg)
        return (False, err_msg)

    return (True, None)


def validate_xml_files(xsd_file_name, xml_file_name):
    print(f"Validating '{xml_file_name}' data against '{xsd_file_name}' schema")
    is_valid = False
    
    try:
      
        xmlschema = get_xsd_file(xsd_file_name)  
        xml_doc = get_xml_file(xml_file_name)  

        # Validate the XML document using the XML schema
        xmlschema.assertValid(xml_doc)
        is_valid = xmlschema.validate(xml_doc)   
      
    except Exception as e:
        err = traceback.format_exception(*sys.exc_info())
        err_msg = err[3]
        print("XML Validation Error: " + err_msg)
        return (is_valid, err_msg)

    print(f"*** Is data valid? {is_valid} ***")
    return is_valid
